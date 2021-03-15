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
military short. This man is the TERMINATOR.'''

from string import ascii_letters
import string
from string import punctuation

with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]

def compress(original):
    original = original.lower()
    buf = []
    for word in original.split():
        if word in dictionary:
            i = dictionary.index(word)
            token = str(i) # '\0' + str(chr(i))
            buf.append(token)
        else:
            buf.append(word)
    compressed = ' '.join(buf)
    return compressed

def decompress(compressed):
    original = ""
    for word in compressed.split():
        if word.isalpha():
            original += " " + word
        else:
            original += " " + dictionary[int(word)]
    return original
        
            

if __name__ == '__main__':
    '''for word in compressed.split():
        if word in dictionary:
     
            compression_ratio = 100 * len(compressed) / len(original)

    print(original)
    print('––')
    print(compressed)
    print('––')
    print(f'{len(compressed)} / {len(original)} ➞ {compression_ratio:.1f}%')'''


    data = compress("hello world sheepsicle")
    print(data)

    text2 = decompress(data)
    print(text2)


    original.split()

    original = original.lstrip(punctuation)
    original = original.rstrip(punctuation)

    print(len(dictionary))
