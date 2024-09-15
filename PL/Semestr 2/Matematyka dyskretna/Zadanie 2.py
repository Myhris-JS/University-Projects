#Zmienne pomocnicze oraz tabela
from tabulate import tabulate
sop_tautology = 0
pos_tautology = 0
sop_data = []
pos_data = []

#Spis zadan
#Zidentyfikuj funkcję SoP dla zadań [1-5], [11-20], [31-40]
#Zidentyfikuj funkcję PoS dla zadań [6-10], [21-30], [41-50]
tasks = {
    'SoP': {
        '1-5': [
            "1101", #Task 1
            "0111", #Task 2
            "0100", #Task 3
            "0001", #Task 4
            "0110"  #Task 5
        ],
        '11-20': [
            "00010110", #Task 11
            "10110101", #Task 12
            "10111111", #Task 13
            "01101001", #Task 14
            "00111000", #Task 15
            "11101100", #Task 16
            "00110101", #Tasl 17
            "10010001", #Task 18
            "01100000", #Task 19
            "11000111"  #Task 20
        ],
        '31-40': [
            "0010110111011001", #Task 31
            "0010011000101111", #Task 32
            "0000100000000100", #Task 33
            "1011100111000001", #Task 34
            "1110000001100000", #Task 35
            "1011110111100011", #Task 36
            "1101100100001011", #Task 37
            "1011110011010011", #Task 38
            "1001001101111000", #Task 39
            "1011110100000011"  #Task 40
            ]
    },
    'PoS': {
        '6-10': [
            "1000", #Task 6
            "1010", #Task 7
            "0101", #Task 8
            "1110", #Task 9
            "1011"  #Task 10
        ],
        '21-30': [
            "01010001", #Task 21
            "10111110", #Task 22
            "10111010", #Task 23
            "00000101", #Task 24
            "00101111", #Task 25
            "00100010", #Task 26
            "00001111", #Task 27
            "11011101", #Task 28
            "00101011", #Task 29
            "10111011"  #Task 30
        ],
        '41-50': [
            "0001001010010100", #Task 41
            "1110101100100110", #Task 42
            "0110110100010000", #Task 43
            "1001001111001101", #Task 44
            "0001110000011101", #Task 45
            "1000010001101010", #Task 46
            "0111001010100001", #Task 47
            "0111100011000000", #Task 48
            "1011110111011110", #Task 49
            "1111011001101000"  #Task 50
        ]
    }
}

#Funkcja do obliczeń SoP
def sop_function(bin_list, start_x):
    sop_results = []
    for idx, bits in enumerate(bin_list, start=start_x):
        t = []
        for i, bit in enumerate(bits):
            if bit == "1":
               t.append(f'x{i+1}')
            else:
               t.append(f'x{i+1}\'')
        sop_results.append([f"{idx}.",' + '.join(t)])
    return sop_results

#Funkcja do obliczeń PoS
def pos_function(bin_list, start_x):
    pos_results = []
    for idx, bits in enumerate(bin_list, start=start_x):
      term = []
      for i, bit in enumerate(bits):
          if bit == '0':
              term.append(f'x{i+1}')
          else:
              term.append(f'x{i+1}\'')
      pos_results.append([f"{idx}.", '(' + ' + '.join(term) + ')'])
    return pos_results

#Wyniki
#Wypisanie zidentyfikowanej funkcji SoP dla poszczególnych zadań.
for key, ranges in tasks["SoP"].items():
    title = f'Funkcje SoP ({key})'
    sop = sop_function(ranges, start_x=1)
    sop_data.extend(sop)
    sop_tautology += sum(is_tautology(bits, sop=True) for bits in ranges)
    print(f'\n{title}')
    print(tabulate(sop, headers=["Zadanie", "Funkcja SoP"], tablefmt="grid"))

#Wypisanie zidentyfikowanej funkcji PoS dla poszczególnych zadań.
for key, ranges in tasks['PoS'].items():
    title = f'Funkcje PoS ({key})'
    pos = pos_function(ranges, start_x=1)
    pos_data.extend(pos)
    pos_tautology += sum(is_tautology(bits, sop=False) for bits in ranges)
    print(f'\n{title}')
    print(tabulate(pos, headers=["Zadanie", "Funkcja PoS"], tablefmt="grid"))
