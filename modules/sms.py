#!/usr/bin/python3

"""
author: c@shed
version: 1.0

"""


import subprocess

def sms(num, msg):
    applescript = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{num}" of targetService
        send "{msg}" to targetBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript])
