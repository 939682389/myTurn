UserIdentity = {
    0: 'user',
    1: 'admin',
    2: 'checker'
}


def STRING2INT(DICT, STRING):
    """
    :param DICT:
    :param STRING:
    :return: list
    """
    return [k for k, v in DICT.items() if v == STRING]


if __name__ == '__main__':
    print(STRING2INT(UserIdentity, 'admin'))
