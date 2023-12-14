class FrequencyTracker:

    def __init__(self):
        self.mp = {}
        self.mpse = {}

    def add(self, number: int) -> None:
        if number not in self.mp:
            self.mp[number] = 1
            if 1 in self.mpse:
                self.mpse[1].add(number)
            else:
                self.mpse[1] = set([number])
        else:
            old_freq = self.mp[number]
            self.mpse[old_freq].remove(number)

            if not self.mpse[old_freq]:
                self.mpse.pop(old_freq)

            self.mp[number] += 1

            if self.mp[number] in self.mpse:
                self.mpse[self.mp[number]].add(number)
            else:
                self.mpse[self.mp[number]] = set([number])
                
        
    def deleteOne(self, number: int) -> None:
        if number in self.mp:
            self.mpse[self.mp[number]].remove(number)

            if not self.mpse[self.mp[number]]:
                self.mpse.pop(self.mp[number]) 
                
            self.mp[number] -= 1
            
            if self.mp[number] != 0:
                if self.mp[number] in self.mpse: 
                    self.mpse[self.mp[number]].add(number)
                else:
                    self.mpse[self.mp[number]] = set([number])
            else:
                self.mp.pop(number)
                
                

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.mpse:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)