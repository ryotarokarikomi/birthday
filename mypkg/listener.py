# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from stopwatch_msgs.msg import Time

def cb(msg):
  global node
  node.get_logger().info("%s" % msg)

rclpy.init()
node = Node("listener")
sub = node.create_subscription(Time, "time", cb, 10)

rclpy.spin(node)
