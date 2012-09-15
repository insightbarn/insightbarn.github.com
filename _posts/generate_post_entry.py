#!/usr/bin/python
# -*- coding: utf-8 -*-

use_krt = True
import sys, os, re
import datetime 
try:
        import krt
except:
        use_krt = False
        print "Korean romanization is disabled"

import getopt

def usage():
        print """usage:
      ./generate_post_entry.py [-t title] [-m markup-language]

          markup-language: textile, markdown(md)
"""

def main():
        global use_krt

        try:
                opts, args = getopt.getopt(sys.argv[1:], "ht:m:",
                                           ["help", "title=", "markup="])
        except getopt.GetoptError, err:
                print str(err)
                usage()
                sys.exit(1)
        
        orig_title = None
        markup = "markdown"
        
        for o, a in opts:
                if o in ("-h", "--help"):
                        usage()
                        sys.exit()
                elif o in ("-t", "--title"):
                        orig_title = a
                elif o in ("-m", "--markup"):
                        markup = a
        
        if markup not in ("md", "markdown", "textile"):
                print "Error: markup should be either textile or markdown(md)"
                sys.exit(1)

        exts = {"textile": "textile", "md": "md", "markdown":"md"}

        if not orig_title:
                orig_title = raw_input("Enter title (alphabet/hangul, numbers or spaces): ")
        
        title = orig_title.replace(" ", "-")
        if use_krt:
                title = krt.romanize(title).lower()
                title = re.sub("[^a-zA-Z0-9 -]", "-", title)

        today = datetime.date.today()

        assert markup in exts, "markup %s not in exts %s" % ( markup, exts )

        filename = "%s-%s.%s"%(today.strftime("%Y-%m-%d"), title, exts[markup])

        if filename in os.listdir("."):
                print "file %s already exists"%filename
                sys.exit(1)
        
        entryf = open(filename, "w")

        if markup == "textile":
                entryf.write("""---
layout: post
title: %s
comments: no
published: false
---

h1. {{ page.title }}"""%orig_title)
        elif markup in ("md", "markdown"):
                entryf.write("""---
layout: post
title: %s
comments: no
published: false
---

{{ page.title }}
%s"""%(orig_title, "="*len(orig_title)))
        else:
                print "ERROR: this is not happenning.... markup: %s" % markup
                sys.exit(1)
        
        entryf.close()

        print "file %s has been created" % filename

if __name__ == "__main__":
        main()
