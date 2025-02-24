---
layout: post
title: Adding Digits in Python (or Smarter-looking doesn't mean better)
---


Given a positive integer, compute the sum of its digits. This very simple task ended up taking me in my first journey through Python's internals.


The first solution that came to my mind was:


{% highlight python %}
def first_way(n):
    stringified_num = str(n)
    ans = 0
    for digit in stringified_num:
        ans += int(digit)
    return ans
{% endhighlight %}

I could make it a one-liner:

{% highlight python %}
def first_way_one_liner(n):
    return sum([int(digit) for digit in str(n)])
{% endhighlight %}

So if I start with the number 1234, I'll first convert it to the string "1234". Then I will look at every character in the string convert it back to an integer and add that. That's ugly, and it sounds so inefficient.


I could get the last digit of an integer doing n % 10. And the next-to-last digit is just the last digit of n/10[^1]:

{% highlight python %}
def second_way(n):
    if n == 0:
        return 0
    return (n % 10) + second_way(n/10)
{% endhighlight %}

Or an iterative version:

{% highlight python %}
def second_way_iterative(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n = n/10
    return ans
{% endhighlight %}

The second way is harder to read, but it's better, right? Python has to know every digit of a number to convert it to a string, so I was duplicating work by looking at every digit again.

### Timing

I decided to experiment calling the 4 functions 100,000 times each [^2] with a 400-digit integer and comparing run times. My theory: there would be no real difference between two functions of the same way, but the second way would be faster then the first. My results:

{% highlight bash %}
~$ time python adding_digits_first_way.py
real	0m11.837s
user	0m11.832s
sys	0m0.008s
~$ time python adding_digits_first_way_one_liner.py
real	0m11.898s
user	0m11.905s
sys	0m0.000s
~$ time python adding_digits_second_way.py
real	0m32.952s
user	0m32.968s
sys	0m0.004s
~$ time python adding_digits_second_way_iterative.py
real	0m32.770s
user	0m32.786s
sys	0m0.004s
{% endhighlight %}

Turns out my intuition was right about the first part, but very wrong about the second.

### Why?

The answer lies in [str(n)](https://github.com/python-git/python/blob/master/Objects/longobject.c#L1294).

Just like second_way, str(n) also does divisions and modulos to get every digit. But it is smarter. For a 400-digit number, instead of doing 400 divisions and modulos by 10 (like second_way) it first does 45 divisions by 10^9, getting 44 9-digit numbers and one 4-digit number. Then it does 400 divisions and modulos by 10 to extract the digits of those numbers.[^3] Those divisions are much faster because the dividend fits in a machine integer[^4] so there is way less overhead and the division is essentially just one machine instruction. On the other hand, almost every dividend in second_way does not fit in a machine int.[^5]

Let's apply this optimization to second_way:

{% highlight python %}
def second_way_optimized(n):
    ans = 0
    while n > 0:
        tmp = int(n % 1000000000)
        while tmp > 0:
            ans += tmp % 10
            tmp = tmp / 10
        n = n/1000000000
    return ans
{% endhighlight %}

And time it:

{% highlight bash %}
~$ time python adding_digits_second_way_optimized.py
real	0m7.991s
user	0m7.987s
sys	0m0.004s
{% endhighlight %}

That's faster than first_way!

### Conclusion

This experience taught me that the smarter-looking code is not always better. Right after I wrote first_way I thought it was a stupid solution. Then I came up with second_way and I got ashamed of myself for having written first_way. Reflecting on why one solution was so much better than the other led me here.

The next time I need to sum the digits of an integer[^6] I will use the first way and be proud of it.




[^1]: I spent a ridiculous amount of time deciding if the base case should be n == 0 or n < 10. If you have a strong opinion about it, please tell me!
[^2]: 100,000 was enough to get a stable run time between several different runs.
[^3]: second_way does d divisions by 10 for a d-digit number, str does d/9 divisions by 10^9 and then d divisions by 10.
[^4]: For 32-bits machines, n fits in a machine integer when  n < 2,147,483,647. Since 999,999,999 < 2,147,483,647, every 9-digit number fits in a machine integer.
[^5]: CPython uses 2 types of integers: PyInt (when the number is smaller then a machine int) and PyLong. PyInt divisions are essentially one machine instruction, for PyLong divisions there is overhead. Since CPython does not automatically convert a PyLong to a PyInt when it fits, **every** division in second_way is a PyLong division. int() forces the conversion.
[^6]: Okay, I never actually needed to add digits, but if it happens, I'm prepared.
