#    0    )
# 8.2.2017(Wed) STUDENTS QUALITY COUNCIL PYTHON CLASS DAY2

'''
     Previous Class1 summary.
     
     Open Source
     History of Python
     
     a=[1,2,3]
     length, min, max, a.append(), len, range, sum, a.remove(), Memory Sharing
     

'''

'''
    
    print statement, input, raw_input
    Strings
    Numbers
    Conditionals
    Lists-Tuples
    for implemetation in lists and tuples
    
'''
# Print Statement
print "this is a string.."                               #this is a string..
print "This number 879 is also a string"                 #This number 879 is also a string
print "We can print in the","same line also"             #We can print in the same line also

#input and raw_input
num=input("Enter the number..")                          #Enter the numner..12        num=12
string=raw_input("Enter the string..")                   #Enter the string..vaasu     string=vaasu

#strings
a="python is fun"
print a.upper()                                                #PYTHON IS FUN
print a.lower()                                                #python is fun
print a.capitalize()                                           #Python is fun
print a.count('n')                                             #2
print a.replace("python","c/c++")                              #c/c++ is fun

#numbers
a=10
print a+2                                                      #12
print a-2                                                      #8
print a*2                                                      #20
print a/2                                                      #5
print a%2                                                      #0
print float(a)/2                                               #5.0

#Conditionals
if True:
     print "something"
else:
     print "nothing"                                     #something
     
num=10
if num==20:
     print "num1"
elif num==30:
     print "num2"
else:
     print "num3"                                       #num3
     
#Lists
a=[1,2,3]
print a                                                 #[1,2,3]
a.append(4)
print a                                                 #[1,2,3,4]
print len(a)                                            #4                             
print max(a)                                            #4
print min(a)                                            #1
print sorted(a)                                         #[1,2,3,4]

#for implementation in lists (same output for both examples)
a=[10,20,30]
for i in a:
     print i                                           #10
                                                       #20
for i in a:print i                                     #30
