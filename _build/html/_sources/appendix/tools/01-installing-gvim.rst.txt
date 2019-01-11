..  _installing-vim:

Programmer's Editor
===================

..  include::    /references.inc

There are literally dozens of outstanding editors for professional programmers
available either commercially, or free on the Internet.  Choosing one is a
challenge, and can lead to religious wars if you try to claim that you choice
is the *best*. I choose to use an editor that is available on almost every Unix
like system (including Linux) and has been around for many years. That editor
is a version of **vi**. For Windows platforms, the specific editor I use is
called gVim_, and it is installed on the lab machines. 

gVim_ is a free editor available from http://www.vim.org.  This particular
version is a full Windows application that integrates fairly well into the
Windows environment - even to the point where there is an *Edit with gVim*
entry on the right-click context menu that you can pop up when browsing for
files using the Windows Explorer tool.

The installation of gVim_ is pretty easy - download the installer and run it on
your system. The current file you want is ``gvim73_46.exe``. I usually install the program under `c:\\tools\\vim` on my
systems. Once this is done, the editor is ready to go, except that I recommend
a few tune-up steps to make the editor work a bit better for our projects.

`gVim` uses a configuration file to set a few parameters that control how it
works. You do not need to modify this file, but adding a few parameters can
make it work a bit nicer. The file is named `_vimrc` and it is found in the
root of the folder where you installed `gVim` (`c:\\tools\\Vim` on my system).
Here are the changes I make to my setup: 

..  code-block:: bash

    behave mswin
    set nobackup
    set tabstop=4
    set shiftwidth=4
    set expandtab
    filetype on


The first of these lines should already be in your default configuration file,
add the rest of them as shown. 

Here is what these additions do:

Kill the automatic backup
-------------------------

By default, `gVim` creates a backup copy of the file you edit.
That file has the same name as the file you are working with, with a
squiggle added to the file name. This backup file can be used to recover
from a bad editing session, if you need such a thing. Simply kill the
current copy and rename the backup and off you go. I choose not to do this.
This line controls this: 

..  code-block:: bash

    set nobackup


Change tabs from 8 spaces to 4 spaces
-------------------------------------

Most programmers use indenting as part of their programming style. By default,
most editors set the tab stops every 8 spaces, which I find to be too many! I
use the tab key to indent my code, but I prefer 4 characters per tab stop. Add
these lines to set this up: 

..  code-block:: bash

    set tabstop=4
    set shiftwidth=4


In addition, since I program in Python a lot, I prefer to have my tabs
automatically expanded into spaces when I type. This helps keep my code
listings on the web look right as well, since most browsers also use 8
spaces for the tab spacing. Here is the addition to make this happen: 

.. code-block:: bash

    set expandtab

..  warning::

    Some programmers object to expanding tabs, but the benefits of doing so far
    outweigh these objections. Many companies set up coding standards that you
    have to live with, and expanding tabs is very common. That way programs
    written by one programmer using their editor will look right when loaded by
    another programmer in a different editor. Since I have to look at all of
    your code, and I will grade on style - let's expand tabs and be done with
    it!

Basic editing
-------------

There are many tutorials available for vi, here is `a gVim tutorial
<http://supportweb.cs.bham.ac.uk/docs/tutorials/docsystem/build/tutorials/gvim/gvim.html>`_
to get you started. 

The most important concept to know about gVim_ is that it is a modal editor.
That means you are in one of two modes at all times. The first mode is
``command mode``, which you can detect by looking at the blinking cursor - it
will be a black box the size of a single character. In this mode, anything you
type will be a command to the editor. The most important commands are: 


* `i` (insert)
  enter text insert mode at the current location 
* `:q` (quit)
  exit the program 
* `:w` (write)
  write out the current text 
* `<Esc>` 
  Exit insert mode and return to command mode

The second mode is ``text entry mode`` which is detected by looking at the
blinking cursor again - it should be a skinny vertical line. In this mode
anything you type will be entered into the text of the file you are editing.
All the normal keys should work fine - cursor keys, tab, backspace and delete,
etc. 

You get out of text mode by typing the `Esc` (escape) key on your keyboard.
Make sure the cursor changes as described above. 

Since `gVim` is a normal graphical program, you have access to the menu system
you should be familiar with from other work in Windows. Check the tutorial for
more info. You will not be tested on anything about the editor so you are free
to choose another one if you prefer. If you are seen using `Notepad`, you may
lose your programmer's license!

Other Settings
---------------

There are a few more settings I use in my teaching activities that you may find
useful:

Wrapping text
,,,,,,,,,,,,,

Normal text entry will not `wrap` lines when they get too long. I like to keep
all my code short so it prints nicely and can be displayed on web pages with
little formatting problems. So, I want all my text lines to be less than about
75 characters ling. I can do this with this setting in `_vimrc`::

    set textwidth=75
    map q gq}

The normal edit window is 80 characters wide, so this works pretty well (for
me). That second line looks pretty odd, but helps. If you edit a properly
formatted paragraph and push lines out past your preferred limit, placing the
cursor (in command mode) at the top of the paragraph and pressing the `q` key
will reformat the paragraph so the line length limit is obeyed.


Spell checking
,,,,,,,,,,,,,,

We can make gVim_ can work differently depending on the type of file you are
editing. For each file name you edit, gVim_ looks at the `file extension` and
loads a special `plugin` file whose name is something like `viext.vim`. These
files are located in the `vim73\ftplugin` directory (assuming you are using
gVim 7.3). As delivered, gVim_ knows about a bunch of different languages. Now,
we probably do not want to spell check a file with program code since lots of
stuff in that file will be misspelled (according to your English teacher).
However, if the file you are editing contains mostly normal text, turning spell
checking on can be handy.

For example, the file containing these notes is being written in
`reStructured Text`, and such documents normally are saved in files
with a `file extension` of `.rst`. Add this line in
`rst.vim` to turn on spell checking when you edit a
`reStructured Text` file:

..  code-block:: bash

    setlocal spell spelllang=en_us

Once this is done, spell checking will be active whenever you edit one of
these files, and gVim_ will place a red squiggly line under any word that
it thinks is misspelled. Click on the offending word, then
`right-click` to see a menu that will help you correct the error. You
can add words to the dictionary gVim_ uses if you like, just make sure your
additions are spelled correctly!

Setup for Windows Vista and Windows 7
-------------------------------------

Under Windows XP, the gVim installation added a nice ``Edit with vim`` entry in the ``Windows Explorer`` context menu that allowed you to right-click on a file and quickly edit that file. Under Vista and Windows 7, this entry occasionally shows up, but most often does not. After Googling the problem, I found a registry patch that restore this feature. Save the following file as ``gvim.reg``:

..  code-block:: text

    Windows Registry Editor Version 5.00

    [HKEY_CLASSES_ROOT\*\shell\Edit with Vim]

    [HKEY_CLASSES_ROOT\*\shell\Edit with Vim\command]
    @="C:\\tools\\Vim\\vim72\\gvim.exe \"%1\""

Run this script by right-clicking on it and choosing "Open with --> Registry editor``. You will get a warning message, but it should work fine.

..  warning::

    If for any reason it does not, you can use the registry editor to remove
    these entries. My system has worked fine with these additions.

Once these entries are in your system, the context menu entry should appear in ``Windows Explorer``.    


..  vim:set filetype=rst spell:
