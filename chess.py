from tkinter import *


class figure(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.IMG[0 if self.color == Color.White else 1]


class Color(object):
    Black = 2
    White = 1
    Empty = 0


class Pawn(figure):
    IMG = ('♟', '♙')


class King(figure):
    IMG = ('♚', '♔')


class Queen(figure):
    IMG = ('♛', '♕')


class Horse(figure):
    IMG = ('♞', '♘')


class Officer(figure):
    IMG = ('♝', '♗')


class Castle(figure):
    IMG = ('♜', '♖')


class board(object):
    def __init__(self):
        self.color = [[Color.Empty] * 8 for y in range(8)]
        self.land = [["  "] * 8 for y in range(8)]
        for y in range(8):
            self.land[1][y] = (Pawn(Color.Black))
            self.color[1][y] = Color.Black
            self.land[6][y] = (Pawn(Color.White))
            self.color[6][y] = Color.White
        for v in range(8):
            if v == 0:
                self.land[0][v] = (Castle(Color.Black))
                self.color[0][v] = Color.Black
                self.land[7][v] = (Castle(Color.White))
                self.color[7][v] = Color.White
            if v == 7:
                self.land[0][v] = (Castle(Color.Black))
                self.color[0][v] = Color.Black
                self.land[7][v] = (Castle(Color.White))
                self.color[7][v] = Color.White
            if v == 1:
                self.land[0][v] = (Horse(Color.Black))
                self.color[0][v] = Color.Black
                self.land[7][v] = (Horse(Color.White))
                self.color[7][v] = Color.White
            if v == 6:
                self.land[0][v] = (Horse(Color.Black))
                self.color[0][v] = Color.Black
                self.land[7][v] = (Horse(Color.White))
                self.color[7][v] = Color.White
            if v == 2:
                self.land[0][v] = (Officer(Color.Black))
                self.color[0][v] = Color.Black
                self.land[7][v] = (Officer(Color.White))
                self.color[7][v] = Color.White
            if v == 5:
                self.land[0][v] = Officer(Color.Black)
                self.color[0][v] = Color.Black
                self.land[7][v] = Officer(Color.White)
                self.color[7][v] = Color.White
            if v == 4:
                self.land[0][v] = Queen(Color.Black)
                self.color[0][v] = Color.Black
                self.land[7][v] = Queen(Color.White)
                self.color[7][v] = Color.White
            if v == 3:
                self.land[0][v] = King(Color.Black)
                self.color[0][v] = Color.Black
                self.land[7][v] = King(Color.White)
                self.color[7][v] = Color.White

    def __str__(self):
        res = ''
        for y in range(8):
            res += ''.join(self.land[y]) + "\n"
        return res


Board = board()


# White = 1, Black=1


def setcolor(color):
    return '\033[%sm' % color


def paint():
    print("  A   B   C   D   E   F   G   H")
    colors = [0, 41]
    res = ''
    i = 1
    for y in range(8):
        res += setcolor(0)
        res += str(y + 1)
        for x in range(8):
            res += setcolor(colors[i]) + ' ' + str(Board.land[y][x]) + ' '
            i = 1 - i
            res += setcolor(44)
        i = 1 - i
        if y != 8:
            res += '\n'
    res += setcolor(0)
    print(res)


def plant_fig(y, x, fig):
    Board.land[y][x] = fig
    Board.color[y][x] = Board.land[y][x].color


def del_fig(y, x):
    Board.land[y][x] = '  '
    Board.color[y][x] = Color.Empty


def ways_of_movements(number, letter):
    ways = []
    if str(Board.land[number][letter]) == str(Pawn(Color.White)):
        if Board.color[number - 1][letter] == Color.Empty and number > 0:
            ways.append(number - 1)
            ways.append(letter)
        if letter - 1 >= 0:
            if Board.color[number - 1][letter - 1] == Color.Black:
                ways.append(number - 1)
                ways.append(letter - 1)
        if letter + 1 < 8:
            if Board.color[number - 1][letter + 1] == Color.Black:
                ways.append(number - 1)
                ways.append(letter + 1)
        if number == 6 and Board.color[number - 2][letter] == Color.Empty and Board.color[number - 1][
            letter] == Color.Empty:
            ways.append(number - 2)
            ways.append(letter)
    elif str(Board.land[number][letter]) == str(Pawn(Color.Black)):
        if  number < 7:
            if Board.color[number + 1][letter] == Color.Empty:
                ways.append(number + 1)
                ways.append(letter)
        if letter - 1 >= 0:
            if Board.color[number + 1][letter - 1] == Color.White:
                ways.append(number + 1)
                ways.append(letter - 1)
        if letter + 1 < 8:
            if Board.color[number + 1][letter + 1] == Color.White:
                ways.append(number + 1)
                ways.append(letter + 1)
        if number == 1 and Board.color[number + 1][letter] == Color.Empty and Board.color[number + 2][
            letter] == Color.Empty:
            ways.append(number + 2)
            ways.append(letter)
    elif str(Board.land[number][letter]) == str(Castle(Color.Black)):
        for y_ in range(-1, 2, 1):
            for x_ in range(-1, 2, 1):
                if x_ == 0 or y_ == 0:
                    for move in range(1, 8, 1):
                        if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                            if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Black):
                                ways.append(number + y_ * move)
                                ways.append(letter + x_ * move)
                            if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Empty):
                                break
    elif str(Board.land[number][letter]) == str(Castle(Color.White)):
        for y_ in range(-1, 2, 1):
            for x_ in range(-1, 2, 1):
                if x_ == 0 or y_ == 0:
                    for move in range(1, 8, 1):
                        if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                            if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.White):
                                ways.append(number + y_ * move)
                                ways.append(letter + x_ * move)
                            if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Empty):
                                break
    elif str(Board.land[number][letter]) == str(Officer(Color.Black)):
        for y_ in range(-1, 2, 2):
            for x_ in range(-1, 2, 2):
                for move in range(1, 8, 1):
                    if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Black):
                            ways.append(number + y_ * move)
                            ways.append(letter + x_ * move)
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Empty):
                            break
    elif str(Board.land[number][letter]) == str(Officer(Color.White)):
        for y_ in range(-1, 2, 2):
            for x_ in range(-1, 2, 2):
                for move in range(1, 8, 1):
                    if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.White):
                            ways.append(number + y_ * move)
                            ways.append(letter + x_ * move)
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Empty):
                            break
    elif str(Board.land[number][letter]) == str(King(Color.Black)):
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                if 8 > number + y >= 0 and 8 > letter + x >= 0:
                    if x != 0 or y != 0:
                        if Board.color[number + y][letter + x] != Color.Black:
                            ways.append(number + y)
                            ways.append(letter + x)
    elif str(Board.land[number][letter]) == str(King(Color.White)):
        for y in range(-1, 2, 1):
            for x in range(-1, 2, 1):
                if 8 > number + y >= 0 and 8 > letter + x >= 0:
                    if x != 0 or y != 0:
                        if Board.color[number + y][letter + x] != Color.White:
                            ways.append(number + y)
                            ways.append(letter + x)
    elif str(Board.land[number][letter]) == str(Queen(Color.Black)):
        for y_ in range(-1, 2, 1):
            for x_ in range(-1, 2, 1):
                for move in range(1, 8, 1):
                    if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Black):
                            ways.append(number + y_ * move)
                            ways.append(letter + x_ * move)
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Empty):
                            break
    elif str(Board.land[number][letter]) == str(Queen(Color.White)):
        for y_ in range(-1, 2, 1):
            for x_ in range(-1, 2, 1):
                for move in range(1, 8, 1):
                    if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.White):
                            ways.append(number + y_ * move)
                            ways.append(letter + x_ * move)
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Empty):
                            break
    elif str(Board.land[number][letter]) == str(Horse(Color.Black)):
        for y_ in range(-2, 3, 1):
            for x_ in range(-2, 3, 1):
                move = 1
                if y_ != 0 and x_ != 0 and (y_ * y_) * (x_ * x_) == 4:
                    if 0 <= number + y_ * move < 8 and 0 <= letter + x_ * move < 8 and (y_ != 0 or x_ != 0):
                        if str(Board.color[number + y_ * move][letter + x_ * move]) != str(Color.Black):
                            ways.append(number + y_ * move)
                            ways.append(letter + x_ * move)
    elif str(Board.land[number][letter]) == str(Horse(Color.White)):
        for y_ in range(-2, 3, 1):
            for x_ in range(-2, 3, 1):
                if y_ != 0 and x_ != 0 and (y_ * y_) * (x_ * x_) == 4:
                    if 0 <= number + y_ < 8 and 0 <= letter + x_ < 8 and (y_ != 0 or x_ != 0):
                        if str(Board.color[number + y_][letter + x_]) != str(Color.White):
                            ways.append(number + y_)
                            ways.append(letter + x_)

    return ways


def write_ways(y, x):
    res = []
    size = len(ways_of_movements(y, x))
    size = (size / 2)
    for i in range(int(size)):
        res_ = []
        k = int(i * 2)
        res_.append(ways_of_movements(y, x)[k])
        res_.append(ways_of_movements(y, x)[k + 1])
        res.append(res_)
    # print(res)
    return res


class side(object):
    def __init__(self, color):
        self.color = color

    def get_King_place(self):
        Kings_place = None
        for y_ in range(8):
            for x_ in range(8):
                if str(Board.land[y_][x_]) == str(King(self.color)):
                    Kings_place = [y_, x_]
        return Kings_place

    def get_all_enemies_moves(self):
        all_enemies_moves = []
        en_col = 3 - self.color
        for y_ in range(8):
            for x_ in range(8):
                if Board.color[y_][x_] == en_col:
                    if str(Board.land[y_][x_]) != str(Pawn(en_col)):
                        for j in range(len(write_ways(y_, x_))):
                            all_enemies_moves.append(write_ways(y_, x_)[j])
                    else:
                        plused = (en_col * 2 - 3) + y_
                        if 0 <= plused < 8:
                            if (x_ + 1) < 8:
                                bump = []
                                if Board.color[plused][x_ + 1] != en_col:
                                    bump.append(plused)
                                    bump.append(x_ + 1)
                                    all_enemies_moves.append(bump)
                            if (x_ - 1) >= 0:
                                bump1 = []
                                if Board.color[plused][x_ - 1] != en_col:
                                    bump1.append(plused)
                                    bump1.append(x_ - 1)
                                    all_enemies_moves.append(bump1)
        return all_enemies_moves

    def now_is_check(self):
        Kings = self.get_King_place()
        smd = self.get_all_enemies_moves()
        rng = range(len(smd))
        for j in rng:
            if smd[j] == Kings:
                return 1
        return 0

    def is_check(self, y1, x1, y2, x2):
        isit = 0
        fig1 = Board.land[y1][x1]
        col1 = Board.color[y1][x1]
        fig2 = Board.land[y2][x2]
        col2 = Board.color[y2][x2]
        move_fig(y1, x1, y2, x2)
        if self.now_is_check():
            isit = 1
        Board.land[y1][x1] = fig1
        Board.color[y1][x1] = col1
        Board.land[y2][x2] = fig2
        Board.color[y2][x2] = col2
        return isit


def correct_moves(y, x):
    ways = []
    ww = write_ways(y, x)
    for j in ww:
        if side(Board.land[y][x].color).is_check(y, x, j[0], j[1]) == 0:
            ways.append(j)
    return ways


def get_figs_coords(color):
    res = []
    for y in range(8):
        for x in range(8):
            if str(Board.color[y][x]) == str(color) and correct_moves(y, x):
                res.append([y, x])
    return res


# def al
def check_way(y1, x1, y2, x2):
    res = [y2, x2]
    cm = correct_moves(y1, x1)
    # print(correct_moves(y1, x1)," куда ходить,  наш ход ", res)
    for l in cm:
        if l == res:
            return 1

    return 0


def get_all_moves(color):
    all_moves = []
    print(1, end='')
    for y_ in range(8):
        for x_ in range(8):
            if Board.color[y_][x_] == color:
                if correct_moves(y_, x_) != []:
                    cm=correct_moves(y_, x_)
                    for j in range(len(cm)):
                        all_moves.append(cm[j])
    return all_moves


def move_fig(y1, x1, y2, x2):
    plant_fig(y2, x2, Board.land[y1][x1])
    del_fig(y1, x1)
    if str(Board.land[y2][x2])==str(Pawn(Color.White)) and y2==0:
        plant_fig(y2, x2, Queen(Color.White))
    if str(Board.land[y2][x2]) == str(Pawn(Color.Black)) and y2 == 7:
        plant_fig(y2, x2, Queen(Color.Black))


def bot_move():
    all_a_prices = []
    res_move=[]
    color = Color.White
    en_color=3-color
    all_a_take = get_figs_coords(color)  # все фигуры для первого хода
    for a_take in all_a_take:
        all_a_move = correct_moves(a_take[0], a_take[1])  # возможныe ходы для фигуры
        for a_move in all_a_move:
            a_taken_fig=Board.land[a_take[0]][a_take[1]]
            a_taken_color=Board.color[a_take[0]][a_take[1]]
            a_moved_fig = Board.land[a_move[0]][a_move[1]]
            a_moved_color = Board.color[a_move[0]][a_move[1]]
            # запоминаем всё начальное.
            move_fig(a_take[0], a_take[1], a_move[0], a_move[1])
            all_b_take = get_figs_coords(en_color)  # все фигуры для ответного хода
            all_b_prices = []
            for b_take in all_b_take:
                all_b_move = correct_moves(b_take[0], b_take[1])  # возможныe ходы для фигуры
                for b_move in all_b_move:
                    b_taken_fig = Board.land[b_take[0]][b_take[1]]
                    b_taken_color = Board.color[b_take[0]][b_take[1]] # запоминаем состояние после первого хода
                    b_moved_fig = Board.land[b_move[0]][b_move[1]]
                    b_moved_color = Board.color[b_move[0]][b_move[1]]
                    move_fig(b_take[0], b_take[1], b_move[0], b_move[1]) # hodim vozmozhniy hod
                    b_price = get_price(color)-get_price(en_color)
                    all_b_prices.append(b_price)
                    # vozvraschaem elementi v nachalnoe sostoianie posle hoda vrazhini
                    Board.land[b_take[0]][b_take[1]] = b_taken_fig
                    Board.color[b_take[0]][b_take[1]] = b_taken_color
                    Board.land[b_move[0]][b_move[1]] = b_moved_fig
                    Board.color[b_move[0]][b_move[1]] = b_moved_color
            minimum = min(all_b_prices)
            all_a_prices.append(minimum)
            if minimum==max(all_a_prices):
                res_move = []
                res_move.append(a_take)
                res_move.append(a_move)
            print(get_price(Color.White)," против ",get_price(Color.Black))
            #возврщаем элементы на начальное состояние
            Board.land[a_take[0]][a_take[1]] = a_taken_fig
            Board.color[a_take[0]][a_take[1]] = a_taken_color
            Board.land[a_move[0]][a_move[1]] = a_moved_fig
            Board.color[a_move[0]][a_move[1]] = a_moved_color


    return res_move


def get_price(color):
    price = 0
    for i in range(8):
        for j in range(8):
            if Board.color[i][j] == color:

                if str(Board.land[i][j]) == str(Queen(color)):
                    price += 90
                elif str(Board.land[i][j]) == str(Pawn(color)):
                    price += 10
                    if color==Color.White: # зависимость от продвижения и центра
                        delta=6-i
                        price+=delta*(8-abs(7-2*j))
                    if color == Color.Black:  # зависимость от продвижения и центра
                        delta=i-1
                        price+=delta*(8-abs(7-2*j))

                elif str(Board.land[i][j]) == str(Horse(color)):
                    price += 30
                elif str(Board.land[i][j]) == str(Officer(color)):
                    price += 30
                elif str(Board.land[i][j]) == str(Castle(color)):
                    price += 50
                # b=side(3 - color).get_all_enemies_moves()
                # a=side(3-color).get_King_place()
                # if a in b:
                #       price += 50
    return price


color_move = 2
t_o_p = 0


def game():
    root = Tk()
    root.title("Шахматы")
    alphabit = list("ABCDEFGH")

    class Coord(object):
        x = None
        y = None

    tooken = Coord()
    tooken.y = 0
    tooken.x = 0
    colors = ("white", "gray")
    color_move = 2
    t_o_p = 0

    # t_o_p = take or place
    def take_or_place(y, x):
        cmd_move = lambda y_=y, x_=x: take_or_place(y_, x_)
        cmd_take = lambda y_=tooken.y, x_=tooken.x: take_or_place(y_, x_)
        global t_o_p
        global color_move
        if Board.color[y][x] == color_move and correct_moves(y, x) != [] and color_move == Color.Black:
            tooken.y = y
            tooken.x = x
            t_o_p = 1
            # print(y,x, " -->",end='')
            # print(correct_moves(y, x))
        elif t_o_p == 1 and (y != tooken.y or x != tooken.x) and check_way(tooken.y, tooken.x, y, x) and Board.color[y][
            x] != color_move:
            Button(text=' ' + str(Board.land[tooken.y][tooken.x]), font="arial 20", bg=colors[(y + x) % 2],
                   command=cmd_move).grid(row=y + 1,
                                          column=x + 1)
            Button(text='    ', font="arial 20", bg=colors[(tooken.y + tooken.x) % 2], command=cmd_take).grid(
                row=tooken.y + 1,
                column=tooken.x + 1)
            move_fig(tooken.y, tooken.x, y, x)
            color_move = 3 - color_move
            t_o_p = 0
        if get_all_moves(2) == [] or get_all_moves(1) == []:
            Label(text="Спасибо за игру!", font="arial 100").grid(row=0, column=0, columnspan=90, rowspan=90)
        if color_move == Color.White and t_o_p == 0:
            t_o_p = 1
            bots_move = bot_move()
            print(bots_move)
            tooken.y = bots_move[0][0]
            tooken.x = bots_move[0][1]
            y = bots_move[1][0]
            x = bots_move[1][1]
            cmd_move = lambda y_=y, x_=x: take_or_place(y_, x_)
            cmd_take = lambda y_=tooken.y, x_=tooken.x: take_or_place(y_, x_)
            Button(text=' ' + str(Board.land[tooken.y][tooken.x]), font="arial 20", bg=colors[(y + x) % 2],
                   command=cmd_move).grid(row=y + 1, column=x + 1)
            Button(text='    ', font="arial 20", bg=colors[(tooken.y + tooken.x) % 2], command=cmd_take).grid(
                row=tooken.y + 1,
                column=tooken.x + 1)
            move_fig(tooken.y, tooken.x, y, x)
            color_move = 3 - color_move
            t_o_p = 0

    for numbers in range(8):
        Label(text=numbers + 1, font="arial 20").grid(column=0, row=numbers + 1)
        Label(text=alphabit[numbers], font="arial 20").grid(column=numbers + 1, row=0)

        for letters in range(8):
            cmd = lambda y=numbers, x=letters: take_or_place(y, x)
            color_set = (letters + numbers) % 2
            global bttn
            bttn = Button(text=Board.land[numbers][letters],
                          font="arial 20",
                          width="3",
                          bg=colors[color_set],
                          command=cmd).grid(row=numbers + 1, column=letters + 1)

    root.mainloop()


game()
