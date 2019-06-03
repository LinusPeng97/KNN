import math


def sort(distance, index):
    """
    使用冒泡法排序，并记录其对应的索引
    :param distance:
    :param index:
    :return:
    """
    for i in range(len(distance) - 1):
        j = i + 1
        min_num = distance[i]
        min_index = i
        while j < len(distance):
            if distance[j] < min_num:
                min_num = distance[j]
                min_index = j
            j += 1
        if min_index != i:
            tmp = distance[min_index]
            distance[min_index] = distance[i]
            distance[i] = tmp
            tmp = index[min_index]
            index[min_index] = index[i]
            index[i] = tmp


def min_max_normalization(chest, waist, hip, height, weight, cup, shoe):
    """
    最小-最大归一化
    :return:
    """
    f = open("../data/modelInfoProcess.txt", 'r')
    lines = f.readlines()
    chest_sum = []
    waist_sum = []
    hip_sum = []
    height_sum = []
    weight_sum = []
    cup_sum = []
    shoe_sum = []
    for i in range(len(lines)):
        if i == 0:
            continue
        chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[i].split(' ')
        chest_sum.append(float(chest_tmp))
        waist_sum.append(float(waist_tmp))
        hip_sum.append(float(hip_tmp))
        height_sum.append(float(height_tmp))
        weight_sum.append(float(weight_tmp))
        cup_sum.append(float(cup_tmp))
        shoe_sum.append(float(shoe_tmp))
    chest_max = max(chest_sum)
    chest_min = min(chest_sum)
    waist_max = max(waist_sum)
    waist_min = min(waist_sum)
    hip_max = max(hip_sum)
    hip_min = min(hip_sum)
    height_max = max(height_sum)
    height_min = min(height_sum)
    weight_max = max(weight_sum)
    weight_min = min(weight_sum)
    cup_max = max(cup_sum)
    cup_min = min(cup_sum)
    shoe_max = max(shoe_sum)
    shoe_min = min(shoe_sum)
    chest = cal_normalization(chest, min=chest_min, max=chest_max)
    waist = cal_normalization(waist, min=waist_min, max=waist_max)
    hip = cal_normalization(hip, min=hip_min, max=hip_max)
    height = cal_normalization(height, min=height_min, max=height_max)
    weight = cal_normalization(weight, min=weight_min, max=weight_max)
    cup = cal_normalization(cup, min=cup_min, max=cup_max)
    shoe = cal_normalization(shoe, min=shoe_min, max=shoe_max)
    return chest, waist, hip, height, weight, cup, shoe


def cal_normalization(arg, min, max):
    return (float(arg) - min) / (max - min)


def convert_cup_to_digit(cup):
    """
    将罩杯数据转换成数值形式
    :param cup:
    :return:
    """
    for j in range(len(cup)):
        if cup[j] == 'A':
            cup = 10
            return cup
        elif cup[j] == 'B':
            cup = 12.5
            return cup
        elif cup[j] == 'C':
            cup = 15
            return cup
        elif cup[j] == 'D':
            cup = 17.5
            return cup
        elif cup[j] == 'E':
            cup = 20
            return cup
    return 0


def convert_data_to_list(chest, waist, hip, height, weight, cup, shoe):
    """
    将数据转化为list形式
    :return:
    """
    data = []
    data.append(chest)
    data.append(waist)
    data.append(hip)
    data.append(height)
    data.append(weight)
    data.append(cup)
    data.append(shoe)
    return data


def get_distance(arg1, arg2):
    """
    获取欧式距离
    :param arg1: list
    :param arg2: list
    :return:
    """
    sum = 0
    for i in range(len(arg1)):
        sum += math.pow(float(arg1[i]) - float(arg2[i]), 2)
    return math.sqrt(sum)