---
title: When does a number end?
layout: post
---

3/16 is exactly equal to 0.1875 but 3/14 is a endless repeating decimal. Why?

A number has a finite decimal representation if we get an integer via
multiplying it by 10 enough times.

For example:
3/16 * 10 = 30/16 = 15/8   or 0.1875 * 10  = 1.875
15/8 * 10 = 150/8 = 75/4   or 1.875 * 10 = 18.75
75/4 * 10 = 750/4 = 375/2  or  18.75 * 10 = 187.5
375/2 * 10 = 3750/2 = 1875 or 187.5 * 10 = 1875
We got an integer!

Multiplying by 10 n times is the same as multiplying by 2^n * 5^n:
3/16 = 3/2^4 * (2^4*5^4) = 3 * 5^4

The denominator disappears. If a (reduced) fraction denominator can be
written as 2^a * 5^b [^1], then if we multiply this fraction by
10^(max(a, b)) we will get an integer, which means that the decimal
representation of the fraction will end. A similar argument shows that
the converse is also true.

# What about binary representations?

As in with 10, a fraction only has a finite representation in binary
if we can get an integer via multiplying it enough times by 2. In base 10,
this meant that the denominator had to be of the form 2^a * 5^b; in
base 2 the denominator has to be of the form 2^a.

This means that innocent-looking numbers in base 10 like 0.1 actually
have an infinite representation in base 2, which means they don't
really fit in a float.


[^1] a, b non-negative integers
