import win32file
import os

import string
from ctypes import windll

#def get_drivestats(drive):
    # if no drive given, pick the current working directory's drive
    #if drive == None:
    #    drive = os.path.splitdrive(os.getcwd())[0].rstrip(':')
    #sectPerCluster, bytesPerSector, freeClusters, totalClusters = \
    #    win32file.GetDiskFreeSpace(drive + ":\\")
    #total_space = totalClusters*sectPerCluster*bytesPerSector
    #free_space = freeClusters*sectPerCluster*bytesPerSector
    #gb = float(1024 * 1024 * 1024)
    #print( "Drive = %s" % drive )
    #print( "total_space = %0.2f Gb" % (total_space/gb) )
    #print( "free_space  = %0.2f Gb" % (free_space/gb) )
    #print( "used_space  = %0.2f Gb" % ((total_space - free_space)/gb) )

    #pourcentage_occupe = (((total_space - free_space)/gb) / (total_space/gb)) *100
    
#driveTypes = ['DRIVE_UNKNOWN', 'DRIVE_NO_ROOT_DIR', 'DRIVE_REMOVABLE', 'DRIVE_FIXED', 'DRIVE_REMOTE','DRIVE_CDROM', 'DRIVE_RAMDISK']

#def get_drives():
#    drives = []
#    bitmask = windll.kernel32.GetLogicalDrives()
 #   for letter in string.uppercase:
#        if bitmask & 1:
#            drives.append(letter)
#        bitmask >>= 1
#
#    return drives

#for drive in get_drives():
 #   if not drive: continue
    #print ("Drive:", drive)
  #  try:
   #     typeIndex = windll.kernel32.GetDriveTypeW(u"%s:\\"%drive)
    #    if typeIndex != 5 and typeIndex != 0 and typeIndex != 1:
            #print ("Type:",driveTypes[typeIndex])
     #       get_drivestats(drive)
    #except Exception as e:
    #    print ("error:",e)

class drives():

    def __init__(self, drivesTypes):
        self.drivesTypes = []
        self.drives = []

    def get_drives():
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1

        return drives

    for drive in get_drives():
        if not drive: continue
        #print ("Drive:", drive)
        try:
            typeIndex = windll.kernel32.GetDriveTypeW(u"%s:\\"%drive)
            if typeIndex != 5 and typeIndex != 0 and typeIndex != 1:
                #print ("Type:",driveTypes[typeIndex])
                get_drivestats(drive)
        except Exception as e:
            print ("error:",e)

    def get_drivestats(drive):
    # if no drive given, pick the current working directory's drive
        if drive == None:
            drive = os.path.splitdrive(os.getcwd())[0].rstrip(':')
        sectPerCluster, bytesPerSector, freeClusters, totalClusters = \
            win32file.GetDiskFreeSpace(drive + ":\\")
        total_space = totalClusters*sectPerCluster*bytesPerSector
        free_space = freeClusters*sectPerCluster*bytesPerSector
        gb = float(1024 * 1024 * 1024)
        #print( "Drive = %s" % drive )
        #print( "total_space = %0.2f Gb" % (total_space/gb) )
        #print( "free_space  = %0.2f Gb" % (free_space/gb) )
        #print( "used_space  = %0.2f Gb" % ((total_space - free_space)/gb) )

        pourcentage_occupe = (((total_space - free_space)/gb) / (total_space/gb)) *100


disques = drives(['DRIVE_UNKNOWN', 'DRIVE_NO_ROOT_DIR', 'DRIVE_REMOVABLE', 'DRIVE_FIXED', 'DRIVE_REMOTE','DRIVE_CDROM', 'DRIVE_RAMDISK'],[])
print(disques.drivesTypes)