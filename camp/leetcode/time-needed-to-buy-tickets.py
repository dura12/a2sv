class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        s=0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                s+=tickets[i]
            elif tickets[i] >= tickets[k] and i > k:
                s+=tickets[k]-1
            else:
                s+=tickets[k]
        return s


        