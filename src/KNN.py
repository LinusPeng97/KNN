from util import data_util


def predict(k, chest, waist, hip, height, weight, cup, shoe):
    """
    预测结果
    :param k:
    :param chest:
    :param waist:
    :param hip:
    :param height:
    :param weight:
    :param cup:
    :param shoe:
    :return:
    """
    train = open("../data/train.txt", 'r')
    train_data = train.readlines()
    distance = []
    for i in train_data:
        chest_train, waist_train, hip_train, height_train, weight_train, cup_train, shoe_train, like_train = i.split(' ')
        data = data_util.convert_data_to_list(chest_train, waist_train, hip_train, height_train, weight_train, cup_train, shoe_train)
        pre_data = data_util.convert_data_to_list(chest, waist, hip, height, weight, cup, shoe)
        distance.append(data_util.get_distance(data, pre_data))
    # 记录索引
    index = []
    for i in range(len(distance)):
        index.append(i)
    data_util.sort(distance, index)
    rank1 = 0
    rank2 = 0
    rank3 = 0
    for i in range(k):
        data = train_data[index[i]].split(' ')
        if data[7].replace('\n', '') == '1':
            rank1 += 1
        elif data[7].replace('\n', '') == '2':
            rank2 += 1
        elif data[7].replace('\n', '') == '3':
            rank3 += 1
    max_rank = rank1
    if rank2 > max_rank:
        max_rank = rank2
    if rank3 > max_rank:
        max_rank = rank3
    if max_rank == rank1:
        return 1
    elif max_rank == rank2:
        return 2
    else:
        return 3


def get_best_k_value():
    """
    通过验证集获得最佳K值
    :return:
    """
    train = open("../data/train.txt", 'r')
    val = open("../data/validation.txt", 'r')
    train_data = train.readlines()
    val_data = val.readlines()
    train.close()
    val.close()
    total_acc = [0]
    for k in range(len(train_data)):
        if k == 0:
            continue
        else:
            acc = 0
            for data in val_data:
                chest, waist, hip, height, weight, cup, shoe, like = data.split(' ')
                result = predict(k, float(chest), float(waist), float(hip), float(height), float(weight), float(cup)
                                 , float(shoe))
                if result == int(like.replace('\n', '')):
                    acc += 1
            total_acc.append(acc)
    max_acc = max(total_acc)
    for i in range(len(total_acc)):
        if total_acc[i] == max_acc:
            return i
    return i


def start():
    k = get_best_k_value()
    print("Please enter all attributes of person you want to predict by following order:")
    print("chest waist hip height weight cup shoe")
    print("E.g. 86 93 74 167 50 C 37")
    while True:
        data = input()
        chest, waist, hip, height, weight, cup, shoe = data.split(' ')
        cup = data_util.convert_cup_to_digit(cup)
        chest, waist, hip, height, weight, cup, shoe = data_util.min_max_normalization(chest, waist, hip, height, weight, cup, shoe)
        result = predict(k, chest, waist, hip, height, weight, cup, shoe)
        if result == 1:
            print("Maybe she is not suitable to you!")
        elif result == 2:
            print("You have feelings for her!")
        else:
            print("She is your soul mate!")


if __name__ == '__main__':
    start()
