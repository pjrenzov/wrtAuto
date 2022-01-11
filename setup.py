#This script is aimed to automate majority of task done to configure sd card after is is flashed with OpenWRT firmware

#importing modules
import os
import pwd
from time import sleep

#getting username for the currnet system 




#executing commands to begin configuring
#First task is to expand the storage for openwrt

#unmound rootfs partition
Dev=str(input("Enter sd Device:\n"))
user=str(input("Enter usernam:\n"))
os.system("sudo umount /media/{}/rootfs".format(user))
os.system("sudo fdisk /dev/{} < cmds".format(Dev))
os.system("sudo e2fsck -f /dev/{}2".format(Dev))
sleep(2)
os.system("y")
sleep(2)
os.system("sudo resize2fs /dev/{}2".format(Dev))
sleep(2)
os.system("sudo umount /dev/{}1".format(Dev))