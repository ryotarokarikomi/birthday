# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from timer_msgs.msg import Timer

def cb(msg):
  global node
  node.get_logger().info("%s" % msg)

rclpy.init()
node = Node("listener")
sub = node.create_subscription(Timer, "timer", cb, 10)

rclpy.spin(node)
