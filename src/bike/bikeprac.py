"""
需求文档：
写一个Bicycle(自行车)类，有run（骑行）方法，调用时显示骑行里程 km（骑行里程为传入的数字）；
再写一个电动自行车类EBicycle类继承自Bicycle，添加电池电量volume属性，通过参数传入，同时有两个方法：
1) fill_charge(vol) 用来充电，vol为电量
2) run(km)方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用Bicycle的run方法骑行，通过传入的骑行里程数，
显示骑行结果
"""


class Bicycle:

    def run(self, distance):
        print(f"脚踩了{distance}公里，好累呀！")


class EBicycle(Bicycle):
    # 添加电池电量volume属性
    def __init__(self, volume):
        self.volume = volume

    def fill_charge(self, add_vol):
        # 充电后的电池电量
        self.volume = self.volume + add_vol

    def run(self, km):
        # 电动车可以骑行的公里数
        distan = 10 * self.volume
        if km <= distan:
            # 依靠电量骑行的公里数
            print(f"电动车骑行了{distan}公里")
        elif km > distan:
            # 计算脚踩的公里数
            res = km - distan
            print(f"电动车骑行了{distan}公里")
            super().run(res)


# 实例化
bicycle = EBicycle(100)
bicycle.run(100)
