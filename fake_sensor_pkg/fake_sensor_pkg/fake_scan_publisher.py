# ===== 1. 필요한 라이브러리 import =====
import rclpy                        # ROS 2 Python 기본 라이브러리
from rclpy.node import Node         # 노드 클래스 (모든 ROS 2 노드의 기본)
from sensor_msgs.msg import LaserScan  # 레이저 스캔 메시지 타입
import random                       # 랜덤 값 생성용
import math                         # 수학 연산 (각도 계산)

class FakeScanPublisher(Node):
    def __init__(self):
        # ===== 2. 노드 초기화 =====
        super().__init__('fake_scan_publisher')  # 노드 이름 설정
        # 부모 클래스(Node) 초기화 - ROS 2 시스템에 노드 등록
        
        # ===== 3. 퍼블리셔 생성 =====
        self.publisher_ = self.create_publisher(LaserScan, '/fake_scan', 10)
        # LaserScan: 발행할 메시지 타입 (레이저 스캔 데이터)
        # '/fake_scan': 토픽 이름 (다른 노드가 구독할 주소)
        # 10: 큐 크기 (메시지 버퍼링 개수 - 네트워크 지연 대비)
        
        # ===== 4. 타이머 설정 =====
        self.timer = self.create_timer(0.5, self.publish_scan)
        # 0.5: 0.5초마다 실행 (2Hz 주기) - 실제 라이다는 보통 10-20Hz
        # self.publish_scan: 호출할 함수 (콜백 함수)
        # 실제 라이다 센서도 주기적으로 스캔 데이터를 보냅니다.
        
        self.get_logger().info('FakeScanPublisher node started')
        # 노드 시작 로그 출력 (디버깅 및 상태 확인용)

    def publish_scan(self):
        # ===== 5. LaserScan 메시지 생성 =====
        scan = LaserScan()  # 빈 LaserScan 메시지 생성
        
        # ===== 6. 헤더 정보 설정 =====
        scan.header.stamp = self.get_clock().now().to_msg()
        # 현재 시간을 타임스탬프로 설정 (데이터 생성 시점 기록)
        # ROS 2에서 시간 동기화와 데이터 시퀀스 추적에 중요합니다.

        # TODO 1: 좌표계 이름을 문자열로 지정하세요
        scan.header.frame_id = None  # 여기에 좌표계 이름 입력
        # 힌트: 'laser_frame', 'base_scan', 'lidar_link' 중 하나를 선택
        # 권장: 'laser_frame' (LaserScan은 센서 중심 좌표계가 일반적)
        # 
        # 💡 frame_id 선택 가이드:
        # - 'laser_frame': 센서 중심 좌표계 (가장 일반적)
        # - 'map': 전역 좌표계 (맵핑/내비게이션용) 
        # - 'base_link': 로봇 중심 좌표계
        
        # ===== 7. 스캔 범위 설정 =====
        scan.angle_min = -math.pi/2     # 시작 각도 (힌트: -math.pi/2 = -90도)
        scan.angle_max = math.pi/2     # 끝 각도 (힌트: math.pi/2 = +90도)
        
        scan.angle_increment = math.pi/180  # 각도 간격 (힌트: math.pi/180 = 1도)
        
        # ===== 8. 거리 측정 범위 설정 =====
        scan.range_min = 0.1        # 최소 측정 거리 (힌트: 0.1)
        scan.range_max = 3.5        # 최대 측정 거리 (힌트: 3.5)
        
        # ===== 9. 측정 점 개수 계산 =====
        num_readings = int((scan.angle_max - scan.angle_min) / scan.angle_increment)
        # (90° - (-90°)) / 1° = 180개의 측정점
        # 각 각도마다 하나의 거리 값이 필요
        
        # ===== 10. 가상 거리 데이터 생성 =====
        scan.ranges = [random.uniform(0.2, 2.0) for _ in range(num_readings)]
        # 각 각도에 대해 0.2~2.0m 사이의 랜덤 거리 생성
        # 실제로는 장애물까지의 실제 거리가 들어감
        # 실제 라이다: 레이저 반사 시간으로 거리 계산
        
        # ===== 11. 메시지 발행 =====
        self.publisher_.publish(scan)
        # 완성된 LaserScan 메시지를 '/fake_scan' 토픽으로 발행
        
        self.get_logger().info('Published fake LaserScan')
        # 발행 완료 로그 (디버깅용)

def main(args=None):
    # ===== 12. 메인 함수 (노드 실행부) =====
    rclpy.init(args=args)           # ROS 2 시스템 초기화
    node = FakeScanPublisher()      # 노드 인스턴스 생성
    rclpy.spin(node)                # 노드 실행 (무한 루프, 콜백 처리)
    node.destroy_node()             # 노드 정리 (메모리 해제)
    rclpy.shutdown()                # ROS 2 시스템 종료

if __name__ == '__main__':
    main()