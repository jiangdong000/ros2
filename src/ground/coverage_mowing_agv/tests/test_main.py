# -*- coding: utf-8 -*-
"""全覆盖往复清扫 AGV 的纯逻辑与 headless 回归测试。"""

import json
import os
import sys
import unittest

os.environ["MPLBACKEND"] = "Agg"

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(_HERE))

import main  # noqa: E402


class PathTest(unittest.TestCase):
    def test_snake_path_alternates_direction(self):
        path = main.build_path()
        # 相邻条带的横向起点方向相反（蛇形换向）
        self.assertLess(path[0][0], path[2][0])
        self.assertGreater(path[2][0], path[4][0])

    def test_path_coords_inside_field(self):
        for x, y in main.build_path():
            self.assertGreaterEqual(x, main.FIELD_X0)
            self.assertLessEqual(x, main.FIELD_X1)
            self.assertGreaterEqual(y, main.FIELD_Y0)
            self.assertLessEqual(y, main.FIELD_Y1)


class CoverageTest(unittest.TestCase):
    def test_obstacle_excluded_from_free_cells(self):
        cmap = main.CoverageMap()
        self.assertEqual(cmap.free_cells(), cmap.nx * cmap.ny - int(
            (main.OBSTACLE[3] - main.OBSTACLE[1]) *
            (main.OBSTACLE[2] - main.OBSTACLE[0])))

    def test_mark_covers_nearby_cells(self):
        cmap = main.CoverageMap()
        cmap.mark(20.0, 35.0, 3.5)
        self.assertGreater(cmap.covered_cells(), 10)
        # 障碍网格不被计入覆盖
        self.assertFalse(cmap.covered[30, 50])

    def test_full_coverage_run(self):
        path = main.build_path()
        cmap = main.CoverageMap()
        sc = main.Mower(path, cmap)
        for _ in range(12000):
            sc.step()
            if sc.finished:
                break
        m = sc.metrics()
        self.assertTrue(m["finished"])
        self.assertGreaterEqual(m["coverage"], 0.95)

    def test_determinism_same_seed(self):
        def run(seed):
            cmap = main.CoverageMap()
            sc = main.Mower(main.build_path(), cmap, seed=seed)
            for _ in range(12000):
                sc.step()
                if sc.finished:
                    break
            return sc.metrics()
        self.assertEqual(json.dumps(run(seed=5), sort_keys=True),
                         json.dumps(run(seed=5), sort_keys=True))


if __name__ == "__main__":
    unittest.main()
