import requests
from bs4 import BeautifulSoup
import smtplib
from unidecode import unidecode

my_email = "adithyagh.testing@gmail.com"
password = "vvgjnfmudohhjeij"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept-Language": "en-US,en;q=0.5"
}
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price_selection = soup.find(class_="a-offscreen")
new_price = price_selection.getText().split("$")[1]
name_selection = soup.find(id="productTitle")
name = name_selection.getText().strip()
message = f"Subject:Amazon Price Alert!\n\n{name} is now ${new_price}\n{URL}"
new_message = unidecode(message)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    message = connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                  msg=f"{new_message}")