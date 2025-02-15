from launch import LaunchDescription
from launch.actions import TimerAction, ExecuteProcess
from launch_ros.actions import LifecycleNode

def generate_launch_description():
    slam_node = LifecycleNode(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',
        name='slam_toolbox',
        namespace='',
        output='screen',
        parameters=[{
            'use_sim_time': False,
            'slam_toolbox_mapping': True
        }],
    )

    configure_slam = TimerAction(
        period=2.0,  # Wait 2 seconds before configuring
        actions=[
            ExecuteProcess(
                cmd=["ros2", "lifecycle", "set", "/slam_toolbox", "configure"],
                output="screen"
            )
        ]
    )

    activate_slam = TimerAction(
        period=4.0,  # Wait 4 seconds before activating (after configuring)
        actions=[
            ExecuteProcess(
                cmd=["ros2", "lifecycle", "set", "/slam_toolbox", "activate"],
                output="screen"
            )
        ]
    )

    return LaunchDescription([slam_node, configure_slam, activate_slam])
