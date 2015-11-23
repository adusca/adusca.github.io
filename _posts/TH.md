---
layout: post
title: How I made Treeherder do something it was not meant to
tags: [mozilla]
---

For the past couple of months I have been working on integrating
[Try Extender](http://try-extender.herokuapp.com/) with
[Treeherder](https://treeherder.mozilla.org/#/jobs?repo=mozilla-inbound).
The goal was to add an "Add new jobs" button to Treeherder that would
display every possible job for that push. Users would then be able to
click on the jobs they want to trigger them.

It was a fun project in which I had a lot of help from the Treeherder
team and I ended up learning a little about how TH works.

## How Treeherder shows jobs

For every push, Treeherder makes a request to its API to obtain a
JSON object with every job for that push and their respective
symbols, status, types, platforms and whatever else is needed to
correctly display them. Every single one of these jobs has an id and
is in a row in Treeherder's job database.

Buildbot jobs enter TH's job database as part of the
[ETL layer](https://github.com/mozilla/treeherder/tree/master/treeherder/etl).
[Celery tasks](http://docs.celeryproject.org/en/latest/userguide/tasks.html)
parse JSON files that are generated every minute by BuildAPI.

## Runnable jobs database

Treeherder already knows how to get a list of jobs from an API
endpoint and display them in the right places (if you are curious,
[mapResultSetJobs](https://github.com/mozilla/treeherder/blob/d91cd4ba31d23bc1d4bebae5e040218584bacc72/ui/js/models/resultsets_store.js#L145)
carries most of the weight). All I needed to do was add a new API
endpoint with the list of every possible job (and the associated
information).

To feed the information to the new endpoint, I created a table of
runnable jobs. Jobs enter this new table through a daily task
that downloads and processes
[allthethings.json](https://secure.pub.build.mozilla.org/builddata/reports/allthethings.json).

## Setting things up

With the database part ready, some things had to be done on the UI
side. An (extremely reasonable) assumption made by Treeherder is that
it will only show jobs that *exist*. Since runnable jobs don't exist,
I had to create a new type of job button that would not open the
information panel and that would allow users to click on several jobs
at the same time.

The triggering part was done by sending Pulse messages to
[Pulse Actions](https://wiki.mozilla.org/Auto-tools/Projects/Pulse_actions),
which would then schedule jobs using mozci and releng's amazing
[BuildBot Bridge](https://github.com/mozilla/buildbot-bridge) (armenzg
did a great job adding BBB support to mozci).

## Possible improvements

The UX is not very intuitive.

Selecting several jobs is very annoying. One idea to fix that is
to have a keyboard shortcut to "select all visible jobs", so users
could use the search box to filter only the jobs they wanted
(e.g. "e10s") and select everything that is showing.

## Known problems

Since the triggering part happens in Pulse Actions and the selecting
part happens in Treeherder, we don't tell users what happened with
their requests. Until
[bug 1032163](https://bugzilla.mozilla.org/show_bug.cgi?id=1032163)
lands, only the push author and people with an "@mozilla.com" email
address will be able to extend pushes. Right now we have no way of
telling users that their request was denied.

We can schedule test jobs when no build job exists, and we can trigger
test jobs when the build job is already completed. But when the build
job is currently running/pending, we don't trigger anything. We could
either trigger an additional build job or do nothing, and we choose to
do nothing to avoid triggering costly unnecessary build jobs.


# What about TaskCluster jobs?

Currently "Add new jobs" only supports triggering Buildbot jobs. What
is needed to support TaskCluster jobs? 2 things:

- Having TC jobs in the runnable jobs database.
- Having a supporting tool that is able to trigger arbitrary TC jobs.

If anyone is interested in working on this, please ping me (I'm adusca
on IRC), or we can talk more about it in Mozlando ;)
