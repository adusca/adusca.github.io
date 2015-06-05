---
title: Outreachy log
---
###Week 1:

####2015-05-25:

* Wrote initial implementation of [pulse_actions](https://github.com/adusca/pulse_actions/)

####2015-05-26:

* Made pulse_actions more generic

####2015-05-27:

* Added [direct retrigger feature to mozci](https://github.com/armenzg/mozilla_ci_tools/pull/224)
* Uploaded pulse_actions to [Pypi](https://pypi.python.org/pypi/pulse-actions)

####2015-05-28:

* Deployed pulse-actions to Heroku
* Added [papertrail](https://addons-sso.heroku.com/apps/pulse-actions/addons/papertrail?q=worker) to Heroku
* Added installing and running guides to pulse_actions' documentation
* Wrote step-by-step guide of how to add more functionality to pulse_actions
* Reviewed [PR 226](https://github.com/armenzg/mozilla_ci_tools/pull/226)

####2015-05-29:

* Added [--existing-only flag to alltalos](https://github.com/armenzg/mozilla_ci_tools/pull/228)

### Week 2

#### 2015-06-01:

* Wrote PR for [issue 232](https://github.com/armenzg/mozilla_ci_tools/pull/234)
* Wrote [tests](https://github.com/armenzg/mozilla_ci_tools/pull/235) for query_jobs_schedule 

#### 2015-06-02:

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
