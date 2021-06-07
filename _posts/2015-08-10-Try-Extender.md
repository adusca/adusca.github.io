---
layout: post
title: Extending Try pushes
tags: [mozilla]
---

Are you tired of having to do a new try push just because you forgot a
test? Your problems are over! Meet Try
Extender. This new web app allows
you to add new jobs to existing try pushes, all you have to do is log
in, choose a revision and pick the jobs you want!

OK, now I'm done with my parody informercial.

Try Extender is a web app running on Heroku that uses
[mozci](https://mozilla-ci-tools.readthedocs.org/en/latest/) to
trigger new jobs for a try push. It is still a prototype, but if you
want to extend a push you are welcomed to try it out! Currently it can
only add new test jobs to completed build jobs or add new build jobs.

Right now the main goal is just to validate the idea. Depending on how
this experiment goes we might work on integrating it into Treeherder,
or leave it as a stand-alone web app.
