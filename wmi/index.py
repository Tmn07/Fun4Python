# -*- coding: utf-8 -*- 

import os, sys 
import time 
import wmi
from mkelib import *

def get_fs_info() : 

     tmplist = [] 
     c = wmi.WMI () 
     for physical_disk in c.Win32_DiskDrive (): 
         for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
             for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
             	tmpdict = {} 
                tmpdict["Caption"] = logical_disk.Caption
                tmpdict["FreeSpace"] = round(long(logical_disk.FreeSpace)/1024.0/1024/1024,1)
                # print int(logical_disk.FreeSpace)/1024.0/1024/1024
                tmplist.append(tmpdict)
     return tmplist 

def writedown(DiskInfo):
	fp = open("Disk.md",'a')
	fp.write('\n')
	date = time.strftime("%m-%d")
	fp.write(mke.UnorderList(date))
	fp.write('\n')
	for num in xrange(len(DiskInfo)):
		fp.write("  - "+mke.EnStrong(DiskInfo[num]['Caption'])+str(DiskInfo[num]['FreeSpace'])+"GB\n")
	fp.close()
	return 1
# import os
# os.system('Disk.md')

while 1:
	fs = get_fs_info()
	writedown(fs)
	time.sleep(3600*24)