from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        top_k = [item for item, freq in count.most_common(k)]
        return top_k
        
