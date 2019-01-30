Time to Talk About Time
#######################

In our discussion up to this point, we have mentioned time a number of times!
Why?

Electricity "flows" through wires. It does not move instantaneously from one
point to another. It does move at a pretty quick speed. The actual speed is
something on the order of 70% of the speed of light, and light blazes along at
a pretty good clip! (Exactly how fast is a homework problem you will get soon.(

It takes some time for our "signals" to move from one part to another one in
our system. It also takes some time for the processing to get done inside each
part. Exactly when the signals move, and when the processing happens is
something we need to explore.

For now let's just consider how we are going to model time in our simulated
computer.

Clocks
******

You should be aware that the computer is controlled in some way by something we
call a "clock". The clock "ticks" at some speed, and things happen each time
that tick happens.

It should be obvious that we will need a way to simulate this clock thing, and
the most obvious way to do that is to set up a simple loop:

.. code-block::   c++

   unsigned int time = 0;

   while (true) {
      tick();
      time ++;
   }

That should do it. This code, basically an "infinite loop", will simply call
this "tick" function over and over. We have an unsigned integer we can use to
model the passing of time. Bigger numbers mean further down that time line we
say time marches along. 

.. note::

   So far as we know, time only moves in one direction, and we are modeling
   that direction with increasing values for this ``time`` variable. No one has
   figured out how to march backwards in time. It is fun to think about what
   would happen if you could do that, though. Many a Science Fiction book has
   been written on that idea!
   
We will need to make something happen as a result of that call to ``tick`` to
get our simulated computer to do something. 

This loop would be simple to write, but it has one serious problem.

Real computers are made up of many simple component parts, each of which
operate simultaneously when a tick rolls around. That means we should be
activating every part at the same time. That would require parallel processing, something not taught currently in most CS classes,  to model a
real computer. That kind of programming is possible, and fascinating, but
beyond what we need to do in tis class. 

Instead, we will "simulate" parallel processing by giving each part in our
simulated computer a chance to do something every time that tick function is
called. Basically, it looks like this:

.. code-block:: c++

   while (true) {
      for int i=0; i< NUM_PARTS; i++) {
         part[i].tick();
      }
   }

Here, it seems that we have an array of parts, each of which supports a
``tick`` method that will make it do whatever processing it needs to do.

This is almost what we need, except we have imposed an order in which things
happen, which is not true parallel processing. This will only work if the
actions of one part do not depend on the actions of any  other part, which we
know cannot be true, since they are interconnected with wires!

So, we might need to come up with another way to decide when parts need to be activated.

Phew, what a mess.

Event Driven Programming
************************

There is a way to deal with this, but it involves a kind of programming that is
probably going to be new to you. This kind of programming goes by the name of
"Event Driven Programming", something that is very common in the computer
world, especially in writing operating systems and games!

The basic idea goes like this.

Once again, we set up a loop that simulates the passing of time. This one is
simple. Inside the loop we check to see if something called an "event" has
happened. In a game, an event might be a mouse movement, or a button press. In
our simulation, we will set up something that says one of our parts needs
attention. If several need attention, we will handle them one by one. 

Let's pick one part and see what might happen. 

Let's assume that the part is just sitting there, happy with its current
situation. The inputs have been processed and the results are sitting on the
outputs. As long as the inputs do not change, there is no reason to do any
work. So no events need to be generated.

Then, at some moment in time, a signal changes on an input. At that moment,
processing is needed to recalculate the outputs. The processing is going to
take some time to complete, so we schedule an event for that end time. The
event says that something has happened, and new values are available on output
pins.  The output signals are copied onto a wire at the right moment in time,
and begin their journey to some other part. For every output attachment on a given
wire, we can calculate a time of arrival for that signal. When the signal
arrives at a pin on some part, we schedule another event saying this part needs
to be triggered to do its processing. 

This sounds messy, but it is fairly simple to set up.

We need a way to record all of these events, and a way to keep things in time
order. The data structure we will use is something called a ``priority queue``.
Fortunately, there is one sitting in the C++ Standard Template Library we can
use. 

We will get to this kind of processing eventually, but we do not need to start
off there. Still, in thinking about the timing of things in a digital system,
it seems logical to record a few more pieces of data for all of the gadgets we
are modeling.

The part we are going to activate will have some signals sitting on its input
pins. (That is why I a putting s simple variable in each pin object, to hold
that value until it is needed.) When we activate that part, it will take some
amount of time for the processing to occur. When that time interval is over,
the part will write the new signal values onto the output pins. At that point,
the signals are supposed to travel along wires to other parts. We can calculate
how long that will take if we know the length of those wires. (Actually, we
might just ignore time along a wire, but maybe not!) To analyze how long it
takes for things to happen in our system, it makes sense to record the time it
will take to do the calculations in each part. That time may be different for
each part, and somehow, we will need to set all of that up when we build our
circuits. 

Hey, this is sounding interesting, and we will be able to see some interesting
things when we fire up our simulated system!

When the signals reach other parts, we might just activate them. However, some
digital parts do no processing until a special signal reaches them. (That is
why I set up the tick method). The part is not activated by some signal
changing, instead the signal reaches the part, and just sits there, until the
"tick" signal comes along. That tick signal is actually generated by the system
clock, which we will need to create in order for out system to do much.

Combinational Parts
===================

A part that activates as soon as a new signal reaches it is called a combinational part. There are many such parts in a real digital system. We might need to deal witht hese in our simulator, but most of what we are going to do will not need these kinds of components.

Sequential Parts
================

Parts that activate only when a special trigger signal reaches them (like a clock signal) are called ``sq=equential`` parts. We will definitely be building a lot of these. 

Event Timing
************

The timing of all of this is what is driving which part we activate, and in
which order we activate a part.

..  note::

    We computer geeks always want faster computers. Some of us "over-clock" our
    systems to make them go faster than the manufacturer claims the chip can
    go. That may work, or it may not. The simple reason why it might not is the
    time it takes for parts to complete their work. If we fire off a tick,
    start the processing, and fire off another tick before that processing is
    done, the values on the outputs are just wrong. Worse yet, they might not
    even be valid digital values, (Hmmm, like 0,47 - which is neither a zero or
    a one). If that happens, your computer is a useful as a door stop! You have
    been warned!

Managing Events
===============

We need to find a way to identify each part, and put that part into a
processing line of some sort, ordered by the time when it should activate. The
``priority Queue`` will do just that.

The ``queue``, which is just an ordered linked list, will hold two pieces of
information. Something to identify a part needing to be activated, and the time
at which that should occur. Actually, we will place a pointer to a part needing
processing into our queue. We will record the time when the event is to happen, and order our ``queue`` by that time.

Now, our simulation loop just looks at the queue, and pulls off the component
needing processing first and calls the "tick" method for that part. We will start that processing, and after the appropriate 
processing time, record the results on output pins.

The puzzle now, is what happens next.

When a new output is available on any pin, we should activate the wire attached
to that pin. The signal from that output travels along the wire until it
reaches another pin on some other component. We could calculate the time it
will take to reach that second pin, if we know how long the wire is. In any
case, when that new signal reaches a pin, the component owning that pin could
be activated to start processing that signal. If the part is combinational, we
should activate it immediately. If that part is sequential, we smple wait until
the next clock signal comes along, then we activate it.

This all sounds complex, and it certainly can get complex if we are not careful
in how we build up our system. My job is to keep you from getting overwhelmed
by all of this. 

We will start off slowly, with a simple example.





