import re

if __name__ == '__main__':
    with open("/Users/zackamiton/Downloads/QuidelSavanna.vdx") as xml:
        data = "".join(xml.readlines())

    print(re.match("<ForeignData(.*?)</ForeignData>", data))

    """            
    unimaged = re.sub(r"(?<=<ForeignData)(.*?)(?=</ForeignData>)", "", data)
    with open("/Users/zackamiton/Downloads/QuidelSavanna.vdx", "w+") as xml:
        xml.write(unimaged)
"""