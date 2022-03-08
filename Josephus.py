# Josephus问题：假设有n个人围坐一圈，
# 现要求从第1个人开始报数，报到第m个数的人退出圈。
# 然后，从下一个人开始继续报数并按同样规则退出，
# 直至所有人退出。要求按序输出各出列人的编号。

# 循环单链表
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d -> %s' % (self.val, self.next)


def Josephus(n, m):
    head = ListNode(1)
    p = head
    for i in range(2, n + 1):
        nd = ListNode(i)
        p.next = nd
        p = nd
    p.next = head
    p = p.next
    j = 1
    res = []
    while p.next != p:
        if j == m - 1:
            res.append(p.next.val)
            p.next = p.next.next
            j = -1
        else:
            p = p.next
        j += 1
    res.append(p.val)
    return res

print(Josephus(10, 3))
print(Josephus(1, 1))
print(Josephus(5, 7))
