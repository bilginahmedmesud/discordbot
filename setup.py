from sys import executable
from subprocess import check_call
import time

def install():
    print('Installing Requirements Package...')
    time.sleep(1)
    python = executable
    check_call([python, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    print("Successfully Installed Requirements Package!")
