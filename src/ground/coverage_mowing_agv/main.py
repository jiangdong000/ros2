# -*- coding: utf-8 -*-
"""区域全覆盖往复清扫 AGV 仿真（纯 NumPy + Matplotlib，不依赖 ROS / Gazebo / CARLA）。

给定矩形作业区与一处矩形障碍，按牛耕式（boustrophedon）往复条带规划
覆盖路径：小车沿梳齿路径逐行清扫，网格统计已覆盖面积并计算覆盖率；
穿越障碍所在条带时自动绕开障碍区段。

用法：
    python main.py --demo --outdir demo_out
    python main.py --headless --duration 60 --seed 42 --outdir demo_out
"""
import argparse
import json
import math
import os
import random

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---------- 作业区几何（单位：米） ----------
FIELD_X0, FIELD_X1 = 0.0, 100.0
FIELD_Y0, FIELD_Y1 = 0.0, 70.0
OBSTACLE = (40.0, 25.0, 60.0, 45.0)   # x0, y0, x1, y1

SWATH = 6.0                 # 清扫带宽（车宽）
CELL = 1.0                  # 覆盖统计网格边长
ARRIVE_R = 1.0
DT = 1.0 / 30.0
SPEED = 8.0
DEFAULT_SEED = 42

CAR_COLOR = (0.95, 0.55, 0.16)
COVER_COLOR = (0.62, 0.82, 0.96)


def build_path():
    """牛耕式往复覆盖路径，返回路径点列表（蛇形换向）。"""
    centers = np.arange(SWATH / 2, FIELD_Y1, SWATH)
    ox0, oy0, ox1, oy1 = OBSTACLE
    path = []
    for k, yc in enumerate(centers):
        if oy0 <= yc <= oy1:
            segments = [(FIELD_X0, ox0), (ox1, FIELD_X1)]
        else:
            segments = [(FIELD_X0, FIELD_X1)]
        for (x0, x1) in segments:
            if k % 2 == 0:
                path.append((x0, yc))
                path.append((x1, yc))
            else:
                path.append((x1, yc))
                path.append((x0, yc))
    return path


class CoverageMap:
    """1 m 网格覆盖统计。"""

    def __init__(self):
        self.nx = int(FIELD_X1 - FIELD_X0)
        self.ny = int(FIELD_Y1 - FIELD_Y0)
        self.covered = np.zeros((self.ny, self.nx), dtype=bool)
        ox0, oy0, ox1, oy1 = OBSTACLE
        self.obstacle = np.zeros_like(self.covered)
        self.obstacle[int(oy0):int(oy1), int(ox0):int(ox1)] = True

    def mark(self, x, y, radius):
        """标记以 (x, y) 为中心、radius 内的可作业网格。"""
        gx = np.arange(self.nx)
        gy = np.arange(self.ny)
        XX, YY = np.meshgrid(gx, gy)
        mask = (XX - x) ** 2 + (YY - y) ** 2 <= radius ** 2
        self.covered[mask & ~self.obstacle] = True

    def free_cells(self):
        return int((~self.obstacle).sum())

    def covered_cells(self):
        return int((self.covered & ~self.obstacle).sum())

    def coverage_ratio(self):
        return self.covered_cells() / self.free_cells()


class Mower:
    """沿覆盖路径巡航的清扫小车。"""

    def __init__(self, path, cmap, seed=DEFAULT_SEED):
        random.seed(seed)
        np.random.seed(seed)
        self.path = path
        self.cmap = cmap
        self.x, self.y = path[0]
        self.theta = 0.0
        self.target = 0
        self.odom = 0.0
        self.trail = [(self.x, self.y)]
        self.finished = False

    def step(self, dt=DT):
        if self.finished:
            return
        tx, ty = self.path[self.target]
        dist = math.hypot(tx - self.x, ty - self.y)
        if dist <= ARRIVE_R:
            self.target += 1
            if self.target >= len(self.path):
                self.finished = True
                return
            tx, ty = self.path[self.target]
        dx, dy = tx - self.x, ty - self.y
        dist = math.hypot(dx, dy)
        step = min(SPEED * dt, dist)
        self.x += dx / dist * step
        self.y += dy / dist * step
        self.theta = math.atan2(dy, dx)
        self.odom += step
        self.cmap.mark(self.x, self.y, SWATH / 2 + CELL * 0.5)
        self.trail.append((self.x, self.y))

    def metrics(self):
        return {
            "finished": self.finished,
            "path_length": round(self.odom, 3),
            "covered_cells": self.cmap.covered_cells(),
            "free_cells": self.cmap.free_cells(),
            "coverage": round(self.cmap.coverage_ratio(), 3),
            "swaths": len(np.arange(SWATH / 2, FIELD_Y1, SWATH)),
        }


def draw(sc, cmap, ax, title):
    ax.set_xlim(-4, FIELD_X1 + 4)
    ax.set_ylim(-6, FIELD_Y1 + 6)
    ax.set_aspect("equal")
    ax.axis("off")

    # 已覆盖区域
    cov = np.ma.masked_where(~cmap.covered, np.ones_like(cmap.covered, dtype=float))
    ax.imshow(cov, origin="lower", extent=[FIELD_X0, FIELD_X1, FIELD_Y0, FIELD_Y1],
              cmap=plt.cm.Blues, alpha=0.35, vmin=0, vmax=1, zorder=1)

    # 作业区边界
    ax.add_patch(Rectangle((FIELD_X0, FIELD_Y0), FIELD_X1 - FIELD_X0,
                           FIELD_Y1 - FIELD_Y0, facecolor="none",
                           edgecolor="black", lw=1.4, zorder=3))
    # 障碍
    ox0, oy0, ox1, oy1 = OBSTACLE
    ax.add_patch(Rectangle((ox0, oy0), ox1 - ox0, oy1 - oy0,
                           facecolor=(0.55, 0.55, 0.55), edgecolor="black",
                           lw=1.0, zorder=4))

    # 梳齿路径
    pl = np.array(sc.trail)
    ax.plot(pl[:, 0], pl[:, 1], color=CAR_COLOR, lw=1.1, alpha=0.8, zorder=5)

    # 小车
    ax.add_patch(Rectangle((sc.x - SWATH / 2, sc.y - 1.4), SWATH, 2.8,
                           facecolor=CAR_COLOR, edgecolor="black", lw=1.0, zorder=6))
    fx = sc.x + math.cos(sc.theta) * 3
    fy = sc.y + math.sin(sc.theta) * 3
    ax.plot([sc.x, fx], [sc.y, fy], color="black", lw=1.3, zorder=7)

    ax.set_title(title, fontsize=11)
    m = sc.metrics()
    info = (f"coverage: {m['coverage'] * 100:.1f}%   "
            f"covered: {m['covered_cells']}/{m['free_cells']} m2   "
            f"path: {m['path_length']:.1f} m   swaths: {m['swaths']}")
    ax.text(0.0, -0.09, info, transform=ax.transAxes, fontsize=9,
            color=(0.2, 0.2, 0.2))


def save_frame(sc, cmap, path, title):
    fig, ax = plt.subplots(figsize=(10.5, 7.2), dpi=110)
    draw(sc, cmap, ax, title)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def run_demo(outdir):
    os.makedirs(outdir, exist_ok=True)
    path = build_path()
    cmap = CoverageMap()
    sc = Mower(path, cmap)
    steps = 0
    while not sc.finished and steps < 12000:
        sc.step()
        steps += 1
    save_frame(sc, cmap, os.path.join(outdir, "coverage_mowing_agv_coverage.png"),
               "Coverage mowing AGV: boustrophedon full-coverage path")
    with open(os.path.join(outdir, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(sc.metrics(), f, ensure_ascii=False, indent=2)
    return sc.metrics()


def run_headless(duration, seed, outdir):
    os.makedirs(outdir, exist_ok=True)
    path = build_path()
    cmap = CoverageMap()
    sc = Mower(path, cmap, seed=seed)
    for _ in range(int(duration / DT)):
        sc.step()
        if sc.finished:
            break
    with open(os.path.join(outdir, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(sc.metrics(), f, ensure_ascii=False, indent=2)
    return sc.metrics()


def main():
    parser = argparse.ArgumentParser(description="全覆盖往复清扫 AGV 仿真")
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--duration", type=float, default=300.0)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--outdir", default="demo_out")
    args = parser.parse_args()

    if args.demo:
        m = run_demo(args.outdir)
    else:
        m = run_headless(args.duration, args.seed, args.outdir)
    print(json.dumps(m, ensure_ascii=False))


if __name__ == "__main__":
    main()
