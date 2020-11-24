#Basic Calculator II
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = '+'
        num = 0
        #iterate through the string
        for i in range(len(s)):
            #get the first value
            val = s[i]
            #if the value is a digit then we want to build out the number (could be multiple chars in a row)
            if val.isdigit():
                num = num*10+int(val)
            #if it is an operator, or it is the second last char in the string.
            if i + 1 == len(s) or (val == '+' or val == '-' or val == '*' or val == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = val
                num = 0
        
        return sum(stack)
