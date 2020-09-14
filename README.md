# cliflags
CLI command flags management using JSON input description

I find that I often write scripts that need "externalized" changes.
By this I mean I have some base script that works fine for many
situations but then someone on my team wants an extention.
That extention usually requires the addition of new CLI arguments of
various forms.

What I wanted was to address the following use cases:

1) one source of "truth" for the collection of arguments for a program
2) one source to edit/add argurments
3) extensible arguement management

Pretty simple I wanted XML or JSON based argument descriptions which can
then be built recursively from bottom to top.

The idea is in the program directory you would have a base level
description of your program arguments.  This file can be hierarchical
using an include directive.  When the program arguments need to be
extended or overwritten from this base level you would then write the
addition and include the base.

The hierarchy of files would be read:

bottom
next
next
next
...
top

any common sections between bottom -> top would always retain the
highest level.

All of this requires a "meta" language and/or schema to manage and check
that the input JSON/XML conforms to the base requirements of the reader.

Python's basic JSON utilities has the ability to read JSON and verify
vs. a schema but lacks an object model.  Because of this the code uses a
PyPi library called python-jsonschema-objects.
Please note this library is Beta so realize there maybe issues with this
code and the object library from a production software standpoint.

Note:
I have not had time to hack on this code so it is in a bad state.
When I get a chance to clean it up I will remove this note and add
information on its status that reflects how usable this code is.


Issues:
this code is written as Python 3
It uses a factory pattern using RTTI / Reflection to auto register
Argument types.
You can do the same thing in Python 2 but the syntax has changed quite a
bit.
If you are interested you can research Python meta class and python
reflection.
