import threading


def show_info(name, age):
    print("name: %s age:%d" % (name, age))


if __name__ == '__main__':
    # 创建子线程,以元组方式传参,要保证元组里面元素的顺序和函数的参数顺序一致
    # sub_thread = threading.Thread(target=show_info, args=("王道", 20))
    # 以字典方式传参,保证键值对应即可
    sub_thread = threading.Thread(target=show_info, kwargs={"name":"王道","age":20})
    sub_thread.start()
