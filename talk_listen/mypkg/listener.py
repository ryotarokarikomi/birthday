# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person.msg import Person 

def cb(msg):
  global node
  node.get_logger().info("Listen: %d" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cb, 10)
rclpy.spin(node)
