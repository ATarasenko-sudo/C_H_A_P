#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header


def enc_vals(linear, angular)
    L = 20
    r = 5
    V = data.linear.x #or y
    w = data.angular.z
    w_l = (2*V + w*L)/(2*r)
    w_r = (2*V + r*w_l)/r
    w_rl = [w_r, w_l]
    return w_rl


def talker(linear, angular):
    rospy.init_node('enc_pub')
    pub = rospy.Publisher("encoder_data", Header)
    msg = Header()
    msg.head.stamp = rospy.Time.now()
    msg.encoder_r = enc_r
    msg.encoder_l = enc_l
    pub.publish(msg)


def listener():
    rospy.init_node("listener")
    sub = = rospy.Subscriber("cmd_vel",Twist, talker)
    
    rospy.spin()


if __name__ == '__main__':
    listener()



    

