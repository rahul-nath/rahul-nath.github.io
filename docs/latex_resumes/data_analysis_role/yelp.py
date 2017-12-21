def max_profit(stocks):
    min_price = min(stocks[0], stocks[1])
    profit = stocks[1] - stocks[0]
    for i in stocks[2:]:
        profit = max(i - min_price, profit)
        min_price = min(i, min_price)
    print profit

max_profit([10, 7, 5, 8, 11, 9])


def min_profit(stocks):    
	pass    

# List the strings that are anagrams from a set of strings? 
# more than one anagram?
def anagrams():
	# to find anagram -- for each word, create frequency table
	
	pass

def dfs(root):
	if not root:
		return
	visit(root)
	root.visited = True
	for n in root.neighbors():
		if not n.visited():
			dfs(n)

def merge_sort(l):
	if len(l) == 1:
		return l
	left = merge_sort(l[:len(l)/2])
	right = merge_sort(l[len(l)/2:])
	return merge(left, right)

def merge(a,b):
	c = []
	while a and b:
		if a[0] > b[0]:
			c.append(b.pop())
		else:
			c.append(a.pop())
	while a:
		c.append(a.pop())
	while b:
		c.append(b.pop())
	return c




