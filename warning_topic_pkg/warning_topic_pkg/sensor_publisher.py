import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        # [TODO 1] 토픽 이름은 'env_data'입니다.
        self.publisher_ = self.create_publisher(String, 'env_data', 10)
        self.timer = self.create_timer(1.0, self.publish_data)
        self.get_logger().info("SensorPublisher node started")

    def publish_data(self):
        temperature = round(random.uniform(20.0, 40.0), 1)
        humidity = round(random.uniform(10.0, 50.0), 1)

        # [TODO 2] 아래 None을 메시지 객체로 바꿔보세요. 메시지 객체는 String 타입입니다.
        msg = String()
        msg.data = f"temperature:{temperature},humidity:{humidity}"
        
        # [TODO 3] publisher가 메시지를 퍼블리시하는 코드를 작성하세요.
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    # [TODO 4] 노드 객체를 생성하세요.
    node = SensorPublisher()
    # [TODO 5] 노드를 실행하세요.
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

