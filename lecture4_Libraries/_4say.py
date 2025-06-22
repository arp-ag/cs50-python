# rough practice 4:-
# PACKAGES:
# third party libraries
# module in a folder
# pypi.org
# cowsay - cow say smtg on screen
# PIP:
# package manager
# program that allows to install packages by just running a command.
""" 
import cowsay
import sys
if  len(sys.argv)==2:
    cowsay.trex("hello, "+sys.argv[1])
 """
# calling the package 'sayings' i made

import sys # cmd line args
from _6sayings import hello
from _6sayings import goodbye
# this statemnet reads the prog top to bottom. 

if len(sys.argv)==2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])


