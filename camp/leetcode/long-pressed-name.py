class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 1
        r = 1
        if name[0] != typed[0]:
            return False
        while l < (len(name)) and r < len(typed):
            if name[l] == typed[r]:
                l += 1
                r += 1
            elif name[l-1] == typed[r]:
                r += 1
            else:
                return False
        while r < len(typed):
            if name[l - 1] == typed[r]:
                r += 1
            else:
                return False
        print(r , l)
        return len(name) == l
        