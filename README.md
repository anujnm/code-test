# code-test
REST API code test

This project demonstrates how a REST API can be used to extract reports and
other useful data.

The constructor of BenchApp makes a set of API requests to the server, extracts
all the data, and stores it as a list of Transaction objects in
all_transactions.

The constructor then calls __process_data to store the data in various formats.
This redundancy is to reduce runtime when the data is requested from the app.

Note that the data is de-duped and cleaned in __process_data. The de-duping is
done by checking all the parameters of each transaction object.

BenchApp contains 6 public functions, all of which are documented with
python docstrings.

I've also included a few basic test cases. Note that these tests are hardcoded
to check against live data. Normally this would not be acceptable, and I would
instead provide each test with its own disposable data, however I felt that this
was beyond the scope of the project.