import re
ptrn=r'[A-Za-z0-9_.-]+@[A-Za-z0-9]+\.(com|net)'
ptrn1=r'[A-Za-z0-9_.-]+@[A-Za-z0-9]+\.'


string_to_search='''
gygvhuqei
random.random@ram.com
hujik random.random@ram.com
fajftugiybhnij56789@gmail.com
abc@b.com
drtcyftgbyhnjmk@dbc.net
'''

string_to_search1='fajftugiybhnij56789@gmail.com dfnavk avek'

ptrn_obj=re.compile(ptrn)

matching_ptrn=ptrn_obj.finditer(string_to_search)
match_all=re.findall(ptrn1, string_to_search)

srch=ptrn_obj.search(string_to_search)
mtch2=ptrn_obj.match(string_to_search1)
if srch:
    print("found the match")

print("match2:",mtch2)

print(match_all)

for each_match in matching_ptrn:
    print(each_match)
    