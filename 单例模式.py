class Single(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


    def __init__(self):
        '''只执行一次'''
        if Single.init_flag:
            return
        print('ssss')
        Single.init_flag = True