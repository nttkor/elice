elicer@da1708dc75f2:~$ ros2 run warning_topic_pkg sensor_publisher
[INFO] [1766495363.355209442] [sensor_publisher]: SensorPublisher node started
Traceback (most recent call last):
  File "/home/elicer/robot_ws/src/install/warning_topic_pkg/lib/warning_topic_pkg/sensor_publisher", line 33, in <module>
    sys.exit(load_entry_point('warning-topic-pkg==0.0.0', 'console_scripts', 'sensor_publisher')())
  File "/home/elicer/robot_ws/src/install/warning_topic_pkg/lib/python3.10/site-packages/warning_topic_pkg/sensor_publisher.py", line 32, in main
    rclpy.spin(node)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
    executor.spin_once()
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 751, in spin_once
    self._spin_once_impl(timeout_sec)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 748, in _spin_once_impl
    raise handler.exception()
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/task.py", line 254, in __call__
    self._handler.send(None)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 447, in handler
    await call_coroutine(entity, arg)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 361, in _execute_timer
    await await_or_execute(tmr.callback)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 107, in await_or_execute
    return callback(*args)
  File "/home/elicer/robot_ws/src/install/warning_topic_pkg/lib/python3.10/site-packages/warning_topic_pkg/sensor_publisher.py", line 23, in publish_data
    self.publisher_.publish(None)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/publisher.py", line 74, in publish
    raise TypeError('Expected {}, got {}'.format(self.msg_type, type(msg)))
TypeError: Expected <class 'std_msgs.msg._string.String'>, got <class 'NoneType'>
[ros2run]: Process exited with failure 1
elicer@da1708dc75f2:~$ ^C
elicer@da1708dc75f2:~$ 
