size=0
board_matrix=[0]

def board_printer():
    global size
    def vertical_drawer(col_number=0,hasnumber=False):
        grid=""
        for x in range(size):
            if hasnumber:
                s=" "
                if int(board_matrix[col_number*size+x]) == 1: 
                    s="X"
                if int(board_matrix[col_number*size+x]) == 2: 
                    s="O"
                grid+="|    "+str(s)+"    "
            else:
                grid+= "|         "
        grid+="|\n"
        return grid

    def horizontal_drawer():
        grid=""
        for x in range(size):
            grid+="+ - - - - "
        grid+="+\n"
        return grid

    grid=""
    for x in range(size):
        grid+=horizontal_drawer()
        grid+=vertical_drawer()
        grid+=vertical_drawer(x,True)
        grid+=vertical_drawer()
    grid+=horizontal_drawer()
    return grid

def is_winner(player):

    def coin_at(x,y):
        loc=(y*size)+x
        return board_matrix[loc]

    global size
    won=[True]*4 #Horizontal,Vertical,DiagonalLeft,DiagonalRight
    for y in range(size):
        won[0]=True
        won[1]=True
        for x in range(size):
            if not(coin_at(x,y)==player):
                won[0]=False
            if not(coin_at(y,x)==player):
                won[1]=False
            if x==y and not(coin_at(x,y)==player):
                won[2]=False
            if x==(size-y) and not(coin_at(x,y)==player):
                won[3]=False
        if won[0] or won[1]:
            return True
    if won[2] or won[3]:
        return True
    return False
        
def point_placer(player,x,y=0):
    # loc=(y*size)+x
    loc=x
    if not(board_matrix[loc]==0):
        return False
    board_matrix[loc]=player
    return True

def winner_display(player):
    board_printer()
    print("Player ",player," wins!")

def match_handler():
    for x in range(0,size*size):
        legitround=False
        while(not(legitround)):
            print(board_printer())
            p=str((x%2)+1)
            legitround= point_placer(p,int(input("Player "+p+" Turn\nEnter position:"))-1)
            if is_winner(p):
                winner_display(p)
                return


    
def match_setup():
    global size
    size=int(input("Enter board size:"))
    global board_matrix
    board_matrix=([0]*(size*size))
    match_handler()



match_setup()