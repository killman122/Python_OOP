# python数据和json数据之间的相互转换
# 导入json模块
import json
# 准备符合json格式的数据(数据指的是python数据),如字典或者是列表中包含着字典
data = [{"name": "老王","age":"20"},{"name":"王道","age":"21"}]
josn_data = {"name": "王三思","age":"22"}
# 通过json.dumps(data)方法将python类型数据转换为json类型数据,如果需要转换的json数据不是ascil编码需要填入参数ensure_ascii = False
data = json.dumps(data)
# 通过json.loads(data)方法将json类型数据还原会python中的数据
data = json.loads(data)
