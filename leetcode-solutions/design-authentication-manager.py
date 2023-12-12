class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return 
        elif self.tokens[tokenId] > currentTime:
            del self.tokens[tokenId]
            self.tokens[tokenId] = currentTime + self.timeToLive
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for keys in self.tokens:
            if self.tokens[keys] > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)