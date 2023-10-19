import random
import math
def calc_distance(x1,y1,x2,y2):
    e = x2 - x1
    f = y2 - y1
    d = math.sqrt(e**2 + f**2)
    return d
a = random.randrange(0,8)
b = random.randrange(0,8)
x = random.randrange(0,8)
y = random.randrange(0,8)
while a != x or b != y:
    distance = calc_distance(a,b,x,y)
    print('スイカとの距離は'+ str(distance))
    print('n,s,e,wのいずれかを入力してください')
    c = input()
    if c == 'n':
        y +=  1
    elif c == 's':
        y -= 1
    elif c == 'e':
        x += 1
    elif c == 'w':
        x -= 1
print('スイカを割りました！')