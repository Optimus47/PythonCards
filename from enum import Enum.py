from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)       # Color.RED
print(Color.RED.name)  # 'RED'
print(Color.RED.value) # 1

print(list(Color))  # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

class OrderStatus(Enum):
    NEW = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELED = 5

print(OrderStatus.NEW)         # OrderStatus.NEW
print(OrderStatus.SHIPPED.name)  # 'SHIPPED'
print(OrderStatus.DELIVERED.value) # 4

for status in OrderStatus:
    print(status)