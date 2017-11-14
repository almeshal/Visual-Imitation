#!/usr/bin/env python

######################################################################################################
import rospy
import math
import baxter_interface
import roslib; roslib.load_manifest("moveit_python")
from moveit_python import PlanningSceneInterface, MoveGroupInterface
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray
rospy.init_node('Mover')

#numero = 0.00

def moveToZero():
	limb_right = baxter_interface.Limb('right')
	limb_left = baxter_interface.Limb('left')

	right = {'right_s0': 0.00, 'right_s1': 0.00, 'right_w0': 0.00, 'right_w1': 0.00, 'right_w2': 0.00, 'right_e0': 0.00, 'right_e1': 0.00}
	left = {'left_s0': 0.00, 'left_s1': 0.00, 'left_w0': 0.00, 'left_w1': 0.00, 'left_w2': 0.00, 'left_e0': 0.00, 'left_e1': 0.00}

	limb_right.move_to_joint_positions(right,5)
	limb_left.move_to_joint_positions(left,5)

def moveTo(name, post):
	limb = baxter_interface.Limb(name)
	if name == 'left':
		moving = {'left_s0': post[0], 'left_s1': post[1], 'left_w0': post[2], 'left_w1': post[3], 'left_w2': post[4], 'left_e0': post[5], 'left_e1': post[6]}
	else:
		moving = {'right_s0': post[0], 'right_s1': post[1], 'right_w0': post[2], 'right_w1': post[3], 'right_w2': post[4], 'right_e0': post[5], 'right_e1': post[6]}

	limb.move_to_joint_positions(moving,3)

def moveTo2(postL,postR):
	limb_left = baxter_interface.Limb('left')
	limb_right = baxter_interface.Limb('right')

	left = {'left_s0': postL[0], 'left_s1': postL[1], 'left_w0': postL[2], 'left_w1': postL[3], 'left_w2': postL[4], 'left_e0': postL[5], 'left_e1': postL[6]}
	right = {'right_s0': postR[0], 'right_s1': postR[1], 'right_w0': postR[2], 'right_w1': postR[3], 'right_w2': postR[4], 'right_e0': postR[5], 'right_e1': postR[6]}

	limb_right.move_to_joint_positions(right,3)
	limb_left.move_to_joint_positions(left,3)

moveToZero()
while True:
	temp = rospy.wait_for_message("chatter", Float64MultiArray)
	#print temp.data[1]
	#radi1 = 3.14 - radi1
	posL = [temp.data[0], temp.data[1], temp.data[4], temp.data[5], 0.0, temp.data[2], temp.data[3]]
	#pos1 = [1, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	posR = [temp.data[6], temp.data[7], temp.data[10], temp.data[11], 0.0, temp.data[8], temp.data[9]]
	#pos13 = [radi3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	#pos2 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 1.59225918246029519]
	#lpos1 = [-1.441426162661994, 0.8389151064712133, 0.14240920034028015, -0.14501001475655606, -1.7630090377446503, -1.5706376573674472, 0.09225918246029519]

	#rpos1 = [1.8342575250183106, 1.8668546167236328, -0.45674277907104494, -0.21667478604125978, -1.2712865765075685, 1.7472041154052735, -2.4582042097778323]
	#lpos2 = [-0.949534106616211, 1.4994662184448244, -0.6036214393432617, -0.7869321432861328, -2.4735440176391603, -1.212228316241455, -0.8690001153442384]

	#moveToZero()
	#moveTo('right', posR)
	#moveTo('left', posL)
	moveTo2(posL,posR)


quit()
