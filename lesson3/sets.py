# my_set = {1, 2, 3}
# print(my_set)
from enum import unique
from operator import length_hint

# my_set = set([4, 5, 6])
# print(my_set)

# my_set = set()
# print(my_set)

# my_set = {1, 2, 3, 3, 4, 5, 6}
# print(my_set)
#
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# union_result_method = set1.union(set2)
#
# union_result_operator = set1 | set2
#
# print("Union of set1 and set2 using union method:", union_result_method)
# print("Union of set1 and set2 using the | operator:", union_result_operator)

my_set = {1, 2, 3}

my_set.add(7)
my_set.remove(3)

my_set.discard(8)

length_set = len(my_set)

my_set.clear()

print(length_set)

my_list = [1, 2, 3, 3, 4, 4, 5, 6]

unique_set = set(my_list)

print(unique_set)

unique_list = list(unique_set)
print(unique_list)

user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "reading", "cooking"}
common_interests = user1_interests.intersection(user2_interests)
print(common_interests)

colors = {"red", "green", "blue"}
color = "green"

print(color in colors)
print(color not in colors)