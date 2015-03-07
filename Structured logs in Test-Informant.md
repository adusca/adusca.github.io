---
layout: post
title: Structured logs in Test-Informant
---

[Test-Informant](http://brasstacks.mozilla.com/testreports/daily/latest.informant-report.html) is a test monitoring service for Mozilla. It provides a high level view of what's going on with automated tests.

It currently uses [pulse](https://pulse.mozilla.org/) to listen for the completion of build jobs and then downloads the associated tests.zip file (that can reach 200Mb), finds test manifests and parses then. After that it saves the information it founds in a Mongo database.

The problem with that approach is that only a subset of tests is compatible with manifestparser, and Test-Informant only support those.

#### Structured Logs

#### Listening for test jobs

Structured logs are attached to test jobs, not build jobs. So the first step to make Test-Informant use structured logs would be to make it [listen for test jobs](https://bugzilla.mozilla.org/show_bug.cgi?id=1124720) instead of build jobs on pulse listener.

The hardest part was making sure my code was working as expected. 
#### Reading structured logs


#### Adding more tests


#### What happened

[This](http://people.mozilla.org/~ahalberstadt/temp-report.html) is a sample report using structured logs. It has a bunch of new tests, and that is actually a problem. The report links to skipped tests, but now not every test lives on https://dxr.mozilla.org/mozilla-central/source/ so our previous way of figuring out the url does not work anymore. My changes are merged on the [structured_log branch](https://github.com/mozilla/test-informant/tree/structured_log), and we are waiting for follow up work from other contributors to merge structured_logs into master.
