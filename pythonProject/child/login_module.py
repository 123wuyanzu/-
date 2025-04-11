from password_protection import encrypt_password


# 登录函数
def login(vip_info):
    print("欢迎来到登录页面")
    while True:
        username = input("请输入用户名: ")
        password = encrypt_password()
        for user in vip_info:
            if user['name'] == username and user['psw'] == password:
                if user['role'] == '普通用户':
                    print("普通用户登录成功")
                    return True, user['role']
                elif user['role'] == '管理员':
                    print("管理员登录成功")
                    return True, user['role']
        print("用户名或密码错误，请重新输入")