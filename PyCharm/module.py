def func_1(type_1='max'):
    def func_2(b):
        if type_1 == 'max':
            return max(b)
        else:
            return min(b)
    return func_2
