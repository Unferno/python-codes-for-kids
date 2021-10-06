#how to access our directory
import os;
print(os.getcwd());
os.chdir("d:\\python");
print(os.getcwd());
print(os.listdir());
print(os.listdir(".")) # dot "." means present working directory

if (not "data" in os.listdir()):
    os.mkdir("data");
else:
    print("data folder already exist. you cant create it again")
    
    
