import os
import json


if __name__ == '__main__':
    root_dict = {'Engineering': 127413603,
                 'Medicine': 71924100,
                 'Computer Science': 41008148,
                 'Materials Science': 192562407,
                 'Biology': 86803240,
                 'Chemistry': 185592680}
    root_list = [192562407, 127413603, 71924100, 41008148, 86803240, 185592680]
    # C:\Users\锴\Desktop\Materials_Science_top100\192562407
    path = os.path.join('C://', 'Users', 'xzk09', 'Desktop', 'Biology_top100', '86803240')
    file_list = os.listdir(path)
    print(len(file_list))
    count = 0
    res_set = set()
    for file in file_list:
        count += 1
        print('%d/%d' % (count, len(file_list)))
        file_name = os.path.join(path, file)
        with open(file_name, 'r') as fr:
            for line in fr:
                author_id = int(line)
                if author_id not in res_set:
                    res_set.add(author_id)
    res_list = list(res_set)
    print(len(res_set))
    with open('86803240', 'w') as fw:
        json.dump(res_list, fw)


