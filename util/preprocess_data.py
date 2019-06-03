import json
from util import data_util


def normalization():
    """
    归一化数据，并划出训练集和验证集，验证集用于选取K值
    :return:
    """
    f = open("../data/modelInfoProcess.txt", 'r')
    ftrain = open("../data/train.txt", 'w')
    fvalidation = open("../data/validation.txt", 'w')
    lines = f.readlines()
    for i in range(len(lines)):
        if i == 0:
            continue
        chest, waist, hip, height, weight, cup, shoe, like = lines[i].split(' ')
        chest, waist, hip, height, weight, cup, shoe = data_util.min_max_normalization(chest, waist, hip, height, weight, cup, shoe)
        if i < 140:
            ftrain.write(str(chest) + ' ' + str(waist) + ' ' + str(hip) + ' ' + str(height) + ' ' + str(weight) + ' ' +
                         str(cup) + ' ' + str(shoe) + ' ' + str(like))
        else:
            fvalidation.write(str(chest) + ' ' + str(waist) + ' ' + str(hip) + ' ' + str(height) + ' ' + str(weight) +
                              ' ' + str(cup) + ' ' + str(shoe) + ' ' + str(like))
    f.close()
    ftrain.close()
    fvalidation.close()


def process_exception_data():
    """
    处理异常数据
    :return:
    """
    f = open("../data/modelInfo.txt", 'r')
    fp = open("../data/modelInfoProcess.txt", 'w')
    fp.write('chest' + ' waist' + ' hip' + ' height' + ' weight' + ' cup' + ' shoe' + ' like\n')
    lines = f.readlines()
    for i in range(len(lines)):
        if i == 0:
            continue
        chest, waist, hip, height, weight, cup, shoe, like = lines[i].split(' ')
        # 处理胸围数据
        index = i + 1
        list = []
        if chest == '0':
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if chest_tmp != '0':
                    list.append(chest_tmp)
                index += 1
            chest = (int(list[0]) + int(list[1])) / 2
        # 处理腰围数据
        index = i + 1
        list = []
        if waist == '0':
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if waist_tmp != '0':
                    list.append(waist_tmp)
                index += 1
            waist = (int(list[0]) + int(list[1])) / 2
        # 处理臀围数据
        index = i + 1
        list = []
        if hip == '0':
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if hip_tmp != '0':
                    list.append(hip_tmp)
                index += 1
            hip = (int(list[0]) + int(list[1])) / 2
        # 处理身高数据
        index = i + 1
        list = []
        if height == '0':
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if height_tmp != '0':
                    list.append(height_tmp)
                index += 1
            height = (int(list[0]) + int(list[1])) / 2
        # 处理体重数据
        index = i + 1
        list = []
        if weight == '0':
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if weight_tmp != '0':
                    list.append(weight_tmp)
                index += 1
            weight = (int(list[0]) + int(list[1])) / 2
        # 处理罩杯数据
        index = i + 1
        list = []
        cup = data_util.convert_cup_to_digit(cup)
        if cup == 0:
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if data_util.convert_cup_to_digit(cup_tmp) != 0:
                    list.append(data_util.convert_cup_to_digit(cup_tmp))
                index += 1
            cup = (list[0] + list[1]) / 2
        # 处理鞋码数据
        index = i + 1
        list = []
        if shoe == '0':
            while len(list) < 2:
                chest_tmp, waist_tmp, hip_tmp, height_tmp, weight_tmp, cup_tmp, shoe_tmp, like_tmp = lines[index].split(
                    ' ')
                if shoe_tmp != '0':
                    list.append(shoe_tmp)
                index += 1
            shoe = (int(list[0]) + int(list[1])) / 2
        # 将处理完成的数据写入文件中
        fp.write(str(chest) + ' ' + str(waist) + ' ' + str(hip) + ' ' + str(height) + ' ' + str(weight) + ' ' + str(cup)
                 + ' ' + str(shoe) + ' ' + str(like))
    fp.close()
    f.close()


def convert_json_to_txt():
    """
    将json格式的文件转换为txt
    :return:
    """
    f = open("../data/modelInfo.json", 'r', encoding='utf-8')
    lines = f.readlines()
    fp = open("../data/modelInfo.txt", 'w')
    fp.write('chest' + ' waist' + ' hip' + ' height' + ' weight' + ' cup' + ' shoe' + ' like\n')
    for i in range(len(lines)):
        line = lines[i].replace('},', '}')
        data = json.loads(line)
        three_measurement = data['three_measurement']
        chest, waist, hip = three_measurement[0].split('-')
        like = data['like']
        weight = data['weight']
        cup = data['cup']
        shoe_size = data['shoe_size']
        height = data['height']
        data_txt = chest + ' ' + waist + ' ' + hip + ' ' + height[0] + ' ' + weight[0] + ' ' + cup[0] + ' ' + shoe_size[0].replace('码', '') + ' ' + like[0] + '\n'
        fp.write(data_txt)
    f.close()
    fp.close()


if __name__ == '__main__':
    """
    按照次序依次运行下列三个函数
    """
    pass
    # convert_json_to_txt()
    # process_exception_data()
    # normalization()
