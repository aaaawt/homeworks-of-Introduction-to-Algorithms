# 已知序列{503，87，512，61，908，170，897，275，653，462，378}，选择合适的线性表结构，用python实现：
# 直接插入排序法，并输出上述序列作非递减排序时的每趟结果；
# 希尔排序法，并输出上述序列作非递减排序时的每趟结果；
# 优化的冒泡排序法，并输出上述序列作非递减排序时的每趟结果；

def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i - 1
        cur = nums[i]
        while j >= 0 and cur < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = cur
    return nums

def shell_sort(nums):
    n = len(nums)
    k = n//2
    while k > 0:
        for i in range(1, n, k):
            j = i
            cur = nums[i]
            while j >= k and cur < nums[j - k]:
                nums[j] = nums[j - k]
                j -= k
            nums[j] = cur
        k = k//2
    return nums

def bubble_sort(nums):
    change = True
    n = len(nums) - 1
    while n >= 1 and change:
        change = False
        for j in range(n):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                change = True
        n -= 1
    return nums

print(insert_sort([503, 87, 512, 61, 908, 170, 897, 275, 653, 462, 378]))
print(shell_sort([503, 87, 512, 61, 908, 170, 897, 275, 653, 462, 378]))
print(bubble_sort([503, 87, 512, 61, 908, 170, 897, 275, 653, 462, 378]))