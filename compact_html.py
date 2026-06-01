import re
p='revolt-group-website.html'
with open(p,'r',encoding='utf-8') as f:
    s=f.read()
# remove whitespace between tags
s=re.sub(r'>\s+<','><',s)
# optional: trim leading/trailing spaces on lines
s='\n'.join(line.rstrip() for line in s.splitlines())
with open(p,'w',encoding='utf-8') as f:
    f.write(s)
print('Compacted',p)