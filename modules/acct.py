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

from modules import apiwrapper as api

from modules import sms

import sys
import os
import random
import time

cfgnum="----"



def acct(oid, num):



    #chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    #chrome_options.add_argument("--user-data-dir=data")
    chrome_options.add_argument("--profile-directory=Default")


    driver = uc.Chrome(options=chrome_options)


    # Common Australian first names for people in their 40s
    first_names = [
        "Andrew", "Ben", "Catherine", "David", "Emma", 
        "Fiona", "Graham", "Helen", "Ian", "Jane", 
        "Karen", "Liam", "Michelle", "Nigel", "Olivia", 
        "Paul", "Rebecca", "Simon", "Tanya", "Wayne",
        "Adam", "Brian", "Chloe", "Daniel", "Elaine",
        "Frank", "Gareth", "Hannah", "Jack", "Kylie",
        "Luke", "Megan", "Nathan", "Oscar", "Patricia",
        "Rachel", "Steven", "Tracy", "Vince", "Yvonne",
        "Alex", "Brendan", "Claire", "Deborah", "Edward",
        "Felicity", "Geoff", "Heather", "Jonathan", "Kirsty",
        "Linda", "Matthew", "Nicole", "Peter", "Renee",
        "Scott", "Trevor", "Victoria", "Wendy", "Zoe",
        "Amanda", "Brett", "Christine", "Dominic", "Erin",
        "Frederick", "Glen", "Harriet", "Jason", "Kim",
        "Lauren", "Mark", "Natalie", "Patrick", "Robyn",
        "Stuart", "Theresa", "Vanessa", "Warren", "Yvette",
        "Anthony", "Bruce", "Cindy", "Damian", "Ellen",
        "Frances", "Gordon", "Hayley", "Jeffrey", "Kara",
        "Leanne", "Murray", "Nina", "Phillip", "Ruth",
        "Shane", "Timothy", "Veronica", "Wayne", "Yvonne"
    ]

    # Common Australian last names
    last_names = [
        "Smith", "Jones", "Williams", "Brown", "Taylor", 
        "Wilson", "Thomson", "White", "Martin", "Walker", 
        "Harris", "Robinson", "Kelly", "King", "Wright", 
        "Mitchell", "Scott", "Evans", "Edwards", "Turner",
        "Morgan", "Parker", "Clark", "Morris", "Stewart",
        "Ward", "Campbell", "Cooper", "Carter", "Phillips",
        "Lee", "Bennett", "Gray", "Ross", "Powell",
        "Patterson", "Sullivan", "Russell", "Brooks", "Duncan",
        "Dixon", "Reid", "Grant", "Armstrong", "Shaw",
        "Murray", "Graham", "Ford", "Mills", "Kennedy",
        "Ellis", "Hamilton", "Hunter", "Warren", "Wells",
        "Arnold", "Stone", "Stephens", "Palmer", "Webb",
        "Rogers", "Lane", "Reynolds", "Gardner", "Chapman",
        "Mason", "Knight", "Harvey", "Pearson", "Holland",
        "Reed", "Hawkins", "Freeman", "Cole", "Hudson",
        "Gibson", "George", "Curtis", "West", "Payne",
        "Johnston", "Banks", "Holmes", "Fisher", "Hunt",
        "Rice", "Long", "Woods", "Hunter", "Rose",
        "Simmons", "Richards", "Grant", "Spencer", "Butler"
    ]


    fname = random.choice(first_names)
    mname = random.choice(last_names)
    lname = random.choice(last_names)
    r = random.randint(999, 9999)


    user = f"{fname}.{lname}.{mname}.{r}"


    bday = "22 11 1984"
    g = "3"
    pwd = "pYm%T!3%+qRBkg+8PmCxfp*)VtX1=+gB"


    try:

        driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

        #name
        print("[/] Entering name -> waiting...", end="\r")
        driver.find_element(By.NAME, "firstName").send_keys(fname)
        driver.find_element(By.NAME, "lastName").send_keys(lname)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()
        print("[+] Entering name -> Done!          ")



        #bday
        print("[/] Entering birthday -> waiting...", end="\r")
        wait = WebDriverWait(driver, 30)
        day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

        birthday_elements = bday.split()

        Select(driver.find_element(By.ID, "month")).select_by_value(birthday_elements[1])
        driver.find_element(By.ID, "day").send_keys(birthday_elements[0])
        driver.find_element(By.ID, "year").send_keys(birthday_elements[2])
        print("[+] Entering birthday -> Done!          ")



        #gender
        print("[/] Entering gender -> waiting...", end="\r")
        Select(driver.find_element(By.ID, "gender")).select_by_value(g)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()
        print("[+] Entering gender -> Done!          ")



        
        #email
        print("[/] Entering custom email -> waiting...", end="\r")
        time.sleep(2)
        if driver.find_elements(By.ID, "selectionc4") :
            custom = wait.until(EC.element_to_be_clickable((By.ID,"selectionc4") ))
            custom.click()
        
        custom = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
        driver.find_element(By.NAME, "Username").send_keys(user)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()
        print("[+] Entering custom email -> Done!          ")


        
        #pwd
        print("[/] Entering and confirming password -> waiting...", end="\r")
        wait.until(EC.visibility_of_element_located((By.NAME, "Passwd"))).send_keys(pwd)
        div = driver.find_element(By.ID, "confirm-passwd")

        div.find_element(By.NAME, "PasswdAgain").send_keys(pwd)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe").click()
        print("[+] Entering and confirming password -> Done!          ")



        #phone
        print("[/] Entering phone number -> waiting...", end="\r")
        time.sleep(4)
        phoneinp = driver.find_element(By.ID, "phoneNumberId")

        if num[0]=="0":
            phoneinp.send_keys("+44"+num[1:])
        else:
            phoneinp.send_keys("+44"+num)

        driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d").click()
        print("[+] Entering phone number -> Done!          ")


        time.sleep(2)

        if "This phone number has been used too many times" in driver.page_source:
            return -1


        #enter code
        print("[/] Retrieving sms code -> waiting...", end="\r")
        code=api.getsms(oid)
        if code==-1:
            api.cancel(oid)
            return
        print("[+] Retrieving sms code -> Done!          ")
        print(f"[!] sms code -> {code}")
        print("[/] Entering sms code -> waiting...", end="\r")
        codeinp=driver.find_element("xpath", "//input[@type='tel']")
        codeinp.send_keys(code)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()
        print("[+] Entering sms code -> Done!          ")


        
        #skip recovery
        print("[/] Skipping recovery -> waiting...", end="\r")
        time.sleep(2)
        #"//button[@id='recoverySkip']"
        driver.find_element(By.XPATH, "//div[@id='recoverySkip']").click()
        print("[+] Skipping recovery -> Done!          ")

        

        #next
        print("[/] Clicking next -> waiting...", end="\r")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()
        print("[+] Clicking next -> Done!          ")



        #terms
        print("[/] Agreeing to ToS -> waiting...", end="\r")
        time.sleep(2)
        trust = driver.find_element(By.XPATH, "//*[text()='I agree']")
        parent = trust.find_element(By.XPATH, "./..")
        parent.click()
        print("[+] Agreeing to ToS -> Done!          ")

        time.sleep(6)



        print(f"\n[!] Account successfully created: {user}@gmail.com\n")

        print("[/] Writing to disk -> waiting...", end="\r")
        f=open("data/creds.txt","a")
        f.write(f"{user}@gmail.com,{pwd}\n")
        print("[/] Writing to disk -> Done!        \n")

        time.sleep(3)

        return user

    except Exception as e:
        print(e)
        print()
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    finally:
        driver.quit()


def clear():

    return 
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear()
    print("\n\n[!] Generating Accounts\n")

    print("[+] Purchasing a new number\n")
    li=api.newnum()
    if "OPEN_" in li:
        oid=li.split("OPEN_")[1]
        print(f"[+] {api.cancel(oid)}")
        main()
        return
    if "NO_BAL" in li:
        sms.sms(cfgnum, f"[GBot] : Juicysms balance is ${api.getbal()},\n               please refill.\n               Rate: $?.?? per review")
        return

    return 0 if li==-1 else 0
    oid=li[0]
    num=li[1]

    succ = acct(oid, num)
    lis=f"[!] Created accounts\n\n\t{succ}@gmail.com"

    while succ != -1:
        clear()
        print(f"[!] Generating Accounts for {num}\n")
        print(lis+"\n\n")

        li=api.reuse(oid)
        print(f"[+] Reusing {num}\n")
        return 0 if li==-1 else 0
        oid=li[0]
        num=li[1]
        succ = acct(oid, num)
        lis+=f"\n\n\t{succ}@gmail.com"

    print(f"[-] Max accounts created for {num}\n")



