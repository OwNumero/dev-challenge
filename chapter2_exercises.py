# Exercises for chapter 2:

# Name: 10 day Dev Challenge
# by OwNumero
# 
print "Exercice 2.1:"

print "When the number entered starts with a zero, Python interprets it as a number base 8 # using numbers 0 through 7"
print "for instance..."
print "0 is 0"
print "01 is 1"
print "04 is 4"
print "07 is 7"
print "010 is 8"
print "011 is 9"
print "note that 08, 09 don't exist because they use numbers after 7, which is the highest in base 8"

print "Exercise 2.2"

print "Here is the script for the sequence"
5
x = 5
x + 1
print "the output is 6"

print "script to print each expression"
x = 5
print x
print x + 1

print "Exercise 2.3"

width = 17
height = 12.0
delimiter = ' . '
print "1. width/2 is an 'int' - integer, value below"
width/2
print "2. width/2.0 is a 'float', value below"
width/2.0
print "3. height/3 is a 'float', value below"
height/3
print "4. 1 + 2 * 5 is an 'int' - integer, value below"
1 + 2 * 5
print "4. delimiter * 5 is an 'str' - string, value below"
delimiter * 5

print "Exercise 2.4"
 
print "1."
r=5
pi=3.14159
r**3*pi*4/3

print "2."
bp=24.95
d=0.6
sh1=3
shs=0.75
nbr=6
print bp*d+sh1+(nbr-1)*shs

print "3."
dtime=6*60+52.0
dist1=1.0
speed1=(8+15/60)
dist2=3.0
speed2=(7+12/60)
atime=(dtime+dist1*speed1+dist2*speed2)/60
hours=int(atime)
minutes=int((atime-int(atime))*60)
seconds=int(((atime-int(atime))*60-int((atime-int(atime))*60))*60)
print "Arrival time is " 
print hours 
print "hours"
print minutes
print "minutes"
print seconds
print "seconds"
