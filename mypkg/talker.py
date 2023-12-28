# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from timer_msgs.msg import Timer

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Timer, "timer", 10)
sec = 0

class timer():
  second = 0
  minute = 0
  hour = 0

def cb():
  global sec
  msg = Timer()
  timer.second = sec

  msg.sec = sec
  msg.second = timer.second
  msg.minute = timer.minute
  msg.hour = timer.hour

  pub.publish(msg)
  sec += 1

node.create_timer(1, cb)
rclpy.spin(node)
