Secure GitHub Access
####################

:Reference: https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process

.. include::   /header.inc

In today's world, evil folks are always trying to steal your secret passwords,
so they can hack your bank account, credit card, IRS tax return, or even your
homework! Personally, I want to collect all of those folks and plant them on a
remote island somewhere, and not send any supplies until the noise stops.

..  note::

    I have been hacked three times in the last five years, even by someone who
    got hold of my Social Security number and tried to file a tax refund, after
    I had already filed. The IRS tracked that idiot down!

The bottom line is simple. Use appropriate security measures any time you
engage in work that causes sensitive information to move over the wires (or
airways) of the Internet!

Secure Shell
************

Normally, when you work with Github_ over the web, your data (web pages you
view) is kept private by using a secure web interface. You know you are using
this interface when you see the ``https`` at the front of the URL you are
accessing (``https://github.com```) The "s" stands for secure, right!

All traffic between your web browser and GitHub_ is encrypted making it very
hard for bad guys to watch it and get anything useful from you. That protects
you when all you are doing is looking at your work after you get things up on
GitHub_. However, we need to move our development work back and forth between
GitHub_ and our local development system, and a web browser does not help much
with that.

We need to secure the data we want to move in both directions. That means
encrypting any data to be moved, moving it over the Internet, then decrypting it when
it gets to the final destination. Git_ and GitHub_ are all set to do this, but
there is one annoying problem.

Every time you interact with GitHub_ (when you use a Git_ command that will
move data between you and  GitHub_, you need to log in and provide your
password. Since we are professional developers, here, we hate to type, and that
gets old very fast! Fortunately, there is a way to fix this. 

On your Linux system, we can use the ``secure shell`` tool to manage this
authentication process. The tool is provided by the OpenSSH_ project.

Checking SSH
============

First, make sure ``ssh`` is installed:

.. code-block:: bash

   $ which ssh
   /usr/bin/ssh


If this does not work, run this command:

.. code-block:: bash

   $ sudo apt-get install openssh

How SSH Authenticates
=====================

``SSH`` uses something called ``public/private -Key Encryption`` to do the hard
work.  Basically this means that data will be encrypted using a pair of
security "keys" that we need to generate on our system. These keys are
important, and come in matched pairs. One of the keys is kept private. You need
to manage this ``private key``, and never let is escape from your control. The
second key is a ``public key`` that you can freely pass around. The ``public
key`` can only be used to encrypt data to be sent to you. Anyone intercepting
this key cannot use it to figure out what you are sending. The ``private key``
can decrypt messages encrypted using your ``public key``. 

We will generate these keys on our system, then copy the ``public key`` up to
the GitHub_ server. Any time you need to communicate with GitHub_, you will
start the session by sending a request to GitHub_ from your system. That
request will include the URL of your repository, so GitHub_ knows it is
sensitive. GitHub_ will use the registered ``public key`` to send an encrypted
message back to your workstation. Git_ will use your local ``private key`` to
unpack this message and then generate a reply that goes back to GitHUb_. If this
reply is what GitHub_ expects, you are who you claim to be, and you are
authenticated. No username or password is required! 

Great, less typing!

Generating the Keys
===================

Run this command on your Linux system:

.. code-block:: bash

   $ ssh-keygen
   Generating public/private rsa key pair.
   Enter file in which to save the key (/home/rblack/.ssh/id_rsa): 
   Enter passphrase (empty for no passphrase): 
   Enter same passphrase again: 
   Your identification has been saved in /home/rblack/.ssh/id_rsa.
   Your public key has been saved in /home/rblack/.ssh/id_rsa.pub.
   The key fingerprint is:
   SHA256:KfjvzhrhyX1/6msrJQS5+31GXHZtefAAMELaJwecPmY rblack@cosc2325vm
   The key's randomart image is:
   +---[RSA 2048]----+
   |       o+oo...   |
   |       o=o .  o  |
   |      ..ooo    +o|
   |     .  E=.    .O|
   |    . ooS+   . +o|
   |     + =. . . o  |
   |      * ...+ .   |
   |       + .o.o +  |
   |      .+=  +*B   |
   +----[SHA256]-----+

You will need to respond to two lines here. The first is when the tool asks
where to put the keys. The default location is ~/.ssh``, which is a hidden
directory in your home directory.

The second response is asking for a "passphrase" for the private key. This
protects the ``private key`` in case someone else uses your system. I use
passphrase on my keys, but that means I need to enter that passphrase when my
``private key`` needs to be accessed. 

Great, we get rid of one password, only to need another one. Never fear, there
is a solution.

Once this command completes, you will have your security keys.

.. code-block:: bash

   $ ls -al !/.ssh
   total 20
   drwx------  2 rblack rblack 4096 Jan 28 08:06 .
   drwxr-xr-x 18 rblack rblack 4096 Jan 28 06:36 ..
   -rw-------  1 rblack rblack 1766 Jan 28 08:06 id_rsa
   -rw-r--r--  1 rblack rblack  399 Jan 28 08:06 id_rsa.pub
   -rw-r--r--  1 rblack rblack  444 Jan 25 15:24 known_hosts
   
The ``private key`` is ``id_rsa``, the public key is ``id_rsa.pub``.

These files are just text files, but you must not ever modify them in any way.
"Look, but do not touch", my mother used to say!

Copy the Public Key to GitHub
=============================

..  code-block:: bash

    $ vim ~/.ssh/id_rsa.pub

Be careful here, you need to copy the entire contents to your clipboard. 

.. note::

   To get copy and paste to work from mu VM on my Mac, I needed to enable it in
   VirtualBox_. Click on ``Devices -> Shared Clipboard -> Enable``.

Once you have the contents copied, open up your web browser and navigate to
your GitHub_ account. Click on the icon at the top right, and in the drop-down
menu, select ``settings``. When that opens look for ``SSH and GPG Keys`` and
open up that screen.

There will be a button that says ``New SSH Key``. Click on that and paste your
key into the text box. Give this a name (I used my machine name) and then click
on ``Add SSH key``. 

That is all you need to do on the GitHub_ side.

Set up ssh-agent
================

We added a passphrase to the ``private-key`` meaning that when we try to access
that key, we need to enter that passphrase. The ``ssh-agen`` tool will manage
your keys for you, if we set it up.

Do this:

.. code-block:: bash

ssh-add ~/.ssh/id_rsa
Agent pid 23573

That starts up the ``ssh-agent`` program, which will run in the background.
Now, we need to add the private key:

.. code-block:: bash

   $ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/rblack/.ssh/id_rsa: 
Identity added: /home/rblack/.ssh/id_rsa (/home/rblack/.ssh/id_rsa)

Now, try to accesses the remote GitHub_ server:

..  code-block:: bash

    $ ssh -T git@github.com
    The authenticity of host 'github.com (192.30.253.113)' can't be established.
    RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'github.com,192.30.253.113' (RSA) to the list of known hosts.
    X11 forwarding request failed on channel 0
    PTY allocation request failed on channel 0
    Hi rblack42! You've successfully authenticated, but GitHub does not provide shell access.

You will only see that "authenticity" message once, as long as you answer "yes"
to the question. This will happen the first time you access any remote server
for the first time with SSH. The program caches this server key in your
``~/.ssh/known-hosts`` file and it will make sure you are talking to the right
sef=rver from then on. Boy, the Internet is full of strange schemes to hack
you!

Let's try a git command now:

.. code-block:: bash

   $ git pull

This time, you should not see a request for your password!



ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPFqOZ9HVe9KDZCwhVeYO2TFxkaFfgkgqxiUPoG7EruQyMol7OPUvHf/QCXYZgG0pUMQx3oCKSLoo4BzgAn9dj0cBkESW+A2cUUUOImzXRiHfMl1C6SveGlrLXPYMIQTyLXlh0rvcguEfWjxE+q2pvHKWhEUCtrY7Kz2J55tVhSRsau0p7Xwk31mDOlDbPiRsDDy11HLD1IRFo+zu9Py6xkyFSR/3i8kHdXxbWDeJcgycB9mHLktw9aNN/fBIo2SFAj44eDfCvz1dfombK6+z50B0fstLL35tGuNqhSILHn0BDhv+xvAL4l8eCx0SusiJL4Rf+SjiLw3uDf7O3OlGz rblack@cosc2325vm

    * Lab1: https://classroom.github.com/a/_-kmlQxQ
