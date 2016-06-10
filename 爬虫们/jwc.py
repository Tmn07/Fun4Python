#-*-coding:utf8;-*-
#qpy:2
#qpy:console


# import the const
from config.jwc_config import *
# from config.jwc_config_demo import *

from bs4 import BeautifulSoup
import urllib2
url = "http://jwc.hit.edu.cn"
data = urllib2.urlopen(url)

html = data.read()
#print html
soup = BeautifulSoup(html,"html.parser")
test=""
for span in soup.find_all("span",class_="news_title"):
    #print span
    s2 = BeautifulSoup(str(span),"html.parser")
    node = s2.find("a")
    title = node.string
    url2 = node["href"]
    test += title+"\t"+url+url2+"\n\n"
    #print url
    
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# email content
msg = MIMEText(test, 'plain', 'utf-8')
msg['From'] = _format_addr(u'爱你的芹菜 <%s>' % from_addr)
msg['To'] = _format_addr(u'亲爱的芹菜 <%s>' % to_addr)
msg['Subject'] = Header(u'来自jwc', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
