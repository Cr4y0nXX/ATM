#ATM
from card import Card
from user import User
from random import randrange
from time import sleep

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers

    #开户
    def openAccount(self):
        print("-------------------开户中！！-------------------")
        name = input("请输入姓名(26字符以内)：")
        phoneNum = input("请输入电话号(4位数字)：")
        if not self.checkPhoneNum(phoneNum):
            return -1
        idCard = input("请输入身份证号(8位数字)：")
        if not self.checkIdCard(idCard):
            return -1
        cardPasswd = input("请输入密码(6位数字)：")
        if not self.checkCardPasswd(cardPasswd):
            return -1
        if not self.checkPasswd(cardPasswd):
            print("密码错误！！开户失败……")
            return -1
        prestoreMoney = int(input("请输入预存款："))
        if prestoreMoney <= 0:
            print("预存款有误！！开户失败……")
            return -1
        cardID = self.createCardID()
        print("------------------开户成功！！------------------")
        print("请牢记卡号(%s)！！" % (cardID))
        input("牢记后按任意键继续……")
        #将信息存入字典
        card = Card(cardID, cardPasswd, prestoreMoney)
        user = User(name, idCard, phoneNum, card)
        self.allUsers[cardID] = user

    #查询
    def searchInfor(self):
        cardID = input("请输入卡号：")
        if self.checkLock(cardID):
            return -1
        if not self.userLogin(cardID):
            return -1
        print("---------------------查询结果---------------------\n")
        print("                    姓名：%s" %(self.allUsers[cardID].name))
        print("     卡号：%s                      余额：%d" %(cardID, self.allUsers[cardID].card.cardMoney))
        print("\n---------------------查询结果---------------------")

    #取款
    def withdrawals(self):
        cardID = input("请输入卡号：")
        if self.checkLock(cardID):
            return -1
        if not self.userLogin(cardID):
            return -1
        while True:
            getMoney = int(input("请输入取款金额："))
            if getMoney < 0 or getMoney > self.allUsers[cardID].card.cardMoney:
                print("输入有误！！操作失败……")
                return -1
            #确认操作
            if not self.confirmOperation():
                print("------------------取消成功！！------------------")
                return -1
            self.allUsers[cardID].card.cardMoney -= getMoney
            print("------------------取款成功！！------------------")
            print("     取款：%d                      余额：%d" %(getMoney, self.allUsers[cardID].card.cardMoney))
            #是否继续操作
            if  not self.confirmRepeat():
                return -1
    #存款
    def deposit(self):
        cardID = input("请输入卡号：")
        if self.checkLock(cardID):
            return -1
        if not self.userLogin(cardID):
            return -1
        while True:
            petMoney = int(input("请输入存款金额："))
            if petMoney < 0:
                print("输入有误！！操作失败……")
                return -1
            if not self.confirmOperation():
                print("------------------取消成功！！------------------")
                return -1
            self.allUsers[cardID].card.cardMoney += petMoney
            print("------------------存款成功！！------------------\n")
            print("     存款：%d                      余额：%d" % (petMoney, self.allUsers[cardID].card.cardMoney))
            print("\n------------------存款成功！！------------------")
            if not self.confirmRepeat():
                return -1

    #转账
    def transferMoney(self):
        cardID = input("请输入卡号：")
        if self.checkLock(cardID):
            return -1
        if not self.userLogin(cardID):
            return -1
        while True:
            transferCardID = input("请输入转账卡号：")
            if transferCardID not in self.allUsers:
                print("查无此人！！转账失败……")
                return -1
            transferMoney = int(input("请输入转账金额："))
            if transferMoney < 0 or transferMoney > self.allUsers[cardID].card.cardMoney:
                print("金额有误！！转账失败……")
                return -1
            if not self.confirmOperation():
                print("------------------取消成功！！------------------")
                return -1
            self.allUsers[cardID].card.cardMoney -= transferMoney
            self.allUsers[transferCardID].card.cardMoney += transferMoney
            print("------------------转账成功！！------------------\n")
            print("转账：%d                余额：%d" % (transferMoney, self.allUsers[cardID].card.cardMoney))
            print("\n------------------------------------------------")
            if not self.confirmRepeat():
                return -1

    #改密
    def changePasswd(self):
        choice = input("是否记得原密码？(yes / no)： ")
        if choice == "yes":
            cardID = input("请输入卡号：")
            if self.checkLock(cardID):
                return -1
            if not self.userLogin(cardID):
                return -1
        elif choice == "no":
            cardID = input("请输入卡号：")
            phoneNum = input("请输入绑定电话号码：")
            idCard = input("请输入身份证号：")
            if cardID not in self.allUsers or self.allUsers[cardID].idCard != idCard or self.allUsers[cardID].phoneNum != phoneNum:
                print("身份不匹配！！操作失败……")
                return -1
        else:
            print("输入有误！！改密失败……")
            return -1
        newCardPasswd = input("请输入新密码：")
        if not self.checkPasswd(newCardPasswd):
            print("两次密码不同！！改密失败……")
            return -1
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        self.allUsers[cardID].card.cardPasswd = newCardPasswd
        print("------------------改密成功！！------------------\n")
        print("请牢记新密码(%s)！！" %(newCardPasswd))
        print("\n------------------------------------------------")

    #锁定
    def lock(self):
        cardID = input("请输入卡号：")
        if self.checkLock(cardID):
            return -1
        if not self.userLogin(cardID):
            return -1
        idCard = input("请输入身份证号：")
        if self.allUsers[cardID].idCard != idCard:
            print("身份证号不匹配！！锁卡失败……")
            return -1
        print("账户信息正确！！")
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        self.allUsers[cardID].card.lock = True
        print("------------------锁定成功！！------------------")
        print("账户目前安全，要想使用请尽快解锁！！")

    #解锁
    def unlock(self):
        cardID = input("请输入卡号：")
        if not self.checkLock(cardID):
            print("该卡未被锁定，无需解锁！！")
            return -1
        if not self.userLogin(cardID):
            return -1
        phoneNum = input("请输入绑定电话号码：")
        idCard = input("请输入身份证号：")
        if cardID not in self.allUsers or self.allUsers[cardID].idCard != idCard or self.allUsers[
            cardID].phoneNum != phoneNum:
            print("身份不匹配！！解锁失败……")
            return -1
        print("账户信息正确！！")
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        self.allUsers[cardID].card.lock = False
        print("------------------解锁成功！！------------------")
        print("请牢记密码！！")

    #补卡
    def reissueCard(self):
        inputUserName = input("请输入姓名：")
        for i in self.allUsers:
            if inputUserName == self.allUsers[i].name:
                inputUserPhoneNum = input("请输入电话号码(4位)：")
                if inputUserPhoneNum == self.allUsers[i].phoneNum:
                    inputUserIdCard = input("请输入身份证号(8位)：")
                    if inputUserIdCard == self.allUsers[i].idCard:
                        print("补卡成功，请牢记卡号：%s" %(self.allUsers[i].card.cardID))
                        input("牢记后按任意键继续……")
                        return -1
                    break
                break
        print("信息不匹配，操作失败……")

    #选号
    def choiceCardID(self):
        print("注意：换号费用为 50 RMB。")
        inputCardID = input("请输入卡号：")
        if self.checkLock(inputCardID):
            return -1
        if not self.userLogin(inputCardID):
            return -1
        cardIDLIst = []
        for i in range(9):
            cardIDLIst.append(self.createCardID())
        print("----------------------可供选择----------------------\n")
        for i in range(0, 9, 3):
            if int(i) % 3 == 0 and int(i) != 0:
                print("\n")
            print("%d：%s        %d：%s       %d：%s" % (int(i + 1), cardIDLIst[i], int(i + 2), cardIDLIst[i + 1], int(i + 3), cardIDLIst[i + 2]))
        print("\n----------------------------------------------------\n")
        choice = int(input("请选择新卡号(输入编号)："))
        print("换号费用为 50 RMB，换号后，原卡号将被注销！！！")
        if not self.confirmOperation():
            print("---------------------取消成功！！---------------------")
            return -1
        if choice in range(1, 10):
            self.allUsers[cardIDLIst[choice - 1]] = self.allUsers.pop(inputCardID)
            print("换号成功！！新卡号为：%s" %(cardIDLIst[choice - 1]))
            input("牢记卡号后，按任意键继续……")
            return -1
        print("输入有误！！操作失败……")
        return -1

    #销户
    def deleteUser(self):
        cardID = input("请输入卡号：")
        if self.checkLock(cardID):
            return -1
        if not self.userLogin(cardID):
            return -1
        idCard = input("请输入身份证号：")
        if self.allUsers[cardID].idCard != idCard:
            print("身份证号不匹配！！销户失败……")
            return -1
        print("账户信息正确！！")
        print("------------------！！注意！！------------------")
        print("销户后，您的账户将不存在(包括目前余额)！！！")
        if not self.confirmOperation():
            print("------------------取消成功！！------------------")
            return -1
        del(self.allUsers[cardID])
        print("努力销户中……")
        sleep(2)
        print("-------------------销户成功！！-------------------")
        print("感谢您的使用，欢迎您再次开户。")

    #验证密码
    def checkPasswd(self, passwd, times = 3):
        if times > 0:
            tmpPasswd = input("请再次输入密码：")
            if tmpPasswd == passwd:
                return True
            times -= 1
            self.checkPasswd(passwd, times)
        return False

    #随机生成卡号
    def createCardID(self):
        while True:
            ID = ""
            for i in range(6):
                ch = chr(randrange(ord("0"), ord("9")))
                ID += ch
            if ID not in self.allUsers:
                return ID

    #判断金额是否合法
    def checkMoney(self, money, times = 2):
        if times > 0:
            if money >= 0:
                return True
            tmpMoney = input("金额错误！！请再次输入：")
            times -= 1
            self.checkMoney(tmpMoney, times)
        return False

    #卡号密码登录
    def userLogin(self, cardID, times = 2):
        if cardID not in self.allUsers:
            print("查无此人！！操作失败……")
            return False
        inputPassWd = input("请输入密码：")
        while times > 0:
            if inputPassWd == self.allUsers[cardID].card.cardPasswd:
                return True
            else:
                print("密码错误！！ %d 次错误后该卡将被锁定！" % (times))
                times -= 1
                inputData = input("请输入密码：")
        self.allUsers[cardID].card.lock = True
        print("密码错误！！该卡已被锁定，请尽快解锁……")
        return False

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

    #重复操作确认
    def confirmRepeat(self):
        choice = input("是否继续操作？(yes / no)： ")
        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("输入有误！！操作结束……")
            return False

    #检查锁定状态
    def checkLock(self, cardID):
        if cardID not in self.allUsers:
            print("查无此人！！操作失败……")
            return True
        if self.allUsers[cardID].card.lock:
            print("该卡已被锁定，请尽快解锁！！")
            return True
        return False

    #检查电话号码
    def checkPhoneNum(self, phoneNum):
        if phoneNum.isdigit() and len(phoneNum) == 4:
            return True
        print("输入有误！！操作失败……")
        return False

    #输入并检查身份证号
    def checkIdCard(self, idCard):
        if idCard.isdigit() and len(idCard) == 8:
            return True
        print("输入有误！！操作失败……")
        return False

    #输入并检查密码
    def checkCardPasswd(self, cardPasswd):
        if cardPasswd.isdigit() and len(cardPasswd) == 6:
            return True
        print("输入有误！！操作失败……")
        return False
