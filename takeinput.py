import re
a="Sand Str 107, 64319 Pfungstadt"
result=re.findall("[0-9]{5}",a)[0]
print(result)