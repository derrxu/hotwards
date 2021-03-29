from classExample.homeworkPractice import Bicycle


class EBicycle:
    # 实例化骑行里程数
    km1 = Bicycle().run()
    # 定义电量消耗完之后剩下的里程数
    num = 0
    # 定义电量变量
    init_volume = int(input("请输入电池初始电量："))
    # 定义充电电量变量
    add_volume = int(input("请输入电池充入电量："))

    def __init__(self):
        super().__init__()

    # 定义fill_charge方法
    def fill_charge(self):
        self.volume = self.init_volume + self.add_volume
        return self.volume


    # 定义run方法
    def run(self):
        volume = self.fill_charge()
        # 对电量乘以10，做计算
        self.new_volume = volume * 10
        # 定义一个剩余里程数
        self.restkm = 0
        while True:
            # 此处判断里程是否能够把电量用完
            if self.km1 <= self.new_volume:
                rest_volume = (self.new_volume - self.km1) / 10
                print(f"此时的骑乘里程数为：{self.km1}千米, 剩余电量为：{rest_volume}度")
                return self.restkm
            else:
                # 剩余公里数
                restkm = self.km1 - self.new_volume
                print("剩余里程数为：{}千米".format(restkm))
                return restkm


# 将EBicycle类实例化
eBicycle = EBicycle()
restkm = eBicycle.run()
