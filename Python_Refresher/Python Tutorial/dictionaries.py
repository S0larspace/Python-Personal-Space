'''Experimental space for learning dictionaries'''

students = {}  # squiggly brackets for dictionary
# the keys here are the student names in string.
students = {"Alice": 22, "Ben": 24, "Charles": 20}

# students.key gives a dict_key item with all the keys
# dict_key does not support indexing, meaning you cannot extricate a particular key using command students.keys()[index]
# Instead, convert the keys into a list then you can extricate, assign to a variable, then extricate the interested key
# a = list(students.keys()) ===> a[0] = interested key

# the same applies to the values
