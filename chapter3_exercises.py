# Exercises for chapter 3:

# Name: OwNumero
#
# Exercise 3.1 
# 
# When repeat_lyrics() appears before
# it's defined, we get 
# 'NameError: name 'repeat_lyrics' is not defined
# 
# Exercise 3.2
# 
# When the definition of function is
# not in a progressive order, the program
# still runs properly
# 
# Exercise 3.3
# 
# one_space=' '
# def right_justify(string):
# 	print one_space*(70-len(string))+string
# 
# Exercise 3.4
# 
# 1.
# 
# def do_twice(f):
# f()
# f()
# def print_spam():
# 	print 'spam'
# do_twice(print_spam)
# 
# 2.
# 
# def do_twice(f, x):
#	f(x)
#	f(x)
# 
# 3.
# 
# def print_twice(x):
# 	print x
#	print x
#
# 4.
# 
# do_twice(print_twice,'spam')
# spam
# spam
# spam
# spam
# 
# 5.
# 
# def do_four(f, x):
# 	do_twice(f, x)
# 	do_twice(f, x)
# 
# do_four(print_twice, 'spam')
# spam
# spam
# spam
# spam
# spam
# spam
# spam
# spam