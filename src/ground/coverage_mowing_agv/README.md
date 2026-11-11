# coverage_mowing_agv

纯 NumPy + Matplotlib 的 **区域全覆盖往复清扫 AGV** 二维仿真：给定矩形作业区与
一处矩形障碍，按牛耕式（boustrophedon）往复条带规划覆盖路径，小车沿梳齿路径
逐行清扫，1 m 网格统计已覆盖面积并计算覆盖率；穿越障碍所在条带时自动绕开障碍
区段。不依赖 ROS / Gazebo / CARLA / MuJoCo。

对应文档：[`docs/ground/coverage_mowing_agv.md`](../../../docs/ground/coverage_mowing_agv.md)

## 文件

```
main.py                              覆盖路径规划、网格覆盖统计、小车巡航、渲染与 CLI
requirements.txt                     numpy、matplotlib
tests/test_main.py                   蛇形换向、障碍剔除、全覆盖跑通、确定性回归测试
```

## 环境

- Python 3.8+

```bash
pip install -r requirements.txt
```

## 运行

在仓库根目录执行：

```bash
python src/ground/coverage_mowing_agv/main.py --demo --outdir demo_out
```

`--demo` 跑完整个作业区并保存 `coverage_mowing_agv_coverage.png` 到 `demo_out/`。

无窗口评测：

```bash
python src/ground/coverage_mowing_agv/main.py --headless --duration 300 --outdir demo_out
```

## 覆盖路径规划

- 清扫带宽 `SWATH = 6 m`，条带中心线沿 y 方向每隔 6 m 一条；
- 偶数条带左→右、奇数条带右→左，蛇形换向衔接；
- 障碍所在 y 区间内的条带拆成障碍左右两段，绕过矩形障碍；
- 小车沿路径点巡航，覆盖统计以车位为中心、带宽半径内的可作业网格。

## 指标

`metrics.json` 字段：

| 字段 | 含义 |
|---|---|
| `finished` | 是否到达最后路径点 |
| `path_length` | 累计行驶里程（米） |
| `covered_cells` | 已覆盖网格数（等价平方米） |
| `free_cells` | 可作业网格数（总面积扣除障碍） |
| `coverage` | 覆盖率 = covered / free |
| `swaths` | 条带数量 |

## 测试

```bash
python -m unittest discover -s src/ground/coverage_mowing_agv/tests -v
```

## 参数

| 参数 | 默认值 | 说明 |
|---|---|---|
| `SWATH` | 6.0 m | 清扫带宽（车宽） |
| `CELL` | 1.0 m | 覆盖统计网格边长 |
| `SPEED` | 8.0 m/s | 巡航速度 |
| `ARRIVE_R` | 1.0 m | 路径点到达判定半径 |
| `DT` | 1/30 s | 固定仿真步长 |

## 限制

- 覆盖统计为离散网格近似，圆形覆盖半径留有半格余量，边角为保守覆盖。
- 障碍为单个矩形，未处理多个障碍、窄通道连通性与重复覆盖优化。
- 路径为开放式往复，未做转弯半径与掉头轨迹约束。
