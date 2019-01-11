..  _project-versions:

Project Versioning
##################

..  wordcount::
..  vim:ft=rst spell:

Many projects track the version of their project using a simple scheme that
looks like this:

..  code-block:: text

    version=2.1.7

Conventional Versioning
***********************

There is a rationale for this numbering scheme. Here are the rules:

Major Number
============

The first number is the version number. Versions are major releases of a
project. There is no requirement that the user interface to the project be
maintained when major versions are released. There is usually a significant
changes in the way the project works with each major version.

Projects start off with major version number zero, until the project reaches a
point where is is ready for real uses to play with it (or pay for it!)

Minor Number
============

Any time a project adds a new feature to the code, adding to the capability of
the project, a minor release number is incremented. Here, the user interface is
preserved, but a set of new features is added to the system.

Minor releases can happen more often over the life of a project. The added
functionality of the new version should not remove, just add ti them.

Patch Number
============

While a release is in use, it is common to issue patches to it. These patches
do not add new features, or make changes to the interface. What they do is
correct bugs detected in the version. 

Patches are a way of life, it seems, in recent projects. Some projects patch
almost continuously. The patch number gives you a sense of how active, or how
buggy a piece of software is. You get to decide if big numbers here are a good
thing or not.

Our Versioning System
*********************

Just for fun, we are going to ditch the patch number and change that to a build
number. I often wonder how many times I build my code, so we will set up a
version system that tracks this number. 

We will set up our ``Makefile`` with targets that help us manage the build
number. For simplicity, we will store the current version number in a hidden
file in the project directory. This file will be constructed, and modified,
inby commands in the project ``Makefile``.

Step 1: Creating the Version File
*********************************

This step is easy. We will set up a simple ``make`` target that displays the
current version. If the file does not exist when this target is run, it will be
created with an initial version of ``0.0.0``.

..  
