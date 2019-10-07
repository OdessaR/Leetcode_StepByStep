#20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/
#With Python


#Solution 1: use right bracket as identifier

class Solution(object):
    def isValid(self, s):
	
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}
    
        for char in s:
        	#if there is a right bracket, find left bracket in stack.
            if char in mapping:
            	#if stack is not empty, pop out top element in stack, else use dummy symbol
                top_element = stack.pop() if stack else '#'
                #if it doesn't match, return false
                if mapping[char] != top_element:
                    return False
            #if there is a left bracket, put it in stack and wait for next right bracket to come
            else:
                stack.append(char)
        #if the stack is empty in the end, then all brackets are matched.            
        return not stack

#Solution 2: use left bracket as identifier

class Solution(object):
	def isValid(self, s):
		stack = []
		mapping = {"(":")", "{":"}", "[":"]"}

		for char in s:
			#if there is a left bracket, put it in stack and wait until right bracket to come
			if char in mapping:
				stack.append(mapping[char])
				continue
			#if there is a right bracket, then the top element in stack should match
			else:
				top_element = stack.pop() if stack else '#'
				if char != top_element:
					return False
		#if stack is empty in the end, then all brackets are matched				
		return not stack



