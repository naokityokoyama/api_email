import pandas as pd
from pretty_html_table import build_table
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
load = load_dotenv()

class Mail:
    def __init__(self, data):
        self.data = data
        

    def build(self)->str:
        frame = self.data
        output_table = build_table(frame, "blue_dark", width='auto', font_size='small', \
                        font_family='Open Sans sans-serif')
        html = f'''<!DOCTYPE html>
        <body>
        <head>
            <link rel="stylesheet" href="style.css">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
   
            <img src="cid:logo" alt="logo linkbr" width=auto height="40">
            
            <h1>
        
            <p>
    
            <span>  
            <h2>
            
            </h2>
        </span>
        <h4> <b>Segue abaixo detalhes do evento</b> </h4>
        </p>
    </h1>
    </head>
        <div> 
        {output_table}
        </div>
            <div>
            <p><h4><b> Para maiores informações entre em contato com o NOC</b> </h4></p>
            </div>
            </body>'''    
        return html 


    def send_mail(self, email)->str:
        html = self.build()

        # CREDENCIAL
        smtp_server = os.getenv('SMTP')
        password = os.getenv("PASSWORD")
        sender_email = "alertas-ddos@linkbrasil.net.br"  
        port = 465
        #receiver_email = ['naokiyokoyama@gmail.com' , 'naokity@msn.com', 'naokity@yahoo.com']#'gkohler@techenabler.com.br'] 
        receiver_email = email
        
        print ('email ->', email)
        #to_mail = ", ".join(receiver_email)   
        to_mail = receiver_email

        # SUBJECT
        message = MIMEMultipart("alternative")
        message["Subject"] = "Alerta Ataque DDoS - LinkBr"
        message["From"] = sender_email
        message["To"] = to_mail

        # add image
        with open('linkbr.png', 'rb') as fp:
            msgImage = MIMEImage(fp.read())

        # incluide image
        msgImage.add_header('Content-ID', '<logo>')
        message.attach(msgImage)  

        part1 = MIMEText(html, "html")
        
        # attach part1 
        message.attach(part1) 

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server,
                      port, 
                      context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string()) 

        print ('email enviado!')


class MAil_Fail:

    def msg_agent_fail(self):   
        html = f'''<!DOCTYPE html>
        <body> 
        <head>
        <img src="cid:stop" alt="logo stop" width=auto height="100">
        </head>
            <h2><b>
            Atention Agent Down!!!!
            </b></h2>
            </body> 
            '''
        
        # CREDENCIAL
        smtp_server = os.getenv('SMTP')
        password = os.getenv("PASSWORD")
        sender_email = "alertas-ddos@linkbrasil.net.br"  
        port = 465
        #receiver_email = ['naokiyokoyama@gmail.com' , 'naokity@msn.com', 'naokity@yahoo.com']#'gkohler@techenabler.com.br'] 
        receiver_email = 'naokiyokoyama@gmail.com'
        to_mail = receiver_email

        # SUBJECT
        message = MIMEMultipart("alternative")
        message["Subject"] = "Serviço Email LinkBR Stop"
        message["From"] = sender_email
        message["To"] = to_mail

        # add image
        with open('stop.png', 'rb') as fp:
            msgImage = MIMEImage(fp.read())

        # incluide image
        msgImage.add_header('Content-ID', '<stop>')
        message.attach(msgImage)  

        part = MIMEText(html, "html")
        
        # attach part1 
        message.attach(part) 

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server,
                      port, 
                      context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string()) 

        print ('email enviado!')