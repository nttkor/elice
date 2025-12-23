import rclpy
from rclpy.node import Node
from std_msgs.msg import Header


class TimePub(Node):
    """Publishes current time at 50 Hz (default)."""

    def __init__(self):
        super().__init__('time_pub')
        # [TODO 1] Header 메시지 퍼블리셔를 선언하세요. 토픽 이름은 '/time_stamped'입니다.
        self.pub = None
        # [TODO 2] 50Hz 주기로 타이머를 생성하세요. (0.02초 간격)
        self.create_timer(None, self.timer_cb)

    def timer_cb(self):
        # [TODO 3] Header 메시지 객체를 생성하세요.
        msg = None
        msg.stamp = self.get_clock().now()
        # [TODO 4] 메시지를 퍼블리시하세요.
        None


def main():
    rclpy.init()
    # [TODO 5] 노드 객체를 생성하세요.
    node = None
    # [TODO 6] 노드를 실행하세요.
    None
    node.destroy_node()
    rclpy.shutdown() 