def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


def check_winner(board, symbol):
    for row in board:
        if row[0] == row[1] == row[2] == symbol:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def get_move(player, board):
    while True:
        try:
            move = int(input(player + "، اختار رقم من 1 إلى 9: ")) - 1
            row = move // 3
            col = move % 3
            if 0 <= move < 9 and board[row][col] == " ":
                return row, col
            else:
                print("الخانه مش فاضية أو الرقم غلط.")
        except:
            print("من فضلك دخل رقم صحيح.")


def use_special_move(board, enemy_symbol):
    while True:
        try:
            move = int(input("اختار رقم الخانة اللي فيها رمز الخصم لمسحها (1-9): ")) - 1
            row = move // 3
            col = move % 3
            if 0 <= move < 9 and board[row][col] == enemy_symbol:
                board[row][col] = " "
                print("✔️ تم مسح خانة الخصم.")
                return
            else:
                print("لا يمكن مسح هذه الخانة.")
        except:
            print("دخل رقم صحيح.")


def main():
    print("أهلاً في لعبة XO ومعاك سوبر موف مرة واحدة 🔥")

    p1 = input("اسم اللاعب الأول: ")
    p2 = input("اسم اللاعب الثاني: ")
    s1 = input(p1 + "، اختار رمزك: ")
    s2 = input(p2 + "، اختار رمزك المختلف: ")
    while s1 == s2:
        s2 = input("رمز مكرر، اختار واحد مختلف: ")

    board = [[" " for _ in range(3)] for _ in range(3)]
    p1_used = False
    p2_used = False
    turn = 1

    print_board(board)

    while True:
        if turn % 2 == 1:
            player = p1
            symbol = s1
            enemy_symbol = s2
            used = p1_used
        else:
            player = p2
            symbol = s2
            enemy_symbol = s1
            used = p2_used

        # سؤال عن استخدام السوبر موف
        if not used:
            use = input(player + "، هل تريد استخدام السوبر موف لمسح خانة خصمك؟ (y/n): ")
            if use.lower() == "y":
                use_special_move(board, enemy_symbol)
                if turn % 2 == 1:
                    p1_used = True
                else:
                    p2_used = True
                print_board(board)

        # الحركة العادية
        row, col = get_move(player, board)
        board[row][col] = symbol
        print_board(board)

        # فحص الفوز أو التعادل
        if check_winner(board, symbol):
            print("🎉 مبروك، " + player + " فاز!")
            break
        elif is_draw(board):
            print("🤝 انتهت المباراة بتعادل.")
            break

        turn += 1


if __name__ == "__main__":
    main()
