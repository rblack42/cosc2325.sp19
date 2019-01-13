Lab 1: The Dance Simulator
##########################

..  include::   /references.inc

For your first lab assignment in this class, I want you to create a C++/Python
program that simulates the dance (version 1) that we did in class. There is C++
starter code at the end of this note.

..  warning::

    The provided code is my solution, stripped of the details needed to make it
    work. It is not a "good" program. It lives in a single file, does not use
    classes, and it has those evil global variables. That is by design. I want
    to to craft your own code, doing as good a job as you can. Use my code as a
    guide to help you put together the needed parts.

General Lab Repository
**********************

We will do a few individual lab projects in this class. As we are doing for the
homework problems, we will set up aa repository inside of which you will create
folders for these labs. The invitation you need to set up this repository is
here:

    * `COSC2325-002 <https://classroom.github.com/a/JM1LkAOv>`_

Accept this repository, then clone it onto your workstation as we did for the
homework repository.

Design in Teams, Code on Your Own
*********************************

For this lab, I want you to form up into teams of three or four classmates.
(Less will be allowed only if needed - more is not allowed.) Your team should
talk through the design of this simulation. After you talk, write your own
code. You can look at each other's code, but no sharing of files is allowed. I
want you to fee that you wrote this code, and I expect you to do real original
work to put this together. You can help each other get this done and put into
your repository as needed to submit this. The "team" is done, when all team
members have code on GitHub_.

Sample Output
*************

The output from this sample program is something I want you to reproduce, as
best as you can. My solution uses the rules in the lecture, so you should be
able to duplicate the output. 

Here is a sample run for dance version 1:

..  literalinclude::    code/dance/sample-run.txt
    :caption: sample-run

And here is the stripped down solution code I created:

..  literalinclude::    code/dance/dance.cpp
    :linenos:
    :caption: dance.cpp

This lab uses some coding techniques and style that is common these days. Take
some time to read this example code over, and note how it is presented. We
will pay more attention to style as the term progresses.

Submitting this Lab
*******************

Place this in your new ``labs-username`` repository as usual.

Debug Output
************

I added a debug switch (``-d``) for the command line, to generate debug output
that shows how the individual "get happy" steps worked. Here is the debug
output from the sample run shown above:

..  literalinclude::    code/dance/sample-run-debug.txt
    :caption: sample-run-debug

..  vim:ft=rst spell:

