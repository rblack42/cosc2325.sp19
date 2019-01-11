..  _graphics-setup:

C++ Graphics Setup
####################

..  include::   /references.inc
..  vim:ft=rst spell:

To better visualize what is happening inside the machine as we build our
simulator, we will set up a simple graphics system you can use in your lab
projects.  All you will need to to is add several files to your C++
installation so you can generate graphics displays. This is not difficult, but
it will require installing a few new files, and setting up the project Makefile
so you can build a graphics application.

..  warning::

    Several of you are using Dev-C++ (or another IDE) and not the command line
    environment we setup in this class. From this point forward, your projects
    must use the command line tools, and be set up with a proper **Makefile**.
    We will be adding automated testing to your coding skill set, and that is
    not easily done using most IDE tools.

Mac Setup
*********

In order to build simple graphics applications, we need a few additional
components. For Mac users, the compiler you are using is part of the XCode
package, which you must install from the Apple App Store. Fortunately, at least
for now, Apple includes all the components we need to build our graphics
projects. All we need to do is set up a project, and create a suitable
**Makefile** as described below, and add the two graphics files I provide.
These notes will walk you through those steps.

Windows Setup
*************

Getting things running on the PC turned out to be a bit involved, but I finally
figured out how to get things working.

We will need to install a package called ``freeglut``. The file you need is
provided here:

    * :download:`freeglut-MinGW-3.0.0-1.mp.zip`

Once this file is on your system, use the ``File Explorer`` program to
"Extract" the files in this ``.zip`` file. This file is a compressed file with
several folders in it.

You will find one major folder named ``freeglut`` inside this package, and
three other folders under that. 

Use the ``Windows Explorer`` program to move the entire ``freeglut`` folder and
its contents into a folder named ``tools`` at the top of your ``C`` drive. You
will end up with a folder named ``C:\tools\freeglut\`` on your system. If you
followed my advice on installing tools on your system, this ``tools`` folder
should already exist. If not, just create it using ``Windows Explorer``.

..  note::

    You may be asked to the "Administrator" password to do this. Just use your
    normal logon password. (If this is not your machine, you may need to find
    the owner.

We need to copy one file from inside of the ``freeglut`` folder to another
place on your system.

32-bit Users
============

If your system is a 32-bit one (or you installed the 32-bit compiler) Your
compiler may live in the ``C:\Program Files (x86)\mingw-w64`` folder. Locate the
following file:

    * ``C:\tools\freeglut\bin\freeglut.dll`` 

Copy that file into this folder:

        * ``C:\Windows\SysWOW64``

64-bit Users
============

If you have a 64-bit system, and you installed the 64-bit compiler, your
compiler may be located in the ``C:\Program Files\mingw-w64`` folder. Locate this
file:

    * ``C:\tools\freeglut\bin\x64\freeglut.dll``

Copy that file into this folder:


    * ``C:\Windows\System32``

..  note::

    Windows has really strange naming conventions. We are placing a 64-bit
    library in a folder with a name that says 32 in it. If we are using 32-bit
    code we place the library file in a folder with 64 in it. That makes no
    sense, Microsoft!

Graphics Project Files
**********************

For all graphics projects we will need a few extra files.

Next, download these files and save them somewhere on your system, where you
can find them later. (Not in a project folder). You will need them for lab
projects.

    * :download:`Graphics.cpp`

    * :download:`Graphics.h`
    
    * :download:`main.cpp`

    * :download:`Makefile`

Testing The Graphics Setup
**************************

..  note::

    I am crossing my fingers that I got all of this working right! I tested
    this on both a Windows 10 Home edition PC< and on my MacBook Pro laptop.


Step 1: Create Your Project
===========================

We will test things using a simple demo project.

Start off by building a project folder. Put this outside of any class repositories (perhaps inside your ``cosc1337`` folder):

..  code-block:: bash

    $ mkdir GraphicsDemo
    $ cd GraphicsDemo
    $ mkdir src
    $ mkdir lib
    $ mkdir include

..  note::

    That sequence will work on Windows systems.

Place the ``Graphics.cpp`` file in the ``lib`` folder, and the Graphics.h``
file in the ``include`` folder. Place the ``main.cpp`` file in the ``src``
folder and place the ``Makefile`` at the top of the project folder.

Step3: Test your Demo
*********************

With everything installed properly, you should be able to run your project as
follows:

..  code-block:: bash

    $ make
    $ make run
    
With any luck, you should see graphics.


Did you see a red ball slide up the screen? If so, you are good to go, if not, see me for help!

..  vim:ft=rst spell:
