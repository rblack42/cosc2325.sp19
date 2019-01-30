HW 2: Hello Project
###################

..  include::   /header.inc

This assignment is designed to make sure you can use Git_ and GitHub_ to manage
your development work.  

Submitting Homework
*******************

To submit a homework assignment, open up a command prompt window and get into
your homework repository directory.

Create a new folder for each homework, named to indicate what assignment it is.
At this point, you need to do this:

..  code-block:: bash

    $ mkdir HW2

In each of these homework folders, place a ``README.rst`` file that looks something like
this:

..  code-block:: text

    HW2: Hello Project
    ##################
    :Author: Roie R. Black
    :Course: COSC2325-003
    :Instructor: Roie R> Black
    :Started on: Jan 27, 2019
    :Submitted on:  Jan 27, 2019

    Place any text you like here.

The note at the bottom should just describe this "project". For more complex
projects, tell a bit of a story here. The idea is to get used to telling the
reader of your project code something about the project. (Actually, we are
placing each homework "project" in this single repository, with each assignment
in a separate subfolder. We could have a separate repository for each
assignment, but that is overkill for our homework projects.

Now, use the "getting started" guide to get this work up onto GitHub_.
Basically that process looks like this:

..  code-block:: bash

    $ git add .
    $ git commit -m "what did I do"
    $ git push origin master

Of course, you might check things along the way by asking Git_ what it thinks.
These three steps are a kind of "mantra" developers just automatically do every
so often!

How often?

You decide. At a minimum, before they walk away from any work session. More
than that? Maybe. I like to do a "push" when I think the project has reached
some milestone. For students, when you get stuck and want to ask for help, push
what you have now. I can update my copy of your project and see what is going
on!

..  note::

    If you only push the project when you get it done, there is no way I can
    see how you went about doing your work. I like to check on your progress,
    and try to get you working smarter. Flailing away is not a good habit to get
    into! (We call that "blasting code"! It rarely generates anything to be
    proud of!)


What About HW2?
***************

We really need a real program here. Select one of these program code examples
and see if you can make it work:

..  literalinclude:: code/hello.cpp
    :linenos:

You can run this program as follows:

..  code-block:: bash

    $ g++ -c hello.cpp -o hello.o
    $ g++ hello.o -o hello
    $ ./hello
    My name is Roie R. Black

Push To GitHub
==============

Now, get this file on GitHub_ using your "mantra"!

Guess what! That is all you need to do.

..  vim:ft=rst spell:
