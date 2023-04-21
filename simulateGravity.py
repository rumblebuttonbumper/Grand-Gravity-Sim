import random

available_s = ["Seoyeon", "Hyerin", "Jiwoo", "Chaeyeon", "Yooyeon", "Soomin", "Nakyoung", "Yubin", "Kaede", "Dahyun",
               "Kotone", "Yeonji", "Nien", "Sohyun"]
evol = []
love = []


def pick_s():
    chosen_s = random.randrange(0, len(available_s))
    return chosen_s


def assign_s():
    evol_no = pick_s()
    love_no = pick_s()
    while evol_no == love_no:
        love_no = pick_s()
    evol_s = available_s[evol_no]
    love_s = available_s[love_no]
    evol.append(evol_s)
    love.append(love_s)
    available_s.remove(evol_s)
    available_s.remove(love_s)


while len(available_s) > 0:
    assign_s()

print("EVOLution:")
for s in evol:
    print(s)
print("\nLOVElution:")
for s in love:
    print(s)
