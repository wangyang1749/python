import requests
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

datas = {}

# 显示菜单
def showMenu():
    print("\n")
    print("=" * 30)
    print(" 疫情数据管理系统V0.1   ")
    print(" 1.显示疫情数据信息")
    print(" 2.添加疫情数据信息")
    print(" 3.修改疫情数据信息")
    print(" 4.显示疫情数据折线图")
    print(" 5.显示疫情数据条形图")
    print(" 0.退出系统")
    print("=" * 30)

# 显示疫情数据信息
def showInfo():
    print("{0:5}{1:5}{2:5}{3:5}".format("国家","新增案例","死亡","累计确诊"))
    for key,value in datas.items():
        # print(key,value)
        new_cases,total_deaths,total_cases =value
        print("{0}      {1}      {2}     {3}".format(key,new_cases,total_deaths,total_cases))


# 添加疫情信息
def addRecord():
    while True:
        print("==疫情信息添加==")
        country = input("请输入国名：")
        new_cases = input("请输入新增确诊人数：")
        total_cases = input("请输入死亡人数:")
        total_deaths = input("请输入治愈人数:")
        if country in datas:
            print("[{0}]已经存在不能添加！".format(country))
            continue
        else:
            datas[country] = (int(new_cases),int(total_deaths),int(total_cases))
        quitconfirm = input("回车继续添加，输入yes返回：")
        if quitconfirm =="yes":
            break

# 更新疫情信息
def updateRecord():
    print("==修改==")
    country = input("请输入国名：")
    if country in datas:
        new_cases = input("请输入新增确诊人数：")
        total_cases = input("请输入死亡人数:")
        total_deaths = input("请输入治愈人数:")
        datas[country] = (new_cases,total_deaths,total_cases)
    else:
        print("{0}不存在不能修改".format(country))

def convertList():
    country_list=[]
    new_cases_list=[]
    total_deaths_list=[]
    total_cases_list=[]
    for key,value in datas.items():
        new_cases,total_deaths,total_cases =value

        country_list.append(key)
        new_cases_list.append(new_cases)
        total_cases_list.append(total_cases)
        total_deaths_list.append(total_deaths)
    return country_list,new_cases_list,total_deaths_list,total_cases_list

def bar():
    country_list,new_cases_list,total_deaths_list,total_cases_list = convertList()
    x = np.arange(len(country_list))
    bar_width = 0.35
    plt.bar(x, total_deaths_list, bar_width, align="center", color="c", label="死亡数", alpha=0.5)
    plt.bar(x+bar_width,new_cases_list, bar_width, color="b", align="center", label="新增确诊数", alpha=0.5)
    plt.legend()
    plt.xticks(x+bar_width/2, country_list)
    plt.title('疫情数据统计条形图')
    plt.show()

def plot():
    country_list,new_cases_list,total_deaths_list,total_cases_list = convertList()
    plt.plot(country_list,new_cases_list,label="新增确诊数")
    plt.plot(country_list,total_deaths_list,label="死亡数")
    plt.plot(country_list,total_cases_list,label="累计确诊数")
    plt.title('疫情数据统计折线图')
    plt.legend()
    plt.show()
    
def main():
    while True:
        showMenu()
        key = input("请选择功能（序号）：")
        print("\n")

        if key == '1':
            showInfo()
        elif key == '2':
            addRecord()
        elif key == '3':
            updateRecord()
        elif key == '4':
            plot()
        elif key == '5':
            bar()
        elif key == '0':
            #退出功能，尽量往不退出的方向引
            quitconfirm = input("确定要退出么 （yes或者no）")
            if quitconfirm == 'yes':
                print("欢迎使用本系统，谢谢")
                break
        else:
            print("您输入有误，请重新输入")
    
if __name__ == "__main__":
    main()