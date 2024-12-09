#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class ExampleEngine(Node):
    def __init__(self):
        super().__init__('example_engine')
        self.get_logger().info('='*50)
        self.get_logger().info('Example Engine Node has been started!')
        self.get_logger().info('Optional commands:')
        self.get_logger().info('  - teleop_keyboard')
        self.get_logger().info('  - leds')
        self.get_logger().info('  - sounds')
        self.get_logger().info('='*50)


def main(args=None):
    rclpy.init(args=args)
    node = ExampleEngine()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()