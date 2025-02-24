---
title: Outreachy log
---
### Week 1:

#### 2015-05-25:

* Weekly 1:1 with Armen
* Wrote initial implementation of [pulse_actions](https://github.com/adusca/pulse_actions/)
* Wrote blog post about gprof2dot

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
* released a new mozci version
* conviced a erahm to try mozci, he found a bug. Fixed his bug and released a new mozci version
* Reviewed Vaibhav's mozci PR

### Week 9

#### 2015-07-20:

* Added sliding menus to try-extender
* Worked on ijson PR for mozci

#### 2015-07-21:

* Worked on ijson PR for mozci
* Released a new mozci version
* Modified pulse_actions to use ijson
* Installed a C library on Heroku
* Weekly 1:1 with Armen
* Meeting about memory usage in mozci

#### 2015-07-22:

* Studied automatic backfilling logs
* Wrote PR for issue 299

#### 2015-07-23:

* Talked with Vaibhav about his PR
* Worked on adding a Flask backend to try-extender

#### 2015-07-24:

* Managed to get try-extender to run locally

### Week 10

#### 2015-07-27:

* Presented try-extender demo on ateam meeting
* Added Persona login to try-extender
* Deployed 2 workers on Heroku

#### 2015-07-28:

* Weekly 1:1 with Armen
* Taught Vaibhav how to do a release
* Turned automatic backfilling on
* Reviewed Vaibhav PRs

#### 2015-07-29:

* Modified try-extender to use guincorn

#### 2015-07-30:

* Deployed try-extender to Heroku
* pulse-actions Heroku work

#### 2015-07-31:

* Added error messages to try-extender
* Made try-extender prettier

### Week 11

#### 2015-08-03:

* Worked on failed_jobs PR
* Reviewed Vaibhav's PR
* Deployed changes to Heroku
* Fixed authentication on try-extender

#### 2015-08-04:

* Wrote try-extender landing page

#### 2015-08-05:

* Fixed allthethings.json x try-extender bug
* Turned on automatic backfilling
* Monitored automatic backfilling

#### 2015-08-06:

* Investigated Heroku timeouts
* Made triggering work in the backgroung for try-extender

#### 2015-08-07:

* Investigated missing Buildapi revisions
* Wrote PR for using pushlog to validate revisions
* Fixed try-extender to only show each job once

### Week 12

#### 2015-08-10:

* Wrote blog post about try extender
* Reviewed Vaibhav's PR and proposed new solution
* Wrote PR for upstream-to-downstream function in mozci

#### 2015-08-11:

* Weekly 1:1 with Armen
* Changed missing jobs logic on TE
* Prepared presentation

#### 2015-08-12:

* Prepared presentation
* Added message about delay on TE

#### 2015-08-13:

* Retrigger failed job on the same push
* Presentation day

#### 2015-08-14:

* Submitted PR to fix tests
* Finished PR for using pushlog to validate revisions
* Started investigating TH jobs UI
* Mozci meeting

### Week 13

#### 2015-08-17:

* Fixed small mozci issues
* Filed a mozci issue
* Wrote a script to hardcode a json with possible jobs
* Wrote a hacky prototype TH push extender UI

#### 2015-08-18:

* Weekly 1:1 with Armen
* SETA meeting
* Discussed automatic backfilling problems
* Backed out previous retriggering change
* Wrote CSS for possible jobs

#### 2015-08-19:

* Made it possible to select jobs on TH
* Wrote the pulse message sending part
* Fixed many bugs with the initial implementation

#### 2015-08-20:

* Made possible jobs work with polling/filters
* TH meeting
* Made TH consume and process a list of builders instead of a harcoded file
* Submitted PR
* Started working on the ETL layer
* Updated PR

#### 2015-08-21:

* Debugged MySQLdb bug on ETL
* Finished the API implementation
* Addressed review comments

### Week 14

#### 2015-08-24:

* Fixed bugs ahal found on try extender
* Addressed more review comments

#### 2015-08-25:

* Last weekly 1:1 with Armen
* Worked on cleaning up the db every day
* Worked on making it possible to hide possible jobs
* Last day!
