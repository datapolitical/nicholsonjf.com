Title: Tips-n-Tricks
Date: 2014-01-01
Tags: howto
Slug: tips-n-tricks

This is a temporary post I'm using to document short snippets of code and commands I want to remember. Eventually I'm going to build a separate page into nicholsonjf.com where I can upload and display these in a cleaner and more accessible manner. Until then, this is [good enough!][1]

###Create a local git repo and push it to Github###
Date: 2014-01-03
Tags: ubuntu, git, github
Sources: [stack overflow post][3], [github][4]

First, [create the repo on Github][4]. Make sure to initialize it with a README file.

Then, `cd` into the local directory you want to push.

`git init` to initialize the local repo.

`git add -A` to track all files.

`git commit -m "commit note"` to commit the changes.

`git add origin git remote add origin https://github.com/username/repo-name.git` to add the Github repo as a remote.

`git pull origin master` this will pull down the README file from Github and prevent a fastforward error when you push.

`git push origin master` enter your username and password to github. The github repo should now be caught up with your local repo.

[3]: http://stackoverflow.com/questions/11276364/after-creating-a-local-git-repo-how-do-i-push-it-on-github "Stack overflow question"
[4]: https://help.github.com/articles/create-a-repo "Github create repo"

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
