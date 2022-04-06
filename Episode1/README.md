
# Command line examples will be shown as such

┌──(kali㉿kali)-[~/PYTHON/Episode1]
└─$ python                                                        1 ⚙
Python 2.7.18 (default, Feb 22 2022, 11:45:08) 
[GCC 11.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> var1 = "foo"
>>> var1="too"
>>> print var1
too
>>>
------------------------------------------
this is an example of changing the value of your variable. 'var1' in this case

>>> var1 = "bar"
>>> print var1
bar
>>>

-----------------------------------------------
this is us importing a function from the standard library. This allow sus to use the methods available to us from importing the library.
>>> import os
>>> os.system("ls")		# this is an example of command substitution

NOTE: If you were to be doing some static code analysis and saw
 the 'import os' command we would know that we should be able to write
 to that file using the os.system method



------------------------------------------------------

>>> 
>>> 
>>> 
>>> passwd = open("/etc/passwd", "r")		# we are creating the variable passwd and telling it to open '/etc/passwd/'
>>> passwd.read()			#  calling the variable passwd and giving it the method read 
'root:x:0:0:root:/root:/usr/bin/zsh\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x:3:3:sys:/dev:/usr/sbin/nologin\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/usr/sbin/nologin\nman:x:6:12:man:/var/cache/man:/usr/sbin/nologin\nlp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin\nmail:x:8:8:mail:/var/mail:/usr/sbin/nologin\nnews:x:9:9:news:/var/spool/news:/usr/sbin/nologin\nuucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin\nproxy:x:13:13:proxy:/bin:/usr/sbin/nologin\nwww-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\nbackup:x:34:34:backup:/var/backups:/usr/sbin/nologin\nlist:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin\nirc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin\nnobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin\n_apt:x:100:65534::/nonexistent:/usr/sbin/nologin\nsystemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin\nsystemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin\nsystemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin\nmysql:x:104:110:MySQL Ser


# The above white text is the contents of the '/etc/passwd/'

>>> city = raw_input("What city do you live in? ")
What city do you live in? Seattle
>>> print city
Seattle
































