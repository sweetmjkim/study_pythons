a1="1"
a2=""
a3="2"
a4=""
a5="3"
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# 1 x 2 x 3

a1, a2 = a2, a1
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# x 1 2 x 3

a3, a4 = a4, a3
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# x 1 x 2 3

a3, a5 = a5, a3
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# x 1 3 2 x

a3, a1 = a1, a3
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# 3 1 x 2 x

a4, a3 = a3, a4
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# 3 1 2 x x

a2, a4 = a4, a2
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# 3 x 2 1 x

a4, a5 = a5, a4
print("{} {} {} {} {}" .format(a1, a2, a3, a4, a5))
# 3 x 2 x 1