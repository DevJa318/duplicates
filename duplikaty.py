import hashlib
import webbrowser

def hashfile(file: str, block_size: int = 65536) -> str:
    """Generate the hash of any file according to the sha256 algorithm."""
    with open(file, 'rb') as message:
        m = hashlib.sha256()
        block = message.read(block_size)
        while len(block) > 0:
            m.update(block)
            block = message.read(block_size)
        digest = m.hexdigest()

    return digest

zbior_hashy = []
with open('/home/pi/allfiles.txt','r') as f:
    for adres in f:
        pliksha = hashfile(adres.strip('\n'))
        zbior_hashy.append((pliksha, adres))
        
posortowane_hashe = sorted(zbior_hashy)

current_hash = (0,0)
poprzedni_hash = posortowane_hashe[0]

for plik in posortowane_hashe:
    if plik[0] != current_hash[0]:
        print(plik[0])
        print('\t' + plik[1])
        current_hash = plik
    elif plik[0] == poprzedni_hash[0]:
        print('\t', plik[1])
    poprzedni_hash = plik
