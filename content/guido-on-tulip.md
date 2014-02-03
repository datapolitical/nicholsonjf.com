Title: Guido van Rossum on Tulip (asynchronous I/O for Python 3)
Date: 2014-01-22
Tags: Python, BayPiggies, Guido, Tulip
Slug: guido-on-tulip
Summary: On Thursday, January 23rd at 7:30pm PST the creator of Python Guido van Rossum gave a talk at LinkedIn, Mountain View about Tulip (asynchronous I/O for Python 3).

<iframe width="560" height="315" src="//www.youtube.com/embed/aurOB4qYuFM" frameborder="0" allowfullscreen></iframe>  
<br>
####Abstract (written by Guido van Rossum):
In October 2012 I decided that it was time to add modern asynchronous I/O to the Python standard library, to replace the ancient and ever-problematic asyncore module. A year later this project is my main focus within the Python world. There is PEP 3156, which specifies an interface that I am hoping to add to the standard library (probably with provisional status), and Tulip, which is an implementation of the PEP and also contains a bunch of client libraries that use it (not all of this will make it into the standard library). Tulip requires Python 3.3 or later, and the code makes extensive use of coroutines, which are specially-marked generators that must be waited for using the new "yield from" syntax introduced by PEP 380. There is a lower-level API based on callbacks, and Future and Task classes that bridge the impedance mismatch between coroutines and callbacks. The PEP 3156 interface has also been heavily influenced by existing third party libraries for asynchronous I/O, in particular Twisted and Tornado, and interoperability with those systems (as well as others, like gevent and Microsoft's Windows 8 API formerly known as Metro) is an explicit goal, to be accomplished through adapters.  
<br>
####Speaker:
Guido van Rossum is Python's creator, and still active as its BDFL. After years at Google he now works at Dropbox. For more information see his personal website at [http://python.org/~guido/][2].<br><br>Also, here's a link to the Google Hangout On Air that was originally hosted here: [http://youtu.be/uDWjtYLmW90][3]  
 

[2]: http://python.org/~guido/ "Guido's personal site"
[3]: http://youtu.be/uDWjtYLmW90 "Video of the Hangout on Air originally hosted here"
