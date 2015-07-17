---
title: Outreachy log
---
### Week 1:

#### 2015-05-25:

* Weekly 1:1 with Armen
* Wrote initial implementation of [pulse_actions](https://github.com/adusca/pulse_actions/)
* Wrote blog post about gproof2dot

#### 2015-05-26:

* Made pulse_actions more generic

#### 2015-05-27:

* Added [direct retrigger feature to mozci](https://github.com/armenzg/mozilla_ci_tools/pull/224)
* Uploaded pulse_actions to [Pypi](https://pypi.python.org/pypi/pulse-actions)

#### 2015-05-28:

* Deployed pulse-actions to Heroku
* Added [papertrail](https://addons-sso.heroku.com/apps/pulse-actions/addons/papertrail?q=worker) to Heroku
* Added installing and running guides to pulse_actions' documentation
* Wrote step-by-step guide of how to add more functionality to pulse_actions
* Reviewed [PR 226](https://github.com/armenzg/mozilla_ci_tools/pull/226)
* Wrote blog post about pulse actions

#### 2015-05-29:

* Added [--existing-only flag to alltalos](https://github.com/armenzg/mozilla_ci_tools/pull/228)

### Week 2

#### 2015-06-01:

* Wrote PR for [issue 232](https://github.com/armenzg/mozilla_ci_tools/pull/234)
* Wrote [tests](https://github.com/armenzg/mozilla_ci_tools/pull/235) for query_jobs_schedule 

#### 2015-06-02:

* Weekly 1:1 with Armen
* Wrote PR to allow reading LDAP credentials from env variables ([issue 237](https://github.com/armenzg/mozilla_ci_tools/pull/238))
* Filed [bug 1170839](https://bugzilla.mozilla.org/show_bug.cgi?id=1170839) to rest pulse_actions on ash 
* Wrote tests for query_repositories, query_repo_url and query_repository

#### 2015-06-03:

* Wrote PR to recognize repo names in b2g jobs
* Wrote PR to allow multiple buildernames in trigger.py

#### 2015-06-04:

* Filed 2 good first bugs for mozci
* Worked on PR to allow multiple buildernames
* Wrote PR to fix 'UnboundLocalError' in mozci
* Fixed bugs in pulse_actions
* Investigated [issue 233](https://github.com/armenzg/mozilla_ci_tools/issues/233)

#### 2015-06-05:

* Investigated python static analysis tools. Tried so far: pylint, pyflakes and pychecker
* Went through pycharm's warnings in mozci, fixed relevant (and small) ones
* Filed 1 good first bug in mozci
* Wrote blog post about static analysis tools

### Week 3

#### 2015-06-08:

* Added tests to buildapi, refactored query_job_status
* Investigated issue 233

#### 2015-06-09:

* Weekly 1:1 with Armen
* Investigated why sometimes coveralls fails randomly

#### 2015-06-10:

* Had a meeting about taskcluster
* Fixed random coverage failures and wrote a blog post about it
* Investigated sending pulse messages

#### 2015-06-11:

* Tried to understand mach_commands.py

#### 2015-06-12:

* Had a meeting about pulse_actions
* Talked with Ryan and Joel about new mozci use cases
* Made PR to also consider unknown jobs as running jobs in mozci

### Week 4

#### 2015-06-15:

* Wrote PR to allow triggering every coalesced job with mozci

#### 2015-06-16:

* Weekly 1:1 with Armen
* Fixed bugs in yesterday PR
* Started writing mozci cookbook

#### 2015-06-17:

* Asked Joel about the right behaviour for coalesced mode and wrote a PR for it

#### 2015-06-18:

* Turned on pulse_actions on the ash branch
* Sent a message to sheriffs about where to turn it on next

#### 2015-06-19:

* Turned off pulse_actions due to permission issues
* Made a mozci release
* Reviewed a new-contributor patch
* Tried running find_all_by_status on Heroku
* Investigated mozci memory usage

### Week 5

#### 2015-06-22:

* Mentored debugger
* Investigated ijson for improving mozci memory usage

#### 2015-06-23:

* Tried making our ijson usage less hacky
* Wrote week summary to replace 1:1

#### 2015-06-24:

* Wrote PR for issue 258
* Wrote PR for issue 213
* Wrote PR for issue 260

#### 2015-06-25:

* Added basic automatic backfilling to pulse_actions
* Wrote experimental pulse publisher

#### 2015-06-26:

* Finished experimental pulse publisher

### Week 6

#### 2015-06-29:

* Wrote blog post about changing goals
* Worked on adding --fill-in mode

#### 2015-06-30:

* Weekly 1:1 with Armen
* Fought internet problems
* Worked on details for next week's trip
* Found PR about unknown jobs that I forgot to submit

#### 2015-07-01:

* Worked on automatic backfilling PR
* Investigated fill-in possibilities

#### 2015-07-02:

* Reviewed Vaibhav's PRs

#### 2015-07-03:

* Released a new mozci version
* Pre-trip day off

### Week 7

Toronto!

### Week 8

#### 2015-07-13:

* Post-trip day off
* Helped Vaibhav get started with pulse actions

#### 2015-07-14:

* Wrote tests for mozillapulse patch (bug 1180897)
* Read web app tutorials

#### 2015-07-15:

* Wrote json-to-html-checkbox part of try_extender

#### 2015-07-16:

* Wrote a function to generate a graph per revision for try_extender
* Worked on fixing tests for mozillapulse patch
* Finished ActiveData PR for mozci
* Reviewed Vaibhav's PR
* Filed an issue for Ryan's feature request

#### 2015-07-17:

* Finished fixing tests for mozillapulse PR
* mozci coordination meeting
