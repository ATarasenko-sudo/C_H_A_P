#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header


def w_vals(linear, angular)
    L = 20
    r = 5
    V = data.linear.x #or y
    w = data.angular.z
    w_l = (2*V + w*L)/(2*r)
    w_r = (2*V + r*w_l)/r
    w_rl = [w_r, w_l]
    return w_rl


def talker(event, linear, angular):
    rospy.init_node('enc_pub')
    pub = rospy.Publisher("encoder_data", Header)
    omegi = w_vals(linear, angular)
    dt = event.last_duration
    msg = Header()
    msg.head.stamp = rospy.Time.now()
    msg.encoder_r = enc_r
    msg.encoder_l = enc_l
    pub.publish(msg)


def listener(event):
    rospy.init_node("listener")
    rospy.Timer(rospy.Duration(0.1), talker)
    sub = rospy.Subscriber("cmd_vel",Twist, talker)

    
    rospy.spin()


if __name__ == '__main__':
    listener()



    

