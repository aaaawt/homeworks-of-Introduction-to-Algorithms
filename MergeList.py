# 用python编写实现“算法作业2-题9-两个有序线性表合并的顺序和链式实现.ppt”中的算法。
# 比较两种算法在数据结构和时间、空间复杂度上的差异。
from typing import Optional

# 有序线性表合并
def merge(LA, LB):
    m = len(LA)
    n = len(LB)
    i, j = 0, 0
    LC = []
    while i < m and j < n:
        if LA[i] <= LB[j]:
            LC.append(LA[i])
            i += 1
        else:
            LC.append(LB[j])
            j += 1
    if i < m:
        LC.extend(LA[i:])
    elif j < n:
        LC.extend(LB[j:])
    return LC

# 有序链表合并
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return "%d -> %s" % (self.val, self.next)

def mergeList(La: Optional[ListNode], Lb: Optional[ListNode]):
    Lc = ListNode()
    head = Lc
    p = La
    q = Lb
    while p and q:
        if p.val <= q.val:
            head.next = p
            p = p.next
        else:
            head.next = q
            q = q.next
        head = head.next
    if p:
        head.next = p
    elif q:
        head.next = q
    return Lc.next

print(merge([3, 5, 7, 16], [2, 6, 7, 18, 21]))
print(mergeList(ListNode(2, ListNode(5, ListNode(8))), ListNode(3, ListNode(5, ListNode(7, ListNode(9))))))
