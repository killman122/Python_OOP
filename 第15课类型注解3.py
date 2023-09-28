my_list: list[int] = [1, 2, 3]

# 使用Union注解
# 使用Union[类型,....类型]
# 可以使用联合类型注解
from typing import Union

my_list: list[Union[str, int]] = [1, 2, 'wangdao', "wangsansi"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 20}

# 联合类型在函数中使用
def func(data: Union[int, str]) -> Union[int, str]:  # 这里的返回值使用Union可以指的是返回值的可能性有int类型或者是str类型
    pass

func()