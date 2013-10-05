### Run Python scripts as a service example (ryrobes.com)
### Usage : python aservice.py install (or / then start, stop, remove)

import win32service
import win32serviceutil
import win32api
import win32con
import win32event
import win32evtlogutil
import os, sys, string, time
import socket
import os
import urllib
import re
import httplib
import ctypes

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
    stat = MEMORYSTATUSEX()
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
    ram = RAM()

    if (stat.dwMemoryLoad >= 50):
        ram.ram += str(stat.dwMemoryLoad)
        visite(ram.ram)
    time.sleep(60)
    checkram()

class aservice(win32serviceutil.ServiceFramework):
   
   _svc_name_ = "Agent"
   _svc_display_name_ = "Agent_Bliss"
   _svc_description_ = "Projet Bliss 2013 - Envoi de la configuration d'un client sur le serveur de supervision"
         
   def __init__(self, args):
           win32serviceutil.ServiceFramework.__init__(self, args)
           self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)           

   def SvcStop(self):
           self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
           win32event.SetEvent(self.hWaitStop)                    
         
   def SvcDoRun(self):
      import servicemanager      
      servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,servicemanager.PYS_SERVICE_STARTED,(self._svc_name_, '')) 
      
      self.timeout = 10000     #10 seconds
      # This is how long the service will wait to run / refresh itself (see script below)

      while 1:
         # Wait for service stop signal, if I timeout, loop again
         rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
         # Check to see if self.hWaitStop happened
         if rc == win32event.WAIT_OBJECT_0:
            # Stop signal encountered
            servicemanager.LogInfoMsg("SomeShortNameVersion - STOPPED!")  #For Event Log
            break
         else:
                 #Ok, here's the real money shot right here.
                 #[actual service code between rests]
                 try:
                     check()
                     checkram()
                     print(toto)
                 except:
                     pass
                 #[actual service code between rests]


def ctrlHandler(ctrlType):
   return True
                  
if __name__ == '__main__':   
   win32api.SetConsoleCtrlHandler(ctrlHandler, True)   
   win32serviceutil.HandleCommandLine(aservice)
