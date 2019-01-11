Getting Started
###############

..  include::   /header.inc

Are you ready to code? We will be building a fair amount of code in this class,
and of course, I want you to write good code. That means your code works, but
it also means that it is "clean", meaning it follows common style conventions,
is well written and documented.

The code you write reflects how much you care about the craft of programming.
Every student in this class is on a path to become a professional who can craft
solutions to complex problems, then get the computer to do the messy work for
you.

We will be using C++ in this course. Some of you may have already studied C++,
but others have never seen this language. No matter! We will start off with a
simple problem, designed to show you how to do your work.

I can hear some of you muttering that you know how to write code, you just fire
up some IDE and type away. 

Wrong!

We will be creating code using an "old-school" approach that does not rely on
fancy development systems. We will pay a lot of attention to how you set up a
project, create the code and documentation, process and test your code, and
publish your code on a public server for other to see.

Why Not use an IDE?
*******************

IDE (Integrated Development Environment) systems are certainly productivity
boosters. Using one can speed up your coding, and help you manage your code.
The real problem with using an IDE in school is simple to explain. When you
finally join a development team and start working on a "real (big) project,
that team will tell you what development tools you need to use. Your current
favorite tools will not be usable now. 

There is another problem with living in an IDE while learning. The IDE hides a
lot of details about building your project from you. I once attended a school
that almost lost its accreditation because no student interviewed (and several
faculty members as well) could explain how a program is actually processed into
something that can run on a real computer!

We will make sure you understand what is going on by making sure you can
function as a developer with only the real development tools available. It may
surprise you to learn that most IDE systems are just fancy wrappers around
standard tools. The wrapper gives you a point-and-clink development world to
live in. Behind the scenes, those standard development tools are running under
control of the IDE.

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

Let's get started by crafting the industry-standard first C++ program: "Hello, World!"

Prerequisites
*************

Before we can get very far, we need to make sure we have a few basic tools available. 

Programmer's Editor
===================

The first tool we need to master is a simple editing tool. We could (but don't)
fire up something simple like Notepad on a PC and type our code. The problem
with that idea is that Notepad knows nothing about programming, and we want a
tool professionals will be comfortable with. Now, 

..  warning::

    This is a topic sure to start "flame wars". 
    
Most programmers have one editor they will use and defend forever. There are
many to choose from, but I have always favored a tool that can be run on just
about any platform you will ever touch in your career. For me that editor is
some version of ``Vim``. I have used this editing tool on $35 Raspberry Pi
computers and on $8 million super-computers! IT ranks near the top of any list
of favorite developer's editors. We will use Vim in this class. 

..  note::

    Even if you end up choosing another editor, you owe it to yourself to know
    the basics of using ``Vim``, since it is commonly installed on many systems
    (just not on Windows, but that is easily fixed!)


We can check that Vim`` is installed by opening up a ``command-prompt window on your PC as follows:

    1. 



