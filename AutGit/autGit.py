import random
import subprocess
import time
class ClassAutGit():
    def __init__(self):
        self.emojis = ['airplane', 'ant', '+1', 'athletic_shoe', 'bamboo',
  	               'beer', 'bicyclist', 'bike', 'black_nib', 'blush', 
  	               'cow', 'crocodile', 'crescent_moon', 'do_not_litter',
  	               'dog2', 'elephant', 'eyeglasses', 'ferris_wheel']
        self.hosts = ('8.8.8.8', 'kernel.org', 'github.com')
        self.emoji = random.choice(self.emojis)
        self.proceso = '''
            echo "Comentario :"
            read  comen 
            git add -A
            git commit -m  "$comen :{}:" 
        '''.format(self.emoji)
        self.github='git push -u origin master'

    def remote_and_local(self):
        final = self.proceso  
        subprocess.call( final, shell=True)

    def ping(host):
        ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w'))
        return ret == 0   

    def run(self):
        print ("[%s] Verificando Internet..." % time.strftime("%Y-%m-%d %H:%M:%S"))
        xstatus = 1
        for h in self.hosts:
            if ClassAutGit.ping(h):
                final = self.proceso  + self.github
                subprocess.call( final, shell=True)
                print ("Se Enviara a el prepositorio Remoto!")
                xstatus = 0
                break
            if xstatus:
                subprocess.call( self.proceso, shell=True)
                print ("[%s] No Se Enviara Al repositorio Remoto :(")
                break
            return xstatus
