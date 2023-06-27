# SpacePacketsPy
Really short library to decode space packets as per the CCSDS standard

# Usage

```
import CCSDS

x = SpacePackets('meteor_m2_lrpt.cadu',1024) #File to read, frame length in bytes
x.read() #Ingest entire file
x.getbits(0,32,0) #Test grabbing the sync word
>>> '0x1acffc1d'
```
