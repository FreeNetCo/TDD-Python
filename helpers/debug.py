from pprint import pprint as pp
from time import sleep

##
# This module is a WIP. It is meant to include several
# helpful functions to ease debugging.
#
# TODO: Include an equivalent to PHP's dd() function,
# write custom functions to ease the use of inspect.getmembers()
# for common debugging tasks, etc.
##

def pause(var, delay=15):
	sleep(delay)
	return var

"""
" dp(var, delay)
" Dump and Pause: Dump all var content to STDOUT
" and pause for the specified time before proceeding
" with the code execution.
"""
def dp(var, delay=15):
	print('\npp out:\n')
	content = pp(var)
	return pause(content, delay)

"""
" dd(var)
" Dump and Die: Dump all var content to STDOUT
" and quit code execution.
"""
def dd(var, delay=15):
	pass
