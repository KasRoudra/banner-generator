import time, os, sys
os.system("clear")
print("If you have generated a banner file using generator.py or your banner is between 30th 35th line of file, you can use this.")
time.sleep(2)
path= input("\nEnter file name or path > ")
try:
    with open(path, 'r') as f3:
        lines = f3.readlines()
        with open(path, 'w') as f:
            lines [33] = "'\'\'+purple+'\'\'"+ lines[33]
            lines [34] = "'\'\'+blue+'\'\'"+ lines[34]
            lines [29] = "'\'\'+green+'\'\'"+ lines[29]
            lines [30] = "'\'\'+cyan+'\'\'"+ lines[30]
            lines [31] = "'\'\'+yellow+'\'\'"+ lines[31]
            lines [32] = "'\'\'+red+'\'\'"+ lines[32]
            f.writelines(lines)
            print("\nColor added successfully!")    
except:
    print("File not found.")