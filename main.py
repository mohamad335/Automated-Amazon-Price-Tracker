from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import smtplib

MY_Email=os.getenv("MY_EMAIL")
My_pass=os.getenv("MY_PASS")


to=os.getenv("TO")
load_dotenv()
BUY_PRICE=101
URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headrs={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/000000000 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}
response=requests.get(URL,headers=headrs)

soup=BeautifulSoup(response.content,"html.parser")
price=soup.find(class_="aok-offscreen").get_text()
float_price=float(price.split("$")[1])
print(float_price)
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
   










  
    


    
    