import datetime

def C_cipher(messeage, day):
   code = ""
   
   for ch in messeage:
      ordvalue = ord(ch) #stores the  value of the character
      cipherValue = ordvalue + day #stores the new value of the character changing it by the day
      if cipherValue > ord('z'): #if the new value is greater than the value of z it will wrap around to a
         cipherValue = ord('a') + day - \
                       (ord('z') - ordvalue + 1)
      code += chr(cipherValue) #stores the new character in the code variable

   return code #returns the code variable
      
def main():
   current = datetime.datetime.now()
   day = current.day #stores the day

   messeage = input("Enter your messeage to be encoded: ")
      
   print (C_cipher(messeage, day))

      


main()