# 出错显示前后文信息和指针位置
def error(s, index):
    raise ValueError('\n{}\nBad Data!\n {} in {}'.format(s[:index+1], s[index], s[index:index+5]))


# 指针在一个新的 object 起点时
def start_position(s, index):
    dct = {
        '[': ld_lst,
        '(': ld_tpl,
        '{': ld_dct,
        '"': ld_str,
    }
    dct.update(dict.fromkeys(['f', 't', 'n'], ld_bool_none))
    dct.update(dict.fromkeys('1234567890', ld_num))
    func = dct.get(s[index], error)
    return func(s, index)


# 指针在一个 objct 末尾时如何跳转
def index_jump(s, index, *args, still=None):
    if s[index] in args:
        expcs = {
            ',': ', ',
            ':': ': ',
            ']': ']',
            ')': ')',
            '}': '}',
            '"': '"',
        }
        expc = expcs[s[index]]
        digit = len(expc)
        return index + digit
    elif s[index] == still:
        return index
    else:
        raise error(s, index)


# 全文停止解析后检查指针位置
def chck_end(s, index):
    if index != len(s):
        raise ValueError('Bad Data End!')


# 解析 list
def ld_lst(s, index):
    lst = []
    index += 1
    while s[index] != ']':
        value, index = start_position(s, index)
        lst.append(value)
        index = index_jump(s, index, ',', still=']')
    index = index_jump(s, index, ']')
    return lst, index


# 解析 tuple
def ld_tpl(s, index):
    lst = []
    index += 1
    while s[index] != ']':
        value, index = start_position(s, index)
        lst.append(value)
        index = index_jump(s, index, ',', still=']')
    index = index_jump(s, index, ']')
    return tuple(lst), index


# 解析 dict
def ld_dct(s, index):
    lst = []
    index += 1
    while s[index] != '}':
        key, index = start_position(s, index)
        index = index_jump(s, index, ':')
        value, index = start_position(s, index)
        lst.append((key, value))
        index = index_jump(s, index, ',', still='}')
    index = index_jump(s, index, '}')
    return dict(lst), index


# 处理 bool 和 None
def ld_bool_none(s, index):
    spcs = dict(
        t=(True, 4, 'true'),
        f=(False, 5, 'false'),
        n=(None, 4, 'null'),
    )
    spc, mv, expc = spcs[s[index]]
    if s[index:index + mv] != expc:
        raise error(s, index)
    return spc, index + mv


# 处理 int/float
def ld_num(s, index):
    result = ''
    isfloat = '.' in s
    while s[index] in '1234567890.':
            result += s[index]
            index += 1
    if isfloat:
        return float(result), index
    else:
        return int(result), index


# 处理 string
def ld_str(s, index):
    result = ''
    index += 1
    while s[index] != '"':
        result += s[index]
        index += 1
    index = index_jump(s, index, '"')
    return result, index


# 主函数
def loads(s: str, index=0):
    result, index = start_position(s, index)
    chck_end(s, index)
    return result
