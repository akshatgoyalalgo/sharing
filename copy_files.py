import shutil

f = open('/home/akshat/program/testing_extract/copy_files.txt', 'r')

wr = open('/home/akshat/program/testing_extract/copied_files.txt','w+')
# lines = f.readline()
# print(f.readline())

i=0
for name in f:
    print(name)
    try:
        s = "/home/akshat/extract/Srini1300/" + name[:-1]+".pdf"
        
        # f=open(s,'r')
        
        
        # f.close()
        # wr.write(name)
        # wr.write('\n')
        shutil.copy(s, "/home/akshat/program/testing_extract/copied_files") 
        i+=1
    except Exception as e:
        print(e)

wr.close()
print(i)