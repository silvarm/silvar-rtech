# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from motoman_msgs/DynamicJointState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class DynamicJointState(genpy.Message):
  _md5sum = "c44649b8de969b98f15adea419fa49a4"
  _type = "motoman_msgs/DynamicJointState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#group[]: # length of this array must match num_groups
#    id:   control-group ID for use on-controller
#    num_joints: # of joints in this motion group
#    valid_fields: #bit field for following items
#    # length of the following items must match num_joints, order set by controller.  Invalid fields (see bit field above) are not included, resulting in a shorter message.
#    positions[]
#    velocities[]
#    accelerations[]
#    effort[]
#    position_desired[]
#    position_errors[]
#    velocity_desired[]
#    velocity_errors[]
#    effort_desired[]
#    effort_error[]

int16 group_number
int16 num_joints
int16 valid_fields
float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
float64[] positions_desired
float64[] positions_errors
float64[] velocities_desired
float64[] velocities_errors
float64[] accelerations_desired
float64[] accelerations_errors
float64[] effort_errors
float64[] effort_desired
"""
  __slots__ = ['group_number','num_joints','valid_fields','positions','velocities','accelerations','effort','positions_desired','positions_errors','velocities_desired','velocities_errors','accelerations_desired','accelerations_errors','effort_errors','effort_desired']
  _slot_types = ['int16','int16','int16','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       group_number,num_joints,valid_fields,positions,velocities,accelerations,effort,positions_desired,positions_errors,velocities_desired,velocities_errors,accelerations_desired,accelerations_errors,effort_errors,effort_desired

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DynamicJointState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.group_number is None:
        self.group_number = 0
      if self.num_joints is None:
        self.num_joints = 0
      if self.valid_fields is None:
        self.valid_fields = 0
      if self.positions is None:
        self.positions = []
      if self.velocities is None:
        self.velocities = []
      if self.accelerations is None:
        self.accelerations = []
      if self.effort is None:
        self.effort = []
      if self.positions_desired is None:
        self.positions_desired = []
      if self.positions_errors is None:
        self.positions_errors = []
      if self.velocities_desired is None:
        self.velocities_desired = []
      if self.velocities_errors is None:
        self.velocities_errors = []
      if self.accelerations_desired is None:
        self.accelerations_desired = []
      if self.accelerations_errors is None:
        self.accelerations_errors = []
      if self.effort_errors is None:
        self.effort_errors = []
      if self.effort_desired is None:
        self.effort_desired = []
    else:
      self.group_number = 0
      self.num_joints = 0
      self.valid_fields = 0
      self.positions = []
      self.velocities = []
      self.accelerations = []
      self.effort = []
      self.positions_desired = []
      self.positions_errors = []
      self.velocities_desired = []
      self.velocities_errors = []
      self.accelerations_desired = []
      self.accelerations_errors = []
      self.effort_errors = []
      self.effort_desired = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3h.pack(_x.group_number, _x.num_joints, _x.valid_fields))
      length = len(self.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.positions))
      length = len(self.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.velocities))
      length = len(self.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.accelerations))
      length = len(self.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.effort))
      length = len(self.positions_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.positions_desired))
      length = len(self.positions_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.positions_errors))
      length = len(self.velocities_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.velocities_desired))
      length = len(self.velocities_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.velocities_errors))
      length = len(self.accelerations_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.accelerations_desired))
      length = len(self.accelerations_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.accelerations_errors))
      length = len(self.effort_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.effort_errors))
      length = len(self.effort_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.effort_desired))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.group_number, _x.num_joints, _x.valid_fields,) = _struct_3h.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.positions = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocities = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.accelerations = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.positions_desired = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.positions_errors = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocities_desired = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocities_errors = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.accelerations_desired = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.accelerations_errors = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort_errors = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort_desired = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3h.pack(_x.group_number, _x.num_joints, _x.valid_fields))
      length = len(self.positions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.positions.tostring())
      length = len(self.velocities)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.velocities.tostring())
      length = len(self.accelerations)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.accelerations.tostring())
      length = len(self.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.effort.tostring())
      length = len(self.positions_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.positions_desired.tostring())
      length = len(self.positions_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.positions_errors.tostring())
      length = len(self.velocities_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.velocities_desired.tostring())
      length = len(self.velocities_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.velocities_errors.tostring())
      length = len(self.accelerations_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.accelerations_desired.tostring())
      length = len(self.accelerations_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.accelerations_errors.tostring())
      length = len(self.effort_errors)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.effort_errors.tostring())
      length = len(self.effort_desired)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.effort_desired.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.group_number, _x.num_joints, _x.valid_fields,) = _struct_3h.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.positions_desired = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.positions_errors = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocities_desired = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocities_errors = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.accelerations_desired = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.accelerations_errors = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort_errors = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort_desired = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3h = struct.Struct("<3h")
