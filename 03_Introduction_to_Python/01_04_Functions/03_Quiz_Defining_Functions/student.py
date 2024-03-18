'''
Write a function named readable_timedelta. 
The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
For example, calling the function and printing the result like this:

print(readable_timedelta(10))
should output the following:

1 week(s) and 3 day(s).
'''

# write your function here
def readable_timedelta(days):
    my_str = f"{days//7} week(s) and {days % 7} day(s)."
    return my_str

# test your function
print(readable_timedelta(10))