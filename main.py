some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)


#generate a list of dupes, I used a set for the comp becasue it automatically dis-allows dupes. then I wrapped it in a set so it is fully compatible with the org example.
duplicates = list({char for char in some_list if some_list.count(char) > 1})


print(duplicates)