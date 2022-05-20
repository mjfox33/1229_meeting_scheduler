class Solution:
    def minAvailableDuration(self, slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
        slots1.sort(key=lambda x:x[0])
        slots2.sort(key=lambda x:x[0])
        p1 = 0
        while p1 < len(slots1):
            p2 = 0
            start1, end1 = slots1[p1]
            if duration > end1 - start1:
                p1 += 1
                continue
            while p2 < len(slots2):
                start2, end2 = slots2[p2]
                if duration > end2 - start2:
                    p2 += 1
                    continue
                if start2 <= start1:
                    if start1 + duration <= end2 and start1 + duration <= end1:
                        return [ start1, start1 + duration ]
                elif start2 + duration <= end1 and start2 + duration <= end2:
                    return [ start2, start2 + duration ]
                p2 += 1            
            p1 += 1
        return []
                