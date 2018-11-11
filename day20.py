
def gifts_number(house_num):
    gifts = 0
    for i in range(1, house_num+1):
        if house_num % i == 0:
            gifts += i
    return gifts


target_gift_num = 3310000

# print(gifts_number(1200000))
# print(gifts_number(1300000))
for house_num in range(10000, 1500000):
    if house_num % 1000 == 0:
        print(house_num)
    gifts = gifts_number(house_num)
    if gifts == target_gift_num:
        print(house_num)
        break
