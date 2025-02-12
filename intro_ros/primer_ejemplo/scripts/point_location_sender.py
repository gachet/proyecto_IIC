#!/usr/bin/env python3
""" This script publishes ROS messages containing the 3D coordinates of a single point """
import rospy
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header
from geometry_msgs.msg import Point
rospy.init_node('send_point_location')    # initialize our ROS node
my_header = Header(stamp=rospy.Time.now(), frame_id="odom")
my_point = Point(1.0, 2.0, 0.0)
my_point_stamped = PointStamped(header=my_header, point=my_point)

#Note: It's also possible to define a PointStamped message in one line, e.g.,

#my_point_stamped = PointStamped(header=Header(stamp=rospy.Time.now(),
#                                              frame_id="odom"),
#                                point=Point(1.0, 2.0, 0.0))



publisher = rospy.Publisher('/my_point', PointStamped, queue_size=10)
# rospy.Rate specifies the rate of the loop (in this case 2 Hz)
r = rospy.Rate(2)
while not rospy.is_shutdown():
    my_point_stamped.header.stamp = rospy.Time.now()    # update timestamp
    publisher.publish(my_point_stamped)
    r.sleep()
