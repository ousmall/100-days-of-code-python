alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from caesar_logo import logo
print(logo)

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction not in ["encode", "decode"]:
    print("You gave a wrong command, please try again.")
    continue

  
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  
  def caesar(start_text, shift, direction_text):
      end_text = ""
      for char in start_text:
          if char in alphabet:
            position = alphabet.index(char)
            if direction_text == "encode":
              new_position = (position + shift) % 26
            elif direction_text == "decode":
              new_position = (position - shift) % 26 
    
            new_letter = alphabet[new_position]
            end_text += new_letter
          else:
            end_text += char
      print(f"The {direction_text}d text is: {end_text}")

  if direction in ["encode", "decode"]:
      caesar(text, shift, direction)

# this part
  re_run = input("Type 'Yes' if you want to run again, otherwise type 'No' to end it up.\n").lower()
  if re_run == "no":
    print("The conversation ends!")
    break
  elif re_run != "yes":
    print("Invalid input. The conversation ends!")
    break
 # learn from ChatGPT   
