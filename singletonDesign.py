class a:
    _instances = []  # Keep track of instance reference
    limit = 1
    inst = None

    def __new__(cls, *args, **kwargs):
        if not len(cls._instances) == cls.limit:
            # raise (RuntimeError, "Count not create instance. Limit %s reached" % cls.limit)
            # return instance
            cls.inst = super(a, cls).__new__(cls,)
            cls._instances.append(cls.inst)
        return cls.inst
    def __init__(self):
        print("init")

    def __del__(self):
        # Remove instance from _instances
        # self._instance.remove(self)
        pass

ob1=a()
print(ob1)#.normalMethod()

ob2=a()
print(ob2)#.normalMethod()

ob3=a()
print(ob2)#.normalMethod()

ob4=a()
print(ob2)#.normalMethod()

ob5=a()
print(ob2)#.normalMethod()
