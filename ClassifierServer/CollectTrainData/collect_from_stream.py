#-----------------------------------------------------------
# Author : Le Thai An EEIT2015 and Nguyen The Viet CS2015
# Organization: Vietnamese-German University
# Date created: 26-3-2016
# Place: Binh Duong Conference Center, Binh Duong New City, Vietnam
# Description: Receive jpeg stream from client (stream_client.py), simulating receive data from camera on the street.  
#-----------------------------------------------------------
from engine import StreamHandler
server = StreamHandler(('0.0.0.0', 6000)) # Specify binding TCP address for StreamHandler server
server.start()
