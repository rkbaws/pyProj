import re
ptrn=r'[A-Za-z0-9_.-]+@[A-Za-z0-9]+\.(com|net)'
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

for each_match in matching_ptrn:
    print(each_match)
    