class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        print(arr)
        res = []
        for s in arr:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if res:
                    res.pop()
            else:
                s = "/"+s
                res.append(s)
        if not res:
            return "/"
            
        return "".join(res)