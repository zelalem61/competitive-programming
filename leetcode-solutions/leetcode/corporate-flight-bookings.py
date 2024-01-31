class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        my_dict = defaultdict(int)
        res = []

        for start, end, value in bookings:
            my_dict[start] += value
            if end + 1 <= n:
                my_dict[end + 1] -= value

        current_sum = 0
        for k in range(1, n + 1):
            current_sum += my_dict[k]
            res.append(current_sum)

        return res