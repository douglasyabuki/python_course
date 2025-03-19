# Default values and field in dataclasses
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field


@dataclass
class Person:
    first_name: str = field(
        default='MISSING', repr=False
    )
    last_name: str = 'Not sent'
    age: int = 100
    addresses: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Person()
    # print(fields(p1))
    print(p1)
