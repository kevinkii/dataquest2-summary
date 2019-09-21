#%% [markdown]
# # Python for Data Science: Intermediate

#%% [markdown]
# ## Transforming and Cleaning Strings
# `len()` function will return the number of row in a list

#%%
# Replace a substring within a string
green_ball = "red ball".replace("red", "green")
print(green_ball)

#%%
# Remove a substring:
friend_remove = "hello there friend!".replace("friend","")
print(friend_remove)

#%%
# Remove a series of characters from a string
bad_chars = ["'", ",", ".", "!"]
string = "We'll remove apostrophes, commas, period, and exclamation marks!"
for char in bad_chars:
    string = string.replace(char, "")
print(string)

#%%
# Remove multiple characters from a string
data = ['(1947)', '(1948)','(1949)','(1950)','(1951)','(1952)','(1953)','(1954)']

#%%
# First Way
def clean_and_convert(date):
    for n in date:
        clean_open = n.replace("(","")
        clean_both = clean_open.replace(")","")
        clean_both = int(clean_both) #convert into integer
        print(clean_both)
clean_and_convert(data) # return as an integer

#%%
# Second Way
bad_chars = ["(", ")"]
def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char, "")
        return(string)
stripped_test_data = []
for char in data:
    char = strip_characters(char)
    stripped_test_data.append(char)
print(stripped_test_data) # return as a list

#%%
# Concert a string to title case
Hello = "hello".title()
print(Hello)

#%%
# Check a string for the existence of a substring
if "car" in "carpet":
    print("The substring was found.")
else:
    print("The substring was not found.")

#%%
# Split a string into a list of strings
split_on_dash = "1980-12-08".split("-")
print(split_on_dash)

#%%
# Slice characters from a string by position:
last_five_chars = "This a long string."[-5:]
print(last_five_chars)

#%%
# Concatenate strings
superman = "Clark" + " " + "Kent"
print(superman)

#%% [markdown]
# ## String Formatting and Format Specifications
# The `str.format()` method allows you to insert values into strings without explicitly converting them
#
# The `str.format()` method also accepts optional format specification, which you can use to format vlaues so they are eaiser to read.

#%%
# Insert values into a string in order
continents = "France is in {} and china is in {}".format("Europe", "Asia")
print(continents)

#%%
# Insert values into a string by position
squares = "{0} times {0} equals {1}".format(3,9)
print(squares)

#%%
# Insert values into a string by name
population = "{name}'s population is {pop} million".format(name = "Brazil", pop = 209)
print(population)

#%%
# Format specification for precision of two decimal places
two_decimal_places = "I own {:.2f}% of the company".format(32.3455452342343)
print(two_decimal_places)

#%%
# Format specification of comma separator
india_pop = "The approximate population of {} is {}".format("India", 1324000000)
print(india_pop)

#%%
# Order for format specification when using precision and comma separator
balance_string = "Your bank balance is {:,.2f}".format(12345.678)
print(balance_string)

#%%
balance_string = "Your bank balance is {bal:,.2f}".format(bal=12345.6789)
print(balance_string)

# `bal` indicates the name of the variable to insert
# `:` indicates start of the format spec
# `,` indicates the comma thousands separator
# `.2f` indicates precision of two decimal places

#%%
# String as number
s = "0123456789"
s[2]

#%%
s[1:4]

#%%
# Creating a frequency table
frequency = {}
for row in data:
    if row not in frequency:
        frequency[row] = 1
    else:
        frequency[row] += 1

#%% [markdown]
# ## Object-Oriented Python
# In **Object-Oriented Programming**, the fundamental building blocks are objects.
# * It differs from **Procedural** programming, where sequential steps are executed.
#
#
# An **Object** in an entity that stores data.
#
# A **Class** describes an object's type. It defines:
# * What data is stored in the object, known as attributes.
# * What actions the object can do, known as methods.
#
#
# An **attribute** is a variable that belongs to an instane of a class.
#
# An **method** is a function that belongs to an instance of a class.
#
# Attributes and methods are accessed using **dot notation**. Attributes does not use parentheses, whereas methods do.
#
# An **instance** describes a specific example of a class. For instance, in the code `x = 3`, `x` is an instance of the type `int`.
# * When an object is created, it is known as **instantiation**.
#
#
# A **class definition** is code that defines how a class behaves, including all methods and attributes.
#
# The init method is a special method that runs at the moment an object is instantiated.
# * The init method(`__init__()`) is one of a number of special methods that Python defines.
#
#
# All methods must include `self`, representing the object instance, as their first parameter.
#
# It is convention to start the name of any attributes or methods that aren't intended for external use with an undersocre.

#%%
# Define an empty class
class MyClass():
    pass

#%%
# Instantiate an object of a class
class MyClass1():
    pass
mc_1 = MyClass1()

#%%
# Define an init function in a class to assign an attribute at instantiation
class MyClass2():
    def __init__(self, param_1):
        self.attribute_1 = param_1
mc_2 = MyClass2("arg_1")

#%%
# Define a method inside a class and call it on an instantiated object
class MyClass3():
    def __init__(self,param_1):
        self.attribute_1 = param_1
    def add_20(self):
        self.attribute_1 += 20
mc_3 = MyClass3(10) # mc_3.attribute is 10
mc_3.add_20() # mc_3.attribute is 30

#%%
class NewList1():
    def first_method(self):
        return "This is my first method"
newlist1 = NewList1()
result1 = newlist1.first_method()
result1

#%%
class NewList2():
    def return_list(self, string):
        return(string)
newlist2 = NewList2()
result2 = newlist2.return_list([1,2,3])
result2 # return as list

#%%
class Newlist3():
    def __init__ (self, initial_state):
        self.data = initial_state
    def append(self, new_item):
        self.data = self.data + [new_item]
my_list = Newlist3([1,2,3,4,5])
print(my_list.data)

my_list.append(6)
print(my_list.data)

#%% [markdown]
# ## Importing Modules and Definitions
# The datetime module contans the following classes:
# * `datetime.datetime`: For working with date and time data.
# * `datetime.time`: For working with time data only.
# * `datetime.timedelta`: For representing time periods.
#
#
# Time objects behave simiarly to datetime objects for the following reasons:
# * They have attributes like `time.hour` and `time.second` that you can use to access individual time components.
# * They have a `time.strftime()` method, which you can use to create a formatted string representation of the object.
#
#
# The timedelta type represents a period of time, e.g. 30 minutes or two days.

#%% [markdown]
# ### Common format codes when wokring with `datetime.datetime.strptime`
#
# | **Strftime Code** | **Meaning** | **Examples** |
# | --- | --- | --- |
# | `%d` |Day of the month as a zero-padded number| `04` |
# | `%A` |Day of the week as a word| `Monday` |
# | `%m` |Month as a zero-padded number| `09` |
# | `%Y` |Year as a four-digit number| `1901` |
# | `%y` |Year as a two-digit number with zero-padding| `01` (2001)<br>`88` (1988) |
# | `%B` | Month as a word | `September` |
# | `%H` | Hour in 24 hour time as zero-padded number | `05` (5 a.m.)<br>`15` (3 p.m.) |
# | `%p` | a.m. or p.m. | `AM` |
# | `%I` | Hour in 12 hour time as zero-padded number | `05` (5 a.m. or 5 p.m. if `AM`/`PM` indicates otherwise)
# | `%M` | Minute as a zero-padded number | `07` |

#%% [markdown]
# ## Operations between timedelta, datetime, and time objects (datetime can be substituted with time):
#
# | **Operation** | **Explanation** | **Resultant Type** |
# | --- | --- | --- |
# | `datetime - datetime` | Calculate the time between two specific dates/times | timedelta |
# | `datetime - timedelta` | Substract a time period from a date or time | datetime |
# | `datetime + timedelta` | Add a time period to a date or time | datetime
# | `timedelta + timedelta` | Add two periods of time together | timedelta |
# | `timedelta - timedelta` | Calulate the difference betwen two time periods | timedelta |

#%%
import datetime as dt
# Creating datetime.datetime string given a month, year, and day
ibm_founded = dt.datetime(1911,6,16)
print(ibm_founded)

#%%
# Creating datetime.datetime string give a month, year, day, hour, and minute
man_on_moon = dt.datetime(1969,7,20,20,17)
print(man_on_moon)

#%%
# Creating a datetime.datetime object from a string
# datetime.strptime(date_string, format)
date_1_str = "12/24/2019"
date_1_dt = dt.datetime.strptime(date_1_str, "%m/%d/%Y")
print(date_1_dt)

#%%
# Converting a datetime.datetime format from a string
# datetime.strftime(format)
dt_object = dt.datetime(1984, 12, 24)
dt_string = dt_object.strftime("%d/%m/%Y")
print(dt_string)

#%%
# Instantiating a datetime.time object
eg_1 = dt.time(hour = 8, minute = 0, second = 5, microsecond = 0)
print(eg_1)

#%%
# Creating a date and a time from a datetime.datetime object
d1 = dt.datetime(1846, 9, 10, 12, 30)
d1_date = d1.date()
d1_time = d1.time()
print(d1_date)
print(d1_time)

#%%
# Instantiating a datetime.timedelta object
eg_3 = dt.timedelta(weeks=3)
print(eg_3)

#%%
# Adding a time period to a datetime.datetime object
d3 = dt.date(1963, 2, 26)
d3_plus_1wk = d3 + dt.timedelta(weeks=1)
print(d3_plus_1wk)

#%%
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(days=56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)
answer_4 = dt_2 + dt.timedelta(hours=56)

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)