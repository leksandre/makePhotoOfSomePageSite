import pprint
# from googleapiclient.discovery import build
import optparse
import re
import threading
import datetime
import random
import json
import psycopg2
import string
import psutil
import base64
import subprocess
from random import shuffle
import urllib.parse
from bs4 import BeautifulSoup
from datetime import timezone
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
try:
    import requests
except ImportError:  # if requests module isn't installed
    if sys.platform.startswith('linux'):  # if platform is linux
        print(" please install requests  module in Debian")
        sys.exit(" sudo apt-get install python-requests ")
    else:
        print(" install requets module for python here : https://pypi.python.org/pypi/requests/2.9.1 or try: pip install requests")
        sys.exit()
from urllib3.exceptions import InsecureRequestWarning

import sys
import time
import os

import PyQt5
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineSettings as QWebSettings
from PyQt5.QtCore import Qt, QUrl, QTimer



try:
    from PIL import Image
except ImportError:
    import Image



import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

gmail_user = 'support@logintap.com'
gmail_password = 'nXvUblDCJryTMP1SSsjd'
sent_from = gmail_user






def markerStart(idRecord):
    try:
        for x in range(0, 999):
            try:
                    tshema = 'great_paraser'
                    conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                            host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'
            except:
                time.sleep(0.2)
                pass
            finally:
                break

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                if 1:
                  if 1:
                    sql = " Update projects set \"tryedLast\"=now() where id=%(id)s "
                    params={"id":idRecord}
                    curpg.execute(sql,params)
            
                curpg.execute(sql,params)
                conpg.commit()


    except psycopg2.DatabaseError as e:
        print('Error %s' % e)




def markerSend(idRecord, mailes):
    try:
        for x in range(0, 999):
            try:
                    tshema = 'great_paraser'
                    conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                            host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'
            except:
                time.sleep(0.2)
                pass
            finally:
                break

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                if len(mailes)>2:
                    sql = " Update projects set \"mailTo\"=%(linksprofileStr)s where id=%(id)s "
                    params={"linksprofileStr":mailes,"id":idRecord}
                    curpg.execute(sql,params)
         
                # sql = " Update projects set  \"LastModified\" = now() where id=%(id)s "
                # params={"isShopify":isShopify,"id":idRecord}
                curpg.execute(sql,params)
                conpg.commit()


    except psycopg2.DatabaseError as e:
        print('Error %s' % e)

def markerFail(idRecord, mailes):
    try:
        for x in range(0, 999):
            try:
                    tshema = 'great_paraser'
                    conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                            host=pghost, port=pgport) # , options=f'-c search_path={pgschema}'
            except:
                time.sleep(0.2)
                pass
            finally:
                break

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                sql = " Set search_path =%(pgdb)s "
                params={"pgdb":pgdb}
                curpg.execute(sql,params)
                # conpg.commit()

        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
                if len(mailes)>2:
                    sql = " Update projects set \"reason\"=%(linksprofileStr)s where id=%(id)s "
                    params={"linksprofileStr":mailes,"id":idRecord}
                    curpg.execute(sql,params)
         
                # sql = " Update projects set  \"LastModified\" = now() where id=%(id)s "
                # params={"isShopify":isShopify,"id":idRecord}
                curpg.execute(sql,params)
                conpg.commit()


    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


class Screenshot(QWebView):

    def capture(self, url, output_file):
        try:
            self.output_file = output_file
            self.load(QUrl(url))
            self.loadFinished.connect(self.on_loaded)
            # Create hidden view without scrollbars
            self.setAttribute(Qt.WA_DontShowOnScreen)
            self.page().settings().setAttribute(
                QWebSettings.ShowScrollBars, False)
            self.show()
        except Exception as ex:
            print ("Something went wrong….1 ",ex)

    def on_loaded(self):
        time.sleep(1)
        #size = PyQt5.QtCore.QSize(2035, 885) #self.page().contentsSize().toSize()
        size = self.page().contentsSize().toSize()
        print('size.height()')
        print(size.height())
        print('size.width()')
        print(size.width())

        if (size.height()<=0)or(size.width()<=0):
            exit()

        # if(size.height()>885):
        #     size.setHeight(885)
        #     size.setWidth(2035)

        # if(size.width()*size.height())>768000:
        #     size.setHeight(885)
        #     size.setWidth(2035)

        size.setHeight(885)
        size.setWidth(2035)

        print('size.height()')
        print(size.height())
        print('size.width()')
        print(size.width())

       
        self.resize(size)
        time.sleep(1)
        # Wait for resize
        QTimer.singleShot(1000, self.take_screenshot)

    def take_screenshot(self):
        self.grab().save(self.output_file, b'PNG')
        self.app.quit()
        self.close()




def fromBase():
    try:
        tshema = 'great_paraser'
        conpg = psycopg2.connect(database=tshema, user=pguser, password=pgpswd,
                                host=pghost, port=pgport, options=f'-c search_path={tshema}')
        curpg = conpg.cursor(name='foo11')
        if conpg:
         with conpg:
             with conpg.cursor() as curpg:
               sql = "SELECT  protocol, domain, id FROM projects where  \"tryedLast\" is null and \"mailTo\" is null  and \"isShopify\" and \"profileUrl\" like '%/account/login%' and \"Emails\" is not null and \"Emails\" like '%@%'  order by \"LastModified\" asc  limit 1 ;" 

               curpg.execute(sql)
               res1 = curpg.fetchall()
               print('res1 len %s' % len(res1[0]))
               return res1
    except psycopg2.DatabaseError as e:
        print('Error %s' % e)


        
pgdb = 'great_paraser'
pguser = 'postgres'
pgpswd = 'postgres'
pghost = '10.72.1.117'
pgport = '5432'
# pgschema = 'great_paraser'
max_process_count = 2
d1 = json.JSONDecoder()





def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename={}'.format(Path(path).name))
        msg.attach(part)
    print('try connect',server, port)
    # smtp = smtplib.SMTP(server, port)
    # if use_tls:
    #     smtp.starttls()
    # smtp.login(username, password)
    # smtp.sendmail(send_from, send_to, msg.as_string())
    # smtp.quit()
    try:
            smtp_server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            smtp_server.ehlo()
            smtp_server.login(username, password)
            smtp_server.sendmail(sent_from, send_to, msg.as_string())
            smtp_server.close()
            print ("Email sent successfully!")
    except Exception as ex:
            print ("Something went wrong….2 ",ex)





def main33(siteData0,siteData1,siteData2):
        fname = "screen1.png"
        if os.path.isfile(fname) :
            os.unlink(fname)
        fname = "screen1_auth.png"
        if os.path.isfile(fname) :
            os.unlink(fname)
        url1 = siteData0+siteData1+'/account/login'
        print('0  '+url1)
        print('markerStart  '+str(siteData2))
        markerStart(siteData2)
        res = s.capture(url1, 'screen1.png')
        print('0 res  ')
        print(res)
        app.exec_()
        app.quit()
        app.exit()
        

        fname = "screen1.png"
        if os.path.isfile(fname) :
            print('1  '+siteData0+siteData1)
        else:
            markerFail(siteData2,'fial create screenshot')
            return False

        im = Image.open(fname)
        (width, height) = im.size

        if(width<2035):
            print('not resized  '+siteData0+siteData1)
            markerFail(siteData2,'not resized')
            return False

        whitePhotoFromRigth = False
        colors = {}
        for i in range(1035):
          for j in range(885):
            color = im.getpixel((i+1000, j))
            colorkey=str(color)
            if colorkey in colors:
             colors[colorkey] = 1 + int(colors[colorkey])
            else:
             colors[colorkey] = 1

        if '(255, 255, 255)' in colors:
         print('colors whie')
         print(colors['(255, 255, 255)'])
         if(colors['(255, 255, 255)']==915975):
            whitePhotoFromRigth = True
         if(colors['(255, 255, 255)']>908000):  
            if(colors['(255, 255, 255)']<911000): 
             whitePhotoFromRigth = True     

        if(whitePhotoFromRigth):
            print('whitePhotoFromRigth '+siteData0+siteData1)
            markerFail(siteData2,'whitePhotoFromRigth')
            return False

        colorsoutput = len(colors)
        if colorsoutput < 10:
            print('less10colors '+siteData0+siteData1)
            markerFail(siteData2,'less10colors')
            return False

        width, height = im.size
        image1 = Image.open("en.png")
        width1, height1 = image1.size
        image1 = image1.convert("RGBA")
        im.paste(image1, (width - width1 - 5, 5))
        im.save("screen1_auth.png", quality=95)


        fname = "screen1_auth.png"
        if os.path.isfile(fname) :
            print('2  '+siteData0+siteData1)
        else:
            markerFail(siteData2,'fial create screenshot auth')
            return False


        filename = "screen1_auth.png"
        files = ["screen1_auth.png"]#,"screen1.png"
        fo = open(filename, "rb")
        filecontent = fo.read()
        encodedcontent = base64.b64encode(filecontent)  # base64


        to = ['jirdis@ya.ru']#,'alex@mobsted.com'
        subject = 'No passwords on '+siteData1+'?' # '+siteData1+'
        body = 'Hi, I found your email on '+siteData1+', when studying how Shopify shops work with logins and passwords for clients.\
\
Do you think you can have a look at the screenshot I made for your shops login page? Does it make sense to rid clients of logins and passwords to make shopping easier?\
\
\Please view letter attachment\
\
\I would be glad to talk it over if you like the idea, or if you think talks are useless you can see more on the biometric login for Shopify  - logintapm.com/shop.\
\
If you have no interest in learning if this can help - (let me know) and I will erase you from my Shopify research.'

        send_mail(sent_from,to,subject,body,files,'smtp.yandex.ru',465,gmail_user,gmail_password);#ssl://
        print('exit '+siteData1)
        markerSend(siteData2,','.join(to))
        # exit()



        print('end')
        # time.sleep(16)

maxProcCount = 2

if True:
    siteGen = fromBase()
    if not siteGen:
        print('error 300')
        sys.exit()
    shuffle(siteGen)
    print(str(len(siteGen))+' - len(siteGen)')
    app = QApplication(sys.argv)
    s = Screenshot()
    s.app = app
    sl1 = 0
    print('-- --  -- --  -- --  -- --  -- --  -- --  -- --  -- --  -- -- -- --  -- --  -- --     start')
    for siteData in siteGen:

        if threading.active_count() < maxProcCount:
            print('startTime:'+str(datetime.datetime.now()))
            print('threading.active_count():'+str(threading.active_count()))
            # thread = threading.Thread(target=main33, args=(siteData))
            res = main33(siteData[0],siteData[1],siteData[2])
            sl1 = sl1+1
            print('-------------------------------- next domain:'+str(sl1))
            exit()
               




