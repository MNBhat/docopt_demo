# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> [<arg4>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg1>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]          Takes any value (this is an optional positional option)
""" 

from docopt import docopt
opt = docopt(__doc__)


# +
# define main function
def main():
    # code for "print" of script goes here

    print(opt)
    print(type(opt))

# call main function
if __name__ == "__main__":
    main()
