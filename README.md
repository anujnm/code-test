# code-test
## Overview

This project demonstrates how a REST API can be used to extract reports and
other useful data.

The constructor of BenchApp makes a set of API requests to the server, extracts
all the data, and stores it as a list of Transaction objects in
all_transactions.

The constructor then calls __process_data to store the data in various formats.
This redundancy is to reduce runtime when the data is requested from the app.

Note that the data is de-duped and cleaned in __process_data. The de-duping is
done by checking all the parameters of each transaction object.


## Setup

The required python packages can be found in requirements.txt. This can be done
using pip as follows:
<pre><code>pip install -r requirements.txt</pre></code>

Once the packages have been installed, run the install command using setup.py as
follows:
<pre><code>python setup.py install</pre></code>

You may test the installation using setup.py as follows:
<pre><code>python setup.py test</pre></code>

## Using the CLI

To run BenchApp, use the following format of commands:

<pre><code>python benchApp.py {command-name} {command-arg}</pre></code>

A list of all available commands can be found in the documentation (below). The
{command-arg} here refers to either a date (for balances), or a category.

Category names have been generated from the ledger entries. Examples include
'Travel Expense, Nonlocal', and 'Equipment Expense'. If you wish to get data
that is unfiltered by category, you can use the 'All' parameter. Note that
category names are case-sensitive.

Example:

<pre><code>python benchApp.py total 'Business Meals & Entertainment Expense'</pre></code>

OR

<pre><code>python benchApp.py total</pre></code>


## Docs:

Docs have been generated using Sphinx, and are located in
./docs/_build/html/index.html


## Tests:

I've also included a few basic test cases. Note that these tests are hardcoded
to check against live data. Normally this would not be acceptable, and I would
instead provide each test with its own disposable data, however I felt that this
was beyond the scope of the project.

To run the tests, run this command from within the tests folder:

<pre><code>python setup.py test</pre></code>

OR

<pre><code>python -m unittest testBench</pre></code>
