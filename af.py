#! pyhton3
#autofill.py-program for getting all id
import shelve ,os,sys,pyperclip
os.chdir("D:\\python_programme_files")  #it ensures datafilesforaf are in a particular folder
data=shelve.open('datafileforaf')
if len(sys.argv)<2:
    print('usage\:python af.py [account]-copy account password')
    sys.exit()

account=sys.argv[1]
if len(sys.argv)==2: #for copying entries
    if account in data:
        pyperclip.copy(data[account])
        print('data copied for '+account+'to the clipcoard')
    elif account=="showall":
        a=list(data.keys())
        print(a)
    elif account not in data:
        print("no presaved value for the keyword"+" "+account)
if len(sys.argv)==4:#for saving new entries
    if account=='save': 
        data[sys.argv[2]]=sys.argv[3]
        print('value saved')
    else:
        print("something is wrong\!\!\!")
if len(sys.argv)==3:#for del any entry
    if account=='del' and sys.argv[2] in data:
        del data[sys.argv[2]]
        print('value deleted successfully')
    else:
        print("something is wrong\!\!\!")    
data.close()