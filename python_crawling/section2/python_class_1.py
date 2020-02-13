class warehouse:

    warehouse_num = 0

    def __init__(self, name):
        self.name = name
        warehouse.warehouse_num += 1


w1=warehouse("hans")
w2=warehouse("yongs")
print("w1", w1.warehouse_num)
print("w2", w2.warehouse_num)
print("warehouse", warehouse.warehouse_num)
print(w1.__dict__)
w1.warehouse_num=77
print(w1.__dict__)
print(w2.__dict__)
print("w1", w1.warehouse_num)
print("w2", w2.warehouse_num)