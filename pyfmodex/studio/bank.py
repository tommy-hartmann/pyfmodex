from ctypes import c_int, c_void_p, byref, create_string_buffer
from .bus import Bus
from .studio_object import StudioObject
from .event_description import EventDescription

class Bank(StudioObject):
    function_prefix = "FMOD_Studio_Bank"
   
    @property
    def path(self):
        required = c_int()
        self._call("GetPath", None, 0, byref(required))
        path_buffer = create_string_buffer(required.value)
        self._call("GetPath", path_buffer, len(path_buffer), None)
        return path_buffer.value.decode("utf-8")
   
    @property
    def event_count(self):
        count = c_int()
        self._call("GetEventCount", byref(count))
        return count.value

    @property
    def events(self):
        count = self.event_count
        array = (c_void_p * count)()
        written = c_int()
        self._call("GetEventList", array, count, byref(written))
        assert count == written.value
        descs = []
        for pointer in array:   
            descs.append(EventDescription(pointer))
        return descs

    @property
    def bus_count(self):
        count = c_int()
        self._call("GetBusCount", byref(count))
        return count.value
    
    @property
    def bus_list(self):
        count = self.event_count
        array = (c_void_p * count)()
        written = c_int()
        self._call("GetBusList", array, count, byref(written))
        assert count == written.value
        descs = []
        for pointer in array:   
            descs.append(Bus(pointer))
        return descs
        
    
        
