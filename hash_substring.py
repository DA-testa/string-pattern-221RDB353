PRIME = 101
BASE = 256


def read_input():
    # Lasīt pirmo ievadi - datu tipu un pēc tam, ja nepieciešams, citus ievades parametrus
    t = input().rstrip()

    # Ja datu tips ir I, lasīt raksta un teksta ievades parametrus
    if t == 'I':
        p = input().rstrip()
        txt = input().rstrip()

    # Ja datu tips ir F, ielasīt faila saturs
    elif t == 'F':
        filename = "06"

        # Pārbaudiet faila pēdējo simbolu un pārliecinieties, vai tas ir pareizais fails
        if str(filename[-1]) != "a":
            try:
                with open(f"./tests/06") as f:
                    contents = f.readlines()
            except FileNotFoundError:
                print("File not found")
                return
            except:
                print("Error reading file")
                return

            p = contents[0].strip()
            txt = contents[1].strip()

        # Ja fails ir nederīgs, izvadīt kļūdas paziņojumu
        else:
            print("Invalid filename")
            return

    # Atgriezt raksta un teksta ievades parametrus
    return p, txt


def print_occurrences(output):
    # Izdrukājiet visus saskaņošanās indeksus
    print(' '.join(map(str, output)))


def find_occurrences(p, txt):
    # Izveidojiet raksta un teksta skaitļu pārstājēju un inicializējiet tos
    p_hash = 0
    txt_hash = 0

    # Aprēķina raksta un teksta skaitļu pārst
    # # Iterējiet cauri rakstam un teksta teksta pēc bāzes vērtības un izmantojiet mod p, lai iegūtu skaitļu pārstājēju
    for i in range(len(p)):
      p_hash = (p_hash * BASE + ord(p[i])) % PRIME
      txt_hash = (txt_hash * BASE + ord(txt[i])) % PRIME

# Izveidojiet tukšu sarakstu, lai saglabātu saskaņošanās indeksus
    occurrences = []
    for i in range(len(txt) - len(p) + 1):

    # Ja raksta un teksta skaitļu pārstājēji ir vienādi, salīdziniet raksta un teksta virknes, lai pārbaudītu, vai tās ir identiskas
      if p_hash == txt_hash:
          if p == txt[i:i+len(p)]:
              occurrences.append(i)

    # Ja raksta un teksta skaitļu pārstājēji nav vienādi, izmantojiet Rabin-Karp algoritmu, lai atjaunotu teksta skaitļu pārstājēju
    if i < len(txt) - len(p):
        txt_hash = ((txt_hash - ord(txt[i]) * (BASE**(len(p)-1))) * BASE + ord(txt[i+len(p)])) % PRIME
        return occurrences

if __name__ == '__main__':
    print_occurrences(find_occurrences(*read_input()))
