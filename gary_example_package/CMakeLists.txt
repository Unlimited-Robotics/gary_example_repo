cmake_minimum_required(VERSION 3.8)
project(gary_example_package)

# Find ament_cmake to enable ROS 2 build macros
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python script
install(PROGRAMS
  resource/example_engine.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch file
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Call the ament_package macro to finalize the package
ament_package()
