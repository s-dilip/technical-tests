def calculate_points(word):


    total_points = 0

    for alpbt in word:

        match alpbt:
            case 'E' | 'A'| 'I'| 'O'| 'N'| 'R'| 'T'| 'L'| 'S'| 'U':
                total_points += 1

            case 'D'| 'G':
                total_points +=2
    

    return total_points



print("Ready to Go")
print(calculate_points("EAI"))

