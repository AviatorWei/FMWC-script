def str_len(string):  # 输入字符串string，输出string的字符个数，适配中文。
    try:
        row_l = len(string)
        utf8_l = len(string.encode('utf-8'))
        return int((utf8_l - row_l) / 2 + row_l)
    except:
        return None


def LineToTxt(parts):  # 输入单行格式的参数parts = [part1, part2, ...]，输出按照此格式的文本。其中每个part = [内容, 长度, 对齐方式]
    output = ''
    for index in range(len(parts)):
        part = parts[index]
        string = str(part[0])
        length = part[1]
        align = part[2]
        if align == 'r':
            output = output + ' ' * (max(length - str_len(string), 0)) + string
        elif index == len(parts) - 1:
            output = output + string
        else:
            output = output + string + ' ' * (max(length - str_len(string), 0))
    output = output + '\n'
    return output


def outputPlayer(team, name, nation, number, position, price):
    number = str(number) + '号'
    price = str(price) + 'm'
    info = [team, name, nation, number, position, price]
    lengths = [5, 20, 12, 8, 4, 6]
    aligns = ['l', 'l', 'l', 'r', 'r', 'r']
    parts = [[string, length, align] for string, length, align in zip(info, lengths, aligns)]
    print(LineToTxt(parts))


if __name__ == "__main__":
    player_list = [
        ["SUI", "Fernandez", "Argentina", 24, "M"],
        ["DEN", "Veljkovic", "Serbia", 5, "D"],
        ["QAT", "Afriyie", "Ghana", 13, "M"],
        ["CAN", "Dominguez", "Ecuador", 22, "G"],
        ["SRB", "Elvedi", "Switzerland", 4, "D"],
        ["CRC", "E.Mendy", "Senegal", 1, "G"],
        ["POR", "Felix", "Portugal", 11, "F"],
        ["SUI", "Rodri", "Spain", 16, "M"],
        ["WAL", "Vitoria", "Canada", 5, "D"],
        ["ENG", "A.Gomez", "Argentina", 17, "M"],
    ]
    for player in player_list:
        outputPlayer(*(player + [10]))