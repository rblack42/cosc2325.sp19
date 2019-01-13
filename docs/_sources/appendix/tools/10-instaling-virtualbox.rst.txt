..  _installing-virtualbox:

Installing VirtualBox
#####################

..  include::   /references.inc

We will set up a Linux machine on your development system. To do this, we need
a ``virtual machine engine``, which is a program designed to act like a real
computer. There are several possible such engines available:

    * VMware_ - used in our labs (a commercial product available on all
      platforms)

	* VirtualBox_ - a free tool from Oracle (which we will use here)

	* Parallels_ - a commercial product for Mac

VMware_ seems to be the most advanced engine, but it is complex. There is a
free version of this product, which is what is installed on lab machines. I
prefer to use the VirtualBox_ engine these days. 

..  note::
    
    There is a free add-on package for VirtualBox_ that I will demonstrate in
    class. This package is called Vagrant_, a tool that lets you spin up
    ``virtual machines`` for testing with a simple text file that controls the
    whole process.  More on that later.

To install VirtualBox_ on a PC, you need to navigate to the product website and
download the correct installer. I am going to demonstrate installing this tool
on my Windows 10 system.


Here is the link I used to get the Windows installer:

    * `VirtualBox-5.2.6-120293-Win.exe
      <https://download.virtualbox.org/virtualbox/5.2.6/VirtualBox-5.2.6-120293-Win.exe>`_

Launch this program by double-clicking on the program file name in ``Windows
Explorer``:

..  image:: images/VBinstall1.png
    :align: center
    :width: 600

Click on "next" to proceed.

..  image:: images/VBinstall2.png
    :align: center
    :width: 600

You can accept the default location for this program. Click "Next" to continue

..  image:: images/VBinstall3.png
    :align: center
    :width: 600

Again, the defaults are fine. Click "Next" to continue.

..  image:: images/VBinstall4.png
    :align: center
    :width: 600

Here, the installer is warning you that you might lose access to the Internet
during the installation. No streaming video should be going on! Click "Next" to
continue.

..  image:: images/VBinstall5.png
    :align: center
    :width: 600

Now, we are ready to install the program. Click "Install" to continue.

..  image:: images/VBinstall6.png
    :align: center
    :width: 600

At this point, the installation will begin. The installer will copy files into
place. You will probably see this pop-up during the process. 

..  image:: images/VBinstall7.png
    :align: center
    :width: 600

Click on "Install" to let drivers be installed.

..  image:: images/VBinstall8.png
    :align: center
    :width: 600

The installation should complete with no problems. Click on "Finish" when this
screen appears.

Now that you have VirtualBox installed, we need to create a real ``virtual
machine`` running Linux. That is the topic of our next lecture!

..  vim:ft=rst spell:

