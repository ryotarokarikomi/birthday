#!/bin/bash

source /opt/ros/humble/setup.bash
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws/src
git clone https://github.com/ryotarokarikomi/time_msgs.git
cd $dir/ros2_ws
colcon build --symlink-install
source $dir/ros2_ws/install/setup.bash
timeout 10 ros2 launch mypkg stop_watch.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'second=9'
