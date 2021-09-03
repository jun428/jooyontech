from bs4 import BeautifulSoup
from selenium import webdriver

import smtplib
from email.mime.text import MIMEText


driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.jooyonshop.co.kr/goods/goods_view.php?goodsNo=1000000230')


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#x= soup.select("#frmView > div > div > div.btn_choice_box.btn_restock_box > button")
check = soup.select('#frmView > div > div > div.btn_choice_box.btn_restock_box > button')
check = check[0].text
if(check=="구매 불가!") :
    driver.close()
else :
    smtp = smtplib.SMTP('smtp.live.com', 587)
    smtp.ehlo()      # say Hello
    context  = ssl.create_default_context(cafile=PATH_TO_CERTIFICATE_AUTHORITY_ROOT_CRT_FILE)
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('tjd428@o.cnu.ac.kr', 'tjd79135!@')
    
    msg = MIMEText('본문 테스트 메시지')
    msg['Subject'] = '테스트'
    msg['To'] = 'tjd42942@gmail.com'
    smtp.sendmail('lee@live.com', 'tjd42942@gmail.com', msg.as_string())
    
    smtp.quit()
    driver.close()
