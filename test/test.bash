#!/bin/bash

cd ~/ros2_ws/src
git clone https://github.com/ryotarokarikomi/time_msgs.git
cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/setup.bash 
timeout 10 ros2 launch mypkg stop_watch.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'second=9'
