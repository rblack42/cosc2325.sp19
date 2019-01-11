Configuring Vim in Ubuntu
#########################

..  include::   /references.inc

Vim_, like most programmer's editors is highly configurable. Every programmer
has an idea of the "best" way to set things up, but one programmer's settings
will annoy another programmer somewhere.

You need to learn how to tune up the editor so YOU are happy with it.

Fortunately, this is pretty easy, but there are a ton of options you can play
with.

In fact do a search for the name of the configuration file (``.vimrc``) in
GitHub_, and stand back. 

..  warning::

    Much of this discussion is aimed at Linux/Mac users. FOr PC uses, watch the
    notes closely. The exact commands are a bit different.

Personal Settings
*****************

All settings in Linux/Mac are stored in a hidden file in your home directory. That
file is this:

    * ``/users/<accountname>/.vimrc``

This is just a text file with commands to Vim_ to set certain options to the
values specified. This file can have comments, which are anything after a
double-quote character to the end of the line. The comments are not needed, but
I am including them in this note to explain what each option does.

..  note::

    On a PC, the file is named ``_vimrc`` and lives in the folder where you
    install gvim.

Create/edit .vimrc
******************

If this ``.vimrc`` file does not exist, you can create it with Vim_
naturally!). The same command will edit an existing configuration file:

..  code-block:: bash

    $ vim ~/.vimrc

That the "~" character is just an alias for ``/home/<accountname>``.

..  note::

    Windows is just realizing that having an easy way to specify where your
    home directory is actually is a good idea. For Windows you create your file
    by navigating to the right folder, then typing this ``vim _vimrc``:

Here are the absolute minimum settings I use:

..  code-block:: vim

    " Chage tab stops to every 4 chars
    set tabstop=4

    " this setting makes indents match the line above
    set autoindent

    " make <Tab> and <BS> work together
    set softtabstop=4

    " highlite code as recommended based on the language
    syntax on

    " this setting must match the tabstop values if using auto indenting
    set shiftwidth=4
    
    " Replace tabs with spaces
    set expandtab

    " Do not create backups
    set nobackup

The last line eliminates the backup files Vim_ creates. Those files all end
with a "~" character after the name. I use Git_, so I do not need backups. 

Here ia a `link <http://vim.wikia.com/wiki/Indenting_source_code>`_ to a web page with more information on teaching Vim_ how to indent the way you like.

Other Settings
==============

These are useful for a beginner:

..  code-block:: vim

    " Show line numbers
    set number

    " Make searches case insensitive
    set ic

There are short forms for all options. That last setting was actually
"ignorecase". "ic" is shorter!

Spell Checking
==============

If you type a lot of text, like you might for documentation (or lecture notes),
you can turn on spell checking by entering this while in command mode in Vim_:

..  code-block:: text

    :set spell

I do not add this to the ``.vimrc`` file, since there are tons of spelling
errors in typical code.

But there is a neat trick you can do in your documentation files.

In my lecture notes, usually at the bottom, you will see this line:

..  code-block:: text

    .. vim:ft=rst spell:


That line is telling Vim that when it reads this file, after processing
anything in the ``.vimrc`` file, it should add two more options. The ``ft`` is
short for ``filetype``, which causes Vim_ to highlight the file as though it
was written in |RST| (those files usually end in ``.rst``). It will do that
even if this file does not end in ``.rst``. Some Python programmers like to use
``.txt`` on their |RST| files. Vim_ will handle both.

If I am editing a lecture note file, or documentation file, using |RST|, I do
want spell checking on, so the one line will make sure it is happening.

Any misspelled word will be shown with a red squiggly line underscoring it. If
you right-click on something Vim_ thinks is misspelled, it will offer to
correct it, or you can tell it to add this word to its dictionary. I have to do
that, since Vim_ insists that my name is misspelled! (Silly Vim!)

More Vim Tricks
***************

You can search for some text in your file easil. Mke sure you are in ``command
mode``, then type a forward slash, followed by the text you are looking for.
When you hit enter, it will put you on the first line below the current cursor
position that contains that text. It will wrap around, and search from the
start of the file, if needed. 

Typing just that slash and enter again will find the next occurrence of that text. 

Explaining everything you can do to tune this editor would take an entire
semester. You can set up custom key combinations that issue a whole string of
text, and some programmers use that trick to create starter code for projects. You
can also run common commands on your system's command line, and see the output
(error messages, anyone?) back in the editor. In fact, you could turn Vim_ into
an IDE if you like. I prefer not to do that!

Do some research, and more reading, and tune this critter up to suit you.
Believe it or not, you can even customize this editor, adding entire new
commands, written in Python! You can set up key combinations that will fire off
those custon commands easily. Of course, you need to learn a lot more about how
Vim_ manages an edited file, but there are examples around that can get you
started on this.

Learn Your Tools
****************

As a software developer, you will spend a lot of time using your editor. Once
we learn how powerful a good editor is (and Vim_ is certainly not the only
editor around), you job is to learn the basics of how to use your chosen tool,
then you learn how to tune it so you get your work done quickly.

I have used this Vim_ editor, or its predecessor, the Vi editor, since around
1976! It keeps getting better all the time. And, I keep finding new tricks, I
did not know about! Those tricks that make me like it even more. I have tried
to kick the Vim_ habit, just to see if I really can get more productive using
something else. So far, Vim_ has always won! YMMV!


