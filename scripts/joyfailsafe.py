#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int8
import pygame as pg

def talker():
    pub = rospy.Publisher('failsafe', Int8, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
         pg.init()
         pg.joystick.init()
    	 joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
  	 if len(joysticks) > 0:
             pub.publish(1)
         else:
             pub.publish(0)
         pg.quit()
         rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
