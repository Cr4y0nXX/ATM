
from admin import Admin
from view import View
from card import Card
from atm import ATM
from time import sleep
from os import path, getcwd
from pickle import load, dump
from os import system

def main():
    #读取文件中的用户信息
    allUsers = {}
    filePath = path.join(getcwd(), "alluser.txt")
    if path.getsize(filePath) > 0:
        with open(filePath, "rb") as f:
            allUsers = load(f)

    atm = ATM(allUsers)
    admin = Admin(allUsers)
    view = View()

    # 开机
    view.printFirstView()
    if not admin.boot():
        return -1
    sleep(2)
    system("cls")
    #用户操作
    while True:
        view.printSystemView()
        choice = input("请输入您的选择：")
        if choice == "open":
            atm.openAccount()
        elif choice == "search":
            atm.searchInfor()
        elif choice == "withdraw":
            atm.withdrawals()
        elif choice == "deposit":
            atm.deposit()
        elif choice == "transfer":
            atm.transferMoney()
        elif choice == "change":
            atm.changePasswd()
        elif choice == "lock":
            atm.lock()
        elif choice == "unlock":
            atm.unlock()
        elif choice == "reissue":
            atm.reissueCard()
        elif choice == "choice":
            atm.choiceCardID()
        elif choice == "delete":
            atm.deleteUser()
        elif choice == "more":
            if admin.adminLogin():
                #管理员操作
                while True:
                    view.printAdminView()
                    moreChoice = input("请输入选择(请您谨慎操作！)：")
                    if moreChoice == "search":
                        admin.searchUserInfor()
                    elif moreChoice == "all":
                        admin.showAllUsersInfor()
                    elif moreChoice == "delOne":
                        admin.delOneUser()
                    elif moreChoice == "delAll":
                        admin.delAllUsers()
                    elif moreChoice == "quit":
                        print("操作成功！！正在返回主页面……")
                        sleep(1)
                        break
                    else:
                        print("输入有误！！正在返回主页面……")
                        sleep(1)
                        break
                    system("cls")
        elif choice == "quit":
            print("感谢您的使用！")
            #写入文件
            creatFile(admin.allUsers)
            return 0
        else:
            print("输入有误，请重新选择!!")
        sleep(1)
        system("cls")
#将用户写入文件
def creatFile(dictFile):
    filePath = path.join(getcwd(), "alluser.txt")
    f = open(filePath, "wb")
    dump(dictFile, f)
    f.close()

if __name__ == "__main__":
    main()




