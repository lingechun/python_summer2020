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
# Heap sort has a time complexity of O(n log n) (Find online)
def heapify(arr, n, i): 
    largest = i # set largest as root
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if (l < n and arr[i] < arr[l]): 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if (r < n and arr[largest] < arr[r]): 
        largest = r 
  
    # Change root, if needed 
    if (largest != i): 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
    # Build a heap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0)
    return arr 



###############################################################################
# Quick sort (Find online)
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot: 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        return arr



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
#plt.legend(['selection sort, 'heap sort'], loc = "upper left", prop = {"size":10})
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
