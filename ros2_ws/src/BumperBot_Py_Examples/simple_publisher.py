import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):

    def __init__(self):
        super().__init__("simple_publisher")
        self.pub = self.create_publisher(String, "chatter", 10)
        self.counter = 0
        self.timer_period = 1.0
        frequency_hz = 1.0 / self.timer_period
        self.get_logger().info("Publishing at %.1f Hz" % frequency_hz)
        self.timer = self.create_timer(self.timer_period, self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter
        self.pub.publish(msg)
        self.counter += 1

def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
