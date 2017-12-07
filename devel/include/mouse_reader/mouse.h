// Generated by gencpp from file mouse_reader/mouse.msg
// DO NOT EDIT!


#ifndef MOUSE_READER_MESSAGE_MOUSE_H
#define MOUSE_READER_MESSAGE_MOUSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Point32.h>

namespace mouse_reader
{
template <class ContainerAllocator>
struct mouse_
{
  typedef mouse_<ContainerAllocator> Type;

  mouse_()
    : header()
    , xy_asukoht()
    , mouse_click()
    , mouse_bool(false)  {
    }
  mouse_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , xy_asukoht(_alloc)
    , mouse_click(_alloc)
    , mouse_bool(false)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::geometry_msgs::Point32_<ContainerAllocator>  _xy_asukoht_type;
  _xy_asukoht_type xy_asukoht;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _mouse_click_type;
  _mouse_click_type mouse_click;

   typedef uint8_t _mouse_bool_type;
  _mouse_bool_type mouse_bool;




  typedef boost::shared_ptr< ::mouse_reader::mouse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mouse_reader::mouse_<ContainerAllocator> const> ConstPtr;

}; // struct mouse_

typedef ::mouse_reader::mouse_<std::allocator<void> > mouse;

typedef boost::shared_ptr< ::mouse_reader::mouse > mousePtr;
typedef boost::shared_ptr< ::mouse_reader::mouse const> mouseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mouse_reader::mouse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mouse_reader::mouse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mouse_reader

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'mouse_reader': ['/home/tudeng/silvar-rtech/src/mouse_reader/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mouse_reader::mouse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mouse_reader::mouse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mouse_reader::mouse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mouse_reader::mouse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mouse_reader::mouse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mouse_reader::mouse_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mouse_reader::mouse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8965cc635db3991b191e85ed23581bbb";
  }

  static const char* value(const ::mouse_reader::mouse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8965cc635db3991bULL;
  static const uint64_t static_value2 = 0x191e85ed23581bbbULL;
};

template<class ContainerAllocator>
struct DataType< ::mouse_reader::mouse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mouse_reader/mouse";
  }

  static const char* value(const ::mouse_reader::mouse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mouse_reader::mouse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
\n\
# Key code as defined in linux/inupt.h\n\
geometry_msgs/Point32 xy_asukoht\n\
\n\
# 'True' if key was pressed, 'False' otherwise\n\
string mouse_click\n\
bool mouse_bool\n\
\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point32\n\
# This contains the position of a point in free space(with 32 bits of precision).\n\
# It is recommeded to use Point wherever possible instead of Point32.  \n\
# \n\
# This recommendation is to promote interoperability.  \n\
#\n\
# This message is designed to take up less space when sending\n\
# lots of points at once, as in the case of a PointCloud.  \n\
\n\
float32 x\n\
float32 y\n\
float32 z\n\
";
  }

  static const char* value(const ::mouse_reader::mouse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mouse_reader::mouse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.xy_asukoht);
      stream.next(m.mouse_click);
      stream.next(m.mouse_bool);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct mouse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mouse_reader::mouse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mouse_reader::mouse_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "xy_asukoht: ";
    s << std::endl;
    Printer< ::geometry_msgs::Point32_<ContainerAllocator> >::stream(s, indent + "  ", v.xy_asukoht);
    s << indent << "mouse_click: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.mouse_click);
    s << indent << "mouse_bool: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.mouse_bool);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOUSE_READER_MESSAGE_MOUSE_H