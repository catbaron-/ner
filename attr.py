import re
###### Regular expression for features #####
# sequence. e.g. 'A.','a.','1.','A)','a)','1)'.'A).','a).','1).'
seq = re.compile(r"\w((\)\.)|(\))|(\.))")
# two digital number, e.g. '12','33'
d2 = re.compile(r"\b\d{2}\b")   
# four digital number, e.g. '1234','0000'
d4 = re.compile(r"\b\d{4}\b")   
# date. e.g. '1234-12-3','12-3-23','3333/12/2/','00/1/1','2121\2\2','21\1\1'
date = re.compile(r"\b\d{2}(\d{2})?[-/\\]\d{1,2}[-/\\]\d{1,2}\b") #[xx]xx/[x]x/[x]x
# single upper letter and dot. e.g. 'A.'
up = re.compile(r"[A-Z]\.$")

# all upper
au = re.compile(r"\b[A-Z]+\b")
# all digits
ad = re.compile(r"\b[0-9]+\b")
# all lower
al = re.compile(r"\b[a-z]+\b")
# initial upper
iu = re.compile(r"\b[A-Z][a-z]+\b")
# contain digits
cd = re.compile(r".*\d")
# digits and alphabets
da = re.compile(r"^\w+$")
# digits and minus. 
dm = re.compile(r"^((\d+-)|(-+\d))(\d|-)*$")
# digits and slash
ds = re.compile(r"^((\d+/)|(/+\d))(\d|/)*$")
# digits and commo
dc = re.compile(r"^((\d+,)|(,+\d))(\d|,)*$")
# digits and dot 
dd = re.compile(r"^((\d+\.)|(\.+\d))(\d|\.)*$")
# all others
ao = re.compile(r"^\W+$")
# contain upper
cu = re.compile(r".*[A-Z]")
# contain lower
cl = re.compile(r".*[a-z]")
# contain alphabets
ca = re.compile(r".*\w")
# contain others
cs = re.compile(r".*\W")
# '#'
sharp = re.compile(r"[#]")      
# comma
comma = re.compile(r",")
# dot
dot = re.compile(r"\.")
# dollar
dollar = re.compile(r"[$]")
# quote
quote = re.compile(r"'")
# double quote
dquote = re.compile(r"\"")
# left parentheses
lp = re.compile(r"[(<[]")
# right parentheses
rp = re.compile(r"[]>)]")
# final character 
fin = re.compile(r"[.!?]")
# middle character
mid = re.compile(r"[;,:-]")

# Save item(i):value(v) into dict(d)
def addDic(d,i,v):
    for k in i.strip().split():
        d[k] = v

# Read KnownWikiList file into dictionary 
def readKnownList(knownList):
    res = {}
    kl = open("./KnownLists/"+knownList+".lst",'r')
    lines = kl.readlines()
    map(lambda l:addDic(d = res,i = l,v = "True"),lines)
    return res

# Read filename of KnownWikiList from a list, and save them to a dictionary
def readKnownLists(knownLists):
    res = {}
    map(lambda l:addDic(d = res, i = l, v = readKnownList(l)),knownLists)
    return res

# See if the word match a regular express(r)
def isX(r,word):
    re = "True" if r.match(word) else "False"
    #print word+"--"+re
    return re

# Regular Express test 
if __name__ == '__main__':
    #test for r2d
    print "\n###test 2d###"
    r2d_test = ["23","123","12ab"]
    map(lambda x:isX(d2,x) ,r2d_test)

    #test for date
    print "\n### test date ###"
    date_test = ["123",
        "1234\\1\\1","12\\12\\12","abcd\\a\\c",
        "123-1-1","1234-1-1","12-12-12",
        "123/1/1","1234/1/1","12/1/12"]
    map(lambda x:isX(date,x),date_test)

    #test for au
    print "\n### test au ###"
    au_test = ["ABC", "Abc","abc","123"]
    map(lambda x:isX(au,x),au_test)


    #test for ad
    print "\n### test ad ###"
    au_test = ["ABC", "Abc","abc","123"]
    map(lambda x:isX(ad,x),au_test)

    #test for al
    print "\n### test al ###"
    au_test = ["ABC", "Abc","abc","123"]
    map(lambda x:isX(al,x),au_test)

    #test for iu
    print "\n### test iu ###"
    au_test = ["ABC", "Abc","abc","123"]
    map(lambda x:isX(iu,x),au_test)

    #test for cd
    print "\n### test cd ###"
    au_test = ["ABC", "Abc","abc","123"]
    map(lambda x:isX(cd,x),au_test)

    #test for da
    print "\n### test da ###"
    au_test = ["A1BC", "A.bc","abc","123"]
    map(lambda x:isX(cd,x),au_test)
