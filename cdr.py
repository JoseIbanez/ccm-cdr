#!/usr/bin/python

import sys;
import csv;
import datetime;
import time;
import struct;
import socket;

def time_to_string(time_value):
    """convert Unix epoch time to a human readable string"""
    if not (time_value.isdigit()):
	return time_value

    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(time_value)))


def int2ip(addr):
    """ convert a 32-bit signed integer to an IP address"""

    try:
       addr=(long(addr) & 0xffffffff)
    except ValueError:
       return addr

    try:
       return socket.inet_ntoa(struct.pack("<I",int(addr)))
    except struct.error:
       print addr
       return "0.0.0.0"
    except ValueError:
       return "0.0.0.0"


#####################################################

reader = csv.reader(iter(sys.stdin.readline, ''))

row = 1
for row in reader:
  row[4]=time_to_string(row[4])  

  row[ 7]=int2ip(row[ 7]) ## Signaling Orig
  row[13]=int2ip(row[13]) ## Media Orig
  row[28]=int2ip(row[28]) ## Signaling Dest
  row[35]=int2ip(row[35]) ## Media Dest


  print ','.join([row[4],row[7],row[28],row[13],row[35],row[8],row[29],row[11],row[33],row[55],row[65],row[2],row[56],row[57]])  
  
  
