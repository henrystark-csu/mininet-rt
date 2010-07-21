import sys

def printhelp():
  print """Usage (as root): python %s [opts]
  opts:

    -n number:  Number of hosts, default 10
    -t time  :  Amount of time to run, default 10
    -r rate  :  Shape links to constant rate, default 100mbit
    -o file  :  Output from tests get written to file
                default: results-$n-$t.html
    -d       :  Start the hosts, configure the network and exit
    -p       :  Just print the commands (a dry-run)
    -h       :  Print this help
"""
