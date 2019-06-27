from ctypes import c_int, c_void_p, byref, create_string_buffer
from .studio_object import StudioObject
from ..channel_group import ChannelGroup


class Bus(StudioObject):
    function_prefix = "FMOD_Studio_Bus"
    
    @property
    def path(self):
        required = c_int()
        self._call("GetPath", None, 0, byref(required))
        path_buffer = create_string_buffer(required.value)
        self._call("GetPath", path_buffer, len(path_buffer), None)
        return path_buffer.value.decode("utf-8")
        
    @property
    def channel_group(self):
        ptr = c_void_p()
        self._call("GetChannelGroup", byref(ptr))
        return ChannelGroup(ptr)
