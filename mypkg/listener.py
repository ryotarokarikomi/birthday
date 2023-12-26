# SPDX-FileCopyrightText: 2023 Ryotaro Karikomi
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from birthday_msgs.msg import Birthday

def cb(msg):
  global node
  node.get_logger().info("%s" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Birthday, "birthday", cb, 10)

rclpy.spin(node)
