import datetime

def coder(messeage, day):
   code = ""
   
   for ch in messeage:
      adjusted_shift = day % 26 #stores the remainder of the day divided by 26
      original = ord(ch) #stores the  value of the character
      coded_l = original + adjusted_shift #stores the new value of the character changing it by the day
      if original == ord(' '): #if the character is a space it will stay a space
         coded_l = ord(' ')
      elif coded_l > ord('z'): #if the new value is greater than the value of z it will wrap around to a
         coded_l = ord('a') + adjusted_shift - \
                       (ord('z') - original + 1)
      code += chr(coded_l) #stores the new character in the code variable

   return code #returns the code variable

def decoder(coded_lessage, day):
   decode = ""
   
   for ch in coded_lessage:
      adjusted_shift = day % 26 #stores the remainder of the day divided by 26
      original = ord(ch) #stores the  value of the character
      decoded_l = original - adjusted_shift #stores the new value of the character changing it by the day
      if original == ord(' '): #if the character is a space it will stay a space
         decoded_l = ord(' ')
      elif decoded_l < ord('a'): #if the new value is less than the value of a it will wrap around to z
         decoded_l = ord('z') - adjusted_shift + \
                       (original - ord('a') + 1)
      decode += chr(decoded_l) #stores the new character in the decode variable

   return decode #returns the decode variable
      
def main():
   current = datetime.datetime.now()
   day = current.day #stores the day

   answer =  input( "would you like to (1)encode or (2)decode a messeage? please enter 1 or 2:  ")

   if answer == 1: #if the user wants to encode a messeage
      messeage = input("Enter your messeage to be encoded: ")

      coded_lessage = coder(messeage, day)
   else :
      messeage = input("Enter your messeage to be decoded: ")

      coded_lessage = decoder(messeage, day)

   coded_lessage = coder(messeage, day) #stores the coded message
      
   print ("Your coded messeage is: ", coded_lessage)

      


main()