
import shutil
import sys
import subprocess
while True:
 if len(sys.argv) == 2:
    for n in range(0,int(sys.argv[0])):
     shutil.copy(sys.argv[0],sys.argv[0] +str(n)+ '.py')
 else:
    print("PONLO BIEN")
    
