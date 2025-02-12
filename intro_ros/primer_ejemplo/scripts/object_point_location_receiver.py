
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PointStamped

class ReceivePointLocation(object):
    """ This node receives ROS messages containing the 3D coordinates of a single point and prints them out """

    def __init__(self):
        rospy.init_node('receive_point_location')
        rospy.Subscriber("/my_point", PointStamped, self.process_point)

    def process_point(self, data):
        print("[{:.2f}, {:.2f}, {:.2f}]".format(data.point.x, data.point.y, data.point.z))

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = ReceivePointLocation()
    node.run()
