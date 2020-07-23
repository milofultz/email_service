#!/usr/bin/env python3

"""

Email Sender Background Service

I use Trello as my capture device to capture my action items, ideas, etc. Trello is essentailly a browser and uses a
ton of memory to run all of the time. My solution is a lightweight program that opens a window for you to enter in the
content to send to your Trello email-to-card service.

OSX has security issues with watching keystrokes in the background, so implementing this only in Python
was difficult to do, even with PyInstaller or Platypus. My solution so far has been to create an Applescript
application and just keeping it in the sidebar. You can see the full instructions on my site:
https://more.milofultz.com/2020/07/22/make-python-apps

"""

import json
import smtplib
import tkinter as tk
from tkinter import simpledialog

def gui_for_input():
    ROOT = tk.Tk()
    ROOT.withdraw()
    content = simpledialog.askstring(
        title="Email", prompt="What's your message?")
    return content

def json2dict(fp):
    """ Converts a JSON file into a dict. """
    with open(fp, 'r') as f:
        dic = json.load(f)
    return dic

def send_email(dic, body):
    un = dic['un']
    pw = dic['pw']
    server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    server.ehlo()
    server.login(dic["un"], dic["pw"])
    server.sendmail(dic["un"], dic["to"], body)
    return

if __name__ == "__main__":
    config_fp = 'config.json'
    email_dic = json2dict(config_fp)
    body = gui_for_input()
    if body is not None:
        send_email(email_dic, body)