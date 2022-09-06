class Password:
    def __init__(self, length, complexity, content):
        self.length = length
        self.complexity = complexity
        self.content = content
        
def PassLength(x):
    return int(input(x))

randomChar = {
    '0' : '1' '2' '3' '4' '5' '6' '7' '8' '9' '0',
    '1' : '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' 
          'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z',
    '2' : '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' 
          'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'
          'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z',
    '3' : '1' '2' '3' '4' '5' '6' '7' '8' '9' '0' 
          'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'
          'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
          '!' '@' '#' '$' '%' '^' '&' '?',
}


UserAnswers = {
    'y' : 'Yes,yes,Y,y',
    'n' : 'No,no,N,n'
}

