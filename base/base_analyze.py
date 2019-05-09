import yaml

def analyze_data(file_name,case_key):
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f)[case_key]
        data_list = []
        data_list.extend(data.values())
        return data_list






# •extend
# 只能添加可迭代对象的元素
# 会对可迭代对象进行最小单元拆分, 依次保存到列表中





# import yaml
# with open("../data/message_data.yaml","r") as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)["test_send_message"]
#     print(data)
#     print("---"*30)
#     data_list = list()
#     print(type(data.values()))
#     print(data.values())
#     print("---" * 30)
#     for i in data.values():
#         data_list.append(i)
#     print(data_list)
#     # 结果: [{'name': 'xiaohua', 'phone': '18800000001'}, {'name': 'xiaoxiao', 'phone': '18800000002'}]  列表嵌套字典,列表中的每个字典代表一个元素



