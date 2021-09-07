# data-capture

## Requirements
This program requires Python 3 for to work properly.

### How to Run

Run the following command. 

`python3 app.py`

Inside the program you can type `help` to get the commands.


## Commands

`add N`

where N is a positive integer from 0 to 1000

`build_stats`

DataCapture prepare your data for your queries.

`less N`

where N is a positive integer from 0 to 1000. It will return values less than N.

`greater N`

where N is a positive integer from 0 to 1000. It will return values greater than N.

`between N M`

where N and M are integers from 0 to 1000. It will return values between N and M.


#### Considerations
The class *data_capture.DataCapture* has extra methods that replicate the same functionality for the methods `less` and `greater`, but with a complexity of O(N), 
this methods are `greater_expensive`and `less_expensive`.
Also a method called `between_using_hash`, is the same that `between` but it return a intersected set() to get the proper values.
