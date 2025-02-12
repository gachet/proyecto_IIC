

#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point, PointStamped
from std_msgs.msg import Header

class SendPointLocation(object):
    """ This node publishes ROS messages containing the 3D coordinates of a single point """

    def __init__(self):
        rospy.init_node('send_point_location')
        self.point_location_pub = rospy.Publisher('/my_point', PointStamped, queue_size=10)

    def run(self):
        my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
        my_point = Point(1.0, 2.0, 0.0)
        my_point_stamped = PointStamped(header=my_header, point=my_point)

        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            my_point_stamped.header.stamp = rospy.Time.now()
            self.point_location_pub.publish(my_point_stamped)
            r.sleep()

if __name__ == '__main__':
    node = SendPointLocation()
    node.run()
