#!/bin/bash

colcon build
source install/setup.bash
timeout 62 ros2 launch mypkg stop_watch.launch.py > tmp/mypkg.log

cat tmp/mypkg.log | grep 'minute=1, second=0'
