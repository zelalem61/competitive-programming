class Solution:
    def smallestNumber(self, num: int) -> int:
        arr = list(str(num))
        if arr[0] == "-":
            arr[1:] = sorted(arr[1:], reverse = True)
            return int("".join(arr))
        else:
            count = 0
            i = 0
            n = len(arr)
            while i < n:
                if arr[i] == "0":
                    count+=1
                    arr.pop(i)
                    n-=1
                else:
                    i+=1
            arr.sort()
            for k in range(count):
                arr.insert(1,"0")
            return int("".join(arr))