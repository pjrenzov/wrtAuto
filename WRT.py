#!/usr/bin/env python3

import paramiko
from paramiko_expect import SSHClientInteraction
from parental_control import ParentalConroll

class OpenWRT():
    #initialize basic variables for the setup
    def __init__(self,ipaddr,port,user,password):
        self.ipaddr = ipaddr
        self.port = port
        self.user = user
        self.password = password
        
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #initialize connection to the router
    def ConnectRouter(self):
        try:
            self.ssh.connect(self.ipaddr,self.port,self.user,self.password)
            print("Connection Established!")
        except Exception as error_message:
            print("Connection Failed!")
            print(error_message)
    
    #run the commands on UCI commandline
    def runCommand(self,commands):
        try:
            with SSHClientInteraction(self.ssh, timeout=10, display=False) as interact:
                for command in commands:
                    interact.send(command)
                interact.expect("*.Running.*")
        except Exception as error_message:
            print("Commandline execution faild")
            print(error_message)

    def addParentalControl(self,ipaddr,name,startTime,endTime):
        try:
            self.runCommand(ParentalConroll(ipaddr, name, startTime, endTime))
            print("Success!")
        except Exception as error_message:
            print("Failed!")
            print(error_message)

    #close the connection
    def closeRouterConnection(self):
        self.ssh.close()