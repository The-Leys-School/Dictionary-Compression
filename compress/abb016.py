original = '''Silence. Gradually the sound of distant traffic
becomes audible. A LOW ANGLE bounded on one side by a
chain-link fence and on the other by the one-story public
school buildings. Spray-can hieroglyphics and distant
streetlight shadows. This is a Los Angeles public school in
a blue collar neighborhood. SLOW PAN as the sound of stray
electrical CRACKLING subsides. FRAME comes to rest on the
figure of a NAKED MAN kneeling, faced away, in the
previously empty yard. He stands, slowly. The man is in his
late thirties, tall and powerfully built, moving with
graceful precision. CLOSEUP - MAN, his facial features
reiterate the power of his body and are dominated by the
eyes, which are intense, blue and depthless. His hair is
military short. This man is the INTERMINATOR.'''
 
with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]


def compress(original):
  punctuation = [',', '...', '.', '!', '?', ':']
  buffet = []
  for word in original.split():
      eggy = False
      for funk in punctuation:
          if funk in word:
              word = word.rstrip(funk)
              eggy = True
              end = funk
      if word in dictionary:
          i = dictionary.index(word)
          coin = '\0' + str(i)
      elif word.lower() in dictionary:
          i = dictionary.index(word.lower())
          coin = '\u2603' + str(i)
      else:
          coin = word
      if eggy == True:
          coin = coin + end
      buffet.append(coin)
      compressed = ' '.join(buffet)
  return compressed

def decompress(compressed):
  punctuation = [',', '...', '.', '!', '?', ':']
  place = False
  for number in compressed.split():
    for fun in punctuation:
      if fun in number:
        number = number.rstrip(fun)
        place = True
        start = fun
    #print(number)
    #if number == 2:
    #  print("pog")



if __name__ == '__main__':
    compressed = compress(original)

    decompress(compressed)

    def test(text):
      data = compressed(orginal)
      assert len(data) < len(text)
      text2 = decompress(data)
      assert text2 == text



    compression_ratio = 100 * len(compressed) / len(original)

    #print(original)
    #print('––')
    #print(compressed)
    #print('––')
    #print(f'{len(compressed)} / {len(original)} ➞ {compression_ratio:.1f}%')
