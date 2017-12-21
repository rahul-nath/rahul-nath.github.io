
def is_balanced(s):
	count = 0
	stack = []
	start_b, end_b = "([{<", ")]}>"
	for b in s:
		count += 1
		if b in start_b:
			stack.append(b)
		elif b in end_b:
			if not stack:
				return count
			else:
				stack_top = stack.pop()
				if stack_top != start_b[end_b.index(b)]:
					return count
		else:
			return count
	return -1

def evaluate(str):
  stack = []
  pushChars, popChars = "<({[", ">)}]"
  count = 0
  for c in str:
  	count += 1
    if c in pushChars:
      stack.append(c)
    elif c in popChars:
      if not len(stack):
        return count
      else :
        stackTop = stack.pop()
        balancingBracket = pushChars[popChars.index(c)]
        if stackTop != balancingBracket :
        	return count
    else :
      return count
  return -1
test = "<(){}[]<"

print evaluate(test)


