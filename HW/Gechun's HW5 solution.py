# Gechun's HW5 solution

class Node:
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next

	def __str__(self):
		return str(self.value)


class LinkedList:
	def __init__(self):
		self.head = None
		
	def addNode(self, new_value = None):
		addnode = Node(_value = new_value)
		if self.head == None: #if this is the first node, just add it as head
			self.head = addnode
		else:  # otherwise, find the last node in the list and add after that
			last = self.head
			while(last.next != None):
				last = last.next
			last.next = addnode

	def addNodeAfter(self, new_value, after_node):
		addnode = Node(_value = new_value)
		afternode = self.head # find the afternode from the head of the list
		# There are two situations that we can't find the afternode
		if afternode == None: # (1)the list is empty
			print('The list is empty and the after_node is not in the list.')
		else:
			try:
			    while(afternode.value != after_node):
				    afternode = afternode.next
				addnode.next = afternode.next
			    afternode.next = addnode
			except AttributeError: # (2)the afternode does not exist in the list
				print('The list is not empty and the after_node is not in the list.')
			    
    
    def addNodeBefore(self, new_value, before_node):
    	addnode = Node(_value = new_value)
		onebeforenode = self.head # find the node before beforenode from the head of the list
		# There are two situations that we can't find the one before beforenode
		if onebeforenode == None: # (1)the list is empty
			print('The list is empty and the before_node is not in the list.')
		else:
			try:
			    while(onebeforenode.next.value != before_node):
				    onebeforenode = onebeforenode.next
				addnode.next = onebeforenode.next
			    onebeforenode.next = addnode
			except AttributeError: # (2)the beforenode does not exist in the list
				print('The list is not empty and the before_node is not in the list.')
			        
			

    def removeNode(self, node_to_remove):
    	onebefore_removenode = self.head # find the node before removenode from the head of the list
    	# There are two situations that we can't find the one before removenode
    	if onebefore_removenode == None: #(1) the list is empty
    	    print('The list is empty and the node_to_remove is not in the list.')
    	else:
    		try: 
    			while(onebefore_removenode.next.value != node_to_remove.value):
    				onebefore_removenode = onebefore_removenode.next
    			removenode = onebefore_removenode.next
    			oneafter_removenode = removenode.next
    			onebefore_removenode.next = oneafter_removenode
    		except AttributeError: #(2)the removenode does not exist in the list
    		    print('The list is not empty and the node_to_remove is not in the list.')

    
    def reverse(self):
    	onebefore = None
    	thisone = self.head
    	while(thisone != None):
    		oneafter = thisone.next
    		thisone.next = onebefore
    		onebefore = thisone
    		thisone = oneafter
    	self.head = onebefore
        
			 	
	def length(self):
		if self.head == None: # if the list is empty, return the length as 0
		    count = 0
	    else:
	    	count = 0 # if the list is not empty, count the number of nodes until the last one
	    	last = self.head
	    	while(last != None):
				last = last.next
				count = count + 1
	    print(count)

	def print(self):
		last = self.head 
		while(last != None):
			print(last.value) # print the nodes in this list one by one
			last = last.next


list = LinkedList()
# add some new nodes to the end of the list 
list.addNode(1)
list.addNode(2)
list.addNode(5)
# check incorrect insertion
list.addNodeAfter(3, 10) 
list.addNodeBefore(4, 15)
# add correct insertion
list.addNodeAfter(3, 2)
list.addNodeBefore(4, 5)
# remove node that does not exist
list.removeNode(Node(6))
# remove a existing node
list.removeNode(Node(4))
# reverse the whole list
list.reverse()
# display the list
list.print()
# calculate the length of the list
list.length()
list.removeNodesByValue(3)



def removeNodesByValue(self, value):	
    	onebefore_removenode = self.head
    	if onebefore_removenode == value:

    	if onebefore_removenode.next.value == value
        while(onebefore_removenode.next.value != value):
    		onebefore_removenode = onebefore_removenode.next
    	removenode = onebefore_removenode.next
    	oneafter_removenode = removenode.next
    	onebefore_removenode.next = oneafter_removenode
    	onebefore_removenode = self.head


  
