webipy: Transforming python functions to web endpoints
======================================================

You need webipy if:

* You like writing python code
* You want to convert your python functions into web endpoints
* You either do not know, do not want to know or do not want to write a web app on top of your functions

Introduction
------------

Webipy helps you define all your python functions in one file i.e `myfunctions.py`.
A unique url is automatically created for each of the function defined in `myfunctions.py` file that is like:

    '/<your_function_name>/'

The url endpoint may now be used to make a call to the function using GET parameters.
GET parameters are automatically converted to respective arguments for the function.


Usage:
------

    mv webipy <any_project_name>
    pip install -r requirements.txt
    # Define your functions as described in next step

    python manage.py runserver
    # Your functions are automatically mapped to web endpoints at runtime.


Defining functions
------------------

Add all your python functions to `myfunctions.py`.
2 example functions are present in the file by default. Called `hello` and `add`.

The arugments to your functions are automatically turned into GET parameters for the
corresponding web url. Named arugments are only supported as of now.

Variable & Keyword arguments may be used in funciton definitions but are not supported
inputs to the web endpoint.

`add` function example:

    def add(a, b):
        return {'output': str(int(a)+int(b))}


Note: Your function defined in `myfunctions.py` must either return a Dictionary, Tuple or List.


Web endpoints
-------------

The reason behind only allowing dictionary, tuples or lists as valid function return type is
because **webipy** will simply be serialize the function output in JSON format and return it
as a valid Http Response. For any other return type the serialization might fail.

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
Webipy is a small project and your suggestions are required to make it solve a bigger purpose.

* What features do you think are definitely needed in a project like this?
* Do you notice any bugs?

Email me with suggests at: mittalp@onid.oregonstate.edu
