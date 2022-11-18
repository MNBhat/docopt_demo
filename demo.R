# author: Tiffany Timbers
# date: 2020-01-15

"This script prints out docopt args.
Usage: demo.R <arg1> [<arg4>] --arg2=<arg2> [--arg3=<arg3>]
Options:
<arg1>            Takes any value (this is a required positional argument)
[<arg4>]          Takes any value (this is a optional required arg)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
" -> doc

library(docopt)
opt <- docopt(doc)

# +
# define main function
main <- function(){
    # code for "print" of script goes here
    
    print(opt)
    print(typeof(opt))
}



# call main function
main()
