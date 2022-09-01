#Question 1
#statistics module. It provides some functions for calculating basic statistics on data like mean, median
import statistics

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sort() function to sort the list and min(),max() to find minimum and maximum values of list respectively.
ages.sort()
print("the Sorted ages: ", ages)
print("The Minimum value of ages: ", min(ages))
print("The Maximum value of ages: ", max(ages))
# insert(position, value) - inserts the value in list at specified position
ages.insert(0,min(ages))
# append(value) - appends the value at the end of list
ages.append(max(ages))
print("List after update: ", ages)
#The biggest advantage of using median() function is that the data-list does not need to be sorted
#before being sent as parameter to the median() function using statistice module
print("Median of ages: ", statistics.median(ages))
print("Average of ages: ", statistics.mean(ages))
print("Range of ages: ", max(ages)-min(ages))

