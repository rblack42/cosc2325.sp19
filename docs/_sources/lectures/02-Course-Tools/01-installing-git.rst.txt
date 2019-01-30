..  _installing-git:

Installing Git on your PC
#########################

..  include::   /references.inc

If you want to install Git_ on your laptop, there are installers available for
that. I have Git_ installed on every machine I run, both physical and virtual.
You do not need to do this for my class, but it is very handy for
other projects.

Windows PC
***********

The installer for Windows can be found at this link:

    * `Git-2.18.0-64-bit.exe
      <https://github.com/git-for-windows/git/releases/download/v2.18.0.windows.1/Git-2.18.0-64-bit.exe>`_

Just run the installer and Git_ should be available on your command line.

..  note::

    There is a portable version of this version that you can load on a flash
    drive if you like.

Installing Git on your Mac
**************************

If you use a Mac, there is an installer available for that as well. 

    *   `Git installer for Mac <https://git-scm.com/download/mac>`_
      
However, I recommend that you install Homebrew_ and use that tool to install
it. Homebrew_ is a nice package loading system many Mac developers use to
install commonly needed tools.

Assuming Homebrew is installed, here is all it takes to install git:

..  code-block:: bash

    $ brew install git

That is it, Git_ should now be ready to go!

Installing Git_ in Linux
************************

This is also easy.

Open up a terminal program, and type this:

..  code-block:: bash

    $ sudo apt-get install -y git-core

The ``sudo`` part of that command will require that you provide your password.
The ``-y`` part just answers yes for a silly pause that asks if you really want
to do this. (Of course I do, you silly computer. Why else would I have typed
that command?)

Git References
**************

Once you have Git_ installed, you need to elarn how to use it. Here are a
couple of good references that will help. (I keep both of these in my DropBox
account:

    * :download:`/files/ProGit.pdf`

    * :download:`/files/GITbook.pdf`


