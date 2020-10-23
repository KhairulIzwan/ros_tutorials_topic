#!/usr/bin/env python

import rospy

from ros_tutorials_topic.msg import MsgTutorial

class TopicSubscriber:
	def __init__(self):
	
		rospy.logwarn("Topic Publisher Node [ONLINE]...")

		# rospy shutdown
		rospy.on_shutdown(self.cbShutdown)

		# Subscribe to MsgTutorial
		self.subscriber_topic = "ros_tutorial_msg"
		self.subscriber_sub = rospy.Subscriber(
						self.subscriber_topic, 
						MsgTutorial, 
						self.cbSub)

		# Allow up to one second to connection
		rospy.sleep(1)

	# 
	def cbSub(self, msg):
		# 
		self.subscriber_time_sec = msg.stamp.secs
		self.subscriber_time_nsec = msg.stamp.nsecs
		self.subscriber_data = msg.data

	#
	def cbPrint(self):
		rospy.loginfo("{}:{}:{}".format(self.subscriber_time_sec, self.subscriber_time_nsec, self.subscriber_data))

	# rospy shutdown callback
	def cbShutdown(self):
		rospy.logerr("Topic Subscriber Node [OFFLINE]...")

if __name__ == '__main__':

	# Initialize
	rospy.init_node('topic_subscriber', anonymous=False)
	sub = TopicSubscriber()
	
	r = rospy.Rate(10)

	# 
	while not rospy.is_shutdown():
		sub.cbPrint()
		r.sleep()
