import tika
tika.initVM()
from tika import parser
parsed = parser.from_file("/Users/zackamiton/Code/PythonNonsense/IBDCrawler/output/Computer Science/2019 November Examination Session/Computer_science_paper_2__HL.pdf")
print(list(filter(None, parsed['content'].split("\n"))))