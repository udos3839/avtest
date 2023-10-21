import sys
import filetohash

if len(sys.argv) != 2:
    print("引数が足りません！")

filename = sys.argv[1]
filehash = filetohash.filetohash(filename)
f = open("main.uhl","a")
f.write(f"{filehash}\n")
f.close()
print("追加しました")
