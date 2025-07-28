from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        total = sum(count)
        min_val = next(i for i, v in enumerate(count) if v > 0)
        max_val = next(i for i in reversed(range(256)) if count[i] > 0)
        
        total_sum = sum(i * count[i] for i in range(256))
        mean = total_sum / total

        mode = max(range(256), key=lambda x: count[x])

        def get_median():
            mid1 = (total + 1) // 2
            mid2 = (total + 2) // 2
            m1 = m2 = None
            acc = 0
            for i, v in enumerate(count):
                acc += v
                if m1 is None and acc >= mid1:
                    m1 = i
                if m2 is None and acc >= mid2:
                    m2 = i
                    break
            return (m1 + m2) / 2

        median = get_median()
        return [float(min_val), float(max_val), mean, median, float(mode)]
