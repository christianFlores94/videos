import os


term_command = "git add ."
comando = 'bash -c \"(%s); exec bash\"' % term_command
os.system(comando)
