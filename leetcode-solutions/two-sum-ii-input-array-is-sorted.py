class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = len(numbers)-1
        while i < j:
            print(i,j)
            if numbers[i] + numbers[j] == target:
                result.append(i+1)
                result.append(j+1)
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        return result
        
        