---
layout: post
title: Structured logs in Test Informant
---

[Test Informant](http://brasstacks.mozilla.com/testreports/daily/latest.informant-report.html) is a test monitoring service for Mozilla. It provides a high level view of what's going on with automated tests.

It currently uses [pulse](https://pulse.mozilla.org/) to listen for the completion of build jobs and then downloads the associated tests.zip file (that can reach 200MB), finds test manifests and parses them. After that it saves the information it found in a Mongo database.

The problem with that approach is that only a subset of tests is compatible with [manifestparser](http://people.mozilla.org/~wlachance/mozbase-docs/manifestparser.html), and Test Informant only supports those.

[mozlog.structured](http://people.mozilla.org/~wlachance/mozbase-docs/mozlog_structured.html) provides structured logs as JSON files with information about tests that is easily machine-readable, but can also be interpreted by humans. [Here](http://mozilla-releng-blobs.s3.amazonaws.com/blobs/mozilla-inbound/sha512/f3e38056b2f2f509e7dfed0c4e4a13c0c39a15b1d0b505d6043d1b2a44cd9687c84c6b33dbce05a7eeb11366445977ff1ce3a4e8cc9ad570db432c9c0e41ce4c) is an example. Most of the suites compatible with manifestparser are also compatible with mozlog.structured, and so by using structured logs we get a lot of new suites. Therefore, the goal was to make Test Informant use structured logs instead of parsing manifests.

### Listening for test jobs

Structured logs are attached to test jobs, not build jobs. So the first step to make Test-Informant use structured logs would be to make it [listen for test jobs](https://bugzilla.mozilla.org/show_bug.cgi?id=1124720) instead of build jobs on pulse listener.

The hardest part was making sure my code was working as expected. I had to wait for tests to show up in pulse, and sometimes that took a long time. One thing that helped was listening to 'mozilla-inbound' instead of 'mozilla-central', because it has much more activity. That way I ended up receiving several "Your pulse queue is full" emails.

### Reading structured logs

After step 1 was ready, it was time to actually consume structured logs. Turns out that it's pretty easy. All I had to do was adapt the example code from [ahal's blog post](http://ahal.ca/blog/2014/consume-structured-test-results/) and that part was done.

Dealing with database issues was harder. I had to worry about race conditions and also deal with chunking (some test suites are split into several chunks that must be added to the same database entry).

### Adding more tests

Test-Informant only deals with tests in its [configuration file](https://github.com/mozilla/test-informant/blob/master/informant/config.py). There were a bunch of new tests that had structured logs but weren't in config.py. I wrote the following script to identify pairs of platforms and suites that were compatible with structured logs:

{% highlight python%}
def print_name(self, data):
     structured_logs = [(fn, url) for fn, url in data['blobber_files'].iteritems() 
                        if fn.endswith('_raw.log')]
     if structured_logs and not self.get_suite_name(data['test'], data['platform']):
         print data['platform'], data['test']
{% endhighlight %}

I left my script running for a couple hours, and after that I added the new platforms/suites I found to [config.py](https://github.com/mozilla/test-informant/pull/3/files).

### What happened

[This](http://people.mozilla.org/~ahalberstadt/temp-report.html) is a sample report using structured logs. It has a bunch of new tests, and that is actually a problem. The report links to skipped tests, but now not every test lives on [https://dxr.mozilla.org/mozilla-central/source/](https://dxr.mozilla.org/mozilla-central/source/), so our previous way of figuring out the URL does not work anymore. My work resulted in four [PRs](https://github.com/mozilla/test-informant/pulls?q=is%3Apr+author%3Aadusca+is%3Aclosed) that were merged on the [structured_log branch](https://github.com/mozilla/test-informant/tree/structured_log), and we are waiting for follow-up work from other contributors to merge structured_logs into master.

It was a really rewarding project and I'm excited about seeing it being used!
