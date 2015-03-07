---
layout: post
title: Winter Break
---

It's Winter break now at Hacker School, but the week was quite productive. I worked on two projects.

### Ray-tracer

My first project of the week was a [ray-tracer](http://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29). I started creating classes for lines, spheres and vectors in a [geometry.py](https://github.com/adusca/ray-tracer/blob/master/geometry.py) file. After a day of work I was able to generate a black dot in a blank screen. Then I added a horizontal plane, a light font, shadows and reflections. I used [these slides](http://fileadmin.cs.lth.se/cs/Education/EDAN30/lectures/S1-rt.pdf) to guide me when I got confused. Now my program is able to generate images like:

![Ray-tracer](/images/rays14.png "Final result")
![Ray-tracer](/images/rays15.png "Final result")

### My first Mozilla bug

I've always wanted to contribute to open-source and now I finally feel ready. I searched for simple Python bugs with no owners on [Bugs Ahoy](http://www.joshmatthews.net/bugsahoy/?py=1&unowned=1&simple=1) and decided to go for [Bug 1052195](https://bugzilla.mozilla.org/show_bug.cgi?id=1052195), because it was a [Django](https://www.djangoproject.com/) bug and I've finished doing the very well explained [tutorial](https://docs.djangoproject.com/en/1.7/intro/tutorial01/) just last week. The actual bug fix involved about 3 lines of codes, but I ended up reading Django's source code to learn how things work, it was a great experience. After submitting my pull request I was asked to add test cases covering my changes. After reading the test files and experimenting a little I was able to add new tests without breaking anything. My [pull request](https://github.com/mozilla/kuma/pull/2976) was merged and now the sole verified email address is checked by default for users with only one verified email. It was a great experience and everyone was really nice with me on the IRC channel. I can't wait to pick up my next bug!
