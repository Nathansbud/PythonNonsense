

if __name__ == '__main__':
    names = {"Hello":"Amiton", "Sup":"Amiton", "Zack":"Amiton", "Hi":"Zinner", "Sir":"Zinner"}
    last_name_dict = {last_name:[] for last_name in names.values()}
    for k, v in names.items():
        last_name_dict[v].append(k)
    print(last_name_dict)
