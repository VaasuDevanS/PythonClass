# 3.2.2017 STUDENTS QUALITY COUNCIL PYTHON CLASS DAY1

'''
Python 2.7

Basics of PICOK --- > Punctuators Identifiers Constants Operators Keywords

Keywords_in_python=['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

Functions and its types were discussed. (User-defined, built-in, methods)
Introduced to lists.
Some basic operations on lists and conditionals.
Lists memory spacing was discussed.

'''

a=[1,2,3]

print "The list is..",a
print "No of elements in a is..",len(a)
print "The Sum of a is..",sum(a)
print "Min of a is..",min(a)
print "Max of a is..",max(a)
print "a is..",type(a)

b=[4,5,6]

print "After combining a and b we get..",a+b
a.append(100)
a.append(200)

print "After appending 100 and 200 a becomes..",a

c=a
print "C is Created using c=a and c is..",c
a.append(300)
print "After appending 300 a becomes..",a
print "300 is appended to a but c also gets changed..",c

print "To stop that behaviour c should be created as c=[]+a"

a.remove(300)
print "After removing 300 a is..",a

# End of Day1