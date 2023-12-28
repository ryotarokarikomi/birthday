#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 62 ros2 launch mypkg stop_watch.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'minute=1, second=0'
