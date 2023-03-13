def heap(self, nums, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and nums[i] < nums[l]:
        largest = l

    if r < n and nums[largest] < nums[r]:
        largest = r

    if largest != i:
        (nums[i], nums[largest]) = (nums[largest], nums[i])
        self.heap(nums, n, largest)

def sortArray(self, nums: List[int]) -> List[int]:
    
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        self.heap(nums, n, i)

    for i in range(n - 1, 0, -1):
        (nums[i], nums[0]) = (nums[0], nums[i])  # swap
        self.heap(nums, i, 0)

    return nums
