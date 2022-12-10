from csv import DictReader, DictWriter
import re

with open("/Users/zackamiton/Downloads/thank_youuu__3333/FNSouzaProcess.txt") as f1:
    lines = f1.readlines()
    pieces = []
    
    cp = {}
    field_names = set()
    for l in lines:
        cl = l.strip()
        split_row = re.split("\t|\s:\s", cl)
        if cl != "":
            field_name = split_row[0].rstrip(": ")
            cp[field_name] = " ".join(split_row[1:]).strip()
            field_names.add(field_name)
        else:
            if cp != {}:
                cp = {}
                pieces.append(cp)
            else:
                continue

with open("/Users/zackamiton/Downloads/thank_youuu__3333/FNSouzaProces.csv", "w+") as f2:
    writer = DictWriter(f2, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(pieces)