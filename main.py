import subprocess
import re

networks = subprocess.call("netsh wlan show  profile")
print(networks)

