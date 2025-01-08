print("Hello, World!")
print((9-3)/(2*(1+2)))
print(12/(1+2)+2**2)


# Variables: Represent data stored as strings, tuples, dictionaries, lists, and objects (note: future readings explain these categories)

# Keywords: Special words that are reserved for specific purposes and that can only be used for those purposes

# Python syntax includes words that represent objects and commands, as well as punctuation that gives the words structure, hierarchy, and context. 
# Together, the words and punctuation communicate ideas and processes; this is known as semantics. Semantics is the meaning conveyed by the syntax. 
# The best way to learn syntax and semantics is through exposure. Practice coding and become familiar and comfortable with reading other people’s code. 
# In addition, there are some general conventions that practitioners use to help maintain stylistic uniformity within the language. 

#Variables: Represent data stored as strings, tuples, dictionaries, lists, and objects (note: future readings explain these categories)

#Keywords: Special words that are reserved for specific purposes and that can only be used for those purposes

in
not
or
for
while
return

#Operators: Symbols that perform operations on objects and values

+
- 
* 
/ 
** 
% 
// 
> 
< 
==

# Expressions: A combination of numbers, symbols, and variables to compute and return a result upon evaluation

# Functions: A group of related statements to perform a task and return a value

def to_celsius(x):
   '''Convert Fahrenheit to Celsius'''
   return (x-32) * 5/9


to_celsius(75)

# Conditional statements: Sections of code that direct program execution based on specified conditions
number = -4


if number > 0:
   print('Number is positive.')
elif number == 0:
   print('Number is zero.')
else:
   print('Number is negative.')


