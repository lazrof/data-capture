The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000.

Implement this challenge in whatever programming language best highlights your skills. Also, please supply a README with details on how to setup and run your application.

Requirements:
The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.
sort
Here’s the program skeleton in Python to explain the structure:
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)

The challenge conditions:
You cannot import a library that solves it instantly
The methods add(), less(), greater(), and between() should have constant time O(1)
The method build_stats() can be at most linear O(n)