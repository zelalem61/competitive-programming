class OrderedStream:
    def __init__(self, n):
        self.pointer = 1
        self.n = n
        self.map = {}

    def insert(self, id, value):
        self.map[id] = value
        result = []
        if id == self.pointer:
            i = self.pointer
            while i <= self.n and i in self.map:
                result.append(self.map[i])
                i += 1
            self.pointer = i
        return result
