import sys
import filetohash

if len(sys.argv) != 2:
    print("引数エラー")
flag = True
filename = sys.argv[1]
argfilehash = filetohash.filetohash(filename)
f = open("main.uhl","r")
uhl_list = f.read().split("\n")
f.close()
for uhl in uhl_list:
    if uhl == argfilehash:
        print("ウイルススキャンに引っかかりました")
        flag = False
        break

if flag == True:
    print("問題はありません。")
