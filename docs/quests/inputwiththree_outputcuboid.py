# 가로 x 세로 x 높이 = 직육면체
# input : 가로 세로 높이
# output : 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3

# width : 4
# depth : 1
# height : 1

width, depth, height = "4 1 1".split()
num_width, num_depth, num_height = int(width), int(depth), int(height)
num_cuboid = (num_width * num_depth * num_height)
print("가로{}m * 세로{}m * 높이{}m = 직육면체{}m^3".format(num_width, num_depth, num_height, num_cuboid))
