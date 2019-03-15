"""A module showing the usage of basic functions."""


# Function in python look like this:
# def name_of_function(parameters)
def some_function():
    """A basic function."""

    print('do some stuff')


# Function can be called just like this:
some_function()

# In python you can provide a function required parameters and optional parameters with a default value
# Required parameters:
def required(name):
    """Name is required."""
    print(name)

required('Arne')


# Optional parameters:
def not_required(name='rofl', nickname='copter'):
    """Name is not required."""
    print('Not required')
    print(name)
    print(nickname)

# We only provide the second one, theoretically we wouldn't need to specify any parameter
not_required(nickname='nuke')


# Mixed parameters:
def mixed(name, nickname='copter'):
    """Name is required."""
    print(name)
    print(nickname)

mixed('Arne', nickname='Nuke')


# FYI:
# required parameters are called `args` (Arguments)
# optional parameters are called `kwargs` (Keyword Arguments), because you need to specify the name of the variable (keyword)
