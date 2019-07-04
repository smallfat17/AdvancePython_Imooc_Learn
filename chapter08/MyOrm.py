import numbers

class Filed:
    pass

class CharField(Filed):
    def __init__(self,db_column,max_length=None):
        self._value = None
        if max_length is None:
            raise ValueError("you must specify max_length")
        self.max_length = max_length
        self.db_column = db_column

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError("string need")
        if len(value) > self.max_length:
            raise ValueError("value's excess max_length")
        self._value = value

class IntegerField(Filed):
    def __init__(self,db_column,min_value,max_value):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("int need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min and max")
        self._value = value

    def __get__(self, instance, owner):
        return self._value

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == 'ModelBase':
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value,Filed):
                fields[key] = value
        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, 'db_table', None)
            if table is not None:
                db_table = table
        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)

class ModelBase(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fileds = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            fileds.append("'"+db_column+"'")
            value = getattr(self,key)
            if isinstance(value,str):
                value = "'" + value + "'"
            values.append(str(value))
        sql = 'insert into {}({}) values ({});'.format(self._meta['db_table'],','.join(fileds),','.join(values))
        print(sql)
        # for key, value in self.attrs:
        #     pass
        # sql = 'insert into {}({}) values ({})'.format()


class User(ModelBase):
    name = CharField(db_column='用户名',max_length=50)
    age = IntegerField(db_column='年龄',min_value=0,max_value=100)

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    user = User()
    user.name = 'jack'
    user.age = 18
    user.save()
