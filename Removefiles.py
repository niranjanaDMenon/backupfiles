import shutil
import os
import time 

path="c:\user\user\downloads"
days=60
seconds = time.time()- (days * 24*60*60)

if os.path.exists(path) :
    
