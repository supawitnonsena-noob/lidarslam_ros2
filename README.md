## 2D
-slamtoolbox
-nav2
-myslamconfig
-velodyne
ขั้นตอนการ run
## SLAM
### Terminal 1
```
 source <your workspace>
ros2 launch lidarslam lidarslam.launch.py
```
### Terminal 2
```
 source <your workspace>
ros2 launch my_slam_config start_slam.launch.py

```
## NAV2
### Terminal 1
```
 source <your workspace>
ros2 launch lidarslam lidarslam.launch.py
```
### Terminal 2
```
 source <your workspace>
ros2 launch my_slam_config start_nav.launch.py

```



## 3D
-lidarslam_ros2(rsasaki0109 ) 
-lidar_localization_ros2(rsasaki0109 ) (ยังไม่ทำ)
-nav2(ยังไม่ทำ)


ไฟล์ทุกอย่างยกเว้น lidarslam_ros2 อยู่ใน all