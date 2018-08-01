## Expected behavior.

When I instantiate a `Foo` and call its `frob` method, rainbows appear and a unicorns `DataFrame` is
returned.


## Observed behavior.

    foo = Foo(...)   # Instantiates a Foo.
    df = foo.frob()  # No rainbows. SAD!
    type(df)         # int type, WTF?!


## Steps to reproduce.

  * Machine: Mac laptop (or EC2 machine, ...).
  * Python: 3.1415926
  * Analytics Tools commit: fa1afe1
