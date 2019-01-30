The CPU Factory
###############

.. include::   /header.inc

.. vim:filetype=rst spell:

We have introduced the basic concepts we will use in building a functional
simulation of a real Processor. It is time to start writing the code.

For the first part of our project, I will provide most of the code. All you
will need to do is piece things together and make sure you can get things
running. As the project progresses, you will be writing most of the required
code yourself.

Baby Steps
**********

I am a firm believer that programming is much more fun if things work. I simply
do not spend much of my time chasing down sill typing mistakes. The basic rule
I want you to follow in coding is this:

::

   Never write more than a half-dozen lines of code before you try to compile
   that code.

If the amount of code you just typed is small, the chances that you can catch
silly mistakes quickly is very high. If ou code for an hour before compiling,
you most likely will spend another hour trying to fix all the mistakes you
managed to put into that code!

There is a corollary to the above rule:

::

    Think up the smallest change you could make to your current code that could
    possibly work, and focus on just that change.

This means do not "blast code" without really thinking about what you are
trying to do. We will start with code we know should work, prove that it does.
Then we will add a tiny new feature to that code and make sure that works. In
working this way, we spend more time seeing positive results from our work, and
very little of our time fighting with code we cannot get to run. 

.. note::

   Trust me, I have been there. I am a much happier coder today! And, Git_ is
   my new best friend, coupled with another cool tool we will use: Catch_

   Catch? WHat are we going to "catch"? Well, silly, ERRORS!

Testing Your Code
*****************

We will be writing a lot of small classes. We will use those classes to
construct a fairly complex system, and we need to make sure things are working
as we go. 

A class is a self-standing unit of code. You should be able to pick up that
class and plant it in a completely new project with no worry that it will not
work properly there. That means we should be able to take our class and create
a simple chunk of code that just exercises that class all by itself. We know
what objects created from that class are supposed to do, our simple code should
focus on proving that it works properly.

The simple code we write is called a :term:`unit test`. The "unit" is the
class, and we are just testing it all by itself. We can take this "unit" idea
down another level, and test each method we write for the class. Once again, we
should know what that method should do, let's prove that the method works
properly!

The bottom line in testing is this:

::

   Every line of code you write should be subjected to a test!

   If it has not been tested, it does not work!

Is that last line true? The only way to prove it wrong is to test that line!
Fortunately, there are tools around that will tell you if all of your code has
been tested. Cool!

On first glance, this is kind of silly. We need to write more code to test our
real code. That would be annoying if the amount of test code we write is large.
But in our work, the amount of test code you write is exceedingly small, so
testing is pretty painless. 

As we work through this project, you will see this testing process in action. I
bet you will like the results! 

..  note::

    No serious project being worked on by developers out there in the
    :term:`real world` is being constructed without serious :term:`unit
    testing` going on. You simply need to be doing this now! Don't worry, us
    lazy programmers can automate the process! (We do that a lot!)

.. warning::

   No, it may strike you that we are really attacking the process of
   programming here. We are, but for a very good reason. More than likely, in
   your classes up to this point, the work you have done to write code has not been
   examined. You went off, "blasted code" and turned in the final result. That
   result might not even work, but you struggled with it long enough, and you
   simply want it done and gone! You have probably developed a lot of bad
   habits along the way, and my goal is to break those habits, and replace them
   with solid development skills that will make you a much more attractive (to
   employers, that is) developer!

How We Will Proceed
*******************

In the lectures that follow, we will practice what I am preaching here. Each
Lecture will focus on one small step. Some of these steps will seem silly, you
could blast through them in minutes. That is just fine! You should do that. But
"blasting" is not what we are doing here. We are working on small
clearly-defined steps, and making sure things work! The key in this is
thinking! In that :term:`real world` out there, the current estimate is that
80% of your development time should be spent thinking about what you are doing,
the coding is actually a small part of your work. By the time you start
pounding on that keyboard, you are pretty sure what you will do.

.. note::

   You will be working on the keyboard while you are tinking. But you will not
   be writing code, you will be writing documentation! More on that later.

Ready to start? On to the next baby lecture!


