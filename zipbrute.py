import zipfile
from tqdm import tqdm

wordlist = "rockyou.txt"
zip_file = input("Enter the file : ")
zipfile = zipfile.ZipFile(zip_file)
num_lines = sum(1 for i in open(wordlist,'r')
with open(wordlist,'rb') as f:
     for word in tqdm(f,total=num_lines):
         try:
            zipfile.extractall(pwd=word.strip())
         except zipfile.BadZipFile:
            print("The file is not compressed properly)
         except zipfile.LargeZipFile:
            print("Its a really large zipfile")
         else:
            print("[+]Password Found : ",word)
            exit(0)
print("[+]Password Not Found")            
         
