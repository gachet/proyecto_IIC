#!/usr/bin/env python3
""" This script receives ROS messages containing the 3D coordinates of a single point and prints them out """
import rospy
from geometry_msgs.msg import PointStamped

rospy.init_node('receive_point_location')
def process_point(data):
    print("[{:.2f}, {:.2f}, {:.2f}]".format(data.point.x, data.point.y, data.point.z))
rospy.Subscriber("/my_point", PointStamped, process_point)
rospy.spin()

