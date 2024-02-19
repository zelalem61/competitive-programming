class RecentCounter:

    def __init__(self):
        self.requests = []
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        val = t - 3000
        count = 0
        index = bisect_left(self.requests,val)
        return len(self.requests)-index




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)