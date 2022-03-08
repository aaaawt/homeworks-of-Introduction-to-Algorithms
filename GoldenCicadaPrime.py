# 金蝉素数：某古寺石碑上依稀刻有神秘自然数，
# 这些数由1、3、5、7、9这5个奇数排列组成的5位素数，
# 同时去掉最高位与最低位数字后的三位数还是素数，
# 同时去掉高二位和低二位后的一位数还是素数。
# 请编写程序求出石碑上的金蝉素数。

# 递归函数，枚举组合
def combi(str):
    if len(str) <= 1:
        return [str]
    ans = []
    for i in range(len(str)):
        for j in combi(str[:i]+str[i+1:]):
            ans.append(str[i] + j)
    return ans

# 判断是否为素数
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False

res = []
for x in combi('13579'):
    if is_prime(int(x)):
        if is_prime(int(x[1:4])):
            if is_prime(int(x[2:3])):
                res.append(x)

print(res)
