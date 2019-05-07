import win32gui
import os
import time
import glob
import sys
import fileinput

global baseScripts
global globalVersion

globalVersion = '1.8.9'
window = 1
baseScripts = ['block_svc.py', 'check.py', 'gui_select.py', 'image.py', 'MCKeyboard.py', 'sectionify.py', 'start.py']

def check(v,version=globalVersion):
    
        window = win32gui.FindWindow(None,"Minecraft %s"%version)

        if window == 0:
                window = 0
                os.system('echo off')
                os.system('cls')
                os.system('title Connection Error')
                print("Open Minecraft Version %s!"%version)
                print()
                print("ConnectionError")
                
                os.system('explorer %PATH%')

        while window == 0:
            v = v +1
            
        else:
            os.system('exit')

def debug():
        os.system('title Debug Mode')
        os.system('cls')
        print('Entering debug mode...')
        print()
        file = sys.argv[0]
        root_dir = os.path.dirname(os.path.realpath(__file__))
        print('Showing Python Scripts For Directory: "' + root_dir + '" .')
        print()
        print('┍--------------------------------')
        for filename in glob.iglob('**/*.py', recursive=True):
                print('| ' + filename)
                print('|')
        try:
                print()
                print('Type The One You Want To Open:')
                script = input('>>> ')
                f = (root_dir + '\\' + script)
                print('Opening ' + f + '...')
                os.startfile(f)
        except Exception as e:
                print()
                print(e,". Got exception!")

try:
        input1 = sys.argv[1]
        if input1 == 'heretocheck.txt':
                check(1)
                os.system('cls')
        
except Exception as e:   
        os.system('cls')
