# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from timer_msgs.msg import Timer

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Timer, "timer", 10)
sec = 1

class timer():
  second = 1
  minute = 0
  hour = 0

def cb():
  global sec
  msg = Timer()

  if timer.second == 60:
    timer.minute += 1
    timer.second = 0

  if timer.minute == 60:
    timer.hour += 1
    timer.minute = 0

  msg.sec = sec
  msg.second = timer.second
  msg.minute = timer.minute
  msg.hour = timer.hour

  pub.publish(msg)
  timer.second += 1
  sec += 1

node.create_timer(1, cb)
rclpy.spin(node)
