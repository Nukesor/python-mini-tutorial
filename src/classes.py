"""A module showing the basic syntax of creating classes."""


class NormalUser():
    """A basic python class.

    Class names are CamelCased.
    """

    # Two static variables of TestClass. they are accessed with e.g. `TestClass.variable_1`
    variable_1 = 'omfg'
    variable_2 = 2152

    def __init__(self, nickname, age):
        """The constructor of NormalUser.

        Everytime a new instance is declared with e.g.:


        `user = NormalUser(50, 60)`


        this function is called and the parameters are provided to the function.
        All member functions of a class get the current instance as the first parameter,
        which is usually named `self`.
        `self` can then be used to instanciate all members of the function.
        """
        self.nickname = nickname
        self.age = age

    def add_to_age(self, number):
        """A class member function, which adds some number to the age.
        
        It's used like this:

        user = NormalUser('roflcopter', 25)
        user.add_to_age(5)
        print(user.age)
        --> 30
        """
        # The following line is the same as:
        # self.age = self.age + number
        self.age += number


class AdminUser(NormalUser):
    """This class is inherited from NormalUser.

    This class inherits all functions and members of the parent NormalUser.
    (Multiple) Inheritance should normally be avoided, but sometimes it's just too handy.
    """

    def __init__(self, nickname, age):
        """Call the constructor of AdminUser."""
        # Call the parent constructor (Ugly syntax, but useful)
        # You hopefully won't need inheritance anyway, but it's nice to know
        super(AdminUser, self).__init__(nickname, age)

        # Set an additional variable
        self.is_admin = True
