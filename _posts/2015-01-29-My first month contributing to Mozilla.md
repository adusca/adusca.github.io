---
layout: post
title: My first month contributing to Mozilla
---

During Hacker School's winter break, I decided that I was finally ready to do something I've always wanted to do: contribute to Open Source.

#### First step

The first thing I had to do was find something to work on. Searching for a project to which I could contribute I found [bugs ahoy](http://www.joshmatthews.net/bugsahoy/), a site that collects mentored bugs in Mozilla. I used the filters to look for [simple Python bugs with no owner](http://www.joshmatthews.net/bugsahoy/?py=1&unowned=1&simple=1). It took me a while, but eventually I found an unclaimed bug that I believed I would be able to fix.

#### Mozilla Developer Network

My very first bug was [a Django bug for MDN](https://bugzilla.mozilla.org/show_bug.cgi?id=1052195). The idea was simple enough to understand: if someone signed up for [MDN](https://developer.mozilla.org/en-US/) with an GitHub account and they only have one verified email this email should be selected by default.

The first step to solve this bug was to get a development environment working, and that was surprisingly easy, thanks to the great [documentation](http://kuma.readthedocs.org/en/latest/installation-vagrant.html).

I started trying to find everything by myself and not bothering anyone, but after hours of grep without finding anything relevant I decided to go to the IRC channel (#mdndev) and ask. That's how I met Luke Crouch (:groovecoder), that became my mentor for this bug. One minute after asking I knew the function that needed to be changed and I was able to start working.

For this bug I wanted to pass a default argument to RadioSelect, and reading Django's documentation didn't help me figure out how to do that. I was getting frustrated when I realized that I could read the source code for Radio Select and after that it became obvious what to do.

When I submitted a [PR](https://github.com/mozilla/kuma/pull/2976), groovecoder asked me if I could add a test for it and I took the opportunity to learn about testing in Django. While working on that I found a little mistake in mdn's repo documentation, and submitted a [PR](https://github.com/mozilla/kuma/pull/2977) to fix that.

After that I looked for another MDN bug to work on and found [bug 1116419](https://bugzilla.mozilla.org/show_bug.cgi?id=1116419). MDN has a nice feature that transforms 'bug XXXXXXX' in a link to the right bugzilla page, but this feature did not work if you wrote 'Bug XXXXXXX', which was annoying.

I knew that there was a function somewhere in the code to generate the link, and I guessed that the string 'bugzilla.mozilla.org' would show up somewhere in the function, so I tried:

```
grep -R bugzilla.mozilla.org *
```

And looking at the results I could identify the right file and from there the right function. From there all I had to do was learn regex basics and I could submit a [PR](https://github.com/mozilla/kuma/pull/2982). Once more I was asked to add tests and this time it was way easier.

#### Auto-tools

I learned in bugs ahoy that auto-tools had some Python projects, and I wanted to get involved. So I searched for a good first bug in Testing and found [bug 1116216](https://bugzilla.mozilla.org/show_bug.cgi?id=1116216): Making the code more robust by accepting arrays as well as strings. It was a simple change, but it was a reason to learn mercurial basics and also learn about [Talos](https://wiki.mozilla.org/Buildbot/Talos), a python performance testing framework that is used at Mozilla to detect regressions.

When I submitted my patch, Joel Maher (:jmaher) left a comment thanking me and inviting me to work on other projects. This made me really happy, and I went looking for other projects in Auto-tools. I discovered they had a very useful [tracking bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1088251) and I look there to see if there was anything else I could do.

I found [bug 1093939](https://bugzilla.mozilla.org/show_bug.cgi?id=1093939). As documented in jmaher's [blog post](https://elvis314.wordpress.com/2014/10/30/a-case-of-the-weekends/) there are more regression alerts on Mondays. A possible explanation for this is that weekends are less noisy. In order to confirm that we needed to measure noise per weekday.

I ended up adding a one file report generating script to Talos, and to get there I had to ask a lot of questions in IRC. Since then I started hanging out on the #ateam channel almost every day (I'm adusca), and people there are very nice.

After my patch landed jmaher told me he had a bug that he though was a good fit for me: [1119444](https://bugzilla.mozilla.org/show_bug.cgi?id=1119444). Currently Talos waits for 12 future commits before sending a regression alert. What would've happened if it waited only 3? 6? They wanted a report with accuracy numbers for different waiting windows. Although this bug also involved creating a report generating script, it was way more difficult. One problem was that the API consumer was not up to date with the real API, to solve that I ended up filing and fixing [bug 1122092](https://bugzilla.mozilla.org/show_bug.cgi?id=1122092).

I felt ready to work on a bigger project. After I mentioned that to jmaher he introduced me to Andrew Halberstadt (:ahal), who was working on [test-informant](http://brasstacks.mozilla.com/testreports/daily/latest.informant-report.html), a service that keeps track of the total number of tests being run, as well as the total number of tests that are skipped or disabled. [The goal](https://bugzilla.mozilla.org/show_bug.cgi?id=1124689) was to change the information source from manifests to structured logs, and the first step to do that was [bug 11124720](https://bugzilla.mozilla.org/show_bug.cgi?id=1124720).
