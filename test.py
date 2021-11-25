import re


a = "屯溪大桥冲毁	https://www.bilibili.com/video/BV17g4y1i7ck?from=search&seid=5443946739813685612&spm_id_from=333.337.0.0"

result = re.findall('(.*)(https:.*)',a)
print(result)