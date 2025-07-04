from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
from pathlib import Path

def generate_launch_description():

    arduinobot_description_dir = get_package_share_directory("arduinobot_description")


    model_arg = DeclareLaunchArgument(
        name = "model2",
        default_value=os.path.join(arduinobot_description_dir,"urdf",
                                   "arduinobot.urdf.xacro"),
                                   description="Path to the URDF file"
                                   #I genuinely hate python launch files ffs
    )

    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model2")]))

    robot_state_publisher = Node(
        package = "robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )


    joint_state_publisher_gui = Node(
        package = "joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )


    rviz_node = Node(
        package = "rviz2",
        executable= "rviz2",
        name = "rviz2",
        output = "screen",
        arguments = ["-d", os.path.join(get_package_share_directory("arduinobot_description"), "rviz", "display.rviz")]
    )


    return LaunchDescription([
        model_arg,
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz_node
    ])