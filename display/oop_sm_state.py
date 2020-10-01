#!/usr/bin/env python
import rospy
from display_block_latest import *
#import new_status
from table import *

from std_msgs.msg import String

cd = CursesDisplay()



class SmStateSub:

    def __init__(self):
        self.sub = rospy.Subscriber("/ilogistics_2_0011/mode/sm_state", String, self.callback)
        
    def callback(self, data):
        self.data = data.data
        # cd.smStateUi(data.data)
        #cd.table(data.data)

if __name__ == '__main__':
    rospy.init_node('state_machine', anonymous=True)
    SmStateSub()
    rospy.spin()
