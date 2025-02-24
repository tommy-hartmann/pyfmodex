from enum import Enum

class PLAYBACK_STATE(Enum):
    PLAYING = 0
    SUSTAINING = 1
    STOPPED = 2
    STARTING = 3
    STOPPING = 4
    
class STOP_MODE(Enum):
    STOP_ALLOWFADEOUT = 0
    STOP_IMMEDIATE = 1