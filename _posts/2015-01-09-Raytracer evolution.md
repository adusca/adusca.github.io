---
layout: post
title: Ray-tracer evolution
---

In the last post I showed my finished ray-tracer. Now I'm going to show the steps I took to get there.

I started creating Lines and Spheres in [geometry.py](https://github.com/adusca/ray-tracer/blob/8e27e37f42a52575b316249489bce484aaaa800b/geometry.py) and generating an PNG image with [PIL](http://effbot.org/imagingbook/pil-index.htm) in [render.py](https://github.com/adusca/ray-tracer/blob/8e27e37f42a52575b316249489bce484aaaa800b/render.py). The first image I was able to generate was:

![Ray-tracer](/images/rays1.png "First Image")

Adding colors and an extra sphere was [easy](https://github.com/adusca/ray-tracer/commit/a9c55cf147658903a5a3e112d378cb5625e5e68e):

![Ray-tracer](/images/rays2.png "Colors")

Then I tried adding a Horizontal plane:

![Ray-tracer](/images/rays3.png "Horizontal Plane")

Making it checkered:

![Ray-tracer](/images/rays4.png "Checkered Horizontal Plane")

But it was in the wrong place:

![Ray-tracer](/images/rays5.png "Bad perspective")

[After](https://github.com/adusca/ray-tracer/commit/f5a6c0a5d6f65dbede2bbee595305a8f64e32d8d) fixing the positions:

![Ray-tracer](/images/rays6.png "Yeah!")

Next I tried implementing [shadows](https://github.com/adusca/ray-tracer/commit/cf251ab85ee3a797f68724ba4fafb7b4d73fefe2), it took me a few tries:

![Ray-tracer](/images/rays7.png "Shadows First Try")
![Ray-tracer](/images/rays8.png "Shadows Second Try (ops)")
![Ray-tracer](/images/rays9.png "Shadows")

How could I make the spheres look 3D? I [followed](https://github.com/adusca/ray-tracer/commit/3da6d8185c4621aa059453823605f07b4c15e620) the part about diffuse lighting in [these slides](http://fileadmin.cs.lth.se/cs/Education/EDAN30/lectures/S1-rt.pdf).

![Ray-tracer](/images/rays10.png "Diffuse light")

Swapping a 2.0 with a 2 in a division in render.py resulted in:

![Ray-tracer](/images/rays11.png "Ops!")

Next step was adding reflections, it was easier then shadows:

![Ray-tracer](/images/rays12.png "Reflection First Try")
![Ray-tracer](/images/rays13.png "Reflection")

And [finally](https://github.com/adusca/ray-tracer):

![Ray-tracer](/images/rays14.png "Final Result")
