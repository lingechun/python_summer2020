# Gechun's HW 4 solution
import random
import datetime
import matplotlib.pyplot as plt
import os 
os.chdir('/Users/lingechun/Documents/GitHub/python_summer2020/HW')


# Define sorting algorithms


###############################################################################
# The selection sort has a time complexity of O(n^2) (Covered in day 8 lecture)
def selection_sort(numbers):
    numbers = numbers.copy()  
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        del numbers[numbers.index(answer[-1])]    
    return answer


###############################################################################
# Heap sort has a time complexity of O(n log n) (Find online: https://www.programiz.com/dsa/heap-sort)
def heapify(numbers, n, i): 
    largest = i # set largest as root
    left = 2 * i + 1     # left = 2*i + 1 
    right = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is greater than root 
    if (left < n and numbers[i] < numbers[left]): 
        largest = left 
  
    # See if right child of root exists and is greater than root 
    if (right < n and numbers[largest] < numbers[right]): 
        largest = right 
  
    # Change root, if needed 
    if (largest != i): 
        numbers[i],numbers[largest] = numbers[largest],numbers[i] # swap 
        # Heapify the root. 
        heapify(numbers, n, largest) 
  
# function to sort an array of given size 
def heapSort(numbers): 
    n = len(numbers) 
    # Build a heap
    for i in range(n, -1, -1): 
        heapify(numbers, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        numbers[i], numbers[0] = numbers[0], numbers[i] # swap 
        heapify(numbers, i, 0)
    return numbers



###############################################################################
# Quick sort (Find online: https://www.geeksforgeeks.org/python-program-for-quicksort/)

def partition(numbers, first, last):
    i = (first-1)         # index of first element
    pivot = numbers[last]     # pick the last element as pivot
 
    for j in range(first, last):
 
        # If current element is smaller than or equal to pivot
        if numbers[j] <= pivot: 
            # increment index of smaller element
            i = i+1
            numbers[i], numbers[j] = numbers[j], numbers[i]
 
    numbers[i+1], numbers[last] = numbers[last], numbers[i+1]
    return (i+1)

def quickSort(numbers, first, last):
    if len(numbers) == 1:
        return numbers
    if first < last:
 
        # pi is partitioning index, numbers[p] is now at right place
        pi = partition(numbers, first, last)
 
        # Separately sort elements before partition and after partition
        quickSort(numbers, first, pi-1)
        quickSort(numbers, pi+1, last)
        return numbers


###############################################################################
# Function to generate 100 lists of N size set of random numbers between 0 and 10000
def number(N):
    randomlist = []
    for i in range(0, 100):
      randomlist.append(random.sample(range(0, 10000), N))
    return randomlist

# Function to calculate times for different sort algorithms
# For each N, simulate 100 times
def time(N):	
	selection_times = []
	heap_times = []
	quick_times = []
    numbers = number(N)	# generate 100 lists of N size set of random numbers
	for i in range(0, 100):  

	  	start = datetime.datetime.now()
		selection_sort(numbers[i])
		this_time = datetime.datetime.now() - start
		selection_times.append(this_time.microseconds)
	
	  
		start = datetime.datetime.now()
		heapSort(numbers[i])
		this_time = datetime.datetime.now() - start
		heap_times.append(this_time.microseconds)
		
	  
	  	start = datetime.datetime.now()
		quickSort(numbers[i], 0, N-1)
		this_time = datetime.datetime.now() - start
		quick_times.append(this_time.microseconds)
		
	return [selection_times, heap_times, quick_times]



#############################################################################
############################## Plotting #####################################
#############################################################################

## Plot 1 comparing the average running time of the selection sort and heap sort
# x-axis: N goes from 1 to 1000
x = range(1, 1001) 

# y-axis: average time for 100 simulation at each N
y_selection_mean = []
y_heap_mean = []
for i in x:
    this_time = time(i)
	this_y_selection = sum(this_time[0])/100
	this_y_heap = sum(this_time[1])/100
	y_selection_mean.append(this_y_selection)
	y_heap_mean.append(this_y_heap)


# plot the data
plt.plot(x, y_selection_mean, label = 'selection sort')
plt.plot(x, y_heap_mean, label = 'Heap sort')
# Add a legend
plt.legend(loc='upper left', ncol=2, shadow=True, fancybox=True)
# y label
plt.ylabel("Average runnig time: microseconds")
# x label
plt.xlabel("Size of set to sort: N")
# plot title
plt.title("The Effect of Different Sort Algorithms on Runtime")
# Show plot
plt.show(block=False)
# Save plot
plt.savefig('plot1.pdf')
# Close plot
plt.close()



## Plot 2 comparing the average, best, and worst case run-time of quick sort
# x-axis: N goes from 1 to 1000
x2 = range(1, 1001)
y_max = []
y_min = []
y_mean = []
for i in x2:
	this_time = time(i)
	this_y_max = max(this_time[2])
	this_y_min = min(this_time[2])
	this_y_mean = sum(this_time[2])/100
	y_min.append(this_y_min)
	y_max.append(this_y_max)
	y_mean.append(this_y_mean)

plt.plot(x2, y_max, label = 'worst case')
plt.plot(x2, y_min, label = 'best case')
plt.plot(x2, y_mean, label = 'average')

plt.legend(loc='upper left', ncol=2, shadow=True, fancybox=True)
plt.ylabel("Runnig time: microseconds")
plt.xlabel("Size of set to sort: N")
plt.title("Average, Best and Worst Case Runtime of QuickSort Algorithm")
plt.show(block=False)
plt.savefig('plot2.pdf')
plt.close()
