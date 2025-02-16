#!/usr/bin/env python3
​
# TOPICS:
#   cmd_vel: publish to, used for setting robot velocity
#   scan   : subscribing, where the wall is
​
import rospy
​
# msg needed for /scan.
from sensor_msgs.msg import LaserScan
​
# msgs needed for /cmd_vel.
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
​
# How close we will get to wall.
distance = 0.4
​
class StopAtWall(object):
    """ This node walks the robot to wall and stops """
​
    def __init__(self):
        # Start rospy node.
        rospy.init_node("walk_to_wall")
​
        # Declare our node as a subscriber to the scan topic and
        #   set self.process_scan as the function to be used for callback.
        rospy.Subscriber("/scan", LaserScan, self.process_scan)
​
        # Get a publisher to the cmd_vel topic.
        self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
​
        # Create a default twist msg (all values 0).
        lin = Vector3()
        ang = Vector3()
        self.twist = Twist(linear=lin,angular=ang)
​
    def process_scan(self, data):
        # Determine closeness to wall by looking at scan data from in front of
        #   the robot, set linear velocity based on that information, and
        #   publish to cmd_vel.
​
        # The ranges field is a list of 360 number where each number
        #   corresponds to the distance to the closest obstacle from the
        #   LiDAR at various angles. Each measurement is 1 degree apart.
​
        # The first entry in the ranges list corresponds with what's directly
        #   in front of the robot.
​
        if (data.ranges[0] >= distance or data.ranges[1] >= distance or data.ranges[2] >= distance or data.ranges[3] >= distance or data.ranges[4] >= distance or data.ranges[5] >= distance or data.ranges[6] >= distance or data.ranges[7] >= distance or data.ranges[8] >= distance or data.ranges[9] >= distance or data.ranges[10] >= distance or data.ranges[230] >= distance or data.ranges[231] >= distance or data.ranges[232] >= distance or data.ranges[233] >= distance or data.ranges[234] >= distance or data.ranges[235] >= distance or data.ranges[236] >= distance or data.ranges[237] >= distance or data.ranges[238] >= distance or data.ranges[239] >=  distance):
            # Go forward if not close enough to wall.
            self.twist.linear.x = 0.1
        else:
            # Close enough to wall, stop.
            self.twist.linear.x = 0
​
        # Publish msg to cmd_vel.
        self.twist_pub.publish(self.twist)
​
​
    def run(self):
        # Keep the program alive.
        rospy.spin()
​
if __name__ == '__main__':
    # Declare a node and run it.
    node = StopAtWall()
    node.run()
