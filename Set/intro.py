# nums={1,2,3,4,5}
# print(type(nums))

# num={1,2,2,3,4,4,5,"deep","bhavna","deep",None,True,2.4,2.4}
# print(num)
# print(type(num))
# print(len(num))

# empty set

# empty_set={}  #  this is not a set this is dictionary
# empty_set=set()
# print(type(empty_set))


# methodes

# collection=set()
# print("After add methode")
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(2)
# collection.add(4)
# collection.add(5)
# collection.add(6)
# collection.add(5)
# print(collection)

# print("After remove methode")  # gives error if element not found
# collection.remove(1)
# collection.remove(10)  # gives error
# collection.discard(6)
# print(collection)

# print("After clear methode")
# collection.clear()
# print(collection)

# print("After pop methode")
# print(collection.pop())
# print(collection)

# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8,9}
# print("Afetr union methode")
# print(s1.union(s2))     #union or  | 
# s3=s1|s2
# print(s3)
# print("Afetr intersection methode")
# print(s1.intersection(s2))    # intersection or & 
# s3=s1 & s2
# print(s3)

# print("Afetr update methode")
# collection.update([1,2,3,4,5,6,7,8,9,1,23,1,2,3,4])

# collection.add([10,20,30])  # not possible
# print(collection)

# diffrence() or -

# a = {1, 2, 3,4}
# b = {2, 3, 4}

# print(a - b)

#symmetric differnce(^)

# a = {1, 2, 3,4}
# b = {3, 4, 5}

# print(a ^ b)


# subset and supreset

# a = {1, 2}
# b = {1, 2, 3}

# print(a.issubset(b))
# a = {1, 5}
# b = {1, 2, 3}

# print(a.issubset(b))

# print(b.issuperset(a))
# disjoint method
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))


# numbers = {10, 20, 30}

# for i in numbers:
#     print(i)


# frozen set 

# data = frozenset([1, 2, 3])

# print(data)

# Program to create a frozen set

# numbers = frozenset([1, 2, 3, 4, 5])

# print("Frozen Set =", numbers)