# 使用pyecharts创建折线图,注意使用pyecharts生成的是网页前端页面
'''
全局配置可以更改图表的显示和相关的工具,主要是和整体相关的
全局配置选项可以通过set_global_opts(global_opts)的方法进行配置,相应的选项和选项的功能如下:
TitleOpts:标题配置项
LegendOpts:图例配置项
ToolboxOpts:工具箱配置项
VisualMapOpts:视觉映射配置项
TooltipOpts:提示框配置项
当实例化Line/xxx类成为对象时,可以使用对象名.set_global_opts()的方法设置全局配置项
'''

# 导包
from pyecharts.charts import Line
from pyecharts.options import *

# 得到折线图对象,实例化Line类
line = Line()
# 添加X轴数据
line.add_xaxis(["中国", "美国", "日本"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 21])  # 第一个参数是图表上的折现的名称

# 设置全局配置项
line.set_dark_mode(True)
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 生成图表
line.render()


# 使用字符串的replae方法在有时能够起到奇效,将一些不合规的json数据转换为空字符串,当然也可以使用正则表达式实现