#!/usr/bin/python3

"""
author: c@shed
version: 1.0

"""

import requests
import time



api="-----"


def newnum():
    try:
        res = requests.get(f"https://juicysms.com/api/makeorder?key={api}&serviceId=1&country=UK")
        return orderparse(res.text)
    except Exception as e:
        print(e)
        return -1


def getbal():
    try:
        res = requests.get(f"https://juicysms.com/api/getbalance?key={api}")
        return float(res.text)
    except Exception as e:
        print(e)
        return -1


def cancel(oid):
    res=requests.get(f"https://juicysms.com/api/cancelorder?key={api}&orderId={oid}")
    return res.text

def getsms(oid):
    try:
        res = requests.get(f"https://juicysms.com/api/getsms?key={api}&orderId={oid}")
        i=0
        while ("WAITING" in res.text):
            if i==60:
                return -1
            time.sleep(1)
            res = requests.get(f"https://juicysms.com/api/getsms?key={api}&orderId={oid}") 
            i+=1
        return res.text.split("G-")[1].split(" is")[0]
    except Exception as e:
        print(e)
        return -1


def reuse(oid):
    try:
        res = requests.get(f"https://juicysms.com/api/reuse?key={api}&orderId={oid}")
        return orderparse(res.text)
    except Exception as e:
        print(e)
        return -1


def orderparse(res):
    if "ORDER_ID" not in res:
        print("[-] "+res)
        return res
    r=res.split("_")
    return [r[2],r[4]]
           #oid  #num 