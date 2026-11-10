Enter file contents here
cmake_minimum_required(VERSION 3.0.2)
project(turn_signal_reminder)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  std_srvs
)

catkin_package()

# 三个脚本都要装：main.py 是入口，reminder_core.py 是纯逻辑（可离线测试），
# reminder_node.py 是 ROS 节点
catkin_install_python(PROGRAMS
  scripts/main.py
  scripts/reminder_core.py
  scripts/reminder_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
