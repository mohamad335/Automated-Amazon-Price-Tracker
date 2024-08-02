from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import time
import smtplib
MY_Email=os.getenv("MY_EMAIL")
My_pass=os.getenv("MY_PASS")


to=os.getenv("TO")
load_dotenv()
BUY_PRICE=100
URL="https://appbrewery.github.io/instant_pot/"
response=requests.get(URL)
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
price=soup.find(class_="a-offscreen")
float_price=float(price.getText().split("$")[1])
if float_price<BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.login(MY_Email, My_pass)
        connection.starttls()
        result = connection.login(MY_Email, My_pass)
        connection.sendmail(
            from_addr=MY_Email,
            to_addrs=to,
            msg=f"Subject:Amazon Price Alert!\n\n{float_price}".encode("utf-8")
        )
   
  
    


    
    