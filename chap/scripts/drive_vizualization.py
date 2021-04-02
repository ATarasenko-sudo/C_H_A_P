#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header
from matplotlib import plot as plt

def listener(event):
    rospy.init_node("listener")
    rospy.Timer(rospy.Duration(0.1), talker)
    sub = rospy.Subscriber("cmd_vel",Twist, talker)

    
    rospy.spin()


if __name__ == '__main__':
    listener()
