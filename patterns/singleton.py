import time
import datetime

class Cache(object):
    #Тут будет храниться сам обьект кэша, который будет или создан или будет озвращаться при попытке
    # создать новый экземпляр

    _instance = None

    #Хранилище нового хэша
    vault: dict = {}

    # Как вы помните __new__ вызывается перед __init__ поэтому тут есть смысл вернутьвозвращаемый объект
    def __new__(cls, *args, **kwargs):
        #если объект еще не создан
        if not cls._instance:
            # ТО создаем новый экземпляр класса передав ему класс и параметры инициализации
            cls._instance = object.__init__(cls, *args, **kwargs)
        return cls._instance #Возвращаем сохраненный обьект


    def set_value(self, key, value):
        """Установить какоето значение по ключу"""
        self.vault[key] = value

    def get_value(self, key):
        """Получть какое либол значение по ключу"""
        return self.vault[key]

    def check(self, key) -> bool:
        """Проверить есть ли такой ключ в коллекции"""
        return key in self.vault

class Source:
    def get_something(self, key):
        """Метод заглушка, ждет 5 сек и возвращает одну и туже строку"""
        time.sleep(5)
        return 'result'

class App:
    def __init__(self):
        self.cache = Cache() # При инициализации получаем эземпляр класса Cache
        self.source = Source() # При инициализации получаем эземпляр класса Source

    def process(self, key):
        start_time = datetime.datetime.now() # время начала выполнения функции
        if self.cache.check(key):# проверяем есть ли этот ключ в класса
            result = self.cache.get_value # возвращаем значение из кэша

        else:
            result = self.cache.get_value(key) # Получаем значение из источника
            self.cache.set_value(key, result) # устанавливаем значение к кэш
            print(datetime.datetime.now() - start_time) # показывает скорость работы функции
        return result

app = App()
app2 = App()

print('Являются ли эти два объекста одинаковыми', id(app) == id(app2))
print('Являются ли их кэши одинаковыми', id(app.cache) == id(app2.cache))
print('запустите приложение в первый раз и получение данных из источника займет примерно 5 секунд')

app.process(1)
print('при повторном запуске данные будут получаьтся уже из кэша, и поэтому они будут получены почти мгновенно')

app.process(1)
print('данные для другого источника по прежнемув первый раз будут получаться долго')

app.process(2)
print('поскольку кэш у нас физически один на два разных обьекта, хотя каждый из них создал для себя экземпляр'
        'самостоятельно то второй уже не будет обращаться к источнику данных а возьмет его уже из кэша')

app2.process(1)
print('если мы выполним этот  блок кода еще раз, то данные будут получены моментально, потому что не '
'смотря на то что объекты app i app2 буждут уже другими - кэш у них будет один и тот же ')

