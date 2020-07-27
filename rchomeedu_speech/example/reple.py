#!/usr/bin/python


import rospy

from std_msgs.msg import String
def control(data):
 print(data.data)
 if " i hate you" in data.data.lower():
	print("okay")
 elif "up" in data.data.lower():
	print("dreaming")
 elif"down" in data.data.lower():
	print("dun be that")
 elif"left" in data.data.lower():
	print("okay")






if __name__ == "__main__":
    rospy.init_node("command_control")


    rospy.Subscriber("lm_data", String, control)
  	
    rospy.spin()
