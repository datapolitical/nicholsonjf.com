nicholsonjf.com
========

I. workflow for publishing a change to nicholsonjf.com

1. cd into ~/nicholsonjf.github.io
    a. git status to make sure there aren't any changes to commit
2. cd into ~/virtualenv/pelican2
    a. source bin/activate to enable virtualenv and pelican
3. cd into ~/virtualenv/pelican2/nicholsonjf.com
    a. make devserver
4. ssh -X ubu (on macbook, in xquartz terminal)
5. cd into ~/virtualenv/pelican2/nicholsonjf.com/content
    a. use vim [filename] and make any desired changes
6. confirm changes are okay to publish in xquartz
7. To publish:
    a. make publish
    b. cd  ~/nicholsonjf.github.io
    c. run git status to make sure files were published to directory
    d. run git branch to make sure 'ubuntu' branch is checked out
    e. run git add -A to make sure any new files/changes are staged
    f. run git commit -m "commit message"
    g. run git push origin ubuntu
8. Go to github and submit a pull request from the ubuntu branch
    a. Then, confirm the pull request
9. Changes should be live on nicholsonjf.com

II. workflow for backing up nicholsonjf.com internals

1. cd into ~/virtualenv/pelican2/nicholsonjf.com
2. make desired changes
3. git status just to see what's going on
4. git add -A to add any untracked files
5. git commit -m "[commit note]"
6. git push origin master and enter credentials
7. check github to confirm backup completed successfully 

