from executer import Exec
import argparse
import pandas as pd
from mail import Mail
from datetime import datetime

now = str(datetime.now())[:19]
parser = argparse.ArgumentParser(description = 'new files.')
parser.add_argument('path', type=str, help='path do arquivo novo')
args = parser.parse_args()

path = args.path

# EXEC
exec = Exec(path=path)
email_send = exec.email_receiver()
data = exec.return_dataframe()

# SAVE DATA
data.to_csv(f'../src/backup/backup_{now}.csv')

# EMAIL
mail = Mail(data=data)
mail.send_mail(email=email_send)









