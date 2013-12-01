Title: Install Python 3.3.2 locally from Source (Ubuntu 12.04.3 LTS)
Date: 2013-11-11
Tags: Python, Ubuntu
Slug: install-python3-locally-from-source
Summary: I rely heavily on the vast amount of how-to guides on the internet. With enough time, curiousity and determination, you can pretty much learn anything you want right from your computer. So, I feel it's my duty as a citizen of the internet to contribute to that body of resources. Also, documenting the way I setup or created something helps me remember it better in the future. 


###Background###
I rely heavily on the vast amount of how-to guides on the internet. With enough time, curiousity and determination, you can pretty much learn anything you want right from your computer. So, I feel it's my duty as a citizen of the internet to contribute to that body of resources. Also, documenting the way I setup or created something helps me remember it better in the future. 

###Props###
Most of what I use below I learned from reading the answer frm [@sergey][6] on [this askubuntu post][4]. Like I said earlier, I make good use of resources around the internet :)

###**\*Disclaimer\***###
I am not a veteran linux sys-admin and have only tested this on my personal server at home. Make sure to test this on a dev machine before trying on any machine of importance.

###The Problem###
For the past six months or so, I've been immersing myself in Python, and have happily used [2.7][1], the version that comes along with OS X 10.8.5 and Ubuntu 12.04. Recently though, I got a hankering for trying out the latest 3-series version which is [3.3][2]. I'm particulary finicky about setting up projects on my home server and use [virtualenv][3] as much as possible. So I decided, if I wanted to install a different version than the system uses, I wasn't going to do it globally. Also, since Python 3.3.2 was only released in May 2013, there isn't a pre-packaged binary available from Ubuntu/Canonical yet. Thus, I was left to compiling and installing it manually.    

###Dependencies###
Before compiling from source, we'll need to download the C compiler. Also, SQLite (if you want your Python install to have it) and the bzip2 data compressor. I chose to install these globally.

```
sudo apt-get install build-essential
sudo apt-get install libsqlite3-dev
sudo apt-get install sqlite3 
sudo apt-get install bzip2 libbz2-dev
```

###Downloading the Source Tarball###
Before doing anything, we need to download the file. To do so, we can use `wget` and point it to [Python's FTP server][5]. As I mentioned earlier, my aim was to install it in a local user directory, not globally, so I first created the folder where I wanted it to live. Replace `nicholsonjf` with the name of your ubuntu user account.

```
mkdir /home/nicholsonjf/opt
```

Using `wget -4` will force the use of IPV4 (initially it tried using IPV6 and was timing out).

```
cd /home/nicholsonjf/opt
wget -4 http://python.org/ftp/python/3.3.2/Python-3.3.2.tar.bz2
``` 

Next, run the below command to extract the .bz2 file that we downloaded above.

```
tar jxf ./Python-3.3.2.tar.bz2
```

Once that's finished, `cd` into the directory that was created from unpacking the tarball.

```
cd ./Python-3.3.2
```

This next step is important. Since we want to install Python3 into a user directory, we run the configure script with the `--prefix` switch, and specify where we want the software to be installed. Again, remember to replace `nicholsonjf` with your username. You can run `./configure --help` if you want to see the other options that are available.

```
./configure --prefix=/home/nicholsonjf/opt/python3.3
```

You should see a ton of output to the terminal saying "checking this" and "checking that". Once that is done, it's compile time. Run the below command and let it do it's thing.

```
make && sudo make install
```

Finally, a finishing touch from our good friend [@sergey][6] that uses a symbolic link to the Python 3.3 executable, allowing one simply type `python3` into the terminal and the Python 3.3.2 interperter will launch. Remember to replace `nicholsonjf` with your username.

```
mkdir ~/bin
ln -s /home/nicholsonjf/opt/python3.3/bin/python3.3 ~/bin/py
```

Now, you should be able to enter `python3` into the terminal and see the below prompt show up.

```
Python 3.3.2 (default, Nov 10 2013, 02:21:02) 
[GCC 4.6.3] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Thanks for reading! If you have any questions, don't hesitate to leave a comment!


[1]: http://docs.python.org/2/ 
[2]: http://docs.python.org/3.3/ 
[3]: http://www.virtualenv.org/en/latest/
[4]: http://askubuntu.com/questions/244544/how-to-install-python-3-3
[5]: http://www.python.org/ftp/python/
[6]: http://askubuntu.com/users/14564/sergey 
