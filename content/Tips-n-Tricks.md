Title: Tips-n-Tricks
Date: 2014-01-01
Tags: howto
Slug: tips-n-tricks

This is a temporary post I'm using to document short snippets of code and commands I want to remember. Eventually I'm going to build a separate page into nicholsonjf.com where I can upload and display these in a cleaner and more accessible manner. Until then, this is [good enough!][1]

###Check if package is installed###
Date: 2014-01-01
Tags: ubuntu, bash
Sources: [ask ubuntu post][2] 

Bash command:
```bash
dpkg-query -l [package-name]
```

Example:
```bash
nicholsonjf@1z4u:~$ dpkg-query -l curl
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                         Version                      Description
+++-============================-============================-========================================================================
ii  curl                         7.22.0-3ubuntu4.6            Get a file from an HTTP, HTTPS or FTP server
```
[1]: http://nicholsonjf.com/blog/good-enough "Good-Enough blog post"
[2]: http://askubuntu.com/questions/140569/how-to-test-if-package-is-installed "Ask ubuntu post"
