
class DIMapper:
    __mapper_dict={}
    @staticmethod
    def inject(cls,arg):
        if cls not in DIMapper.__mapper_dict:
            DIMapper.__mapper_dict[cls] = args

    @staticmethod
    def get_mappers():
        return DIMapper.__mapper_dict

class DIMetaClass(type):
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls,*args,**kwargs)
        mapper_dict = DIMapper.get_mappers()
        if cls in mapper_dict:
            cls.__init__(obj,mapper_dict[cls])
        else:
            cls.__init__(obj,*args,**kwargs)
        return obj