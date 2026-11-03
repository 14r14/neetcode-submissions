class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        res = []
        for num in nums:
            count_map[num] += 1
            
        sorted_keys = sorted(count_map, key=count_map.get, reverse=True)
    
        return sorted_keys[:k]
