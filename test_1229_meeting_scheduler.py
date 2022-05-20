from code_1229_meeting_scheduler import Solution

def test_example_1():
    s = Solution()
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    duration = 8
    output = [60,68]
    assert s.minAvailableDuration(slots1,slots2,duration) == output

def test_example_2():
    s = Solution()
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    duration = 12
    output = []
    assert s.minAvailableDuration(slots1,slots2,duration) == output