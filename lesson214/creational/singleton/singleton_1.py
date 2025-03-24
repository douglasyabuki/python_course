"""
Singleton ensures that a class has only one instance
and provides a global point of access to it.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, in an interview for informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        """ The init will be called every time """
        self.theme = 'Dark theme'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.theme = 'Light theme'
    print(as1.theme)

    as2 = AppSettings()
    print(as2.theme)
