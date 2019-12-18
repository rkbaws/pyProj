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

ptrn_obj=re.compile(ptrn)

matching_ptrn=ptrn_obj.finditer(string_to_search)
match_all=re.findall(ptrn1, string_to_search)

srch=ptrn_obj.search(string_to_search)
print("if search is found:", srch)

print(match_all)

for each_match in matching_ptrn:
    print(each_match)
    