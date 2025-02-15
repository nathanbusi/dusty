from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Start the RPLIDAR node
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            name='rplidar',
            output='screen',
            parameters=[{'serial_port': '/dev/ttyUSB0'},  # Update if needed
                        {'frame_id': 'laser_frame'}],
        ),

        # Start SLAM Toolbox (for ROS 2 Jazzy)
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{'use_sim_time': False}],
        )
    ])
