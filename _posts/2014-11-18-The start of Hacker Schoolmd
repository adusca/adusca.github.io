---
layout: post
title: The start of Hacker School
---
This is my second day at Hacker School. Yesterday I spent my day installing Ubuntu, setting up Emacs Prelude and learning more about Git. My plan for today was to start working my way through Structure and Interpretation of Computer Programs. Before I started I though "Maybe I should use the [Pomodoro Technique](http://en.wikipedia.org/wiki/Pomodoro_Technique) to be more productive" followed by "I should make my own Pomodoro timer". So before starting SICP I made my own Pomodoro timer in Python.

#### Writing a Pomodoro timer in Python

So, I would need some way to count the time and a way to show notifications. The first part is easy with Python time module. For the second part, I first tried to use Tkinter and Tkmessagebox, and it worked OK, except that to see the notification, I couldn't be doing anything else. Looking for a way to show desktop notifications I found pynotify, wich solves the problem in a prettier way then what I was doing. My [code](https://github.com/adusca/pomodoro/blob/master/pomodoro.py) ended up this way:
{% highlight python %}
import time
import pynotify

def sendmessage(title, message, minutes):
    time.sleep(minutes*60)
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return

minutes = int(raw_input("How long? (in minutes) "))
sendmessage("Time is up!", "Take a 5 minutes break", minutes)
{% endhighlight %}

And now  I only have type python pomodoro.py in the command line, say for how many minutes I want to work and be notified when the time for my next break is up.

So now I'm back to SICP, I'm trying to read everything and do all the exercises, I'm currently in exercise 1.7. This detour cost me 1 hour, but I learned about Python modules that I didn't knew before, so I didn't just wasted 1 hour setting up a productivity tool.
