import math

user_input = int(input("Enter radius value to calc area and circumference of circle: "))

def circle(user_input):
    area = math.pi * user_input * user_input
    coc = math.pi * user_input * 2
    return area,coc

circle_area, circle_coc = circle(user_input)
print("Area is: ",math.floor(circle_area*2), "Coc is: ",round(circle_coc,3))


# 4 ----4.7---- 5
#               ↑ closer to 5!
# round(4.7) → 5  ✅  (4.7 is closer to 5)
# round(4.3) → 4  ✅  (4.3 is closer to 4)
# Simple rule: 
# Below .5 → go down. .5 or above → go up.

# math.floor() — "Always go to the LEFT (always go DOWN)"
# It ignores the decimal and always picks the smaller whole number. Like a floor you're standing on — you always go down to the floor.

# 4 ----4.7---- 5
# ↑ floor is always here!
# math.floor(4.7) → 4  ✅
# math.floor(4.1) → 4  ✅
# math.floor(4.9) → 4  ✅  (even 4.9 goes down!)