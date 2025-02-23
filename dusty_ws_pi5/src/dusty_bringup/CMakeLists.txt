cmake_minimum_required(VERSION 3.5)
project(dusty_bringup)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(bringup_node src/bringup_node.cpp)
ament_target_dependencies(bringup_node rclcpp std_msgs)

install(TARGETS
  bringup_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
