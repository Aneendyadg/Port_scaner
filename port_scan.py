import socket
import threading
from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()
find = socket.gethostname()
f_IP = socket.gethostbyname(find)
print ('Now Scanning: ', f_IP)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((f_IP, port))
      with print_lock:
         print(port, 'OPEN')
      con.close()
   except:
      pass

def threader():
   while True:
      zoro = q.get()
      portscan(zoro)
      q.task_done()

q = Queue()
   
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 65535):
   q.put(worker)
   
q.join()
