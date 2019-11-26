#管理员
from time import sleep

class Admin(object):
    adminUserName = "admin"
    adminPassed = "admin"
    adminConfirmID = "1234abcd"

    def __init__(self, allUsers):
        self.allUsers = allUsers

    #开机
    def boot(self, times = 2):
        inputData = input("输入“boot”开机：")
        while times > 0:

            if inputData == "boot":
                print("开机成功……")
                return True
            else:
                print("输入有误！！您还有 %d 次机会，请重新输入……" %(times))
                times -= 1
                inputData = input("输入“boot”开机：")
        print("次数用尽！！开机失败……")
        return False

    #管理员登录验证
    def adminLogin(self):
        inputAdminUserName = input("请输入管理员账户：")
        if inputAdminUserName != self.adminUserName:
            input("管理员账户有误，登陆失败！！按任意键继续……")
            return False
        inputAdminPassed = input("请输入管理员密码：")
        if inputAdminPassed != self.adminPassed:
            input("管理员密码有误，登陆失败！！按任意键继续……")
            return False
        print("登陆成功！！请稍等……")
        sleep(1)
        print("-----------------------管理员须知-----------------------")
        print("您好，这里是管理员须知。\n"
              "作为管理员，请确认您是合法途径进入该系统且所有操作均合法。\n"
              "您需做到以下几点：\n"
              "  • 1、不随意复制用户信息。\n"
              "  • 2、不随意传播用户信息。\n"
              "  • 3、不随意修改用户信息。\n"
              "  • 4、不随意删除用户信息。\n"
              "  • 5、不得随意删库！！！")
        print("--------------------------------------------------------")
        input("请谨慎操作！！按任意键继续……")
        return True

    #更多（管理员操作）
    def more(self):
        if not self.adminLogin():
            return -1
        self.printAdminView()
        choice = input("请选择：")
        if choice == "all":
            self.showAllUsersInfor()
        elif choice == "delAll":
            self.delAllUsers()
        else:
            print("输入有误！！正在返回首页……")

    #查询用户信息
    def searchUserInfor(self):
        inputUserName = input("请输入用户姓名：")
        print("-----------------------查询结果-----------------------\n")
        for i in self.allUsers:
            if inputUserName != self.allUsers[i].name:
                print("查无此人！！操作失败……\n")
                return -1
            print("姓名：%s   卡号：%s   身份证号：%s   电话：%s" % (self.allUsers[i].name, self.allUsers[i].card.cardID, self.allUsers[i].idCard, self.allUsers[i].phoneNum))
        print("\n------------------------------------------------------\n")

    #展示所有用户
    def showAllUsersInfor(self):
        print("---------------------用户信息---------------------")
        print("        用户数：%d           总金额：%d\n" % (len(self.allUsers), self.dataStatistics()))
        for i in self.allUsers:
            print("姓名：%s        卡号：%s        余额：%d" % (
                self.allUsers[i].name, self.allUsers[i].card.cardID, self.allUsers[i].card.cardMoney))
            print("电话号码：%s                  身份证号：%s\n" % (self.allUsers[i].phoneNum, self.allUsers[i].idCard))
        print("--------------------------------------------------\n")

    #删除单个用户
    def delOneUser(self):
        inputAdminConfirmID = input("请输入管理员验证码：")
        if inputAdminConfirmID != self.adminConfirmID:
            print("验证码错误！！删除失败……")
            return -1
        print("-------------------危险操作！！-------------------")
        print("        用户数：%d           总金额：%d\n" % (len(self.allUsers), self.dataStatistics()))
        for i in self.allUsers:
            print("姓名：%s        卡号：%s        余额：%d" % (
                self.allUsers[i].name, self.allUsers[i].card.cardID, self.allUsers[i].card.cardMoney))
        print("--------------------------------------------------\n")
        inputDelUserCardID = input("请输入要删除账户卡号：")
        if inputDelUserCardID not in self.allUsers:
            print("无此卡号，操作失败……")
            return -1
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        del(self.allUsers[i])
        print("删除成功！！正在返回……")

    #删除所有用户
    def delAllUsers(self):
        inputAdminConfirmID = input("请输入管理员验证码：")
        if inputAdminConfirmID != self.adminConfirmID:
            print("验证码错误！！删除失败……")
            return -1
        print("-------------------危险操作！！-------------------")
        print("     目前用户数：%d           总金额：%d\n" % (len(self.allUsers), self.dataStatistics()))
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        self.allUsers = {}
        print("努力删库中……")
        sleep(2)
        print("------------------删库成功！！------------------")
        print("正在返回首页面……")
        sleep(1)

    #数据统计
    def dataStatistics(self):
        sumMoney = 0
        userAmount = len(self.allUsers)
        for i in self.allUsers:
            sumMoney += self.allUsers[i].card.cardMoney
        return sumMoney

    #

    #操作确认
    def confirmOperation(self):
        choice = input("确认执行此操作？(yes / no)： ")
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("输入有误！！操作结束……")
            return False



