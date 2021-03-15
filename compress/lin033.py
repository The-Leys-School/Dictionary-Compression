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
 
with open('english10k.txt') as f:
    dictionary = [l.strip() for l in f]

#def compress(original,dictionary):
def compress(original):
    alist = [',','.','!']
    buf = []
    add =''
    for word in original.split():
        x=False
        for punc in alist:
            if punc in word:
                word = word.rstrip(punc)
                add = punc
                x=True

        if word in dictionary:
            i = dictionary.index(word)
            if len(str(i))<len(word):
                token = '\0' + str(i)
                buf.append(token)
            else:
                buf.append(word)
        elif word.lower() in dictionary and word[1:].islower() :
            i = dictionary.index(word.lower())
            token = '\u2603'+str(i)
            buf.append(token)
        #elif word.lower() in dictionary:
            #i = dictionary.index(word.lower())
            #token = '\u2600'+str(i)
            #buf.append(token)
        else:
            buf.append(word)
        if x == True:
            buf.append(add)

    compressed = ' '.join(buf)
    return compressed

def decompress(compressed):
    text=[]
    for word in compressed.split():
        #print(word)
        if '\u2603' in word:
            word = word[1:]
            i=dictionary[int(word)]
            new_word = i[0].upper()+i[1:]
            text.append(new_word)
        elif word == '.'or word==',':
            text.append(word)
            
        
        elif '\0' in word:
            word =word[1:]
            x=dictionary[int(word)]
            text.append(x)
            
        else:
            text.append(word)

        decompressed = ' '.join(text)
    #print(decompressed)
    return decompressed

        
            
  
if __name__ == '__main__':
    compressed = compress(original,dictionary)
    compression_ratio = 100 * len(compressed) / len(original)

    print(original)
    print('––')
    print(compressed)
    print('––')
    print(f'{len(compressed)} / {len(original)} ➞ {compression_ratio:.1f}%')

    #decompress
    #arr = bytearray(compressed,'utf-8')
    #print(arr)
    print("")

