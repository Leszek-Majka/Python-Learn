fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
type(result)
print(result)  #typ Tuple - niezmienna lista

hours, minutes, seconds = result
print(hours, minutes, seconds) #rozpakowanie typu Tuple, przypisanie wartości do pojedyńczych zmiennych
print(hours)

hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)


animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
print(enumerate(winners))
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))


def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))




def skip_elements(elements):
    # Inicjalizacja listy wynikowej przed pętlą
    result = []
    
    # Iteracja po indeksach i elementach
    for index, element in enumerate(elements):
        if index % 2 == 0:  # Sprawdzenie, czy indeks jest parzysty
            result.append(element)  # Dodanie elementu do wynikowej listy
    
    return result

# Testowanie funkcji
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Powinno być ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Powinno być ['Orange', 'Strawberry', 'Peach']


multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

multiples = [x*7 for x in range(1,11)]
print(multiples)


languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)


z = [x for x in range(0,101) if x % 3 == 0]
print(z)


### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)

# Select Run to compare the two results.




print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])

# The list comprehension above accomplishes the same result as
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

# Select Run to observe the two results.


def squares(start, end):
    # Generowanie kwadratów liczb w zakresie [start, end]
    return [n * n for n in range(start, end + 1)]

# Testowanie funkcji
print(squares(2, 3))    # Powinno wypisać [4, 9]
print(squares(1, 5))    # Powinno wypisać [1, 4, 9, 16, 25]
print(squares(0, 10))   # Powinno wypisać [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple, 
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)

# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])








filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename.replace("hpp", "h"))
    else:
        new_filenames.append(filename)


print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = [ filename.replace("hpp", "h") if filename.endswith("hpp") else filename for filename in filenames]  # Start your code here


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]




def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    letter=word[0]

    word=word[1:]
    # Turn the list back into a phrase
    say+=word+letter+"ay "
  return say
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for person in people:


        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession"   
        name, age, profession = person


        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}.".format(name, age, profession))




# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])


# Click Run to submit code


# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer