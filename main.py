#!/usr/bin/env python3

"""

Email Sender Background Service

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