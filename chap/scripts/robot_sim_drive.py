#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header

#Симулируем угловую скорость с помощью апериодического звена
def omega_simulation(angular, recent_vals, dt)
    T = 20
    beta = dt/(3*T + dt)
    w = beta*recent_vals + (1-beta)*angular.z
    return w

#вычисляем угловые скорости каждого колеса через МЦС
def w_vals(linear, W_sim)
    L = 20
    w_r = linear.y / ((linear.y/W_sim)-L/2)
    w_l = linear.y / ((linear.y/W_sim)+L/2)
    w_rl = [w_r, w_l]
    return w_rl

#Переводим значения угловых скоростей в количество меток в секунду 
def encode(Wrl):
    N = 4096
    Er = Wrl[0]* N /(2*3.1415)
    El = Wrl[1]* N /(2*3.1415)
    E_rl = [Er, El]
    return E_rl



def talker(event, linear, angular):
    rospy.init_node('enc_pub')
    

    sub = rospy.Subscriber("recent_w", String)

    recent_w = data.recent_w

    dt = event.last_duration()
    omega_sim = omega_simulation(angular,recent_w dt)
    omega_rl = w_vals(linear, omega_sim)
    enc_vals = encode(omega_rl)
    enc_r = enc_vals[0]
    enc_l = enc_vals[1]
    
    pub = rospy.Publisher("recent_w", string)

    data.recent_w = omega_sim

    pub = rospy.Publisher("encoder_data", Header)
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



    

