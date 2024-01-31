class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        
        for passengers, start, end in trips:
            timestamp.append((start, passengers))
            timestamp.append((end, -passengers))
        
        timestamp.sort()
        
        current_capacity = 0
        for _, passenger_change in timestamp:
            current_capacity += passenger_change
            if current_capacity > capacity:
                return False
        
        return True
