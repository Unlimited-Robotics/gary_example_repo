#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class ExampleEngine(Node):
    def __init__(self):
        super().__init__('example_engine')
        self.get_logger().info('Example Engine Node has been started!')

def main(args=None):
    rclpy.init(args=args)
    node = ExampleEngine()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
