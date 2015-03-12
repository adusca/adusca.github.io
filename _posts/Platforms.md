---
layout: post
title: Platforms, buildbots and allthethings
---

When I asked about larger projects to get involved in, Joel (:jmaher) told me about a new tool's suite that's being written in Python: [Mozilla Continuous Integration Tools](https://github.com/armenzg/mozilla_ci_tools). The project maintainer is Armen Zambrano (:armenzg) and talking with him on the #ateam IRC channel I discovered that a big problem they had was the function [associated_build_job()](https://github.com/armenzg/mozilla_ci_tools/blob/ddea68d3446a5eb29175ab29e451bbef18e866c5/mozci/platforms.py#L46) in platforms.py. That ended up sending me in a journey through [buildbot source code](https://hg.mozilla.org/build/braindump/file/961db9340928/buildbot-related/dump_master_json.py). But first, the problem.

#### What should associated_build_job() do?

When someone makes a new commit to a Mozilla repo, a lot of tests run in a lot of different platforms. You can see what is happening live on [Treeherder](https://treeherder.mozilla.org/). Every test job has a corresponding build job that triggers it, [e.g.](https://treeherder.mozilla.org/#/jobs?repo=mozilla-central&revision=30916c9ca768) "Ubuntu VM 12.04 mozilla-central opt test cppunit" is triggered by "Linux mozilla-central build" (you can see the name of the build job clicking on the green 'B').

The function associated_build_job should receive a test job and return its corresponding build job. That sounds easy, Treeherder already knows every test run by a given build job, right? Turns out that's not the case. Treeherder just shows what's happening on Mozilla's machines, it has no knowledge of what triggers what and it uses [regexes](TODO) to display the content in the right lines.

