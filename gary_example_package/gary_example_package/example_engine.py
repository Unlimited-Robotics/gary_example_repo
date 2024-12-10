#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ExampleEngine(Node):
    def __init__(self):
        super().__init__('example_engine')

        # Init messages
        self.get_logger().info('='*50)
        self.get_logger().info('Example Engine Node has been started!')
        self.get_logger().info('Optional commands:')
        self.get_logger().info('  - teleop_keyboard')
        self.get_logger().info('  - leds')
        self.get_logger().info('  - sounds')
        self.get_logger().info('='*50)

        # Publish a counter in topic 'example_topic'
        self.i = 0
        self.publisher_ = self.create_publisher(String, 'example_topic', 10)
        
        # Publisher time (every second)
        self.timer = self.create_timer(1.0, self.publish_message)

    # Published message content
    def publish_message(self):
        msg = String()
        msg.data = str(self.i) if self.i > 0 else 'Hello from example publisher!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing i = : "{msg.data}"')
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    node = ExampleEngine()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()