def process_number_squares(start, end):

    numbers = list(range(start, end + 1))
    
    
    squares = []
    for num in numbers:
        squares.append(num * num)
    
 
    even_squares = []
    odd_squares = []
    
    for square in squares:
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
    
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)        
if __name__ == "__main__":
    process_number_squares(1, 5)