#!/usr/bin/env python

import rospy

from ros_tutorials_topic.msg import MsgTutorial

class TopicPublisher:
	def __init__(self):
		# Initialize
		self.publisher = MsgTutorial()
#		self.now = rospy.get_rostime()
		
		self.count = 0

		rospy.logwarn("Topic Publisher Node [ONLINE]...")

		# rospy shutdown
		rospy.on_shutdown(self.cbShutdown)

		# Publish to String
		self.publisher_topic = "ros_tutorial_msg"
		self.publisher_pub = rospy.Publisher(
						self.publisher_topic, 
						MsgTutorial, 
						queue_size=100)

		# Allow up to one second to connection
		rospy.sleep(1)

	# 
	def cbPub(self):
		# 
		self.now = rospy.get_rostime()

		#
		self.publisher.stamp = self.now
		self.publisher.data = self.count

		self.publisher_pub.publish(self.publisher)

		self.count += 1

	# rospy shutdown callback
	def cbShutdown(self):
		rospy.logerr("Topic Publisher Node [OFFLINE]...")

if __name__ == '__main__':

	# Initialize
	rospy.init_node('topic_publisher', anonymous=False)
	pub = TopicPublisher()
	
	r = rospy.Rate(10)

	# 
	while not rospy.is_shutdown():
		pub.cbPub()
		r.sleep()
