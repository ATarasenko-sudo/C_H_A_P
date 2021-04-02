#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Header
from matplotlib.pyplot as plt
import math
import scipy.integrate as integrate

r = 5
L = 20

def plt_dynamic(x, y, ax, colors=['b']):
    for color in colors:
        ax.plot(x, y, color)
    fig.canvas.draw()

def listener(event):
    rospy.init_node("listener")
    rospy.Timer(rospy.Duration(0.1), talker)
    sub = rospy.Subscriber("encoder_data",Header)
    
    x_vals = []
    y_vals = []

    #тут мы получаем значения энкодеров для правого и левого колеса, а также значение времени, по которому и интегрируем
    msg = Header()
    time = msg.head.stamp
    enc_r = msg.encoder_r 
    enc_l = msg.encoder_l

    #Тут я начал реализовывать, но можно продолжить или вовсе переписать
    w_l = (enc_l-enc_l_previous)*(2*3.1415)/(4096*time)
    w_r = (enc_r-enc_r_previous)*(2*3.1415)/(4096*time)

    V= r*(w_r + w_l )/2
    Vx=lambda t: V*cos(teta)
    x=integrate.quad(Vx, 0, time)
    Vy=lambda t: V*sin(teta)
    y=integrate.quad(Vy, 0, time)


    #Здеась записываются значения для динамического графика
    x_vals.append(x)
    y_vals.append(y)
    plt_dynamic(x_vals,y_vals)

    #Это предыдуцщие значения энкодеров и пока не совсем понял, будет ли так работать
    #Но они нужны для дельа Е(см. формулы)
    enc_l_prev = enc_l
    enc_r_prev = enc_r
    
    rospy.spin()


if __name__ == '__main__':
    listener()