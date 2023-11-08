import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from glob import iglob
from os.path import getmtime
from os import system, utime
from datetime import datetime
from mail import MAil_Fail

#time now
now = str(datetime.now())[:19]

# Email Stop
mail = MAil_Fail()


#created class for use get file
class Look(FileSystemEventHandler):
    def on_created(self, event):
        path = '../app_api/output/'
        file_extensao = '*.json'
        files = iglob(path+file_extensao)
        
        arquivo_mais_recente = max(files, key=getmtime)
        arquivo_mais_recente = str(arquivo_mais_recente)
        #print(str(arquivo_mais_recente))
        #src(arquivo_mais_recente)
        #path_(arquivo_mais_recente)
        #print(os.listdir())
        system(f"python3 main.py '{arquivo_mais_recente}'")
        #system("python3 main.py '{}'".format(arquivo_mais_recente))
        


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    look = Look()

    observer = Observer()
    observer.schedule(look, path, recursive=True)
    observer.start()
    print ('starting...')
    print ('watch new files...')
    try:
        while True:
            time.sleep(1)
    except:
        #IF STOP
        observer.stop()
        print ('STOP')
        fname = f'../src/logs/STOP_AGENT_{now}'
        with open(fname, 'a'):
            utime(fname, None)
        mail.msg_agent_fail()    
        
    observer.join()