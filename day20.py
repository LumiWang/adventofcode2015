
def gifts_number(house_num):
    gifts = 0
    for i in range(1, house_num+1):
        if house_num % i == 0:
            gifts += i
    return gifts


N = 33100000
# N = 100

"""
The algorithm below doesn't work.
It is supposed to be correct,
but it takes too much time to compute. Too complex.
"""
#
# for i in range(200000, int(N/10+1)):
#     sum = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             sum += j * 10
#     if i % 1000 == 0:
#         print(i)
#         print(sum)
#     if sum >= N:
#         print(i)
#         break

"""
cheated algorithm:
for i = 1 .. N / 10
    for j = i .. N / 10 in steps of i
        house[j] += i * 10
        
Think: How this algorithm is more efficient than the one above.
"""

house = dict()
for i in range(1, int(N/11)+1):
    for j in range(i, int(N/11), i):
        if j not in house:
            house[j] = 0
        if j / i <= 50:
            house[j] += i * 11

# print(house)

lucky_houses = dict()
for item in sorted(house.keys()):
    if house[item] > N:
        print(item)
        break