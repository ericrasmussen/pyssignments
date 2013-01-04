Git Clone
=========
Instructions forthcoming.


Virtual Environment
===================
Install virtualenv if you don't already have it. More information here:
   http://pypi.python.org/pypi/virtualenv

Once installed, change to your <repo> folder and run:

   $ virtualenv .
   $ source bin/activate
   $ python setup.py develop

Now you can run the python and nosetests commands in an isolated environment
that won't affect the system level commands.


Running Tests
=============
After you activate your virtual environment (see above), navigate to
<repo>/pyssignments/ and run:

    $ nosetests assignment<number>

You should see output showing failed tests and tracebacks with details. You can
use that information to update the code. Keep re-running the tests as you make
changes to the code.




