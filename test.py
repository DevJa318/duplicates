import hashlib

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
    
    tablica.append((sha5,pełna_ścieżka))

tablica = [(31,312),(21,32),(32,31),(31,19),
           (21,17),(32,12),(31,222)]

lista = sorted(tablica)
print(lista)

a = (0,0)
lista2 = []
for i in lista:
    if i[0] == a[0]:
        lista2.append((a[1],i[1]))
        print(a[1],i[1])
    a = i

def usuwanie(lista2):
    for i in lista2:
        print('Który z plików usunąć?:')
        print('\t 1.', i[0], '\t czy ' +
              '\t2.', i[1])
        print('Który')
# pobierz przycsk
# dodaj odpowiedni plik do pliku tekstowego abc.txt
# print koniec
# print wyświetlić plik?

usuwanie(lista2)