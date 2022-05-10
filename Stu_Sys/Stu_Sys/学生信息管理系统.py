# 开发者： 陈家奇
# 开发时间： 2022/2/12 19:03

'''学生信息管理系统分为三个对象：用户、菜单、功能
功能分为:
（一）学生信息维护
1.录入学生信息
2.删除学生信息
3.修改学生信息
（二）查询/统计
1.按学生id查找
2.显示所有学生信息并统计学生人数
（三）排序（升序及降序）
1.根据高数成绩排序
2.根据英语成绩排序
3.根据Python成绩排序
4.根据C语言成绩排序
4.根据总成绩排序
'''

info_list=[]


def menu():
    print('='.ljust(44,'='))
    print("学生管理系统".center(40,'-'))
    print("1.录入学生信息".center(40))
    print("2.删除学生信息".center(40))
    print("3.修改学生信息".center(40))
    print("4.查找指定学生".center(40))
    print("5.显示学生信息".center(40))
    print("6.成绩排序  ".center(40))
    print("7.导出学生信息".center(40))
    print("0.退出系统  ".center(40))
    print('='.ljust(44, '='))


def fun():
    upload()  #从文件中读取信息到操作的列表中
    while True:
        menu()
        choice=int(input("请选择想使用的功能：>"))
        if choice==1:
            enter()
            save()
        elif choice==2:
            delete()
            save()
        elif choice==3:
            modify()
            save()
        elif choice==4:
            search()
        elif choice==5:
            show()
        elif choice==6:
            sort()
            save()
        elif choice==7:
            impo()
        elif choice==0:
            if input("是否退出：>Y/N\n").upper()=='Y':
                print("退出系统，感谢您的使用")
                break
            else:
                continue
        else:
            continue


def upload():
    global info_list
    try:
        pf=open("info.txt",'r',encoding='utf-8')
        info_list = pf.readlines()
    except:
        pass


def save():
    if input("是否保存：>Y/N\n").upper()=='Y':
        pf=open("info.txt",'w',encoding='utf-8')
        for item in info_list:
            if item:
                print(str(item).strip('\n'), file=pf)
        print("保存成功")
        pf.close()
    else:
        print("取消保存")


def enter_plug(id):
    try:
        name = input("请输入学生姓名：>")
        math = float(input("请输入高数成绩：>"))
        if math < 0 or math > 100:
            print("输入成绩无效，请重新输入")
            math = float(input("请输入高数成绩：>"))
        english = float(input("请输入英语成绩：>"))
        if english < 0 or english > 100:
            print("输入成绩无效，请重新输入")
            english = float(input("请输入英语成绩：>"))
        python = float(input("请输入Python成绩：>"))
        if python < 0 or python > 100:
            print("输入成绩无效，请重新输入")
            python = float(input("请输入Python成绩：>"))
        c_grade = float(input("请输入C语言成绩：>"))
        if c_grade < 0 or c_grade > 100:
            print("输入成绩无效，请重新输入")
            c_grade = float(input("请输入C语言成绩：>"))
        sum = math + english + python + c_grade
        info = {'id': id, 'name': name, 'math': math, 'english': english, 'python': python, 'c_grade': c_grade,
                'sum': sum}
        # noinspection PyTypeChecker
        info_list.append(str(info))#因为sort操作的是info_list()中的元素，则如果先录入在排序，该元素会为字典类型，
        # 而eval()函数的参数要求是字符窜str类型，则会报错，则在添加该字典时就将其转换为str类型添加
    except:
        print("输入无效，请重新输入")


def enter():
    while True:
        id = int(input("请输入学生学号：>"))
        for item in info_list:
            if eval(item)['id']==id:
                if input("该学生已存在，是否重新录入：>Y/N\n").upper()=='Y':
                    info_list.remove(item)
                    enter_plug(id)
                else:
                    print("取消录入")
                break
        else: #说明该学号没有录入
            enter_plug(id)
        if input("是否继续录入：>Y/N\n").upper()=='N':
            break


def delete():
    while True:
        if info_list:
            target_id=int(input('请输入删除学生的学号：>'))
            for item in info_list:
                if eval(item)['id']==target_id:  #因为readlines()返回的是一个字符串列表，
                    info_list.remove(item)      #则列表的元素为一个字符串，利用eval()函数将字符串转为字典
                    print("删除成功")
                    break
            else:
                print("该学生不存在")
            if input("是否继续删除：>Y/N\n").upper()=='N':
                break
        else:
            print("学生信息为空，请先录入信息")


def modify():
    while True:
        if info_list:
            target_id = int(input('请输入修改学生的学号：>'))
            for item in info_list:
                if eval(item)['id']==target_id:
                    info_list.remove(item)    #删除的是info_list里的元素，不是item，item成为了一个新的对象
                    enter_plug(target_id)
                    print("修改成功")
                    break
            else:
                print("该学生不存在")
            if input("是否继续修改：>Y/N\n").upper()=='N':
                break
        else:
            print("学生信息为空，请先录入信息")


def search():
    while True:
        if info_list:
            target_id = int(input('请输入查找学生的学号：>'))
            for item in info_list:
                if eval(item)['id']==target_id:
                    format_title = '{:^6}\t{:^6}\t{:^8}\t{:^8}\t{:^10}\t{:^9}\t{:^8}'
                    print(format_title.format("学 号", "姓  名", "高数成绩", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
                    format_data = '{:^6}\t  {:^8}\t {:^8}\t {:^8}\t{:^10}\t {:^9}\t {:^8}'
                    print(format_data.format(eval(item)['id'],eval(item)['name'],eval(item)['math'],eval(item)['english'],
                                             eval(item)['python'], eval(item)['c_grade'], eval(item)['sum']))
                    break
            else:
                print("该学生不存在")
            if input("是否继续查找：>Y/N\n").upper()=='N':
                break
        else:
            print("学生信息为空，请先录入信息")


def show_plug(lis):
    format_title = '{:^6}\t{:^8}\t{:^8}\t{:^8}\t{:^10}\t{:^9}\t{:^8}'
    print(format_title.format("学 号", "姓  名", "高数成绩", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    for item in lis:
        try:
            if item:
                format_data = '{:^6}\t{:^8}\t {:^8}\t {:^8}\t{:^10}\t {:^9}\t {:^8}'
                print(format_data.format(eval(item)['id'],eval(item)['name'],eval(item)['math'],eval(item)['english'],
                                         eval(item)['python'], eval(item)['c_grade'], eval(item)['sum']))
        except:
            continue


def show():
    try:
        sort_pf=open("info.txt",'r',encoding='utf-8')
        lis=sort_pf.readlines()
        if not lis:
            print("学生信息为空，请先录入信息")
            return
        print("学生总人数为：%d人".rjust(71) % len(lis))
        show_plug(lis)
        sort_pf.close()
    except:
        print("学生信息为空，请先录入信息")


def sort_plug(flag):
    sign=1
    choice = int(input("请选择是升序还是降序：>0/1\n"))
    '''
    for i in range(len(info_list) - 1):
        for j in range(len(info_list) - 1 - i):
            if choice==0:
                if eval(info_list[j])[flag]>eval(info_list[j+1])[flag]:
                    info_list[j],info_list[j+1]=info_list[j+1],info_list[j]
                    sign=0
            elif choice==1:
                if eval(info_list[j])[flag] < eval(info_list[j+1])[flag]:
                    info_list[j],info_list[j+1]=info_list[j+1],info_list[j]
                    sign=0
        if sign:#一趟排序完都没有更改说明已经排序完全了，则不需要再拍了，退出循环
            break
        '''
    if choice==0:
        info_list.sort(key=lambda x:eval(x)[flag])
    else:
        info_list.sort(key=lambda x:eval(x)[flag],reverse=True)


def impo_grade():
    ranking=1
    pf=open("成绩单.xlsx",'w')
    print("成 绩 单".center(60), file=pf)
    print("学 号", "姓  名", "高数成绩", "英语成绩", "Python成绩", "C语言成绩", "总成绩", "排 名", sep='\t', file=pf)
    for item in info_list:
        if item:
            print(eval(item)['id'], eval(item)['name'], eval(item)['math'], eval(item)['english'],
                  eval(item)['python'],
                  eval(item)['c_grade'], eval(item)['sum'], ranking, sep='\t', file=pf)
            ranking += 1
    pf.close()


def sort():
    while True:
        choice = int(input("请选择排序依据：>(高数: 1 / 英语: 2 / Python: 3 / C语言：4 / 总成绩：5)\n"))
        if choice==1:
            sort_plug('math')
            show_plug(info_list)
        elif choice==2:
            sort_plug('english')
            show_plug(info_list)
        elif choice==3:
            sort_plug('python')
            show_plug(info_list)
        elif choice==4:
            sort_plug('c_grade')
            show_plug(info_list)
        elif choice==5:
            sort_plug('sum')
            show_plug(info_list)
        else:
            print("选择无效，请重新选择")
        if input("是否重新排序：>Y/N\n").upper()=='N':
            if input("是否导出成绩单：>Y/N\n").upper()=='Y':
               impo_grade()
               print("成功导出文件 成绩单.xlsx")
            break


def impo():
    try:
        sort_pf=open("info.txt",'r',encoding='utf-8')
        pf=open("学生信息.xlsx",'w')
        lis=sort_pf.readlines()
        print("学 生 信 息".center(60),file=pf)
        print("学号", "姓名", "高数成绩", "英语成绩", "Python成绩", "C语言成绩","总成绩",sep='\t',file=pf)
        for item in lis:
            try:
                if item:
                    print(eval(item)['id'],eval(item)['name'],eval(item)['math'],eval(item)['english'],eval(item)['python'],
                          eval(item)['c_grade'],eval(item)['sum'],sep='\t',file=pf)
            except:
                continue
        print("\n",file=pf,end='')
        print("学生总人数为：%d人".rjust(60) % len(lis),file=pf)
        sort_pf.close()
        pf.close()
        print("成功导出文件 学生信息.xlsx")
    except:
        print("学生信息为空")


if __name__=='__main__':
    fun()
