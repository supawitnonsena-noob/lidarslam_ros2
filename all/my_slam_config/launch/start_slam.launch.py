import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    pkg_my_config = get_package_share_directory('my_slam_config')
    slam_config_file = os.path.join(pkg_my_config, 'config', 'my_slam_params.yaml')


    pkg_slam_toolbox = get_package_share_directory('slam_toolbox')
    slam_launch_file = os.path.join(pkg_slam_toolbox, 'launch', 'online_async_launch.py')

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_launch_file),
            launch_arguments={'slam_params_file': slam_config_file}.items()
        )
    ])
