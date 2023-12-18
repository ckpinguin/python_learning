alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
  result = ""
  
  shift_amount = shift
  if direction == "decode":
    shift_amount = shift * -1
      
  for char in text:
    position= alphabet.index(char)
   
    new_position = (position + shift_amount) % len(alphabet)
    result += alphabet[new_position]
    
  print(f"The {direction}d text is {result}")

caesar(text, shift, direction)

exit(0)