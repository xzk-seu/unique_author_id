import json


if __name__ == '__main__':
    with open('86803240', 'r') as fr:
        js = json.load(fr)
    print(len(js))
    with open('86803240.txt', 'w') as fw:
        for i in js:
            fw.write(str(i)+'\n')
