Documenting Your Project With |RST|
###################################

..  vim:ft=rst spell:
..  include::   /references.inc
..  wordcount::

You absolutely should be writing documentation at the same time you write code.
No, I do not mean add comments to your code! I mean write a separate document
that *explains* your code to some poor soul who will inherit your creation and
have to "maintain" it. You need to establish a habit of working on your
documentation, and treat that as something as important as the code itself!

Good Documentation
******************

What makes for good documentation?

For one thing, it is designed to convey information to the reader. But who is
that reader? Perhaps it is you a week from now, when you have forgotten why you
did what you did. Most certainly, it is another developer who inherits your
code a year from now, when you are not around to help out. Maybe you are
working on another project, maybe you have left the company. Who knows?

`Donald Knuth`_, one of the most respected computer scientists this country has
produced, thought this was so important, he proposed a new way of programming
he called `Literate Programming`_.

In his system, you wrote the source code for a book, describing the code you
were developing. That code was processed using another great tool developed by
Knuth_, the TeX_ typesetting system, and generated something a published could
use to print a real book (or, today, a nice PDF). Where is the code you need to
compile? It is buried in the documentation source, and extracted by a tool
designed to generate the code file the compiler could process. Knuth_ was
concerned that documentation and code might wander in different directions, so
he made is hard for humans to read the generated code. The compiler could care
less, so Knuth_ hoped that developers would stay focused on writing the
"literate" documentation instead.

Knuth's system never really took off, but it became part of the programming
landscape, and still has many proponents (including me)!

Writing Documentation
*********************

To get you started in writing this documentation, I am going to have you use a
very popular system for processing your documentation into something easy to
read.  Shoot, you are reading the product of that system right now. I have been
using this tool for my lecture notes ever since it hit the planet in 2008!

The tool we will use is Sphinx_, a Python tool that has a huge following now.
Although it was designed to support documenting the Python project, itself,
developers are using it for all kinds of projects, not just Python projects.

Prerequisites
=============

In order to use Sphinx_, you need to have Python installed, and a support tool
used to install Python libraries. That support tool is named ``pip``. This
program will install Python libraries published by developers all over the
world by running a simple command on your command-line:

..  code-block:: bash

    $ pip install packagename

``Pip`` will download the named package and install it in your Python
installation so it is ready to use. If that package needs anything else, ``pip``
will install that as well. In the end, you should be ready to use the new tool. 

Let's get ready to go:

Windows Setup
-------------

If you installed Python3 using the standard Python installer, you should have
the needed tools. ``Pip`` is not installed in the same folder as Python
itself. That means we need to edit the system PATH variable, and add one more
folder.

On my PC, I installed Python 3.7 under ``C:\tools\Python37``. ``Pip`` is
located under ``C\tools\Python37\Scripts``. When I added that to the system
PATH (see the notes in the appendix on how to do that). ``pip`` was ready to
run:

..  code-block:: bash

    $ pip --version
    pip 10.0.1 from c:\tools\Python37\lib\site-packages\pip (python 37)

That tells me I am ready to go.

Mac
---

On Mac systems, you should be using HomeBrew_ to load things. Here is how I set
up my Mac for Python development:

..  code-block:: bash

    $ brew install python
    $ python --version
    $ pip3 --version

..  warning::

    On Mac systems, if you run ``pip``, you are using Python 2.7. We need to
    run ``pip3 to get the correct versions of our libraries. My examples will
    show  ``pip3`` as the command.

Linux
-----

I use Ubuntu Linus. Run these commands to get things set up:

..  code-block:: bash

    $ sudo apt-get install python3
    $ sudo apt-get install python3-pip


Documentation Setup 
===================

The first thing you need to do is set up a folder for your documentation. The
usual home for this is a ``docs`` folder at the root of your project folder.
However, we will be publishing our documentation on GitHub_, so we want to
reserve ``docs`` for actual web pages. On my projects, I set up a folder named
``rst`` where I place all of my documentation files. Sphinx_ will process those
files and build the web pages i need in the ``docs`` folder.  :

..  code-block:: bash

    $ cd <project root>
    $ mkdir docs
    $ mkdir rst

Installing Sphinx
=================

With these folders in place, it is time to install Sphinx_

..  code-block:: bash

    $ pip3 install sphinx
    $ pip3 install sphinx-rtd-theme

That last line installs a theme I like to use on my documentation. We will
configure our project to use this theme in this note.

Initializing the Documentation
==============================

Sphinx_ comes with a tool for setting up a documenting project. We will use
that tool for the next step:

..  code-block:: bash

    $ cd rst
    $ sphinx-quickstart

That command will set up the SPhinx_ project. You will be asked a bunch of
questions, most of which you can just leave as the default answer (except for
your name and the project name).  

Be sure to say "yes" when it asks if you want a ``nojekyll`` file. We will need
that if we want to see our web pages on GitHub_.

..  note::

    On PC systems, create a file named ``build.bat`` in the ``rst`` folder. Place this line in that file:

    ..  code-block:: text

        sphinx-build -b html -d _build/doctrees . ../docs

Save this file when done.

Running Sphinx
==============

To test your setup, or to build your documentation, open a command line in your
``rst`` folder, and do this:

..  code-block:: text

    $ build

When this command completes, you fill find web pages in the ``docs`` folder we
set up earlier. Using Windows Explorer, navigate to that folder and
double-click on the ``index.html`` file. You should see your web pages in
your browser.

Adding a Theme
**************

The default theme is a bit ugly for my tastes. In the ``rst`` folder, there is
a file named ``conf.py``. This file has a lot of stuff in it we really do not
need. I usually strip away most of the "fluff" and  use something simple, like
this:

..  literalinclude::    code/conf.py
    :linenos:
    :caption: conf.py

Look this over, and change the lines that obviously are about you and your
project. Leave everything else alone. 

Build your docs again, and open up ``index.html``. You should see something a
bit nicer.

If you get to this point, you are ready to document. There is still a bit of
work to do, though

Publishing on GitHub
********************

Of course, your project is on GitHub_ and you are using Git_ to manage things.
Here is what you need to do next:

:Reference: https://pages.github.com/


Repository Setup
================

Before you can get web pages published on GitHub_ make sure you have built your
documentation at lease once, and pushed your work (and web pages) to GitHub_.
If the ``docs`` folder does not exist, the following steps will not work.

Once you are ready, press on:

	1. Open your project repository in GitHub_.

	2. Select ``settings``

	3. Scroll down until you see the GitHub Pages area.

    4. Enable GitHub Pages for this project, then select 
           ``Master Branch/docs folder`` as the source for your site.

	5. Place any HTML file in that folder. (we did that by running Sphinx_)

	6. Navigate to https://ghuser.github.io/project-name to see your site

..  note::

    Your website for class projects will appear at a URL that looks something like thi:
    
    * https://ACC.COSC1337-004.github.io/i35sim-teamname

This website is available for free for any repository you set up on GitHub_. I
highly recommend learning how to do this, then building nice documentation for
every project you create.

..  warning::

    Public project, of course. School work should be kept private!


Learning reStructuredText
*************************

The next thing you need to do is to explore |RST|_ and get a feel for how you
set up your documentation.

All of my lecture notes are written in |RST|_ markup, so you can use the :show
source" link to see what I wrote Much of what you see is a bit advanced,
because I have extended Sphinx_ with some additional "plugins" that let is do
cool things. For you, just starting up< use one of the online tutorials on
SPhinx_ to get started.

Here are a couple of useful links:

    * `Sphinx Reference <http://www.sphinx-doc.org/en/1.6/markup/inline.html>`_

    * `Sphinx Tutorial
      <https://media.readthedocs.org/pdf/brandons-sphinx-tutorial/latest/brandons-sphinx-tutorial.pdf>`_


    
