class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = False
        ans = []
        row_one = "qwertyuiop"
        row_two = "asdfghjkl"
        row_three = "zxcvbnm"
        low_words  = [word.lower() for word in words]
        for word in low_words:
            for letter in word:
                if letter in row_one:
                    a = True
                else:
                    a = False
                    break
            if a == True:
                ans.append(words[low_words.index(word)])
            for letter in word:
                if letter in row_two:
                    
                    a = True
                else:
                    a = False
                    break
            if a == True:
                ans.append(words[low_words.index(word)])
            for letter in word:
                if letter in row_three:
                    
                    a = True
                else:
                    a = False
                    break
            if a == True:
                ans.append(words[low_words.index(word)])
        return ans