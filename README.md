# ROS2 Manipulators:

A simple robotic arm with grippers, built using ROS 2, URDF/XACRO, and MoveIt. This project demonstrates basic manipulator design, simulation, and motion planning.

## Features
- 6-DOF robotic arm (custom design)
- Gripper support
- ROS 2 control integration
- MoveIt motion planning
- Simulated in Gazebo

## Technologies Used
- ROS 2 (tested with Jazzy)
- Gazebo
- URDF / XACRO
- MoveIt

## How to Launch

1. **Launch the robot in Gazebo:**
   ros2 launch arduinobot_description gazebo.launch.py
2. **Start the ROS2 controllers:**
   ros2 launch arduinobot_controller controller.launch.py
3. **Launch MovevIt for motion planning:**
   ros2 launch arduinobot_moveit moveit.launch.py

Once MoveIt is running, you can plan and execute trajectories using the MoveIt Rviz interface.

## License:
This project is open-source. Feel free to use, modify and share.
