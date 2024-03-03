class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        left, right = 0, len(people) - 1 
        count=0
        while left<= right:
            diff=limit - people[right]
            right-=1
            count+=1
            if left <= right and people[left] <= diff:
                left+=1
        return count

