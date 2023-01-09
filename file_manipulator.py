import sys

length = len(sys.argv)
print("Check input Argument : " + str(len(sys.argv)))

commandType = sys.argv[1]

# command'reverse': inputpathにあるファイルを受け取り、
# outputpathにinputpathの内容を逆にして新しいファイルを作成。
# 実行時、引数に　reverse inputpath outputpath の順番で渡す。 
if commandType == "reverse":
    if length != 4:
        print("Argument error!!")
        print("You need 4 arguments.")
        sys.exit()
    else:
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        try:
            with open(inputpath, "r") as f:
                content = f.readlines()

            with open(outputpath, mode="w") as f:
                reversedContent = ''.join(reversed(content))
                f.write(str(reversedContent))
                print("All done!!")

        except FileNotFoundError:
            print("Inputfile can not find")
            sys.exit()

# command 'copy': inputpathのファイルのコピーを作成し、outputpathとして保存する。
# ファイルが存在する場合はエラーを返す。
# 実行時、引数に　copy inputpath outputpath の順番で渡す。 
elif commandType == "copy":
        if length != 4:
            print("Argument error!!")
            print("You need 4 arguments.")
            sys.exit()
        else:
            inputpath = sys.argv[2]
            outputPath = sys.argv[3]
            try:
                with open(inputpath, "r") as f:
                    content = f.read()

                with open(outputPath, mode="x") as f:
                    f.write(str(content))
                    print("All done!!")

            except FileNotFoundError:
                print("InputFile" + " " + inputpath + " " + "not exists !!!")
                sys.exit()

            except FileExistsError:
                print("OutputText.txt" + " " + outputPath + " " + "exists!!!")
                sys.exit()

# command 'duplicate-contents': inputpathの内容を読み込み、
# その内容を複製し複製された内容をinputpathのファイルにn回複製する。
# 実行時、引数に duplicate-contents inputpath n の順番で渡す。 
elif commandType == "duplicate-contents":
    if length != 4:
        print("Argument error!!")
        print("You need 4 arguments.")
        sys.exit()
    else:
        inputpath = sys.argv[2]
        duplicateCount = sys.argv[3]
        try:
            with open(inputpath, mode="r") as f:
                content = f.read()

            for i in range(int(duplicateCount)):
                with open(inputpath, mode="a") as f:
                    f.write("\n" + content)
            print("All done!!")

        except ValueError:
            print("Check Value!!!")
            sys.exit()
        
        except FileNotFoundError:
            print("InputFile" + " " + inputpath + " " + "not exists !!!")
            sys.exit()

# command 'replace-string': inputpathの内容から文字列’needle’を検索し、
# 'needle'すべてを'newstring'に置き換える。
# 実行時、引数に replace-string inputpath needle newstring の順番で渡す。 
elif commandType == "replace-string":
    if length != 5:
        print("Argument error!!")
        print("You need 5 arguments.")
        sys.exit()
    else:
        inputpath = sys.argv[2]
        needle = sys.argv[3]
        newstring = sys.argv[4]
        try:
            with open(inputpath, mode="r") as f:
                content = f.read()
            
            with open(inputpath, mode="w") as f:
                if needle in content:
                    modify = content.replace(needle, newstring)
                    f.write(modify)
                    print("All done!!")
                    
        except FileNotFoundError:
            print("InputFile" + " " + inputpath + " " + "not exists!!!")
            sys.exit()
else:
    print("Command" + " " + commandType +" " + "error!!")