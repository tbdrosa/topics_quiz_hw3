#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

twist = Twist()
twist.linear.x = 1
twist.angular.z = 0


def turnl():
    twist.angular.z = 1
    twist.linear.x = 0


def stop():
    twist.angular.z = 0
    twist.linear.x = 0


def callback(msg):

    readf = msg.ranges[360]
    # readl = msg.ranges[719]
    readr = msg.ranges[0]
    # print(readl, readf, readr)
    pub.publish(twist)
    a = 0.5
    if readf < a:
        stop()
        turnl()
    if readr - a < float(1/100000) and readf == float('Inf'):
        stop()
        twist.linear.x = 1


rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=3)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.spin()
