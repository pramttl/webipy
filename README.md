webipy: Automated web app generator for python code
===================================================

Python functions = Functional web endpoints

Webipy transforms the functions in your python code to a ready to use (django) web app
with each function having a unique web endpoint.


Introduction
------------

You need webipy if:

* You like writing python code
* You want to convert your python functions into web endpoints
* You either do not know, do not want to know or do not want to manually write a web app on top of your functions

Webipy helps you define all your python functions in one file i.e `myfunctions.py`.
A unique url is automatically created for each of the function defined in `myfunctions.py` file that is like:

    '/<your_function_name>/'

The url endpoint may now be used to make a call to the function using GET parameters.
GET parameters are automatically converted to respective arguments for the function.


Usage:
------

    cd webipy
    sudo pip install -r requirements.txt
    #
    # Define your functions as described in next step
    #
    python manage.py runserver
    # Your functions are automatically mapped to web endpoints at runtime.


Defining functions
------------------

Add all your python functions to `myfunctions.py`.
2 example functions are present in the file by default. Called `hello` and `add`.

The arugments to your functions are automatically turned into accetable GET parameters for the
corresponding web url. Only named arguments are supported as of now. Variable & Keyword arguments
may be used in funciton definitions but are not supported inputs to the web endpoint.

`add` function example:

    def add(a, b):
        return {'output': str(int(a)+int(b))}


Notes:

* Your function defined in `myfunctions.py` must either return a Dictionary, Tuple or List.
* If you do not want a function to have a web endpoint add an `_` (underscore) prefix to the function name.


Web endpoints
-------------

The reason behind only allowing dictionary, tuples or lists as valid function return type is
because **webipy** serializes the function output in JSON format and return it as a valid Http Response.
For any other return type the serialization might fail.

Example of web endpoint:

Run python manage.py runserver in root directory of webipy if you havent,
and open the following in your web browser.

    http://localhost:8080/add/?a=1&b=2

You will see the following output (JSON:

    {"output": "3"}

Notice: output is sum of `1` and `2` i.e. `3`. Also notice how function definition which was
called `add` automatically translated to a web endpoint `/add`, which makes it easy to
mentally associate the webendpoints with your python functions.


Suggestions
-----------
Webipy is a small project and your suggestions are required to make it solve a bigger problem
which developers who do not like web programming face.

* What features do you think are definitely needed in a project like this?
* Do you notice any bugs?
* Do you want to contribute?

Email me with suggestions at: mittalp@onid.oregonstate.edu
