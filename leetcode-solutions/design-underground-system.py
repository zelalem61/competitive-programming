class UndergroundSystem:

    def __init__(self):
        self.checkInDic = {}
        self.placeWithTime = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInDic[id] = [stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s = self.checkInDic[id]
        netTime = t - s[1]
        place = (s[0],stationName)
        if place not in self.placeWithTime:
            self.placeWithTime[place] = [netTime]
        else:
            self.placeWithTime[place].append(netTime)
            
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.placeWithTime[(startStation,endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)