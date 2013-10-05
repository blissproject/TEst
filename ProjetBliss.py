import win32service
import win32serviceutil
import win32event
import urllib.request
import socket
import os

SITE = "http://ingesup1g.alwaysdata.net/"

def visite(lien):
    print (lien)
    req = urllib.request.Request(lien)
    response = urllib.request.urlopen(req)
    the_page = response.read()

def find():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip =  s.getsockname()[0]
    s.close()
    return ip

class config:
    import platform

    def __init__(self):

        lien = ""
        Nom = ""
        IP = ""
        self.IP = "&ip="
        self.Nom = "reception.php?client=" + platform.node()
        #self.Nom = "reception.php?client=MachineTest1"
        config.lien = self.Nom

class RAM():

    def __init__(self):
        ram = ""
        self.ram = "configuration.php?ram="

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
    config2.IP += find()
    config2.lien += config2.IP
    lien = SITE + config2.lien
    visite(lien)

def checkram():
    stat = MEMORYSTATUSEX()
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
    ram = RAM()

    if (stat.dwMemoryLoad >= 50):
        ram.ram += str(stat.dwMemoryLoad)
        lien = SITE + ram.ram
        visite(lien)
    threading.Timer(20, checkram).start()


class PySvc(win32serviceutil.ServiceFramework):
    # you can NET START/STOP the service by the following name
    _svc_name_ = "PySvc1"
    # this text shows up as the service name in the Service
    # Control Manager (SCM)
    _svc_display_name_ = "Bliss_agent1"
    # this text shows up as the description in the SCM
    _svc_description_ = "This service insert datas into a MySQL database"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    # core logic of the service   
    def SvcDoRun(self):

        import servicemanager

        f = open('test.dat', 'w+')
        rc = None

        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            check()
            checkram()
            f.write('TEST DATA\n')
            f.flush()
            # block for 5 seconds and listen for a stop event
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
            
        f.write('SHUTTING DOWN\n')
        f.close()

    
    # called when we're being shut down    
    def SvcStop(self):
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
        win32event.SetEvent(self.hWaitStop)
        
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PySvc)
