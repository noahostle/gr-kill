from sqlalchemy import true
import undetected_chromedriver as uc
import pandas as pd
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
from time import sleep

class GoogleReviewBot:
    
    def __init__(self,email,pwd,comment):
        self.mailaddress = email
        self.password = pwd
        self.comment = comment
        self.waitDuration = [3,4,5]
        self.initialize()

    def initialize(self):
        self.i = 0
        #PlaceURL = "https://www.google.com/search?q=g%26d+cleaning+and+maintenance+services+smeaton+grange&sca_esv=f911e4bfb540ceed&sca_upv=1&biw=1440&bih=685&tbm=lcl&sxsrf=ADLYWIJoNHx3DncPzTRj9qRYRtvCWFiDcw%3A1720590136290&ei=OB-OZtGuEf2l2roPtYq2sAs&oq=g&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIgFnKgIIADIEECMYJzIEECMYJzIEECMYJzIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIQEAAYgAQYsQMYQxiDARiKBTILEAAYgAQYsQMYgwEyChAAGIAEGEMYigUyEBAAGIAEGLEDGEMYgwEYigVI1gxQAFgAcAB4AJABAJgBrAGgAawBqgEDMC4xuAEByAEA-AEBmAIBoAK4AZgDAJIHAzAuMaAH4Qk&sclient=gws-wiz-local" #ENTER YOUR LINK HERE
        PlaceURL = "https://www.google.com/search?q=docker+river+airport&sca_esv=f911e4bfb540ceed&sca_upv=1&biw=1440&bih=685&tbm=lcl&sxsrf=ADLYWII23NQcyhTpgaLDwOtPa2X4d_YSLw%3A1720590177931&ei=YR-OZqbAOIml2roPhtu-gA4&ved=0ahUKEwjm9O_y4ZuHAxWJklYBHYatD-AQ4dUDCAk&uact=5&oq=docker+river+airport&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIhRkb2NrZXIgcml2ZXIgYWlycG9ydDIEECMYJzIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiiBBiJBTIIEAAYgAQYogRIuTNQ6wZYrzBwBHgAkAEBmAGEAqAB9ySqAQYwLjE2Ljm4AQPIAQD4AQGYAhygApUkqAIKwgICECbCAgsQABiABBiRAhiKBcICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAgcQIxgnGOoCwgIREAAYgAQYkQIYsQMYgwEYigXCAgoQABiABBhDGIoFwgINEAAYgAQYsQMYQxiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgoQABiABBgUGIcCwgIFEAAYgATCAgYQABgWGB7CAggQABgWGB4YD8ICBRAhGKABwgIEECEYFZgDBYgGAZIHBjQuMTYuOKAH0ZwB&sclient=gws-wiz-local"
        self.driver = uc.Chrome()
        self.driver.delete_all_cookies()
        self.urls = ["https://accounts.google.com/v3/signin/identifier?ifkv=AdF4I75QJIJ2YH6aEWPPXLrxDZJ0WCKgWVcfD-GuIu-vt4PeSPwzUmRRowzbZSkmBjGnAwfyEXoG&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1242411337%3A1720590362249819&ddm=0",PlaceURL]
        self.driver.get(self.urls[self.i])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,("identifierNext"))))
        
    def _login(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,("identifierNext"))))
            login=self.driver.find_element(By.ID,"identifierId")
            login.send_keys(self.mailaddress)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,("identifierNext")))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"passwordNext")))
            password=self.driver.find_element(By.NAME,("password")) 
            password.send_keys(self.password)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID,"passwordNext"))).click()
            sleep(random.choice(self.waitDuration))
        except:
            print("There is a problem 1.")
            pass
         
    def _comment(self):
        try:
            self.i +=1
            self.driver.get(self.urls[self.i]) 
            sleep(random.choice(self.waitDuration))   
            WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[18]/iframe")))
            self.driver.find_element(By.XPATH,("/html/body/div[1]/c-wiz/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/textarea")).send_keys("Comment")
            elem=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#yDmH0d > c-wiz > div > div > div > div > div.O51MUd > div.l5dc7b > div.DTDhxc.eqAW0b > div.euWHWd.aUVumf > div > div:nth-child(5)")))
            self.driver.execute_script("arguments[0].click();", elem)
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#ZRGZAf > span"))).click()
            sleep(random.choice(self.waitDuration))
            self.completedAccounts.write(self.mailaddress + "-" + self.password + "\n")
            self.driver.close()
        except:
            print("There is a problem in Comment.")
            pass

    
    
if __name__ == "__main__":
    credsfile=open("creds.txt","r")

    for line in credsfile:
        a=line.split(",")
        email=a[0]
        pwd=a[1]
        comment="test"

        GRB = GoogleReviewBot(email,pwd,comment)
        try:
            GRB._login()
            GRB._comment()
        except:
            print("There is a problem.")
            pass