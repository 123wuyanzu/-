from child.password_protection import encrypt_password


# 注册函数
def register(vip_info):
    print("欢迎来到注册页面")
    while True:
        sensitive_character = ["傻", "屁", "草", "操", "垃圾", "z"]
        new_username = input("请输入注册用户名: ")
        for i in sensitive_character:
            while i in new_username:
                new_username = new_username.replace(i, '*')
                print("用户名包含非法字符，请重新输入。")
                new_username = input("请输入注册用户名: ")

        new_password = encrypt_password()
        new_user = {'name': new_username, 'psw': new_password, 'role': '普通用户'}
        vip_info.append(new_user)
        print("注册成功")
        break