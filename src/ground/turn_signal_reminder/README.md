
Enter file contents here
# turn_signal_reminder

转向灯使用提醒：根据方向盘转角与转向灯开关状态，做两类提醒——

1. **未打灯告警**：正在打方向但转向灯没开，连续若干帧后告警；
2. **忘关灯提醒**：方向盘回正后转向灯还亮着，持续若干秒后提醒关灯。

判定核心在 `scripts/reminder_core.py`，纯 Python 标准库，不依赖 CARLA、不需要显卡。

## 运行环境

- ROS Noetic（Ubuntu 20.04，Python 3）；脚本同时兼容 Python 2.7（Melodic）与 3.x
- 依赖：`rospy`、`std_msgs`、`std_srvs`（都是 ROS 标准包，无需额外安装）

## 运行步骤

```bash
# 1. 把本包放到工作空间的 src/ground/ 下，编译
cd ~/catkin_ws
catkin_make
source devel/setup.bash

# 2. 启动节点（默认参数）
roslaunch turn_signal_reminder main.launch

# 3. 另开一个终端，手动喂转角与灯状态验证
rostopic pub /vehicle/steering std_msgs/Float64 "data: 0.4" -1
rostopic pub /vehicle/turn_signal std_msgs/Bool "data: false" -1
# 连续 3 帧（10 Hz，约 0.3 s）后会在 /reminder/no_signal_warn 上看到告警

# 4. 不重启节点，直接跑内置四个场景、看 7 条断言
rosservice call /turn_signal_reminder/simulate
# 返回 success: True，message: "断言：7 通过 / 0 失败；结论：PASSED"
```

## 离线自测（不需要 ROS）

```bash
cd scripts
python3 reminder_core.py
```

预期输出 7 条 `[PASS]`，最后一行 `结论：PASSED`。

## 可调参数（都能在 roslaunch 命令行覆盖）

| 参数 | 默认 | 含义 |
|---|---|---|
| `enter_steer` | 0.25 rad | 超过它判定为在打方向 |
| `exit_steer` | 0.15 rad | 低于它判定为已回正（迟滞死区） |
| `no_signal_frames` | 3 | 未打灯告警需要连续多少帧 |
| `lamp_off_delay` | 3.0 s | 回正后灯还亮多久才提醒关灯 |
| `no_signal_cooldown` | 5.0 s | 同一次未打灯告警的冷却时间 |
| `sample_hz` | 10.0 Hz | 节点采样频率 |

例如关掉帧数确认：

```bash
roslaunch turn_signal_reminder main.launch no_signal_frames:=1
```

## 与其他模块的关系

本模块只回答「转角到没到要打灯的程度、灯该不该提醒开/关」，不负责车道保持（`carla_lane_keeping`）、盲区监测（`carla_bsd_blind_spot`）、自动灯光（`carla_auto_light`），也不直接控制车辆。
