#!/bin/bash

source install/setup.bash
mkdir tmp
touch tmp/mypkg.log
timeout 62 ros2 launch mypkg stop_watch.launch.py > tmp/mypkg.log

cat tmp/mypkg.log | grep 'minute=1, second=0'
