Email Service
---

I use Trello as my capture device to capture my action items, ideas, etc. Trello is essentailly a browser and uses a
ton of memory to run all of the time. My solution is a lightweight program that opens a window for you to enter in the
content to send to your Trello email-to-card service.

OSX has security issues with watching keystrokes in the background, so implementing this only in Python
was difficult to do, even with PyInstaller or Platypus. My solution so far has been to create an Applescript
application and just keeping it in the sidebar. You can see the full instructions on my site:
https://more.milofultz.com/2020/07/22/make-python-apps