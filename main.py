#caesar-cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue = True

while continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
  text = input("Type your message:").lower()
  shift = int(input("Type the shift number:"))
  
  
  def cesar(sh = shift, te = text, dir = direction):
    mes = ""
    for i in range(len(te)):
      for j in range(len(alphabet)):
        if alphabet[j] == te[i]:
          if dir == "encode":
            if j+sh >= len(alphabet):
              mes += alphabet[ (j + sh) - len(alphabet)]  
            else:
              mes += alphabet[j+sh] 
            break
          else:
            if j - sh < 0:
              mes += alphabet[len(alphabet) - (sh - j)]  
            else:
              mes += alphabet[j - sh] 
            break
    return mes
  
  print(cesar())
  cont = input("Want to continue?(yes/no)").lower
   if(cont == "yes"):
     continue = True
   else:
     continue = False


  
