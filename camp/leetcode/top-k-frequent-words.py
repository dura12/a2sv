
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def insertion_sort(bucket):
            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
                
            return bucket
        dic = Counter(words)
        ans = []
        res = []
        def bucket(num , n):
            bucket = [[] for i in range(n)]
            for key , val in dic.items():
                bucket[val].append(key)
            for i  in range(len(bucket)-1 , -1 , -1):
                if len(bucket[i])  > 0:
                    s=insertion_sort(bucket[i])
                    ans.extend(s)
                    if len(ans) >= k:
                        break
            return ans[:k]
        return bucket(words  , len(words))
        
    
    

        
                

        
            

 

        
        