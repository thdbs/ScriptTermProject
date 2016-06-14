import smtplib
import mimetypes

from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from xml.dom.minidom import getDOMImplementation


def sendMail(mvDictData, sender, passWd,recipient):
    # mvDictData -> HTML

    impl = getDOMImplementation()
    newdoc = impl.createDocument(None, "html", None)
    topElement = newdoc.documentElement
    header = newdoc.createElement('header')
    topElement.appendChild(header)
    body = newdoc.createElement('body')
    for k, v in mvDictData.items():
        b = newdoc.createElement('b')
        bText = newdoc.createTextNode(k)
        b.appendChild(bText)
        body.appendChild(b)
        br = newdoc.createElement('br')
        body.appendChild(br)
        if v.__class__ == type(list()):
            if k == "posters":
                for x in v:
                    p = newdoc.createElement('img src'+'='+x)
            else:
                for x in v:
                    p = newdoc.createElement('p')
                    pText = newdoc.createTextNode(x)
                    p.appendChild(pText)
        else:
            p = newdoc.createElement('p')
            pText = newdoc.createTextNode(v)
            p.appendChild(pText)
        body.appendChild(p)
        body.appendChild(br)
    topElement.appendChild(body)
    html = newdoc.toxml()

    host = sender.rpartition('@')
    host = "smtp." + host[2]
    port = "587"
    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "[" + mvDictData["title"] + "] Movie Imformation"
    msg['From'] = sender
    msg['To'] = recipient
    htmlPart = MIMEText(html,'html', _charset = 'UTF-8')

    msg.attach(htmlPart)

    s = smtplib.SMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sender, passWd)
    s.sendmail(sender, recipient, msg.as_string())
    s.close()


    
