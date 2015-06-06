---
layout: post
title: UnboundLocalError
tags: [mozilla]
---

Recently we had an ['UnboundLocalError' in mozci](https://pastebin.mozilla.org/8835719). A local variable was being referenced before assignment. Turns out we were only defining the variable in one branch of an 'if' statement. It was very [straightforward](https://github.com/armenzg/mozilla_ci_tools/pull/244/files) to fix. What bothered me was that this is the exact sort of error that would have been caught at compile time in other languages.

Is there a Python static analysis tool that would have caught this? I wrote a very simple module with the same bug and tried with different tools[^1]:

{% highlight python %}
"""This module bakes pizzas."""


def bake_pizza():
    """Bake a pizza."""
    number = int(raw_input())

    if number > 3:
        additional = 2
    else:
        number += 1
    print number + additional

if __name__ == '__main__':
    bake_pizza()
{% endhighlight %}

Neither [Pylint](http://pylint.org/), [Pyflakes](https://launchpad.net/pyflakes) nor [PyChecker](https://pypi.python.org/pypi/PyChecker) were able to notify me about the possibility of an 'UnboundLocalError'.

ekyle suggested that PyCharm might be able to solve this problem, and indeed, [PyCharm code inspection](https://www.jetbrains.com/pycharm/help/code-inspection.html) shows the message I wanted:

> Local variable 'additional' might be referenced before assignement

I spent a couple of hours today going through every PyCharm warning in mozci to see if there were any other bugs that it could catch. It didn't find other serious issues (I don't know if that's fortunate or not).

[1]: It ended up being the only module I've ever written that scored 10.0/10 in pylint.
