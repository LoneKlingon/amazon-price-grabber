import mail
from urllib.request import urlopen
URL = 'http://www.amazon.com/Practical-Electronics-Inventors-Paul-Scherz/dp/0071771336' #or enter your own url 

file = urlopen(URL)
html = file.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)


res  = soup.find('span', {"class" : "a-size-medium a-color-price"})
price = float (res.get_text())
target = 20.00


if price <= target:


    #Block that just goes here is actually suppoed to send me an email
    #with the message 
    mail.send_email("Price of item is at target price" + str(targeT) )
    print("Price is lower than" +str(target))
