from login_module import login
from register_module import register

# 假设已有用户信息列表，这里先简单定义
vip_info = [
    {'name': '张三', 'psw': 'zs333333', 'role': '普通用户'},
    {'name': 'admin', 'psw': 'admin123', 'role': '管理员'}
]

if __name__ == "__main__":
    while True:
        print("===========================")
        print("欢迎使用图书馆借阅管理系统")
        print("1 注册")
        print("2 登录")
        print("3 退出系统")
        print("===========================")
        choice = input("请输入（1 or 2 or 3）选择系统功能: ")
        if choice == "1":
            register(vip_info)
        elif choice == "2":
            logged_in, role = login(vip_info)
            if logged_in:
                break
        elif choice == "3":
            print("退出系统")
            break
        else:
            print("输入错误，请重新输入")