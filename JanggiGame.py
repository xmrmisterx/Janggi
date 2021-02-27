# Author: Bobby Nguyen
# Date: 2/26/21
# Description: Code a Janggi game

class Board:

    """
    Class the represents the Janggi board.
    """

    def __init__(self):

        """
        Creates the board and places all the game pieces.
        """

        # create board

        self._board = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ["_", "_", "_", "_", "_", "_", "_", "_", "_"]]

        # print board

        self.display_board(self._board)

    def display_board(self, board):

        """
        Displays the board.
        """

        for column in self._board:
            for row in column:

                print(row, end=" ")
                # 'end=""' changes the new line of print to an empty space

            print()
            # 'print()' creates a new line after each row


board = Board()





# from the wikipedia, Janggi is a chess knockoff, Korean chess, or adaptation of Chinese chess. It's played on a 9 lines
# wide and 10 lines long board (the diagram on wikipedia shows a grid of 8 squares wide and 9 squares long, which I
# guess is 9 by 10 lines). The players are Blue and Red, with Blue moving first. Each side has a 2 x 2 box, which is
# further divided by 2 intersecting diagonal lines through the big square (see wikipedia digram). The pieces include a
# general, who occupies the 2 x 2 board (does he move the entire 2 x 2 board with him? Oh, it seems the lines ARE
# important. From the diagram, we see that all the pieces are at the intersections of the lines (unlike chess, where
# the lines create squares for the pieces to be placed into, here the pieces are at the line intersections), so the
# general can only move in his palace (which is the 2 x 2 grid) and he only has 9 spots he can move, those being the
# 9 intersections in the 2 x 2 grid.

# To recap... generals can't leave there 2 x 2 palace. You can't make a move that puts or leaves the general in check.
# You can pass the turn without moving the general (you can pass the turn without moving any pieces actually). The goal
# of the game is to get the other general in check, like in chess.

# Guard pieces are 2 that are below the general. They are one of the weakest pieces, as like the general, they can't
# leave the palace and can only move where the general moves.

# Horse pieces are similar to knights in chess, but they can only move one spot orthogonally (up, down, left, right) and
# then 1 spot diagonally. However, in this 2 part move, there can't be another piece, otherwise the move is blocked. It
# is possible to gain an advantage by blocking the opponent's horse, while leaving your horse able to take the opponents
# horse (this means you can only block the orthogonal move, but the diagonal move, if there is an opponent there, you
# can finish a move diagonally to capture the opponent's piece).

# Elephants begin the game one space to the left and right of guards, and have a move of one spot orthogonally and 2
# spots diagonally. Just like horses, elephants can be blocked in their othogonal move.

# Chariots begin the game in the corners and are the most powerful piece in the game. They can move any number of spots
# horizontally or vertically (like the rook in chess). They can also move diagonally inside the palace, but only in
# straight lines (lol, what does this mean?). Clarification, they can move diagonally, but only inside the fortress, so
# at most 2 spaces to edge of fortress.

# Cannons start behind the soldiers, directly ahead of the horses. Cannons move horizontally or vertically (like the
# chariots) but must jump a unit in order to move. To clarify, they must jump exactly one friendly or enemy unit on
# their move for it to be legal. To take a piece with the cannon, there needs to be exactly one piece in between the
# cannon and the target. They can capture diagonally along the palace, but there will need to be a piece in the middle
# of the diagonal and the cannon thus needs to be in a corner spot. Cannons can't capture other cannons. In addition,
# cannons can't jump over other cannons.

# Soldiers are similar in power to pawns in chess. They start with 5 in the front. Soldiers can only move 1 spot
# up or 1 spot sideways. Unlike pawns in chess, once they reach the end of the board, they can only move sideways (they
# can no longer move up). Soldiers can move 1 spot diagonally forward when within the palace.

# Alright, so we checked the janggi game rules again and looked over the CRC method of creating classes. We also looked
# at some sample chess code online, because we were having problems identifying whether "piece" should be a class at all
# since technically the pieces are on the board. However, we thought about it and didn't know how to create a board
# with pieces. If we think about it in terms of objects, then pieces are definitely an object in the game, perhaps the
# important objects in the game, so they should definitely be a class in that since. In the end, I think we'll use the
# player class, board class, game class, and piece class. The piece class will have all the pieces inherit from it, and
# we want separate classes for things like red horse and blue horse.

# Alright, with our classes initially sketched out, I think the first thing we want to do, is create the Board class and
# try to print out the board. The game is centered around the pieces on the board, so we definitely need to get a board
# visual representation up to see what's going on with the pieces and game logic we will implement later on. Wait, do
# we put the board class inside the game class, or a Janggi class? We're not sure, I mean, thinking big picture here,
# how do we call the game class to make a new game? The other two games that we coded in CS 161, it was all under 1
# class, so we simply created the game object and called the play function. I think for now, the only change we want is
# to change the game class to Janggi class to be more specific.

# so, we create the Board class, what are we going to put in its initialization? I think theoretically, the board should
# start by creating the grid and filling in the pieces no? Ok, that sounds good, but how do we create the board? What is
# the board made of? From the spreadsheet in the README, the columns go from A to I (9 columns) and the rows go from 1
# to 10 (10 columns) with row one the starting spot for the red player and row 10 the starting spot for the blue player.
# Ok, so its a 9 by 10 grid, how do we create a game grid again? As we recall, its a loop within a loop, but what are
# we doing inside the loop? We are printing, but what are we printing? I think we used "_" underscores before, they are
# probably good enough to represent the grid. Alright, let's try some coding to print out the board. Wait, do we print
# the rows or columns first? Does it even matter? Let's just try and see what happens. Lol, we can't iterate though a
# range of A-I, but we can iterate through each letter in the string "ABCDEFGHI" which I guess is the same thing. Wait,
# I remember now, we hardcoded the board before, in the last game we did, let's see if we can do that. Oh, we remember
# now. Currently our board looks like this:

# _board = ["_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_",
#           "_", "_", "_", "_", "_", "_", "_", "_", "_"]

# but to actually get the the format we want, we want the put each line in its own list, so that we can iterate though
# a loop within a loop to target the exact spot on the board, so the board is now this:

# self._board = [["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"],
#                ["_", "_", "_", "_", "_", "_", "_", "_", "_"]]

# Also, in order to display the board, we have run a loop inside a loop for the rows and columns to print out the board,
# with special "end" print parameter to remove the new line from each print statement, and a print() call after each
# row to create a new line after each row.

# Alright, now we need to do the piece class and create derive all the pieces from it. Look at the chess example we
# found online to see what kind of properties to initialize with each piece. We're assuming we need to put in each
# pieces move, but not sure how to do that right now.
