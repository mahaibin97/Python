#通过遍历对文件进行copy

def main():

      f1=input("Please enter one souce file's name:").strip()
      f2=input("Please enter one destination file's name:").strip()

      file1=open(f1,"r")
      file2=open(f2,"w")

      #copy the souce file
      countLines=countChars=0
      for line in file1:
            countLines +=1
            countChars +=len(line)
            file2.write(line)

      print(countLines,"lines and",countChars,"chars copied")

      file1.close()
      file2.close()

main()
