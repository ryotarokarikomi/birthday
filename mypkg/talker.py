# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from stop_watch_msgs.msg import Time

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Time, "time", 10)
sec = 1

class time():
  second = 1
  minute = 0
  hour = 0

def cb():
  global sec
  msg = Time()

  if time.second == 60:
    time.minute += 1
    time.second = 0

  if time.minute == 60:
    time.hour += 1
    time.minute = 0

  msg.sec = sec
  msg.second = time.second
  msg.minute = time.minute
  msg.hour = time.hour

  pub.publish(msg)
  time.second += 1
  sec += 1

node.create_timer(1, cb)
rclpy.spin(node)
