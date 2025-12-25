import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. ระบุตำแหน่งไฟล์ต่างๆ
    pkg_my_config = get_package_share_directory('my_slam_config')
    pkg_nav2 = get_package_share_directory('nav2_bringup')
    
    # ระบุไฟล์ Map และ Params ที่คุณทำไว้
    map_file = '/home/supawit/test02.yaml' 
    params_file = '/home/supawit/slam2d_ws/src/my_slam_config/params/my_nav2_params.yaml'
    nav2_launch_file = os.path.join(pkg_nav2, 'launch', 'bringup_launch.py')

    return LaunchDescription([

        # --- ส่วนที่ 2: เปิด Nav2 (ระบบนำทางหลัก) ---
        # ส่งคำสั่งไปที่ cmd_vel_nav เพื่อให้ Collision Monitor ตรวจก่อน
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_file),
            launch_arguments={
                'map': map_file,
                'params_file': params_file,
                'use_sim_time': 'False',
                'autostart': 'True',
                # 'cmd_vel_topic': 'cmd_vel_smoothed' # <--- สับรางตรงนี้!
            }.items(),
        ),
        
        # --- ส่วนที่ 3: เปิด Collision Monitor (ยามเฝ้าระวัง) ---
        # รับ cmd_vel_nav -> ตรวจความปลอดภัย -> ส่ง cmd_vel (ไปล้อ)
        Node(
            package='nav2_collision_monitor',
            executable='collision_monitor',
            name='collision_monitor',
            output='screen',
            parameters=[params_file],
        ),

        # --- ส่วนที่ 4: เปิด RViz ---
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', os.path.join(pkg_nav2, 'rviz', 'nav2_default_view.rviz')],
            output='screen'
        )
    ])
