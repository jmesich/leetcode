#Decode String
from collections import deque
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #if it is an empty string then just return
        if not s:
            return ""
        
        st = []
        end = 0
        #iterate through the string
        while end < len(s):
            #if the char in the string is a digit
            if s[end].isdigit():
                #we are converting the string to number
                num = 0
                while end < len(s) and s[end].isdigit():
                    num = num*10 + int(s[end])
                    end += 1
                #add the number to the stack
                st.append(num)
            #if the char in the string is an opening bracket, add it and continue
            elif s[end] == "[":
                #add to the stack
                st.append("[")
                end += 1
            #if the char is a alphabetic char, add the whole alphabetic substring to the stack
            elif s[end].isalpha():
                temp = []
                while end < len(s) and s[end].isalpha():
                    temp.append(s[end])
                    end += 1
                #add it to the stack
                st.append("".join(temp))
            #if the char is an end bracket
            elif s[end] == "]":
                #create a deque
                x = deque()
                #put the whole sequence bracket to bracket into the queue(but dont include the brackets)
                while st[-1] != "[":
                    x.appendleft(st[-1])
                    st.pop()
                st.pop()
                #if the stack isnt empty and the next value on the stack is a int, then we can decode
                if st and type(st[-1]) is int:
                    #decode
                    temp_str = "".join(x) * st[-1]
                    #remove the number
                    st.pop()
                    #re-add the temp_str
                    st.append(temp_str)
                end += 1
        return "".join(st)
        
        
        
