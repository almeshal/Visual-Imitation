
// %Tag(FULLTEXT)%
#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <cmath>

int main( int argc, char** argv )
{
  ros::init(argc, argv, "points_and_lines");
  ros::NodeHandle n;
  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);

  ros::Rate r(30);

  float f = 0.0;
  while (ros::ok())
  {
// %Tag(MARKER_INIT)%
    visualization_msgs::Marker points, line_strip, line_list;
    points.header.frame_id = line_strip.header.frame_id = line_list.header.frame_id = "/my_frame";
// %EndTag(MARKER_INIT)%

// %Tag(ID)%

// %EndTag(ID)%

// %Tag(TYPE)%
    points.type = visualization_msgs::Marker::POINTS;

// %EndTag(TYPE)%

// %Tag(SCALE)%
    // POINTS markers use x and y scale for width/height respectively
    points.scale.x = 0.1;
    points.scale.y = 0.1;
    points.scale.z = 0.1;

    // LINE_STRIP/LINE_LIST markers use only the x component of scale, for the line width

// %EndTag(SCALE)%

// %Tag(COLOR)%
    // Points are green
    points.color.g = 1.0f;
    points.color.a = 1.0;

    // Line strip is blue

    // Line list is red

// %EndTag(COLOR)%

// %Tag(HELIX)%
    // Create the vertices for the points and lines

      geometry_msgs::Point p1,p2;
      p1.x = 200*0.002;
      p1.y = 156*0.002;
      p1.z = 2000*0.002;
      p2.x = 0*0.002;
      p2.y = 0*0.002;
      p2.z = 0*0.002;

      points.points.push_back(p1);
      points.points.push_back(p2);

      // The line list needs two points for each line


// %EndTag(HELIX)%

    marker_pub.publish(points);

    r.sleep();

  }
}
// %EndTag(FULLTEXT)%
