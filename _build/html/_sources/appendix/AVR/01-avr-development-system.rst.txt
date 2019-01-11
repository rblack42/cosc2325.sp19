Building an AVR Development System
###################################

..  include::   /references.inc
..  wordcount::    
..  vim:ft=rst spell:

In this note, we will construct a simple build environment for AVR projects.
This setup will not use the Arduino_ IDE, which many folks use. Instead, we
will install build tools for the AVR chips, and use Make_ as our build
management tool.

In this project, we will use Linux. If you are using a PC or Mac, you need a
way to run Linux programs. Rather than rush out and buy a new computer, we will
install a ``Virtual Machine`` on your system. 

..  note::
    
    If you are using a Linux system, you do not need to do this step!

Setting Up a Virtual Machine
****************************

A ``Virtual Machine`` is just a program. However, this program pretends to be a
real computer, and does so well enough that you can install an operating
system, and applications, just like on a real machine. Obviously, this setup
will be slower than a real computer, but not significantly slower, so it is
quite usable for most work.

Installing VirtualBox
=====================

This process is pretty easy. Navigate to the VirtualBox_ website and download
the program needed for your system. VirtualBox_ is available for both PC and
Mac.

This install should be done using an account that has permission to access
protected areas of a Windows PC. That means you need to have "Administrator"
privileges. Assuming that is true, simply run the installation program.

Once VirtualBox_ is installed, download the ``VirtualBox Extension Pack`` and
install that as well. This component is needed so you can access folders on
your host machine from inside the virtual machines you will create.

Installing Vagrant
==================

While it is common to just download an ``iso`` file, which could be used to
burn a DVD, and use that to install the operating system, that process is
pretty tedious. A better approach will use another tool that manages the
installatiom of an operating system for you. That tool is called Vagrant_.

Vagrant_ can be used to quickly spin up a test machine for whatever development
work you need to do. The machine can be destroyed and rebuilt as needed, with a
fairly simple setup. 

..  note::

    Vagrant_ needs VirtualBox_ on the host machine. It is possible to use
    VMware, but that setup requires a commercial add-on, which I am not using
    here.  

Again, installation is simple. Just download the installer you need for your
system, nd run it. You need administrator privileges for this tool as well.

Installing Linux
================

Assuming Vagrant_ is installed, we need to get Linux installed in a virtual
machine. Vagrant_ will do that job, and the installed system will be run by
VirtualBox.

You begin this setup by creating a single text file, called ``Vagrantfile`` in
a folder where you will do your development. 

..  note::

    You can build a skeleton of this file by running ``vagrant init`` in the
    project folder. You will need to modify this file a bit for this project.

Here is the ``Vagrantfile`` I am using for this project:

..  literalinclude::    code/Vagrantfile
    :linenos:
    :caption: Vagrantfile

Look at the last part of this file. I could add lines there to have Vagrant_
set up my machine, but I am going to use a cooler tool to do that.

Start Your VM
=============

This is actually fun, especially if you have set up a VM the "hard" way!

With this file in your development directory, do this:

..  code-block:: bash

    $ vagrant up

The first time you run this command, Vagrant_ will download a preconfigured VM image
containing the OS you chose. In this case, it is a server version of Ubuntu
16.04. We will not have a GUI interface to this system. Instead we will do all
of our work on the command line. (Hey, that is why I am teaching you how to
operate in this environment!)

It will take a few minutes to get the VM running. Once the machine is running, do this:

..  code-block:: bash

    $ vagrant ssh
    Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-142-generic x86_64)
    
     * Documentation:  https://help.ubuntu.com/

     System information disabled due to load higher than 1.0

      Get cloud support with Ubuntu Advantage Cloud Guest:
        http://www.ubuntu.com/business/services/cloud

    0 packages can be updated.
    0 updates are security updates.

    New release '16.04.4 LTS' available.
    Run 'do-release-upgrade' to upgrade to it.


    vagrant@vagrant-ubuntu-trusty-64:~$ whoami
    vagrant
    vagrant@vagrant-ubuntu-trusty-64:~$ pwd
    /home/vagrant
    vagrant@vagrant-ubuntu-trusty-64:~$ ls /vagrant
    blink.S  config.inc  delay1.S  delay.S  main.S  Vagrantfile
    vagrant@vagrant-ubuntu-trusty-64:~$ 
    
If you look at tis output closely, you see that you are logged in as a user
named ``vagrant``. THat user has ``sudo`` privileges in this system. The
password for this account is super-secret: ``vagrant``. (Remember, this is a
test setup, not something you would make public!) You do not need to use the
password to run ``sudo`` commands in this setup.

Even better the VM has mounted your project directory into the VM file system
at ``/vagrant``. Any work you do in that directory will really live on your host
machine in your project folder. This is very handy!

Exiting the VM
==============

When you are done working on the project, you exit the VM by doing this:

..  code-block:: bash

    vagrant@vagrant-ubuntu-trusty-64:~$ exit

YOu will be back on your host machine after this.

..  warning::

    Your VM is still running, and you can log back in by running ``vagrant
    ssh`` again. Leaving it running can drain your battery! YMMV.
    
To stop the machine, do this:

..  code-block:: bash

    $ vagrant stop

If, for some reason, you want to remove this VM from your system, do this:

..  code-block:: bash
    
    $ vagrant dstroy

What this does is remove the running version of the VM you created when you ran
``vagrant up``. The image used to build this VM is still on your system,
meaning that if you want to start it again, you will not need to wait for
the image to download. This means you can get a VM up and running in seconds
whenever you need one. I keep the base image on my system, and create
customized VM machines for different projects, A project-tuned ``Vagrantfile``
is all I need to set a new system up!

..  note::

    This is how I did development for many years on my Mac laptop. Then came
    Docker, and my entire development setup changed. We will look at that in
    another note.

Provisioning the VM for AVR 
***************************

We can run normal install commands in this VM to configure it as we like. That
means "manual labor", and I hate running a bunch of commands manually. I could
set up a simple ``Makefile`` to get things set up, but in this note I am going
to demonstrate another cool tool: Ansible_. This tool is Python program folks
are using to configure thousands of machines. I have been using this tool to
set up all my Mac and Linux systems for several years now. Sadly, work on
getting Windows to behave in this way is way behind, but some developers are
working on that.

The commands that follow are run inside of the VM.

Installing Ansible
==================

We start off by getting Ansible_ installed.

..  code-block:: bash

    $ sudo apt-add-repository ppa:ansible/ansible
    $ sudo apt-get update
    $ sudo apt-get install ansible

That first line adds data needed for the apt tool to find the Ansible_ software.

I actually do not do that manually. (Remember, I am lazy, and proud of it!).

Instead, I have this script in my project folder:

..  literalinclude::    code/bootstrap.sh
    :linenos:
    :caption: bootstrap.sh

With this file in my project folder, I start up the new VM and run this command:

..  code-block:: bash

    $ /vagrant/bootstrap.sh

And the software installs as before. This script can be run multiple times. It
checks if ``ansible`` is installed, and does nothing if so. This is a ``bash``
script, common in Linux/Mac world.

..  warning::

    You might need to mark that file as "executable" by doing this before you
    run it:

    ..  code-block:: bash

        $ chmod +x /vagrant/bootstrap.sh

Now we have Ansible_ installed. It is time to tell it how we want this machine
to be set up.

Configuring for Your Project
============================

Ansible _ is an interesting tool. You do not tell it what to do. Instead, you
tell it how you want your machine to look, and it makes that happen. It already
knows how to load software on many servers, so telling it how to do that is not
needed.

The setup is simple, but it involves a bunch of files in a particular directory
structure. Here is my setup for this VM:

..  code-block:: bash

    $ tree ansible
    ansible
    ├── inventory
    ├── Makefile
    ├── roles
    │   ├── apt
    │   │   └── tasks
    │   │       └── main.yml
    │   └── avr
    │       └── tasks
    │           └── main.yml
    └── site.yml
  
..  note::

    All of this is set up in my project folder on my MacBook. That way, I can
    copy this setup to another project, and spin up a VM for that using Vagrant
    as well!

The files needed in this setup are shown below. To learn how to setup such a
system on your own, look at the documentation online. There are many tutorials
to get you going.

..  literalinclude::    code/ansible/inventory
    :linenos:
    :caption: ansible/inventory

..  literalinclude::    code/ansible/Makefile
    :linenos:
    :caption: ansible/Makefile

..  literalinclude::    code/ansible/site.yml
    :linenos:
    :caption: ansible/site.yml

..  literalinclude::    code/ansible/roles/apt/tasks/main.yml
    :linenos:
    :caption: ansible/roles/apt/tasks/main.yml

..  literalinclude::    code/ansible/roles/avr/tasks/main.yml
    :linenos:
    :caption: ansible/roles/avr/tasks/main.yml

..  literalinclude::    code/ansible/roles/avr/tasks/main.yml
    :linenos:
    :caption: ansible/roles/avr/tasks/main.yml


With this admittedly strange directory setup in place, all we need to do is run
one command and our machine will have all the software we need installed.

..  warning::

    The ``Makefile`` you use is in your project directory, which is mapped into
    the VM under ``/vagrant``. When you start the VM using "vagrant ssh", you
    run the make command inside the VM. Ansibke is installed in Linux, and thie
    command will not work from your host machine.

This is what I saw when building my machine:

..  code-block:: bash

    $ make provision
    ansible-playbook -i inventory site.yml

    PLAY [update vm] ***************************************************************

    TASK [Gathering Facts] *********************************************************
    ok: [localhost]

    TASK [apt : update apt] ********************************************************
    changed: [localhost]

    TASK [avr : Install AVR build tools] *******************************************
    changed: [localhost] => (item=[u'binutils-avr', u'gcc-avr', u'avr-libc', u'avrdude'])

    PLAY RECAP *********************************************************************
    localhost                  : ok=3    changed=2    unreachable=0    failed=0 
    
That last line is important. If anything failed to work, we will see error
messages. In this case, everything ran fine, and "failed=0" is seen, indicating
that Ansible_ finished its work with no problems!

You can run the command again, and Ansible_ will install nothing, but it will
check that everything it was told to install is in place. This is much like how
Make_ operates, but on a different scale!

Checking the AVR Tools
======================

Let's verify that we have all the tools we will need:

..  code-block:: bash

    $ which avr-gcc
    /usr/bin/avr-gcc
    $ which avrdude
    /usr/bin/avrdude
    $ which avr-objcopy
    /usr/bin/avr-objcopy
    $ which avr-objdump
    /usr/bin/avr-objdump

That is all we need to build AVR programs in the VM.

Wrapping up
***********
    
We set up Ansible_ to run on one machine. In fact, it will run on whole fleets
of servers. I have a single directory on my laptop set up with "roles" to
install everything I want on seven different machines at present. All I do to
check them all is run one simple ``make`` command on my laptop, and Ansible_
runs on my MacBook, directing installs on remote servers using the ``ssh``
protocol. It sends commands to each server. That is how Ansible_ is used to
manage thousands of machines all at once. This is one powerful tool for
managing servers, or just simple virtual machines. In fact, I manage all
software installed on my personal Mac/Linus systems using this tool as well!

If it worked better on Windows, I would have that working as well. 





