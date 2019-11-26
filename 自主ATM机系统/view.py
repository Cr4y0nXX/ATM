#管理员
class View(object):
    #打印首界面
    def printFirstView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*                                                 *")
        print("*                 工科学生死板板                   *")
        print("*                     ATM机                       *")
        print("*                                                 *")
        print("*                                                 *")
        print("***************************************************")

    #打印系统界面
    def printSystemView(self):
        print("***************************************************")
        print("*                                                 *")
        print("*      开户(open)               查询(search)      *")
        print("*      取款(withdraw)           存款(deposit)     *")
        print("*      转账(transfer)           改密(change)      *")
        print("*      锁定(lock)               解锁(unlock)      *")
        print("*      补卡(reissue)            换号(choice)      *")
        print("*      销户(delete)             更多(more)        *")
        print("*                    退出(quit)                   *")
        print("*                                                 *")
        print("***************************************************")

    #打印管理员操作界面
    def printAdminView(self):
        print("***************************************************")
        print("*                 请您谨慎操作！！！              *")
        print("*                                                 *")
        print("*      查询信息(search)       查看数据(all)       *")
        print("*      删除用户(delOne)       清空数据(delAll)    *")
        print("*                                                 *")
        print("*                   退出(quit)                    *")
        print("*                                                 *")
        print("***************************************************")



