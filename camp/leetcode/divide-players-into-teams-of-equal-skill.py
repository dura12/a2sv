class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        d = 0
        
        if len(skill) <= 1:
            return -1
        
        start = 0
        end = len(skill) - 1
        r = skill[start] + skill[end]
        d = skill[start] * skill[end]
        
        start += 1
        end -= 1
        
        while start < end:
            if r == (skill[start] + skill[end]):
                r = skill[start] + skill[end]
                d += skill[start] * skill[end]
                end -= 1
                start += 1
            else:
                return -1
        
        return d