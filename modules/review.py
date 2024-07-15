#!/usr/bin/python3

"""
author: c@shed
version: 1.0

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import undetected_chromedriver as uc

from modules import sms
from modules import bard

import sys
import os
import random
import time

cfgnum="-----"
star_rating="5" #(1,2,3,4,5)
placeurl="-----"
#you can go to a place on maps and click review to start writing, then copy the link and it will even keep the review textbox open for you hahaha

def review(email,pwd):



    #chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    #chrome_options.add_argument("--user-data-dir=data")
    chrome_options.add_argument("--profile-directory=Default")


    driver = uc.Chrome(options=chrome_options)

    try:

        name=email.split(".")[0]

        driver.get("https://accounts.google.com/v3/signin/identifier?hl=en-gb&ifkv=AdF4I75c624myeSaERYqPTkkidomC6WusiqWHanG2SHUODzIyVvo2jTzMpQeAc9Bc8u8Dv-5i4Kr7g&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1476408863%3A1721005061913896&ddm=0")

        #login
        print(f"\n[/] Logging in as {name} -> waiting...", end="\r")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,("identifierNext"))))
        driver.find_element(By.ID,"identifierId").send_keys(email)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,("identifierNext")))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"passwordNext")))
        driver.find_element(By.NAME,"Passwd").send_keys(pwd)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,"passwordNext"))).click()
        

        try:
            notnow = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Not now']")))
            parent = notnow.find_element(By.XPATH, "./..")
            parent.click()
        except:
            pass

        print(f"[+] Logging in as {name} -> Done!          ")


        #LEAE REVIEW

        print(f"[/] Giving {star_rating} star review -> waiting...", end="\r")
        WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        driver.get(placeurl)


        iframe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//iframe[@name='goog-reviews-write-widget']")))
        
        driver.switch_to.frame(iframe)

        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='Posting publicly across Google']"))).click()


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[@data-rating='{star_rating}']"))).click()
        print(f"[+] Giving {star_rating} star review -> Done!           ")


        print(f"[/] Generating review -> waiting...", end="\r")
        reviewtext = bard.getreview()
        print(f"[/] Generating review -> Done!\n")

        print("[!] Review:\n"+reviewtext+"\n")
        print("[/] Tweak the prompt to better suit your business, or override reviewtext with desired string literal\n")


        print(f"[/] Posting review -> waiting...", end="\r")
        driver.find_element(By.XPATH, "//textarea[@placeholder='Share details of your own experience at this place']").send_keys(reviewtext)

        post = driver.find_element(By.XPATH, f"//*[text()='Post']")
        parent = post.find_element(By.XPATH, "./../../..")
        parent.click()
        print(f"[/] Posting review -> Done!              \n\n")

        sms.sms(cfgnum, f"[GBot] : {name} just left a review!")
        

        time.sleep(3)
        driver.quit()


    except Exception as e:
        print(e) 

def main():


    c = open("data/creds.txt", "r")
    u = open("data/used.txt", "r")

    clines=c.readlines()
    cl=len(clines)
    ul=len(u.readlines())

    u.close()
    u=open("data/used.txt", "a")

    print(f"\n[/] {ul} reviews made!")
    print(f"[+] {cl} accounts available\n")
    n=input("[?] Number of reviews to leave (-1 for max)\n[?] >> ")
    try:
        n=int(n)
    except:
        print("[-] invalid input\n\n")

    if n==-1:
        n=cl

    if n>cl or n<0:
        print("[-] invalid input\n\n")
        return


    for x in range(0,n):
        creds = clines.pop(0).strip()
        u.write(creds+"\n")
        creds=creds.split(",")
        review(creds[0],creds[1])


    c.close()
    u.close()

    print(clines)
    c=open("data/creds.txt", "w")
    c.writelines(clines)
    c.close()



