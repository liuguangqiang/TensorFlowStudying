import json
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fm = matplotlib.font_manager

# set default font
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'

with open("jjc27.json") as json_file:
    data = json.load(json_file)
    dict = {}
    for item in data["data"]:
        force = item["personInfo"]["force"]
        dict[force] = dict.get(force, 0) + 1

    label, count = [], []

    for i in dict.keys():
        label.append(i)
        count.append(dict[i])

    fig = plt.figure()
    plt.bar(label, count, width=0.7, align="center")
    plt.title(u'第27周33竞技场 1-200个人排行')
    plt.ylabel(u'人数')
    plt.xlabel(u'门派')
    for a, b in zip(label, count):
        plt.text(a, b, "%d" % b, ha="center", va="bottom", fontsize=10)

    plt.show()