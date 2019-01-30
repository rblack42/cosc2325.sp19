..  _installing-cpp:

Installing a C++ Compiler
#########################

.. vim:ft=rst spell:

Many (but not all) IDE systems come with all the tools you need. We are not
using an IDE, so we need to install those tools ourselves. Since we are going
to use C++ at the command line for much of our work, we need a good C++
compiler. One of the best available is the Gnu C/C++ tool set. This is found on
all Linux machines, and can be installed on Mac and WIndoes if needed.

..	note::

        I have about four different C/C++ compilers available on my systems. It
        is a good idea to test your code on various compilers, to make sure it
        is in the best possible shape before you turn it loose on other humans!

Windows Setup
*************

There is a great version of this compiler available from the Mingw-w64 project:

   * `Mingw-w64 GCC <http://mingw-w64.org/doku.php#mingw-w64>`_

If you have a 64-bit Windows PC (you probably do if it is running Windows 10,
or is fairly new, use this link:
   
   * `Mingw-w64 (64-bit) <http://mingw-w64.org/doku.php#mingw-w64>`_

For other (or older) systems, see me, or look around on the project page. There
are installers for just about anything.

Mac Setup
*********

If you do much development work on a Mac, you are going to need to install
XCode. This package is free, but you do need to have a good network connection.
Last time I installed it, it was a 5GB download that took a while. You get it
from the Apple "App Store". 

Once that package is downloaded and installed, open it up to complete the
initial setup. Then navigate to the following link:

   * Xcode -> Open Developers Tool -> More Developers Tools

You will be asked to sing up as a developer, and provide your Apple ID to do
this. It is all free, o fill out the forms and get se tup.

Then select "Command Line Tools" and add them to your system. Once all of this
has been done, ou should be ready to code

To verify that you are set, we need to open up a "command prompt" window on your system.

Windows Command LIne
********************

Use the search tool and type "CMD". Select "Command Prompt"

Mac
***

Open up the "Terminal.app" program (found under Applications->Utilities)

.. code-block:: text

   $ g++ --version
   Configured with: --prefix=/Applications/Xcode.app/Contents/Developer/usr --with-gxx-include-dir=/usr/include/c++/4.2.1
   Apple LLVM version 9.1.0 (clang-902.0.39.2)
   Target: x86_64-apple-darwin17.7.0
   Thread model: posix
   InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin

This is what I see on my current development Macbook Pro. On a PC, you will see
something different. As long as you get something similar as a response, you
are ready to code!



     
  
