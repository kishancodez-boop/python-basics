with open ('mylist.txt','w')as f:
    f.write('apple\nbanana\ncherry\ndate\nelderberry\nfig\ngrape\nhoneydew\n')
    f.truncate(20)
with open('mylist.txt', 'r') as f:
    print(f.read())