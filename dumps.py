def dumps(s):
    def dmp_lst(obj):                   # 处理 list
        lst0 = [dumps(value) for value in obj]
        return '[' + ', '.join(lst0) + ']'

    def dmp_tpl(obj):                   # 处理 tuple
        lst0 = [dumps(value) for value in obj]
        return '[' + ', '.join(lst0) + ']'

    def dmp_dct(obj):                   # 处理 dict
        lst0 = [(dumps(key) + ': ' + dumps(value)) for key, value in obj.items()]
        return '{' + ', '.join(lst0) + '}'

    def dmp_bool(obj):                  # 处理 bool
        return str(obj).lower()

    def dmp_none(obj):                  # 处理 None
        return 'null'

    def dmp_num(obj):                   # 处理 int/float
            return str(obj)

    def dmp_str(obj):                   # 处理 string
            return '"{}"'.format(obj)

    def error(obj):                     # 调试用的 error
        raise ValueError('Bad Data!\n{}'.format(obj))

    rt = {
        list: dmp_lst,
        tuple: dmp_tpl,
        dict: dmp_dct,
        bool: dmp_bool,
        type(None): dmp_none,
        int: dmp_num,
        float: dmp_num,
        str: dmp_str
    }
    func = rt.get(type(s), error)
    return func(s)
