Getting Started
###############

..  include::   /header.inc

Are you ready to code? We will be building a fair amount of code in this class,
and of course, I want you to write good code. That does not just mean that your
code works! It it also means that your code is "clean", meaning it follows
common style conventions, is well written and documented.

..  note::

    The code you write reflects how much you care about the craft of
    programming.  Every student in this class is on a path to become a
    professional who can craft solutions to complex problems, then get the
    computer to do the messy work for you.

We will be using C++ in this course. Some of you may have already studied C++,
but others have never seen this language. No matter! We will start off with a
simple problem, designed to show you how to do your work.

I can hear some of you muttering that you know how to write code, you just fire
up some :term:`IDE` and type away. 

Wrong!

We will be creating code using an "old-school" approach that does not rely on
fancy development systems. We will pay a lot of attention to how you set up a
project, create the code and documentation, process and test your code, and
publish your code on a public server for others to see.

Why Not use an IDE?
*******************

:term:`IDE` (:term:`Integrated Development Environment`) systems are certainly
productivity boosters. Using one can speed up your coding, and help you manage
your code.  The real problem with using an :term:`IDE` in school is simple to
explain.  When you finally join a development team and start working on a "real
(big) project, that team will tell you what development tools you need to use.
Your current favorite tools will not be usable now. Some companies invest a lot
of money for tools that seriously help manage a big project. Some of those
tools are amazing, and take a long time to master. You do need to be familiar
with an IDE, and we will look at a popular one later in the course. For now, no
:term:`IDE` is allowed!

There is another problem with living in an :term:`IDE` while learning. The
:term:`IDE` hides a lot of details about building your project from you. I once
attended a school that almost lost its accreditation because no student
interviewed (and several faculty members as well) could explain how a program
is actually processed into something that can run on a real computer!

We will make sure you understand what is going on by making sure you can
function as a developer with only the real development tools available. It may
surprise you to learn that most :term:`IDE` systems are just fancy wrappers around
standard tools. The wrapper gives you a point-and-clink development world to
live in. Behind the scenes, those standard development tools are running under
control of the :term:`IDE`.

Working on the "Command Line"
*****************************

..  objective::
    1. Use the command line to build a C++ program.

..  objective::
    1.1 Explain the parts of a system command.

All operating systems support a user interface where the mouse is not to be
used. There is no :term:`Graphical User Interface` (:term:`GUI`) here. Instead,
you tell the OS what to do by typing in commands using your keyboard only. This
kind of interface has been around almost as long as computers themselves, but
is largely ignored by most computer users today. Still, as a developer, it is an
important part of the programming landscape, especially when you start
interacting with computers in that "cloud" thing we all hear about today.

Servers that you might need to control somewhere on the Internet rarely have a
:term:`GUI` interface. That kind of thing is way too expensive to support over a long
network connection. Instead, we transmit short strings of characters to the
remote machine, and it replies with another short set of characters. Hey! That
is exactly how the Web works! Only here, we are telling an operating system
what to do.

The interface we will use is called different things on different machines. On
a PC, it goes by the name "Command Prompt". On a Mac/Linux machine it is called
a "Shell". In either case, there will be a line on your screen with some kind
of 'prompt', and that prompt it telling you to type in a command of some sort. 

Commands are a series of space-separated chunks of text beginning with the name
of a program you want the operating system to run. All the chunks after that
program name are considered "options" that will be interpreted by the named
program. Those options control exactly what the named program does when it
runs. 

When you press the "Enter" key at the end of the line, the operating system
searches for the named program in a set of directories (folders for you PC
folks). If it finds the program, it launches it and hands it those options on
the command line. If the OS cannot find the program (because you mistyped its
name, or that program is not installed so it can be found) you get an error
message, and another prompt.

If the program is found and launched, what you see on the screen will be output
from that program, possibly with error messages from the OS. When the program
finishes running, you get another prompt.

The System PATH
===============

..  objective::
    1.2 Understand how to configure the system PATH 

Exactly where the OS searches for programs you name is controlled by something
called an :term:`environment variable`. There are many such variables in a table
maintained by the OS. The variable used to locate programs is called the ``PATH``
variable. This is just a long string listing all of the directories where
programs are installed. There is a separator character between each directory
name: A colon character on the PC, and a semicolon on Linux/Mac machines.

You can modify this ``PATH`` variable if needed, something we will do as we install
our development tools later.

Let's try out this new interface!

Command Prompt on PC
====================

..  note::

    Since most students are showing up with laptops running WIndows 10, we will
    use that system for this example. For older versions of WIndows, the way
    you launch the "command Prompt" tool is slightly different. See me for
    help.

Open up the ``Command Prompt`` window on a PC by typing "cmd" (no quotes) in
the search box at the lower left corner of your screen.


You should see something like this:

..  image:: images/mac-terminal.png
    :align: center
    :width: 600


Managing Tools Directly
***********************

Rather than live in that point-and-click world, we will work on the system's
``command line``. Some of you have never seen this side of your computer, but
it is important that you know how to work in this strange environment. Working
on remote systems is a big part of the development world these days. Often the
interface to those systems does not provide a fancy graphical interface, just
that plain text-only ``command line``.

Being able to log in on a remote system, write some code  and run commands
there is something you just need to know how to do. So you will be learning
that way of working in this class. 

Don't worry, things will be simple enough, after you learn the basics!

Let's get started by crafting the industry-standard first C++ program: "Hello,
World!"

Fundamental Build Tools
***********************

..  objective::
    1.3 Know the primary tools used to build and run C++ programs

Before we can get very far, we need to make sure we have a few basic tools available. 

Programmer's Editor
===================

The first tool we need to master is a simple editing tool. We could (but won't)
fire up something simple like ``Notepad`` on a PC and type our code. The problem
with that idea is that ``Notepad`` knows nothing about programming, and we want a
tool professionals will be comfortable with. Now, 

..  warning::

    This is a topic sure to start "flame wars". And, yes, I know about
    ``Notepad++``. I choose to use one I consider much better! YMMV! 
    
Most programmers have one editor they will use and defend forever. There are
many to choose from, but I have always favored a tool that can be run on just
about any platform you will ever touch in your career. For me that editor is
some version of ``Vim``. I have used this editing tool on $35 Raspberry Pi
computers and on $8 million Cray super-computers! It ranks near the top of any
list of favorite developer's editors. We will use ``Vim`` in this class. 

..  note::

    Even if you end up choosing another editor, you owe it to yourself to know
    the basics of using ``Vim``, since it is commonly installed on many systems
    (just not on Windows, but that is easily fixed!)

Installing gVim_
----------------

Installing gVim_ (or most tools you will want) in Ubuntu Linusx is pretty simple:

..  code-block:: bash

    $ sudo apt-get install -y vim-gtk

..  note::

    You will be asked for your password when you run any command thta starts
    with ``sudo``. ``sudo`` stands for "super-user do". This elevated your
    permission level to the all-powerful "root" user who can do just about
    anything in Linux. This level of control can get you in trouble, so most
    Linux users limit the time that use this power. Basically, we ned this
    power to install files in areas of the file system off-limits to normal
    users.

We can check that ``Vim`` is installed by opening up a ``command-prompt``
window and typing a simple command:

..  code-block:: bash

    C:\User\rblack> gvim --version

If gVim_ is installed, you should see something telling you what version you
are running. 

Program Build Tools
===================

We need another set of tools to process progran code files. All of the additional tools needed for this purpose are packages in a simple package we install as follows:

..  code-block:: bash

    $ sudo apt-get install -y build-essential

After running this command, we cna check that the tools we really need are installed:

C++ Compiler
------------

After you edit a C++ program, and same the code file on your system, we need to
process that file using a suitable C++ compiler. There are many such compilers
available. We will use a version of the Gnu_ C++ Compiler, which is
industry-strength, free, and available on all machines. 

We can check that the compiler is ready for action as follows:

..  code-block:: bash

    $ g++ --version

Make
----

We could manage the building process manually, and we will do that for our
first examples. However, typing in long strange looking commands on the
:term:`command line` gets old pretty quickly. For that reason, we will use a
tool that has been a part of programming for a long time. That tool is called
Make_. Basically, we will set up a simple
control file for Make_ and let it do all of the work 

Let's check that Make_  is installed:

..  code-block:: bash

    $ make --version

Git
---

This last tool is one most of you have never heard of. It is one of the most
important tools you will learn in this course. Git_ was developed by `Linus
Torvalds`_, the creator of the Linux Kernel, to help him manage the over 1000
programmer's who help manage this huge pile of code. Since Linus published Git_
it has "gone viral", and is now used daily by millions of programmers.

Git_ manages the history of your project. We will be discussing how it works,
and why you need to use it later in the course. For now, let's get it
installed:

..  code-block:: bsh

    $ sudo apt-get install -y git

And we check it as usual:

..  code-block:: bash

    $ git --version


    If you get this far you are ready to write some code in thsi new world
    called Linux. 


