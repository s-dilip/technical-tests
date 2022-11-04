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

print(calculate_points("GUARDIAN"))

