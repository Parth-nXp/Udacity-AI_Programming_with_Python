'''
If your solution is robust, you should be able to use it with any dictionary of items to count the number of fruits in the basket. 
Try the loop for each of the dictionaries below to make sure it always works.
'''

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, value in basket_items.items():
    if fruit in fruits:
        result += value

print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, value in basket_items.items():
    if fruit in fruits:
        result += value

print(result)


for fruit, value in basket_items.items():
    if fruit in fruits:
        result += value

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, value in basket_items.items():
    if fruit in fruits:
        result += value

print(result)