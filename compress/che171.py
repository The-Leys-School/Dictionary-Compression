#from termcolor import cprint
original = "Silence. Gradually the sound of distant traffic becomes audible. A LOW ANGLE bounded on one side by a chain-link fence and on the other by the one-story public school buildings. Spray-can hieroglyphics and distant streetlight shadows. This is a Los Angeles public school in a blue collar neighborhood. SLOW PAN as the sound of stray electrical CRACKLING subsides. FRAME comes to rest on the figure of a NAKED MAN kneeling, faced away, in the previously empty yard. He stands, slowly. The man is in his late thirties, tall and powerfully built, moving with graceful precision. CLOSEUP - MAN, his facial features reiterate the power of his body and are dominated by the eyes, which are intense, blue and depthless. His hair is military short. This man is the TERMINATOR."
neworiginal = original.lower()
with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]


def compress(text):
  text = text.split()
  new = []
  for word in text:
    fstop = False
    comma = False
    up = False
    fup = False
    if word.isupper():
      up = True
    elif word[:1].isupper() and len(word) >= 1:
      fup = True
    for cha in word:
      if cha == ',':
        comma = True
      elif cha == '.':
        fstop = True
    if up == True:
      word = '#'+ word.lower()
    elif fup == True:
      word = '*'+ word.lower()
    
    if fstop == True:
      new.append(word[:-1])
      new.append('^^')
    elif comma ==True:
      new.append(word[:-1])
      new.append('^')
    else:
      new.append(word)

    hahapoor = new
    buf = []
    bells = []
    for word in hahapoor:
        if word in dictionary:
            i = dictionary.index(word)
            token = '\0' + str(chr(i))
            buf.append(token)
            bells.append(token)
        else:
            buf.append(word)
            bells.append(word)

    compressed = ' '.join(buf)
    return compressed

'''
idk = ' '.join(bells)

for number in range(len(buf)):
  try:
    if buf[number+1]=='^^':
      buf[number]=buf[number]+'.'
      buf.pop(number+1)
    elif buf[number+1]=='^':
      buf[number]=buf[number]+','
      buf.pop(number+1)
  except IndexError:
    pass
 
compressed = ' '.join(buf)

compression_ratio = 100 * len(compressed) / len(original)

cprint(original,'cyan')
cprint('--------------------------------------------------------------','red')
print(compressed)
cprint('--------------------------------------------------------------','red')
print(f'{len(compressed)} / {len(original)} ➞ {compression_ratio:.1f}%')
'''

def decompress(data):
    #ded = idk.split()
    ded = data.split()
    lol = []
    #print(ded)
    for word in ded:
      if not word.isalpha():
        i = dictionary[(ord(word[-1]))]
      else:
        i = word
      lol.append(i)
    finish = ' '.join(lol)
    return finish
