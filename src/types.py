"""Module for showing basic types in python."""


# Lets start with the most basic types:

bool_variable = True
bool_variable = False
string_variable = 'Some string'
string_variable = "Some string"  # Strings can be either with ' or with ", but we prefer to use '
int_variable = 42
# Everything that has a decimal place becomes a float
# If one for instance divides a normal int (e.g. 10/8) it will become a float automatically
# You really don't need to worry about this stuff
float_variable = 42.2


# Now one gets the the more interesting types


""" The List:

The python list is a very simple array you can add or remove items from.
"""
# A very basic python list:
some_strings = ['a', 'b', 'c']

# But a python list can contain any type and can also mix types as well:
mixed_stuff = [1, 'a', 42.5, 'roflcopter']

# A specific entry of a list is accessed with this syntax:
print(some_strings[0])  # This returns the first entry `a` of the list
print(some_strings[1])  # This returns 'b' and so on.

# You can add items into the list with this:
some_strings.append('new item')
# It will be appended to the end of the list. Thereby it would look like this:
# ['a', 'b', 'c', 'new item']

some_strings.pop()  # This removes the last item of the list (in our case 'new_item').
# python lists are somewhat like stacks, but they offer additional functions which allow to use them like normal lists


""" The Dictionary (or Map/Hashmap) :

The dictionary (dict) is a very handy structure if you want to map a key to a specific value.

They always have the following pattern:
{
    key: value,
    key2: value2,
}

For instance if one wants to know the zipcode for a specific name.
"""

zipcodes_by_name = {
    'Kevin Spacko': 22529,
    'Derp Herp': 22527,
}

# If one wants to know the zipcode of Derp Herp, one can just do the following:
zipcode = zipcodes_by_name['Derp Herp']
print(zipcode)  # This will print 22527


# The key of a dictionary can be pretty much everything (not important for now), while the value of a dictionary can be everything.

some_variable = 'hehehehehe'
some_other_variable = 'hohohohoho'
a_mixed_dictionary = {
    1: 'test',  # An integer key that points to a string
    'rofl': 'test',  # An string that points to a string
    'answer': 42,  # You get the idea
    some_variable: some_other_variable,  # Migth be confusing at first, but this is just the exact same thing as the next line:
    # 'hehehehehe': 'hohohohoho',  # Same as above
}

print(a_mixed_dictionary['hehehehehe'])


# You can also add or overwrite variables of an existing dict by doing this:
a_mixed_dictionary[1] = 'overwriting an existing key'
a_mixed_dictionary['new_key'] = 'new_value'
