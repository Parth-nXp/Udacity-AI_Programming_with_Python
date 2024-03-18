'''
Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

Now in addition, address what would happen if someone gives a start_num that is greater than end_num. 
If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." 
Otherwise, set result to the value of break_num.
'''

start_num = 1#provide some start number
end_num = 30#provide some end number that you stop when you hit
count_by = 4#provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
break_num = start_num


if start_num < end_num:
    while break_num <= end_num:
        break_num += count_by
        print(break_num)
else:
    print("Oops! Looks like your start value is greater than the end value. Please try again.")


