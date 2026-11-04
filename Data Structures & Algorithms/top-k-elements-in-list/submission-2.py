class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(n + 1)]
        for num, frequency in count.items():
            buckets[frequency].append(num)

        result = []
        for frequency in range(n, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if len(result) == k:
                    return result
        return result