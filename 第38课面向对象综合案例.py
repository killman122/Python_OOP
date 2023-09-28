'''
设计一个Game类
属性:
定义一个类属性'top_score'记录游戏的最高历史得分
定义一个实例属性'player_name'记录当前游戏的玩家姓名

方法:
静态方法'show_help'显示游戏的帮助信息
类方法'show_top_score'显示历史最高分
实例方法'start_game'开始当前玩家的游戏
'''


class Game:
    # 定义类属性top_score
    top_score = 0  # 定义初始化类属性为空None会引发异常


    # 定义初始化方法/构造器
    def __init__(self, player_name):
        self.player_name = player_name

    # 定义静态方法,用于输出需要的帮助信息
    @staticmethod
    def show_help():
        print("现在显示的是游戏帮助")

    #
    @classmethod
    def show_top_score(cls):
        print(f'本游戏历史最高{cls.top_score}')

    def start_game(self):
        print(f"{self.player_name}开始游戏")


Game.show_top_score()


# 实例化类生成类对象
# 显示游戏帮助
Game.show_help()
game = Game('王三思')
game.start_game()
