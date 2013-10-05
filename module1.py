
import socket
import os
import urllib
import re
import httplib
import time

SITE = "ingesup1g.alwaysdata.net"

def visite(lien):
    print(lien)
    conn = httplib.HTTPConnection(SITE)
    conn.request("GET", lien)

def get_external_ip():
    import httplib
    conn = httplib.HTTPConnection(SITE)
    conn.request("GET", "/ip.php")
    r1 = conn.getresponse()
    data1 = r1.read()
    return data1

def findname():
    import platform
    return platform.node()

class config:
    import platform

    def __init__(self):

        lien = ""
        Nom = ""
        IP = ""
        self.IP = "&ip="
        self.Nom = "/reception.php?client="
        #self.Nom = "reception.php?client=MachineTest1"
        config.lien = self.Nom

class RAM():

    def __init__(self):
        ram = ""
        self.ram = "/configuration.php?ram="

import ctypes

class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("ullTotalPhys", ctypes.c_ulonglong),
        ("ullAvailPhys", ctypes.c_ulonglong),
        ("ullTotalPageFile", ctypes.c_ulonglong),
        ("ullAvailPageFile", ctypes.c_ulonglong),
        ("ullTotalVirtual", ctypes.c_ulonglong),
        ("ullAvailVirtual", ctypes.c_ulonglong),
        ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
    ]

    def __init__(self):
        # have to initialize this to the size of MEMORYSTATUSEX
        self.dwLength = ctypes.sizeof(self)
        super(MEMORYSTATUSEX, self).__init__()

def check():
    config2 = config()
    config2.Nom += findname()
    config2.IP += get_external_ip()
    config2.lien = config2.Nom + config2.IP
    visite(config2.lien)

def checkram():
    #stat = MEMORYSTATUSEX()
    #ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
    #ram = RAM()

    #if (stat.dwMemoryLoad >= 50):
    #    ram.ram += str(stat.dwMemoryLoad)
     #   visite(ram.ram)
    print("toto")
    time.sleep(2)
    checkram()

#check()
checkram()