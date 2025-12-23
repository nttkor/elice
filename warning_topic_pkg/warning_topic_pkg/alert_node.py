import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class AlertNode(Node):
    def __init__(self):
        super().__init__('alert_node')
        # [TODO 1] 아래 파라미터 선언을 채워보세요. (예: 'overheat', 30.0)
        self.declare_parameter('overheat', 30.0)  # 온도 임계값
        self.declare_parameter('dry', 20.0)  # 습도 임계값
        # [TODO 2] 토픽 이름은 'env_data'입니다.
        self.subscription = self.create_subscription(
            String,
            'env_data',
            self.listener_callback,
            10)
        self.get_logger().info("AlertNode started")

    def listener_callback(self, msg):
        data = msg.data
        try:
            temp_str, hum_str = data.split(',')
            temperature = float(temp_str.split(':')[1])
            humidity = float(hum_str.split(':')[1])
            if temperature > self.get_parameter('overheat').value:
                self.get_logger().warn(f"🔥 온도 초과 경고! ({temperature}°C)")
            if humidity < self.get_parameter('dry').value:
                self.get_logger().warn(f"💧 습도 낮음 경고! ({humidity}%)")
        except Exception as e:
            self.get_logger().error(f"Failed to parse message: {e}")

def main(args=None):
    rclpy.init(args=args)
    # [TODO 3] 노드 객체를 생성하세요.
    node = AlertNode()
    # [TODO 4] 노드를 실행하세요.
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
