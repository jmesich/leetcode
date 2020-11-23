#Unique Morse Code Words

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        #sets dont allow duplicates
        s=set()
        #iterate through each word and find the morse representation
        for word in words:
            temp=''
            for c in word:
                temp+=morse_codes[ord(c)-97]
            s.add(temp)
        return len(s)
