---
layout: post
title: Platforms, buildbots and allthethings
tags: [mozilla]
---

When I asked about larger projects to get involved in, Joel (:jmaher) told me about a new tool suite that's being written in Python: [Mozilla Continuous Integration Tools](https://github.com/armenzg/mozilla_ci_tools). The project maintainer is Armen Zambrano (:armenzg) and talking with him on the #ateam IRC channel I discovered that a big problem they had was the function [associated_build_job()](https://github.com/armenzg/mozilla_ci_tools/blob/ddea68d3446a5eb29175ab29e451bbef18e866c5/mozci/platforms.py#L46) in platforms.py. That ended up sending me in a journey through [buildbot source code](https://hg.mozilla.org/build/braindump/file/961db9340928/buildbot-related/dump_master_json.py). But first, the problem.

#### What should associated_build_job() do?

When someone makes a new commit to a Mozilla repo, a lot of tests run in a lot of different platforms. You can see what is happening live on [Treeherder](https://treeherder.mozilla.org/). Every test job has a corresponding build job that triggers it, [e.g.](https://treeherder.mozilla.org/#/jobs?repo=mozilla-central&revision=30916c9ca768) "Ubuntu VM 12.04 mozilla-central opt test cppunit" is triggered by "Linux mozilla-central build" (you can see the name of the build job clicking on the green 'B').

The function associated_build_job should receive a test job and return its corresponding build job. That sounds easy, Treeherder already knows every test run by a given build job, right? Turns out that's not the case. Treeherder just shows what's happening on Mozilla's machines, it has no knowledge of what triggers what.

platforms.py used a mapping to know that "Ubuntu VM 12.04" is Linux, but that mapping wasn't very robust and already failed for some buildernames.

#### How a build job triggers test jobs

If there is no list of what triggers what, how test jobs get triggered? To answer that I had to study a bit of buildbot source code.

In buildbot, when a build job finishes it sends a message. When a test scheduler receives the right message, it triggers the tests it knows about. For example, "Linux mozilla-central build" sends the message "mozilla-central-linux-opt-unittest" and the test scheduler "tests-mozilla-central-ubuntu32_vm-opt-unittest" waits for that message to trigger all of its test jobs, including "Ubuntu VM 12.04 mozilla-central opt test cppunit".

There is a file called [allthethings.json](https://secure.pub.build.mozilla.org/builddata/reports/allthethings.json) where a lot of information about builders is dumped every day. I thought that adding what message a build job sends and what message a test scheduler listens to would solve platforms.py problems.

After I started working on [that](https://bugzilla.mozilla.org/show_bug.cgi?id=1129594), I discovered that the problem was more complicated than what it looked originally. Not every builder sends a message the same way, and how a builder sends a message is going to change soon, because a lot of jobs are moving to [mozharness](https://wiki.mozilla.org/ReleaseEngineering/Mozharness).

The code ended up really messy, fragile to changes and hard to maintain. Instead of trying to improve it, I talked with armenzg, my mentor, and we decided that it was not a reasonable approach. But I did have a version of allthethings.json with triggers information, and I could use that to generate test cases (12576 of them!) for associated_build_job(). Turns out that the original version returned a error in 1707 of those cases and got the wrong result 5340 times.

#### New heuristic

Working with allthethings.json and buildbot I noticed that the message sent by a build job was always just it's shortname with one or two suffixes appended. I could guess what message a build job would send from its shortname, a parameter already available in allthethings. I still needed to have a key in every test scheduler telling what message it listens to, but that part was ready from my previous approach.

After my patch to add more things to allthethings was merged, I could fully test my new heuristic. It passed every one of the 12576 test cases! It has been in production for about 3 weeks and so far no bugs. In fact, when I wrote a script to find out if it failed for any builder in allthethings I ended up finding 300 test jobs that didn't have build jobs, and this was actually a previously unknown [buildbot bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1141566).
