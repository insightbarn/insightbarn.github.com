---
title: Home
layout: default 
---

Sangman Kim's Blog
==================

This is Sangman's official blog. You may also want to take a look at [my academic page](http://cs.utexas.edu/~sangmank) or [my wife Jiwoo's page](http://www.cerc.utexas.edu/~jiwoo/). 

Writing
-------
 {% for post in site.posts %}
 * {{ post.date | date_to_string }} - [{{ post.title }}]({{ post.url }})
 {% endfor %}

Things I like
-------------
 * [github](http://www.github.com)
 * [Emacs org mode](http://orgmode.org/)

