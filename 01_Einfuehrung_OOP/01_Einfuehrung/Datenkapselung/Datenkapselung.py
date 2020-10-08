class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71
        self._protected_field = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

    def get_protected_field(self):
        return self._protected_field


baz = MyChildObject()
# print(baz.get_private_field())
print(baz.get_protected_field())
print(baz._MyParentObject__private_field)
