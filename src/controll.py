"""A Module showing some basic controll structures in python."""


"""The most basic controll structure: If elseif else."""

something_false = False
something_true = True

if something_false:
    print('nope')
elif something_true:
    print('rofl')
else:
    print("we wont't get here")


# Or something simpler

if False:
    print('nope')
else:
    print('yep')


# Or even simpler

if False:
    print('nope')


"""Then there are for-loops.

There are two basic examples of for loops you should know.
"""

# For loops for normal lists
some_list = ['I', 'am', 'not', 'stupid']
for string in some_list:
    print(string)


some_dictionary = {
    'name': 'Rofl',
    'nickname': 'Copter',
}
for key, value in some_dictionary.items():  # The .items() call can be confusing, but it's needed to make this work
    print(key, value)


"""And of course the while loop."""

# This will increment the counter until it reaches 2
counter = 0
while counter < 2:
    counter += 1
    print(counter)
