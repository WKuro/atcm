#-----------------------------------------------------------
# Author : Le Thai An EEIT2015 and Nguyen The Viet CS2015
# Organization: Vietnamese-German University
# Date created: 26-3-2016
# Place: Binh Duong Conference Center, Binh Duong New City, Vietnam
# Description: Transfering video data about traffic condition on the street, using TCP protocol 
#-----------------------------------------------------------
from engine import ClientStream
client = ClientStream(('localhost', 6000), (320, 240), 15) # Specify TCP address, Size of frame and frame per second variables
client.stream()
