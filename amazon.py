import mail
from urllib.request import urlopen
URL = 'http://www.amazon.com/Practical-Electronics-Inventors-Paul-Scherz/dp/0071771336'

file = urlopen(URL)
html = file.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)


res  = soup.find('span', {"class" : "a-size-medium a-color-price"})
print(res.get_text())
if res.get_text() == '$20.43':


    #Block that just goes here is actually suppoed to send me an email
    #with the message 
    mail.send_email()
    print("Message sent")
