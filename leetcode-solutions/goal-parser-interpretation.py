class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        n = len(command)
        i = 0
        while i <= n-1:
            if command[i] == "G":
                ans+="G"
                i+=1
            elif command[i] == "(" and command[i+1] == ")":
                ans+="o"
                i+=2
            elif command[i] == "(" and command[i+1] == "a":
                ans+= "al"
                i+=4
        return ans