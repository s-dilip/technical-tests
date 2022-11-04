import random

class Rack:

    def __init__(self, tiles):
        self.tiles = tiles

    def show_rack(self):
        return self.tiles

class TileBag:

    def __init__(self):
        
        self.tiles = self.generate_tiles()

    def generate_tiles(self):

        tiles_distribution ={
            12: ['E'],
            9: ['A', 'I'],
            8: ['O'],
            6: ['N', 'R', 'T'],
            4: ['L', 'S', 'U', 'D'],
            3: ['G'],
            2: ['B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y'],
            1: ['K', 'J', 'X', 'Q', 'Z']
        }

        




def calculate_points(word):

    total_points = 0

    for alpbt in word:

        match alpbt:
            case 'E' | 'A'| 'I'| 'O'| 'N'| 'R'| 'T'| 'L'| 'S'| 'U':
                total_points += 1
            case 'D'| 'G':
                total_points +=2
            case 'B'| 'C'| 'M'| 'P':
                total_points +=3
            case 'F'| 'H'|'V'| 'W'|'Y':
                total_points +=4
            case 'K':
                total_points +=5
            case 'J'| 'X':
                total_points +=8
            case 'Q'| 'Z':
                total_points +=10
    
    return total_points

# tiles = ['G', 'U', 'A', 'R', 'D', 'I', 'A', 'N']
# rack = Rack(tiles)
# print(rack.show_rack())

def get_random_letters():

    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tiles_2_return =[]

    for x in range(7):
        tiles_2_return.append(random.choice(alphabets))
    
    return tiles_2_return

print(get_random_letters())







