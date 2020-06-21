
def getDatas():
    url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
    data = requests.post(url).json()["data"]
    country_list= [] # 国家
    totoal_case_list= [] # 累计确诊
    dead_case_list= [] # 死亡数
    new_case_list= [] # 新增确诊
    for item in data:
        country_list.append(item["name"]) 
        totoal_case_list.append(int(item["confirm"]))
        dead_case_list.append(int(item["dead"]))
        new_case_list.append(int(item["confirmCompare"]))

    
    print(country_list[:10])
    print(totoal_case_list)
    print(dead_case_list)
    print(new_case_list)
    # plt.plot(country_list[:10],new_case_list[:10],label="新增确诊数")
    # plt.plot(country_list[:10],dead_case_list[:10],label="死亡数")
    # plt.plot(country_list[:10],totoal_case_list[:10],label="累计确诊数")
    # plt.title('前十个国家累计确诊条形统计图')
    # plt.legend()
    # plt.show()
    # x = np.arange(20,2)
    # bar_width = 0.35
    # plt.bar(x, new_case_list[:10], bar_width, align="center", color="c", label="班级A", alpha=0.5)
    # plt.bar(x+bar_width, dead_case_list[:10], bar_width, color="b", align="center", label="班级", alpha=0.5)
    # plt.bar(x+2*bar_width, dead_case_list[:10], bar_width, color="r", align="center", label="班级", alpha=0.5)

    # plt.legend()
    # plt.show()

# getDatas()