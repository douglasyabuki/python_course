def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        self.theme = 'Dark theme'
        self.font = '18px'


@singleton
class Test:
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = 'Light theme'
    print(as1.theme)

    as2 = AppSettings()
    print(as2.theme)

    t1 = Test()
    t2 = Test()
    print(t1 == t2)
