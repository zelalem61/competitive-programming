class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        kelvin = celsius + 273.15
        far = celsius * 1.80 + 32
        
        res.append(kelvin)
        res.append(far)
        return res
        