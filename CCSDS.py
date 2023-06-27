import os
import numpy

class SpacePackets(object):
    def __init__(self, file, frame_len):
        self.bytes_in_file = os.path.getsize(file)
        self.num_frames = int(self.bytes_in_file/frame_len)
        self.filename = file
        self.syncdef = "0x1acffc1d"
        
    def read(self):
        self.bytes_file = numpy.fromfile(self.filename, dtype = "uint8")
        self.bits_file = numpy.unpackbits(self.bytes_file)
        self.bits_file = numpy.array_split(self.bits_file, self.num_frames)
    
    def getbits(self,b,e,frame_num):
        return hex(int(str(numpy.array2string(self.bits_file[frame_num][b:e]).replace("]","").replace("[","").replace(" ","")), 2))
