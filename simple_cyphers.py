alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def caesar_decode(sentence,offset):
  char_list = []
  for char in sentence:
    if char in alphabet:
      index = alphabet.index(char)
      shifted = index + offset
      if shifted <= 25:
        char_list.append(alphabet[shifted])
      else:
        char_list.append(alphabet[shifted % 26])
    else:
      char_list.append(char)
  
  final_string = "".join(char_list)
  return final_string

def caesar_encode(sentence,offset):
  char_list = []
  for char in sentence:
    if char in alphabet:
      index = alphabet.index(char)
      shifted = index - offset
      char_list.append(alphabet[shifted])
    else:
      char_list.append(char)
  final_string = "".join(char_list)
  return final_string


def vigenere_decode(sentence,keyword):
  char_list = []
  length = len(keyword)
  count = 0
  sentence = sentence.lower()
  keyword = keyword.lower()
  for char in sentence:
    if char in alphabet:
      shift = alphabet.index(char) + alphabet.index(keyword[count % length])
      char_list.append(alphabet[shift % 26])
      count += 1
    else:
      char_list.append(char)

  final_string = ''.join(char_list)
  return final_string


def vigenere_encode(sentence,keyword):
  char_list = []
  length = len(keyword)
  count = 0
  sentence = sentence.lower()
  keyword = keyword.lower()
  for char in sentence:
    if char in alphabet:
      shift = alphabet.index(char) - alphabet.index(keyword[count % length])
      char_list.append(alphabet[shift])
      count += 1
    else:
      char_list.append(char)

  final_string = ''.join(char_list)
  return final_string

print(vigenere_encode("Callum is super duper gay","nutsack"))
print(vigenere_decode("pgstuk yf ybxep thvlz gyo","nutsack"))



