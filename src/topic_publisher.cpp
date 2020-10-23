// ROS Default Header File
#include "ros/ros.h"

// MsgTutorial Message File Header
// The header file is automatically created when building the package.
#include "ros_tutorials_topic/MsgTutorial.h"

// Node Main Function
int main(int argc, char **argv)
{
	// Initializes Node Name
	ros::init(argc, argv, "topic_publisher");
	
	// Node handle declaration for communication with ROS system
	ros::NodeHandle nh;
	
	// Declare publisher, create publisher 'ros_tutorial_pub' using the 'MsgTutorial'
	// message file from the 'ros_tutorials_topic' package. The topic name is
	// 'ros_tutorial_msg' and the size of the publisher queue is set to 100.
	ros::Publisher ros_tutorial_pub = nh.advertise<ros_tutorials_topic::MsgTutorial>("ros_tutorial_msg", 100);

	// Set the loop period. '10' refers to 10 Hz and the main loop repeats at 0.1 second intervals
	ros::Rate loop_rate(10);

	// Declares message 'msg' in 'MsgTutorial' message
	// file format
	ros_tutorials_topic::MsgTutorial msg;

	// Variable to be used in message
	int count = 0;

	while (ros::ok())
	{
		// Save current time in the stamp of 'msg'
		msg.stamp = ros::Time::now();

		// Save the the 'count' value in the data of 'msg'
		msg.data = count;

		// Print the 'stamp.sec' message
		ROS_INFO("send msg = %d", msg.stamp.sec);

		// Print the 'stamp.nsec' message
		ROS_INFO("send msg = %d", msg.stamp.nsec);

		// Print the 'data' message
		ROS_INFO("send msg = %d", msg.data);

		// Publishes 'msg' message
		ros_tutorial_pub.publish(msg);

		// Goes to sleep according to the loop rate defined above.
		loop_rate.sleep();

		// Increase count variable by one
		++count;
	}
	return 0;
}

