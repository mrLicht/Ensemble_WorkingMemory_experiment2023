import numpy as np
import random
from random import randint

#!Begin experiment
Mo = randint(15, 180)  # set random orientation as the mean of an ensemble

st_d = (30) # sd for set

list_random = None

##set size of sequence
# 0 - the same color, 1 - different color
set_size_0 = [16, 24, 36] * 1
set_size_1 = [16, 24, 36] * 1

shuffle_set_0 = random.sample(set_size_0, len(set_size_0))
shuffle_set_1 = random.sample(set_size_1, len(set_size_1))

randomization_gr = list([shuffle_set_0, shuffle_set_1])

# make a set size of ensemble
trial_elements = randomization_gr

set_size = trial_elements.pop()
s = None

if len(set_size) > 0:
    if len(trial_elements) > 0:
        s = set_size.pop()
        print("number of el", s)


#make a vector of angle for set
if s == 16:
    list_random = np.random.normal(Mo, st_d, 16)
    print("1 variant", list_random)
elif s == 24:
    list_random = np.random.normal(Mo, st_d, 24)
    print("2 variant", list_random)
else:
    list_random = np.random.normal(Mo, st_d, 36)
    print("3 variant", list_random)

x = len(list_random) / 2

print(int(x))
#x = len(number_of_elements) / 2
#print("Number is completed", x)
#y = len(number_of_elements) / 2

gr1 = list_random[:int(x)]
gr2 = list_random[int(x):]


gr12 = [150, 160, 170, 180]

mean_one_unnecessary_1 = [1] * 20


#get opacity for set
##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36




#orientation0 = np.random.randint(0, 15, int(x))
#orientation1 = np.random.randint(-15, 0, int(x))

orientation1 = -15
orientation2 = 15

list_random = np.random.normal(Mo, st_d, 16)
print("list random", list_random)

sort_vers = sorted(list_random)

gr1 = sort_vers[:int(8)]
gr2 = sort_vers[int(8):]
print("check gr1", gr1)
print("check gr2", gr2)

gr1 = list(np.asarray(gr1) + (orientation1))
gr2 = list(np.asarray(gr2) + (orientation2))

print("list of group 1", gr1)
print("list of group 2", gr2)


print(- 65 - 13)



color = ["black", "blue", "yellow", "red"] * 3

print(color)

color_except = subtracted(color - 2)

print(color_except)


from psychopy.tools.monitorunittools import posToPix
from statistics import mean

#make mouse invisible
event.Mouse(visible=False, newPos=[0,0], win=None)

##position grid
#first pair
l1_2.pos = [x1+randint(-j,j),y1+randint(-j,j)]
l2_2.pos = [x2+randint(-j,j),y1+randint(-j,j)]
l3_2.pos = [x3+randint(-j,j),y1+randint(-j,j)]
l4_2.pos = [x4+randint(-j,j),y1+randint(-j,j)]
l5_2.pos = [x5+randint(-j,j),y1+randint(-j,j)]
l6_2.pos = [x6+randint(-j,j),y1+randint(-j,j)]
#second pair
l7_2.pos = [x1+randint(-j,j),y2+randint(-j,j)]
l8_2.pos = [x2+randint(-j,j),y2+randint(-j,j)]
l9_2.pos = [x3+randint(-j,j),y2+randint(-j,j)]
l10_2.pos = [x4+randint(-j,j),y2+randint(-j,j)]
l11_2.pos = [x5+randint(-j,j),y2+randint(-j,j)]
l12_2.pos = [x6+randint(-j,j),y2+randint(-j,j)]
#third pair
l13_2.pos = [x1+randint(-j,j),y3+randint(-j,j)]
l14_2.pos = [x2+randint(-j,j),y3+randint(-j,j)]
l15_2.pos = [x3+randint(-j,j),y3+randint(-j,j)]
l16_2.pos = [x4+randint(-j,j),y3+randint(-j,j)]
l17_2.pos = [x5+randint(-j,j),y3+randint(-j,j)]
l18_2.pos = [x6+randint(-j,j),y3+randint(-j,j)]
#fourth pair
l19_2.pos = [x1+randint(-j,j),y4+randint(-j,j)]
l20_2.pos = [x2+randint(-j,j),y4+randint(-j,j)]
l21_2.pos = [x3+randint(-j,j),y4+randint(-j,j)]
l22_2.pos = [x4+randint(-j,j),y4+randint(-j,j)]
l23_2.pos = [x5+randint(-j,j),y4+randint(-j,j)]
l24_2.pos = [x6+randint(-j,j),y4+randint(-j,j)]
#fifth pair
l25_2.pos = [x1+randint(-j,j),y5+randint(-j,j)]
l26_2.pos = [x2+randint(-j,j),y5+randint(-j,j)]
l27_2.pos = [x3+randint(-j,j),y5+randint(-j,j)]
l28_2.pos = [x4+randint(-j,j),y5+randint(-j,j)]
l29_2.pos = [x5+randint(-j,j),y5+randint(-j,j)]
l30_2.pos = [x6+randint(-j,j),y5+randint(-j,j)]
#sixth pair
l31_2.pos = [x1+randint(-j,j),y6+randint(-j,j)]
l32_2.pos = [x2+randint(-j,j),y6+randint(-j,j)]
l33_2.pos = [x3+randint(-j,j),y6+randint(-j,j)]
l34_2.pos = [x4+randint(-j,j),y6+randint(-j,j)]
l35_2.pos = [x5+randint(-j,j),y6+randint(-j,j)]
l36_2.pos = [x6+randint(-j,j),y6+randint(-j,j)]

Mo = randint(15,180) # set random orientation as the mean of an ensemble

#save Mo for routine
st_d = (30) # sd for set

list_random = None

## make a set size of ensemble
if len(set_size) >= 0:
    if len(trial_elements) > 0:
        s = set_size.pop()

#make a vector for the set
if s == 16:
    list_random = np.random.normal(Mo, st_d, 16)
elif s == 24:
    list_random = np.random.normal(Mo, st_d, 24)
else:
    list_random = np.random.normal(Mo, st_d, 36)

x = len(list_random) / 2

#Line size (I should draw them wider)
size_line = (25, 50)
line_Width = 1.3

l1_2.lineWidth = line_Width
l2_2.lineWidth = line_Width
l3_2.lineWidth = line_Width
l4_2.lineWidth = line_Width
l5_2.lineWidth = line_Width
l6_2.lineWidth = line_Width
l7_2.lineWidth = line_Width
l8_2.lineWidth = line_Width
l9_2.lineWidth = line_Width
l10_2.lineWidth = line_Width
l11_2.lineWidth = line_Width
l12_2.lineWidth = line_Width
l13_2.lineWidth = line_Width
l14_2.lineWidth = line_Width
l15_2.lineWidth = line_Width
l16_2.lineWidth = line_Width
l17_2.lineWidth = line_Width
l18_2.lineWidth = line_Width
l19_2.lineWidth = line_Width
l20_2.lineWidth = line_Width
l21_2.lineWidth = line_Width
l22_2.lineWidth = line_Width
l23_2.lineWidth = line_Width
l24_2.lineWidth = line_Width
l25_2.lineWidth = line_Width
l26_2.lineWidth = line_Width
l27_2.lineWidth = line_Width
l28_2.lineWidth = line_Width
l29_2.lineWidth = line_Width
l30_2.lineWidth = line_Width
l31_2.lineWidth = line_Width
l32_2.lineWidth = line_Width
l33_2.lineWidth = line_Width
l34_2.lineWidth = line_Width
l35_2.lineWidth = line_Width
l36_2.lineWidth = line_Width

#get opacity for set
##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36

if s == 16:
    op_gr1 = 1
    op_gr2 = 0
    op_gr3 = 0
elif s == 24: # + 8
    op_gr1 = 1
    op_gr2 = 1
    op_gr3 = 0
else: # 24 + 12
    op_gr1 = 1
    op_gr2 = 1
    op_gr3 = 1

#sort from smaller to higher
sort_vers = sorted(list_random)

#split group
gr1 = sort_vers[:int(x)]
gr2 = sort_vers[int(x):]

#gr1 = list_random[:int(18)]
#gr2 = list_random[int(18):]

#тут условная функция  должна выдавать n (16; 24; 36) случайных значений
#orientation1 = np.random.randint(0, 15, int(x))
#orientation2 = np.random.randint(-15, 0, int(x))

orientation1 = -15
orientation2 = 15
#gr1 += orientation1
#gr2 += orientation2

#gr 1 - CCW, gr 2 - CW
gr1 = list(np.asarray(gr1) + (orientation1))
gr2 = list(np.asarray(gr2) + (orientation2))

# randomize target and distractor
randomization = list([gr1, gr2])
random.shuffle(randomization)
target = randomization[0]
dist = randomization[1]

mean_dist_test = mean(target)
mean_target_test = mean(dist)

mean_one_unnecessary_1 = [1] * 20
mean_one_unnecessary_2 = [1] * 12

#get opacity for set
##op_gr1(16) = 8, 9, 10, 11, 14, 15 ,16 ,17, 20, 21, 22, 23, 26, 27, 28, 29
##op_gr2(24) = 7, 12, 13, 18, 19, 24, 25, 30
##op_gr3(36) = 1, 2, 3, 4, 5, 6, 31, 32, 33 ,34 ,35, 36

if s == 16:
    l8_2.ori,l9_2.ori, l14_2.ori, l15_2.ori, l20_2.ori, l21_2.ori, l26_2.ori, l27_2.ori = target
    l10_2.ori, l11_2.ori, l16_2.ori, l17_2.ori, l22_2.ori, l23_2.ori, l28_2.ori, l29_2.ori = dist
    l1_2.ori, l2_2.ori, l3_2.ori, l4_2.ori, l5_2.ori, l6_2.ori, l7_2.ori, l12_2.ori, l13_2.ori, l18_2.ori, l19_2.ori, l24_2.ori, l25_2.ori, l30_2.ori, l31_2.ori, l32_2.ori, l33_2.ori, l34_2.ori, l35_2.ori, l36_2.ori = mean_one_unnecessary_1
elif s == 24:
    l7_2.ori, l8_2.ori, l9_2.ori, l13_2.ori, l14_2.ori, l15_2.ori, l19_2.ori, l20_2.ori, l21_2.ori, l25_2.ori, l26_2.ori, l27_2.ori= target
    l10_2.ori, l11_2.ori, l12_2.ori, l16_2.ori, l17_2.ori, l18_2.ori, l22_2.ori, l23_2.ori, l24_2.ori, l28_2.ori, l29_2.ori, l30_2.ori = dist
    l1_2.ori, l2_2.ori, l3_2.ori, l4_2.ori, l5_2.ori, l6_2.ori, l31_2.ori, l32_2.ori, l33_2.ori, l34_2.ori, l35_2.ori, l36_2.ori= mean_one_unnecessary_2
else:
    l1_2.ori, l2_2.ori, l3_2.ori, l7_2.ori, l8_2.ori, l9_2.ori, l13_2.ori, l14_2.ori, l15_2.ori, l19_2.ori, l20_2.ori, l21_2.ori, l25_2.ori, l26_2.ori, l27_2.ori, l31_2.ori, l32_2.ori, l33_2.ori = target
    l4_2.ori, l5_2.ori, l6_2.ori, l10_2.ori, l11_2.ori, l12_2.ori, l16_2.ori, l17_2.ori, l18_2.ori, l22_2.ori, l23_2.ori, l24_2.ori, l28_2.ori, l29_2.ori, l30_2.ori, l34_2.ori, l35_2.ori, l36_2.ori = dist

#randomization of color
if len(condition_color_list) > 0:
    current_color = condition_color_list.pop(0)
elif len(condition_color_list) < 0:
        break

#draw 1 and 2 group from color_square (vWM) and colorList with exception
if s == 16:
    color_for_1gr = [[color_square]] * int(x)
    line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
    color_for_2gr = [[line_color_gr2]] * int(x)
    zero_color = [[line_color_gr2]] * (36 - int(s))
if s == 24:
    color_for_1gr = [[color_square]] * int(x)
    line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
    color_for_2gr = [[line_color_gr2]] * int(x)
    zero_color = [[line_color_gr2]] * (36 - int(s))
else:
    color_for_1gr = [[color_square]] * int(x)
    line_color_gr2 = random.choice([ele for ele in colorList if ele != color_square])
    color_for_2gr = [[line_color_gr2]] * int(x)

#draw color's lines for group 2 from colorList with exception
#line_color_gr2 = random.choice ([ele for ele in colorList if ele != color_square])
#color_for_2gr = [[line_color_gr2]] * 18

if current_color == 0:
    current_set_size = s
    ANS_color_square = color_square
    color_for_1gr == color_square
    color_gr1 = color_square
elif current_color == 1:
    current_set_size = s
    ANS_color_square = random.choice ([ele for ele in colorList if ele != color_square])
    line_color_gr1 = random.choice ([ele for ele in colorList if ele != color_square])
    color_for_gr1 = [[line_color_gr1]] * int(x)
    color_gr1 = line_color_gr1


if s == 16:
    l8_2.color,l9_2.color, l14_2.color, l15_2.color, l20_2.color, l21_2.color, l26_2.color, l27_2.color = color_for_1gr
    l10_2.color, l11_2.color, l16_2.color, l17_2.color, l22_2.color, l23_2.color, l28_2.color, l29_2.color = color_for_2gr
    l1_2.color, l2_2.color, l3_2.color, l4_2.color, l5_2.color, l6_2.color, l7_2.color, l12_2.color, l13_2.color, l18_2.color, l19_2.color, l24_2.color, l25_2.color, l30_2.color, l31_2.color, l32_2.color, l33_2.color, l34_2.color, l35_2.color, l36_2.color = zero_color
elif s == 24:
    l7_2.color, l8_2.color, l9_2.color, l13_2.color, l14_2.color, l15_2.color, l19_2.color, l20_2.color, l21_2.color, l25_2.color, l26_2.color, l27_2.color= color_for_1gr
    l10_2.color, l11_2.color, l12_2.color, l16_2.color, l17_2.color, l18_2.color, l22_2.color, l23_2.color, l24_2.color, l28_2.color, l29_2.color, l30_2.color = color_for_2gr
    l1_2.color, l2_2.color, l3_2.color, l4_2.color, l5_2.color, l6_2.color, l31_2.color, l32_2.color, l33_2.color, l34_2.color, l35_2.color, l36_2.color= zero_color
else:
    l1_2.color, l2_2.color, l3_2.color, l7_2.color, l8_2.color, l9_2.color, l13_2.color, l14_2.color, l15_2.color, l19_2.color, l20_2.color, l21_2.color, l25_2.color, l26_2.color, l27_2.color, l31_2.color, l32_2.color, l33_2.color = color_for_1gr
    l4_2.color, l5_2.color, l6_2.color, l10_2.color, l11_2.color, l12_2.color, l16_2.color, l17_2.color, l18_2.color, l22_2.color, l23_2.color, l24_2.color, l28_2.color, l29_2.color, l30_2.color, l34_2.color, l35_2.color, l36_2.color = color_for_2gr

n=36 #set size
rand_jitter_x=[]
rand_jitter_y=[]
for i in range(n):
    rand_jitter_x.append(random.randint(-j, j)) # это лист со случайными занчениями для небольшого сдвига положений в пространстве
    rand_jitter_y.append(random.randint(-j, j))


#lists of X and Y coordinates + random jitter
x_list = np.repeat([x1, x2, x3, x4, x5, x6],6) + rand_jitter_x #output like x1,x1,x1,x1,x1,x2,x2,x2....x6,x6
y_list = np.array([y1, y2, y3, y4, y5, y6] * 6)+ rand_jitter_y #output like y1,y2,y3,y4,y5,y6,y1,y2....y5,y6
coord_index = list(range(n)) #create list of indexes for x_list and y_list to randomize the coordinates
random.shuffle(coord_index) #shuffle coordinates indexes

# assign line spatial location
l1_2.pos=[x_list[coord_index[0]], y_list[coord_index[0]]]
l2_2.pos=[x_list[coord_index[1]], y_list[coord_index[1]]]
l3_2.pos=[x_list[coord_index[2]], y_list[coord_index[2]]]
l4_2.pos=[x_list[coord_index[3]], y_list[coord_index[3]]]
l5_2.pos=[x_list[coord_index[4]], y_list[coord_index[4]]]
l6_2.pos=[x_list[coord_index[5]], y_list[coord_index[5]]]
l7_2.pos=[x_list[coord_index[6]], y_list[coord_index[6]]]
l8_2.pos=[x_list[coord_index[7]], y_list[coord_index[7]]]
l9_2.pos=[x_list[coord_index[8]], y_list[coord_index[8]]]
l10_2.pos=[x_list[coord_index[9]], y_list[coord_index[9]]]
l11_2.pos=[x_list[coord_index[10]], y_list[coord_index[10]]]
l12_2.pos=[x_list[coord_index[11]], y_list[coord_index[11]]]
l13_2.pos=[x_list[coord_index[12]], y_list[coord_index[12]]]
l14_2.pos=[x_list[coord_index[13]], y_list[coord_index[13]]]
l15_2.pos=[x_list[coord_index[14]], y_list[coord_index[14]]]
l16_2.pos=[x_list[coord_index[15]], y_list[coord_index[15]]]
l17_2.pos=[x_list[coord_index[16]], y_list[coord_index[16]]]
l18_2.pos=[x_list[coord_index[17]], y_list[coord_index[17]]]
l19_2.pos=[x_list[coord_index[18]], y_list[coord_index[18]]]
l20_2.pos=[x_list[coord_index[19]], y_list[coord_index[19]]]
l21_2.pos=[x_list[coord_index[20]], y_list[coord_index[20]]]
l22_2.pos=[x_list[coord_index[21]], y_list[coord_index[21]]]
l23_2.pos=[x_list[coord_index[22]], y_list[coord_index[22]]]
l24_2.pos=[x_list[coord_index[23]], y_list[coord_index[23]]]
l25_2.pos=[x_list[coord_index[24]], y_list[coord_index[24]]]
l26_2.pos=[x_list[coord_index[25]], y_list[coord_index[25]]]
l27_2.pos=[x_list[coord_index[26]], y_list[coord_index[26]]]
l28_2.pos=[x_list[coord_index[27]], y_list[coord_index[27]]]
l29_2.pos=[x_list[coord_index[28]], y_list[coord_index[28]]]
l30_2.pos=[x_list[coord_index[29]], y_list[coord_index[29]]]
l31_2.pos=[x_list[coord_index[30]], y_list[coord_index[30]]]
l32_2.pos=[x_list[coord_index[31]], y_list[coord_index[31]]]
l33_2.pos=[x_list[coord_index[32]], y_list[coord_index[32]]]
l34_2.pos=[x_list[coord_index[33]], y_list[coord_index[33]]]
l35_2.pos=[x_list[coord_index[34]], y_list[coord_index[34]]]
l36_2.pos=[x_list[coord_index[35]], y_list[coord_index[35]]]






if s == 16:
    l8_2.color,l9_2.color, l14_2.color, l15_2.color, l20_2.color, l21_2.color, l26_2.color, l27_2.color = color_for_1gr
    l10_2.color, l11_2.color, l16_2.color, l17_2.color, l22_2.color, l23_2.color, l28_2.color, l29_2.color = color_for_2gr
    l1_2.color, l2_2.color, l3_2.color, l4_2.color, l5_2.color, l6_2.color, l7_2.color, l12_2.color, l13_2.color, l18_2.color, l19_2.color, l24_2.color, l25_2.color, l30_2.color, l31_2.color, l32_2.color, l33_2.color, l34_2.color, l35_2.color, l36_2.color = zero_color
elif s == 24:
    l7_2.color, l8_2.color, l9_2.color, l13_2.color, l14_2.color, l15_2.color, l19_2.color, l20_2.color, l21_2.color, l25_2.color, l26_2.color, l27_2.color= color_for_1gr
    l10_2.color, l11_2.color, l12_2.color, l16_2.color, l17_2.color, l18_2.color, l22_2.color, l23_2.color, l24_2.color, l28_2.color, l29_2.color, l30_2.color = color_for_2gr
    l1_2.color, l2_2.color, l3_2.color, l4_2.color, l5_2.color, l6_2.color, l31_2.color, l32_2.color, l33_2.color, l34_2.color, l35_2.color, l36_2.color= zero_color
else:
    l1_2.color, l2_2.color, l3_2.color, l7_2.color, l8_2.color, l9_2.color, l13_2.color, l14_2.color, l15_2.color, l19_2.color, l20_2.color, l21_2.color, l25_2.color, l26_2.color, l27_2.color, l31_2.color, l32_2.color, l33_2.color = color_for_1gr
    l4_2.color, l5_2.color, l6_2.color, l10_2.color, l11_2.color, l12_2.color, l16_2.color, l17_2.color, l18_2.color, l22_2.color, l23_2.color, l24_2.color, l28_2.color, l29_2.color, l30_2.color, l34_2.color, l35_2.color, l36_2.color = color_for_2gr


