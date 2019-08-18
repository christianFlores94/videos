import os
import time

dia = "hoy"
adding = "git add ."
commits = "git commit -m " + dia
push = "git push" 
comando = 'bash -c \"(%s); exec bash\"' % adding
os.system(comando)
comando = 'bash -c \"(%s); exec bash\"' % commits
os.system(comando)
comando = 'bash -c \"(%s); exec bash\"' % push
os.system(comando)
os.system("echo christianFlores94")
time.sleep(5)
os.system("echo 2718Chfl")