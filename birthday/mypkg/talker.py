# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
import datetime
from rclpy.node import Node
from birthday_msgs.msg import Birthday

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Birthday, "birthday", 10)

class birth:
  year = 2000
  month = 9
  day = 13
  hour = 0
  minute = 0
  second = 0

def cb():
  date = datetime.datetime.now()
  msg = Birthday()
  
  msg.name = "Ryotaro Karikomi"
  age = date.year - birth.year
  month = date.month - birth.month
  day = date.day - birth.day
  hour = date.hour  - birth.hour
  minute = date.minute - birth.minute
  second = date.second - birth.second

  msg.age = age
  msg.month = month
  msg.day = day
  msg.hour = hour
  msg.minute = minute
  msg.second = second
  pub.publish(msg)

node.create_timer(1, cb)
rclpy.spin(node)
