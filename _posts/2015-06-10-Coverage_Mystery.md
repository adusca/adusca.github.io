---
layout: post
title: Tracking down a non-deterministic coverage failure
tags: [mozilla]
---


At Mozilla CI Tools, we use [Coveralls](https://coveralls.io/) to track our test coverage progress. In the past month we noticed that sometimes the coverage changes even in PRs that only [changed files that are not tracked by coveralls](https://github.com/armenzg/mozilla_ci_tools/pull/251). How come?

Comparing coverage reports for builds in which this problem happens, I noticed that [this line](https://github.com/armenzg/mozilla_ci_tools/blob/0bd7e3ff5db8f4786671ad544662bc29b0e0c20e/mozci/platforms.py#L231) would sometimes be marked as covered, sometimes as not covered. The line belongs to a function that builds a graph from a list. An interesting thing about this function is that the order of the list does not affect the final graph, but it does affect the code path taken inside the function. In the test for this function, the input comes from a call to a dict.keys() method. Also, an interesting thing about the .keys() method is that it always produces a list containing the same elements, but the order varies. Mystery solved!

So a single [sort()](https://github.com/armenzg/mozilla_ci_tools/pull/254) command could fix those annoying random coverage failures!
