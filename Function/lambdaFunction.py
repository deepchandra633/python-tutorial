# What is a Lambda Function?

# A lambda function is a small anonymous function in Python.

# Anonymous means:

# Function without a name.

# Used for:

#1. Short operations
#2. One-line functions
#3. Quick calculations

# syntax---->  lambda arguments : expression

# lambda--->Keyword used to create lambda function.
# arguments--->Input values.Input values.
# : ----> Separates arguments and expression.
# expression---> Operation to perform.

# normal function:

# def square(x):

#     return x * x

# print(square(5))

# lambda function

# square = lambda x: x * x

# print(square(5))


# Example 1: Add Two Numbers

# add = lambda a, b: a + b

# print(add(10, 20))


# Example 2: Even or Odd

# check = lambda n: "Even" if n % 2 == 0 else "Odd"
# print(check(7))

# Example 3: Largest Number

# largest = lambda a, b: a if a > b else b

# print(largest(10, 20))
# Lambda with No Arguments

# greet = lambda : "Hello"
# print(greet())



# Difference Between Normal Function and Lambda Function
# Normal Function        	Lambda Function
# Uses def	                    Uses lambda
# Multiple lines possible    	Single expression only
# Has function                   name	Anonymous
# Uses return	                    Automatic return



# Lambda with filter()
# filter()

# Applies function to all elements.

# Example

# numbers = [1, 2, 3, 4]
# result = list(filter(lambda x: x * 2, numbers))
# print(result)



# Lambda with filter()
# filter()

# Filters elements based on condition.

# Example

# numbers = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)

# sort a list of string based on their lenght

# list= ["Deep","Bhavna","Kushwah","Deepchandra"]
# result=sorted(list,key=lambda x:len(x))

# result=sorted(list,key=lambda x:len(x),reverse=True)
# # result=sorted(list)

# print(result)
