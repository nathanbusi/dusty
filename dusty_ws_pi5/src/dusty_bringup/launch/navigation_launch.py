from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os

def generate_launch_description():
    # Paths
    bringup_dir = os.path.join(
        get_package_share_directory('nav2_bringup'), 'launch')
    nav2_params_file = os.path.join(
        get_package_share_directory('dusty_bringup'),
        'params',
        'nav2_params.yaml'
    )

    # Launch Configuration
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # Include Nav2 Launch
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(bringup_dir, 'navigation_launch.py')
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'params_file': nav2_params_file
        }.items()
    )

    return LaunchDescription([
        nav2_launch
    ])
