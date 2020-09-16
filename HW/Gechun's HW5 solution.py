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
		if self.head == None: # (1)the list is empty
			print('The list is empty.')
		elif self.head.value == after_node.value:
			addnode.next = self.head.next
			self.head.next = addnode
		else:
			try:
			    while(afternode.value != after_node.value):
				    afternode = afternode.next
				addnode.next = afternode.next
			    afternode.next = addnode
			except AttributeError: # (2)the afternode does not exist in the list
				print('The list is not empty and the after_node is not in the list.')
			    
    
    def addNodeBefore(self, new_value, before_node):
    	addnode = Node(_value = new_value)
		onebeforenode = self.head # find the node before beforenode from the head of the list
		# There are two situations that we can't find the one before beforenode
		if self.head == None: # (1)the list is empty
			print('The list is empty.')
		elif self.head.value == before_node.value:
			head = self.head
			self.head = addnode
			addnode.next = head	
		else:
			try:
			    while(onebeforenode.next.value != before_node.value):
				    onebeforenode = onebeforenode.next
				addnode.next = onebeforenode.next
			    onebeforenode.next = addnode
			except AttributeError: # (2)the beforenode does not exist in the list
				print('The list is not empty and the before_node is not in the list.')
			        
			

    def removeNode(self, node_to_remove):
    	onebefore_removenode = self.head # find the node before removenode from the head of the list
    	# There are two situations that we can't find the one before removenode
    	if self.head == None: #(1) the list is empty
    	    print('The list is empty.')
    	elif self.head.value == node_to_remove.value:
    		nextone = self.head.next
    		self.head.value = nextone.value
    		self.head.next = nextone.next

    	else:
    		try: 
    			while(onebefore_removenode.next.value != node_to_remove.value):
    				onebefore_removenode = onebefore_removenode.next
    			removenode = onebefore_removenode.next
    			oneafter_removenode = removenode.next
    			onebefore_removenode.next = oneafter_removenode
    		except AttributeError: #(2)the removenode does not exist in the list
    		    print('The list is not empty and the node_to_remove is not in the list.')
    
    def removeNodesByValue(self, value):	
    	# check if the list is empty
    	if self.head == None:
    		print('The list is empty.')
    	elif self.head.value == value: #when the first node is the node to remove
    		nextone = self.head.next
    		self.head.value = nextone.value #remove the first node
    		self.head.next = nextone.next
    		removenode = self.head # continue to check if there are still nodes to remove
    		try:
    	        while(removenode.value != value): # find the nodes to remove until the end of the list
    		        removenode = removenode.next # go to next one if this one does not have the specified value
    		        if removenode.value == value: 
    		            if removenode.next == None: # make sure if it is the last node in the list
    		        	    removenode.value == None # if is the last node, just remove it and end the function
    		        	    break
    		            else:
    			            nextone = removenode.next # if it is not the last node
    	                    removenode.value = nextone.value # remove the node and continue to check next one
    	                    removenode.next = nextone.next
            except AttributeError: 
            	pass
    	else:
    		removenode = self.head
    	    try:
    	        while(removenode.value != value): # find the nodes to remove until the end of the list
    		        removenode = removenode.next # go to next one if this one does not have the specified value
    		        if removenode.value == value: 
    		            if removenode.next == None: # make sure if it is the last node in the list
    		        	    removenode.value == None # if is the last node, just remove it and end the function
    		        	    break
    		            else:
    			            nextone = removenode.next # if it is not the last node
    	                    removenode.value = nextone.value # remove the node and continue to check next one
    	                    removenode.next = nextone.next
            except AttributeError: # check whether has nodes with the specified value
        	    print('The list is not empty and there is no nodes with the specified value in the list.')

    
    def reverse(self):
    	onebefore = None
    	thisone = self.head # start from the first node of the list
    	while(thisone != None):
    		oneafter = thisone.next # get the node after the current node
    		thisone.next = onebefore # exchange the position of the current node with the node before the current node
    		onebefore = thisone # store the nodes that have been reversed
    		thisone = oneafter # go the next node until finished the whole reversion 
    	self.head = onebefore # pass all reversed nodes to the head
        
			 	
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

	def print(self): # instead of having a str(self), I use print method to display the list
		last = self.head 
		while(last != None):
			print(last.value) # print the nodes in this list one by one
			last = last.next



list = LinkedList()
# add some new nodes to the end of the list 
list.addNode(2)
list.addNode(3)
list.addNode(6)
# check incorrect insertion
list.addNodeAfter(1, Node(10)) 
list.addNodeBefore(4, Node(15))
# add correct insertion
list.addNodeBefore(0, Node(2))
list.addNodeAfter(1, Node(0))
list.addNodeAfter(4, Node(3))
list.addNodeBefore(5, Node(6))
list.addNodeBefore(5, Node(6))
# remove node that does not exist
list.removeNode(Node(7))
# remove a existing node
list.removeNode(Node(3))
# remove node that does not exist
list.removeNodesByValue(9)
# remove the node with value 0, which is the first node in the list
list.removeNodesByValue(0)

# Seem only can remove one node with the specified value
# Please help: don't understand why the while-if loop does not work properly
list.removeNodesByValue(5)

# reverse the whole list
list.reverse()
# display the list
list.print()
# calculate the length of the list
list.length()


# I think the time complexity of the above methods are O(n). 
    	


  
