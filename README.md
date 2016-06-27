# code-test
## Overview

This project demonstrates how a REST API can be used to extract reports and
other useful data.

The constructor of BenchApp makes a set of API requests to the server, extracts
all the data, and stores it as a list of Transaction objects in
all_transactions.

The constructor then calls __process_data to store the data in various formats.
Ideally this data would then be cached/stored in the app for quick retrieval.
However, this is beyond the scope of the current requirements.

Note that the data is de-duped and cleaned in __process_data. The de-duping is
done by checking all the parameters within each transaction object.


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

Here is the list of the available CLI commands:

total {category-name}

transactions {category-name}

balance {date}

The category names have been generated from ledger entries. Examples include
'Travel Expense, Nonlocal', and 'Equipment Expense'. Note that these category
names are case-sensitive

All the above commands can also be used with the category 'All' so that data
can be returned without category-based filtering.

Example:

<pre><code>python benchApp.py total 'Business Meals & Entertainment Expense'</pre></code>

OR

<pre><code>python benchApp.py total</pre></code>


## Docs:

I've also generated docs from the functions using Sphinx, so that the code can
be used as a packaged library. They can be found at:
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
