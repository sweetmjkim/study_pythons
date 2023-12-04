a1 = "1"
a2 = " "
a3 = "2"
a4 = " "
a5 = "3"
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a1, a2 = a2, a1
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a2, a4 = a4, a2
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a2, a3 = a3, a2
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a3, a5 = a5, a3
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a4, a5 = a5, a4
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a1, a3 = a3, a1
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a2, a3 = a3, a2
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

print("--------------------------------------")

a1 = "1"
a2 = " "
a3 = "2"
a4 = " "
a5 = "3"
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a2 = a1
a1 = " "
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a4 = a2
a2 = " "
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a2 = a3
a3 = " "
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a3 = a5
a5 = " "
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a5 = a4
a4 = " "
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a1 = a3 
a3 = " "
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))

a3 = a2
a2 = " " 
print("{} {} {} {} {}".format(a1, a2, a3, a4, a5))