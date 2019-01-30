..  _glossary:

Glossary
########

..  include::   /references.inc

..  glossary::
    :sorted:

    Syntax
        In programming, the rules that defing the language tell you how to fown constructs in that language. The rules define the "syntax" of the languagg. Failure to follow these rules results in "syntax" errors.

    Semantics
        In programming, if you follow the :term:`syntax` rules correctly, each
        construct will be transformed into something the computer can process.
        When that processing occurs, some :term:`state` change will occur in
        the system. Your understanding of that :term:`state` change is the
        "semantics" of the language.

    State
        In programming, we say a system (or the computer while running a
        program) is in some "state" at any moment in time. THat state consists
        of the contents of every variable in your program at that instant. As
        your code "executes" each line causes something to change in the
        system. That change is a "state change". You should clearly understand
        what will happen when each line of code you write is processed.

    Real World
        That mystical place where everything is supposed to work properly.
        Since in your world things are never working properly, that "real
        world" is always just out of reach. But, you really want to live there!

    Path
        The exact location of any file or folder in a file
        system is defined by specifying the "path" to that resource. The path
        begins with the :term:`Root Directory`, followed by the names of each
        subfolder leading to the resource. Between each folder name, we place
        the :term:`Path Separator` character.

    Path Separator
        The character used between names on the system PATH. On a PC, this
        separator is a back-slash, on other systems it is a forward-slash.

    Environment Variable 
        Each Operating system maintains a list if "variables" that help it
        manage various functions. These variables are simply strings of some
        sort, and applications can set up variables for their own use. The most
        common variable you will use maintains the list of locations where
        programs can be found. This variable is normally named just
        :term:`Path`.  
        
    Root Directory 
        File systems are structured as a series of folders and sub-folders. The
        top level of this system is called the "root directory".  The name for
        this folder is just the :term:`Path Separator` character, either "/"
        or "\".

    Home Directory
        User accounts on all systems set up a special folder where tat user can
        store files. The folder associated with the account is called the "home
        directory". 

    Current Working Directory
        When working on the :term:`command line`, you are placed in some
        directory in the file system. The directory you are in at the moment is
        called the "current working directory". You cna change to another
        directory with the "CD" command on most systems.

    Reserved Word
        Most programming languages include a set of words that are used to help
        identify what language feature you are specifying when you write code
        in that language. Normally, these special words may not be used for any
        other purpose.

    Directory
    Folder
        Files, and other directories/folders are collected into a logical group
        within a container. That container modes a file folder in an office
        filing system. Each such folder can contain files or other folders.

    VM
    Virtual Machine
        A software implementation of a computer architecture. These programs
        can mimic a real computer completely.

    Recursion
        A programming techniques where you write a function that calls itself
        as part of its implementation.

    GUI
        Graphical User Interface. Think "Windows"!

    Open-Source
        The "Open Source" world is one where all code is freely available and
        all source code is available as well. There are a variety of licenses
        that control how you can use this software, but basically, as long as
        you give credit to the original authors, you can use this code in your
        own "open source" projects.

    Base
        When talking about number systems, the base of that system refers to the number of symbols used. 

    GUI
    Graphical User Interface
        A Windows based interface, driven largely using a mouse. Invented by
        Xerox, and introduced to most of us when we first got our Windows
        machine or a Macintosh! (Steve and Bill basically swiped the idea from
        Xerox!)

    Interrupt 
    Interrupts 
        At the end of each "four-step" cycle in a processor, a signal can be
        detected that effectively calls a special function to deal with that
        signal. This happens independently of any normal program running at the
        time. Interrupts are used to deal with fast response hardware issues.

    Over-Clock 
        To run a processor faster than the manufacturer recommends. Some chips
        can handle this, since manufacturers are conservative in their ratings.
        However, pushing the chip to far will result in internal failures since
        components need a minimum amount of time to reach valid levels.

    truth table
        A simple table showing the outputs resulting from a fixed set of
        inputs. Truth tables are commonly used to show hor Boolean Functions
        operate. 

    HDL
    Hardware Description Language
        A formal language used to describe the operation of a hardware system.
        Currently, HDL languages are actively used to design computer systems,
        replacing old techniques where circuits were drawn directly.


    gates
        In digital systems, "gates" are small components designed to perform
        simple Boolean operations. Internally, they model a simple `Truth
        Table`` defining the operation of the gate. These components need no
        clock, they simply transform input signals to output signals.

    Battery
        A device that can deliver electrons to a circuit for some period of
        time. Some batteries are depleted by this action, others can be
        "recharged" so they can function repeatedly.

    Atom
        A small fundamental building block making up the matter in the
        universe. These atoms are constructed out of even smaller components
        called Electrons, Protons, and Neutrons.

    Conservation Laws
        Mathematical laws governing interactions going ion in our universe.
        Three laws include the ``Conservaton of Mass``, ``Conservation of
        Energy``, and ``Conservtion o Momentum``. There are many others in
        different fields of study. These laws can be expressed as mathematical
        equations, and studied in detail, which makes up much of the work in
        science and engineering.

    Object
        A logical container modeling something from our "human" world. All data
        and functions that work on those data should be inside of the
        container. This isolates parts of the program, increasing the
        reliability of that code.


    Encapsulate
        To create a protected shell around something. We use such a shell to
        prevent outside code from modifying data, or accessing functions that
        only the object should access.


    Attribute
    Attributes
        A variable stored inside of a logical structure called an object. In
        theory, the object can control access to this variable, protecting it
        from being modified maliciously by some other code.


    Class 
        A "blueprint" for an "object". The blueprint is used to manufacture
        objects at runtime.

    Methods
        Functions contained inside of an object are called "methods". The
        method can be asked to perform some action, but that method can
        determine exactly what to do. By using this approach, objects can
        control their own actions.

    Programmer's Editor
        A good editing tool that understands you are writing a computer
        program, and helps you do that properly. I use Vim_ as my personal
        editor.

    Shell
    Command Prompt
        The "old fashioned" way of controlling a computer. On Windows systems,
        this involves opening a window where you can type in commands. On Mac
        and Linux systems, you open up a :program:`Terminal` program.

    Command Line 
        A simple text line on your screen where you can type in a
        :term:`command` to the operating system.
 
    Command 
        A series of space-separated text items handed to the operating system.
        The first of these items is the name of some program (which may be
        internal to the operating system) you want to run. The rest of the
        items are called :term:`parameters` which are processed by the program
        and control exactly what that program does. 


    Machine Language
    Machine Code
        The :term:`low-level` binary language a particular processor
        understands.  :term:`Machine Language` is a set of very simple
        instructions that the processor can :term:`execute`. These languages
        are designed by the processor manufacturer, and are unique to that
        processor (or processor family). Usually that manufacturer designs an
        Assembly Language to go along with their :term:`machine language`, but
        you are not required to use that language. As long as your
        :term:`assembler` generates correct :term:`machine language`, your code
        can run on that processor.

    NTP
    Network Time Protocol
    Network Time Synchronization
        Servers on the Internet with access to very accurate (usually based on
        atomic vibrations) time signals, keep track of the current time and can
        report that time to your system using a simple protocol. Most machines
        connected to the Internet can be set up to synchronize their view of
        the current time with these servers. (The software can even account for
        the time it takes for those signals to reach your machine!)


    Assembly Language
        A human readable form of :term:`machine language`. An :term:`assembler`
        converts code written in this language into :term:`machine language`.
        These languages are processor specific.

    High-Level Language 
        Most programming languages are designed to help humans instruct a
        machine in how to solve some problem. These languages do not care what
        processor they will run on, and are called `machine independent`.  You
        use a :term:`compiler` designed to convert your high-level code into
        :term:`machine language` for a particular processor. A different
        :term:`compiler` is needed for each language machine combination.

    Voltage
        A measure of the difference in electrical potential between two
        reference points.

    Current
        A measure of the movement of electrical potential across some distance

    Amperes
        TBD

    Voltage
        TBD

    Cloud
        TBD

    IDE
    Integrated Development Environment
        TBD

    Function Prototype
        TBD

    Assembler
        TBD

    Compiler
        TBD

    Parameters
        TBD

    Low-level
        TBD

    Function Prototype
        TBD

    Namespace
        TBD

    Execute
        TBD

    Script
        When you write a short program to help you manage your system, we call
        that program a "script". Popular scripting languages include Python,
        and "Bash".

    Test Driven Development
        This is a development technique where you create simple test code that
        verifies that a new feature you plan to add to your project actually
        works as required. You write this test before creating the feature,
        then add code to make that feature work and pass the test. Repeat this
        process until you are done.


..  vim:ft=rst spell:
