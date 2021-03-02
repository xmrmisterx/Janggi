# Author: Bobby Nguyen
# Date: 2/26/21
# Description: Janggi game halfway progress report

# class Board:
#
#     """
#     Class that represents the Janggi board. The Board class will be responsible for creating the board, creating the
#     pieces on the board, placing the pieces on the board, and converting the letter number coordinates into the
#     coordinates of the data structure of the board. The board will communicate with the Player class (when the player
#     decides where to place their piece, the board takes those coordinates), the JanggiGame class (which looks at the
#     game board to determine if there is a winner yet), and all the derivatives of the Piece class (to place those pieces
#     on the board).
#     """
#
#     def __init__(self):
#
#         """
#         Creates the board and places all the game pieces.
#         """
#
#         # create coordinate conversion dictionary
#
#         # self._coordinate_conversion_dict = {
#         #     "a1": [0, 0],
#         #     "b1": [0, 1],
#         #     "c1": [0, 2],
#         #     "d1": [0, 3],
#         #     "e1": [0, 4],
#         #     "f1": [0, 5],
#         #     "g1": [0, 6],
#         #     "h1": [0, 7],
#         #     "i1": [0, 8],
#         #     "a2": [1, 0],
#         #     "b2": [1, 1],
#         #     "c2": [1, 2],
#         #     "d2": [1, 3],
#         #     "e2": [1, 4],
#         #     "f2": [1, 5],
#         #     "g2": [1, 6],
#         #     "h2": [1, 7],
#         #     "i2": [1, 8],
#         #     "a3": [2, 0],
#         #     "b3": [2, 1],
#         #     "c3": [2, 2],
#         #     "d3": [2, 3],
#         #     "e3": [2, 4],
#         #     "f3": [2, 5],
#         #     "g3": [2, 6],
#         #     "h3": [2, 7],
#         #     "i3": [2, 8],
#         #     "a4": [3, 0],
#         #     "b4": [3, 1],
#         #     "c4": [3, 2],
#         #     "d4": [3, 3],
#         #     "e4": [3, 4],
#         #     "f4": [3, 5],
#         #     "g4": [3, 6],
#         #     "h4": [3, 7],
#         #     "i4": [3, 8],
#         #     "a5": [4, 0],
#         #     "b5": [4, 1],
#         #     "c5": [4, 2],
#         #     "d5": [4, 3],
#         #     "e5": [4, 4],
#         #     "f5": [4, 5],
#         #     "g5": [4, 6],
#         #     "h5": [4, 7],
#         #     "i5": [4, 8],
#         #     "a6": [5, 0],
#         #     "b6": [5, 1],
#         #     "c6": [5, 2],
#         #     "d6": [5, 3],
#         #     "e6": [5, 4],
#         #     "f6": [5, 5],
#         #     "g6": [5, 6],
#         #     "h6": [5, 7],
#         #     "i6": [5, 8],
#         #     "a7": [6, 0],
#         #     "b7": [6, 1],
#         #     "c7": [6, 2],
#         #     "d7": [6, 3],
#         #     "e7": [6, 4],
#         #     "f7": [6, 5],
#         #     "g7": [6, 6],
#         #     "h7": [6, 7],
#         #     "i7": [6, 8],
#         #     "a8": [7, 0],
#         #     "b8": [7, 1],
#         #     "c8": [7, 2],
#         #     "d8": [7, 3],
#         #     "e8": [7, 4],
#         #     "f8": [7, 5],
#         #     "g8": [7, 6],
#         #     "h8": [7, 7],
#         #     "i8": [7, 8],
#         #     "a9": [8, 0],
#         #     "b9": [8, 1],
#         #     "c9": [8, 2],
#         #     "d9": [8, 3],
#         #     "e9": [8, 4],
#         #     "f9": [8, 5],
#         #     "g9": [8, 6],
#         #     "h9": [8, 7],
#         #     "i9": [8, 8],
#         #     "a10": [9, 0],
#         #     "b10": [9, 1],
#         #     "c10": [9, 2],
#         #     "d10": [9, 3],
#         #     "e10": [9, 4],
#         #     "f10": [9, 5],
#         #     "g10": [9, 6],
#         #     "h10": [9, 7],
#         #     "i10": [9, 8],
#         #
#         # }
#
#         # create board
#
#         # self._board = [["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
#         #               ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"]]
#
#         # blue_general = BlueGeneral(1, "e9")
#         # self.place_piece(blue_general, "e9")
#         #
#         # red_general = RedGeneral(1, "e2")
#         # self.place_piece(red_general, "e2")
#         #
#         # blue_guard1 = BlueGuard(1, "d10")
#         # self.place_piece(blue_guard1, "d10")
#         #
#         # blue_guard2 = BlueGuard(2, "f10")
#         # self.place_piece(blue_guard2, "f10")
#         #
#         # red_guard1 = RedGuard(1, "d1")
#         # self.place_piece(red_guard1, "d1")
#         # red_guard2 = RedGuard(2, "f1")
#         # self.place_piece(red_guard2, "f1")
#         #
#         # blue_soldier1 = BlueSoldier(1, "a7")
#         # self.place_piece(blue_soldier1, "a7")
#         # blue_soldier2 = BlueSoldier(2, "c7")
#         # self.place_piece(blue_soldier2, "c7")
#         # blue_soldier3 = BlueSoldier(3, "e7")
#         # self.place_piece(blue_soldier3, "e7")
#         # blue_soldier4 = BlueSoldier(4, "g7")
#         # self.place_piece(blue_soldier4, "g7")
#         # blue_soldier5 = BlueSoldier(5, "i7")
#         # self.place_piece(blue_soldier5, "i7")
#         #
#         # red_soldier1 = RedSoldier(1, "a4")
#         # self.place_piece(red_soldier1, "a4")
#         # red_soldier2 = RedSoldier(2, "c4")
#         # self.place_piece(red_soldier2, "c4")
#         # red_soldier3 = RedSoldier(3, "e4")
#         # self.place_piece(red_soldier3, "e4")
#         # red_soldier4 = RedSoldier(4, "g4")
#         # self.place_piece(red_soldier4, "g4")
#         # red_soldier5 = RedSoldier(5, "i4")
#         # self.place_piece(red_soldier5, "i4")
#         #
#         # blue_horse1 = BlueHorse(1, "c10")
#         # self.place_piece(blue_horse1, "c10")
#         # blue_horse2 = BlueHorse(2, "h10")
#         # self.place_piece(blue_horse2, "h10")
#         # red_horse1 = RedHorse(1, "c1")
#         # self.place_piece(red_horse1, "c1")
#         # red_horse2 = RedHorse(2, "h1")
#         # self.place_piece(red_horse2, "h1")
#         #
#         # blue_elephant1 = BlueElephant(1, "b10")
#         # self. place_piece(blue_elephant1, "b10")
#         # blue_elephant2 = BlueElephant(2, "g10")
#         # self. place_piece(blue_elephant2, "g10")
#         # red_elephant1 = RedElephant(1, "b1")
#         # self. place_piece(red_elephant1, "b1")
#         # red_elephant2 = RedElephant(2, "g1")
#         # self. place_piece(red_elephant2, "g1")
#         #
#         # blue_chariot1 = BlueChariot(1, "a10")
#         # self.place_piece(blue_chariot1, "a10")
#         # blue_chariot2 = BlueChariot(2, "i10")
#         # self.place_piece(blue_chariot2, "i10")
#         # red_chariot1 = RedChariot(1, "a1")
#         # self.place_piece(red_chariot1, "a1")
#         # red_chariot2 = RedChariot(2, "i1")
#         # self.place_piece(red_chariot2, "i1")
#         #
#         # blue_cannon1 = BlueCannon(1, "b8")
#         # self.place_piece(blue_cannon1, "b8")
#         # blue_cannon2 = BlueCannon(2, "h8")
#         # self.place_piece(blue_cannon2, "h8")
#         # red_cannon1 = RedCannon(1, "b3")
#         # self.place_piece(red_cannon1, "b3")
#         # red_cannon2 = RedCannon(2, "h3")
#         # self.place_piece(red_cannon2, "h3")
#
#     # def get_coordinate_conversion_dict(self):
#     #
#     #     """
#     #     Returns the coordinate conversion dictionary.
#     #     """
#     #
#     #     return self._coordinate_conversion_dict
#
#     def display_board(self):
#
#         """
#         Displays the board.
#         """
#
#         for column in self._board:
#             for row in column:
#
#                 print(row, end=" ")
#                 # 'end=""' changes the new line of print to an empty space
#
#             print()
#             # 'print()' creates a new line after each row
#
#     def convert_coordinates(self, coordinates):
#
#         """
#         Converts the game board coordinates to the actual coordinates on the board and returns the actual coordinates.
#         """
#
#         for key in self._coordinate_conversion_dict:
#             if key == coordinates:
#                 return self._coordinate_conversion_dict[key]
#
#     def place_piece(self, piece, target_coordinate):
#
#         """
#         Places the game piece in the parameter at the target coordinate in the parameter.
#         """
#
#         # convert target coordinate into actual coordinates
#
#         actual_target_coordinate = self.convert_coordinates(target_coordinate)
#
#         # place piece on board
#
#         self._board[actual_target_coordinate[0]][actual_target_coordinate[1]] = piece


class Piece:
    """
    Represents all the game pieces on the board. Every game piece has private properties for color, type, number, name,
    and coordinates. Has getter functions to access all of these private properties as well. Communicates with the Board
    class (to place the pieces) and the JanggiGame class (game class determines whether a move is legal, and if the
    pieces result in a winning game state).
    """

    def __init__(self, color, type, number, coordinates=None):

        """
        Every piece starts off with private properties for the color, type, number, name and coordinates, which are
        equal to their parameter counterparts.
        """

        self._color = color
        self._type = type
        self._number = number
        self._name = list(color)[0] + list(color)[1] + list(color)[2] + list(type)[0] + list(type)[1] + list(type)[2] \
            + str(number)
        self._coordinates = coordinates

    def __repr__(self):

        """
        Overrides object's print method to print out its name to better visualize the board.
        """

        return self._name

    def get_color(self):

        """
        Returns the piece's color.
        """

        return self._color

    def get_name(self):

        """
        Returns the piece's name.
        """

        return self._name

    def get_number(self):

        """
        Returns the piece's number.
        """

        return self._number

    def get_type(self):

        """
        Returns the piece's type.
        """

        return self._type

    def get_coordinates(self):

        """
        Returns the piece's coordinates.
        """

        return self._coordinates

    def set_coordinates(self, target_coordinate):

        """
        Changes the piece's current coordinates to the target coordinate.
        """

        self._coordinates = target_coordinate

    def move_up_coordinates(self, up_amount):

        """
        Returns the resultant coordinate after moving up an up_amount number of spaces from the parameter.
        """

        # to move up, we need to subtract one from y-coordinates value

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get new x coordinate

        x = list(current_coordinate)[0]
        # print("x:", x)

        # get new y coordinate

        y = int(list(current_coordinate)[1]) - up_amount
        # print("y:", y)

        # get up_coordinate

        up_coordinate = x + str(y)
        # print("up_coordinate:", up_coordinate)
        return up_coordinate

    def move_down_coordinates(self, down_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate down a down_amount of spaces in
        the parameter.
        """

        # x stays the same, add down_amount to y value

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get new x coordinate

        x = list(current_coordinate)[0]
        # print("x:", x)

        # get new y coordinate

        y = int(list(current_coordinate)[1]) + down_amount
        # print("y:", y)

        # get down_coordinate

        down_coordinate = x + str(y)
        # print("down_coordinate:", down_coordinate)
        return down_coordinate

    def move_left_coordinates(self, left_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate left a left_amount of spaces in
        the parameter.
        """

        # x decrements by a left_amount of letters, y stays the same

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get y coordinate

        y = list(current_coordinate)[1]
        # print("y:", y)

        # get x coordinate

        x = chr(ord(list(current_coordinate)[0])-left_amount)
        # print("x:", x)

        # get left coordinate

        left_coordinate = x + y
        # print("left_coordinate:", left_coordinate)
        return left_coordinate

    def move_right_coordinates(self, right_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate right a right_amount of spaces in
        the parameter.
        """

        # x increments by a right_amount of letters, y stays the same

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get y coordinate

        y = list(current_coordinate)[1]
        # print("y:", y)

        # get x coordinate

        x = chr(ord(list(current_coordinate)[0])+right_amount)
        # print("x:", x)

        # get left coordinate

        right_coordinate = x + y
        # print("right_coordinate:", right_coordinate)
        return right_coordinate

    def move_north_east_coordinates(self, north_east_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate northeast a north_east_amount of
        spaces in the parameter.
        """

        # x increments by a north_east_amount of letters, y decrements by a north_east_amount

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(list(current_coordinate)[1])-north_east_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(list(current_coordinate)[0])+north_east_amount)
        # print("x:", x)

        # get northeast coordinate

        north_east_coordinate = x + y
        print("north_east_coordinate:", north_east_coordinate)
        return north_east_coordinate

    def move_north_west_coordinates(self, north_west_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate northwest a north_west_amount of
        spaces in the parameter.
        """

        # x decrements by a north_west_amount of letters, y decrements by a north_west_amount

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(list(current_coordinate)[1])-north_west_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(list(current_coordinate)[0])-north_west_amount)
        # print("x:", x)

        # get northwest coordinate

        north_west_coordinate = x + y
        print("north_west_coordinate:", north_west_coordinate)
        return north_west_coordinate

    def move_south_west_coordinates(self, south_west_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate southwest a south_west_amount of
        spaces in the parameter.
        """

        # x decrements by a south_west_amount of letters, y increments by a south_west_amount

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(list(current_coordinate)[1])+south_west_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(list(current_coordinate)[0])-south_west_amount)
        # print("x:", x)

        # get southwest coordinate

        south_west_coordinate = x + y
        print("south_west_coordinate:", south_west_coordinate)
        return south_west_coordinate

    def move_south_east_coordinates(self, south_east_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate southeast a south_east_amount of
        spaces in the parameter.
        """

        # x increments by a south_east_amount of letters, y increments by a south_east_amount

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(list(current_coordinate)[1])+south_east_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(list(current_coordinate)[0])+south_east_amount)
        # print("x:", x)

        # get southeast coordinate

        south_east_coordinate = x + y
        print("south_east_coordinate:", south_east_coordinate)
        return south_east_coordinate

class BlueGeneral(Piece):

    """
    Represents a blue general piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):

        """
        Initializes the general piece with private attributes for a blue color, general type, number and coordinates.
        """

        super().__init__("blue", "General", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d8", "d9", "d10", "e8", "e9", "e10", "f8", "f9", "f10"]

        # get current coordinates

        current_coordinate = self.get_coordinates()
        print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        print("right_coordinates:", right_coordinates)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        print("down_coordinates:", down_coordinates)

        # get northeast coordinates

        northeast_coordinates = self.move_north_east_coordinates(1)

        # get northwest coordinates

        northwest_coordinates = self.move_north_west_coordinates(1)

        # get southeast coordinates

        southeast_coordinates = self.move_south_east_coordinates(1)

        # get southwest coordinates to possible moves list

        southwest_coordinates = self.move_south_west_coordinates(1)

        # add moves to "all moves list"

        all_moves_list = [northwest_coordinates, up_coordinates, northeast_coordinates, left_coordinates,
                          current_coordinate, right_coordinates, southwest_coordinates, down_coordinates,
                          southeast_coordinates]
        print("all moves list:", all_moves_list)

        # filter all moves list to possible moves list if coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        print("possible moves list:", possible_moves_list)
        return possible_moves_list


class RedGeneral(Piece):

    """
    Represents a red general piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):

        """
        Initializes the general piece with private attributes for a red color, general type, number and coordinates.
        """

        super().__init__("red", "General", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]

        # get current coordinates

        current_coordinate = self.get_coordinates()
        print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        print("right_coordinates:", right_coordinates)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        print("down_coordinates:", down_coordinates)

        # get northeast coordinates

        northeast_coordinates = self.move_north_east_coordinates(1)

        # get northwest coordinates

        northwest_coordinates = self.move_north_west_coordinates(1)

        # get southeast coordinates

        southeast_coordinates = self.move_south_east_coordinates(1)

        # get southwest coordinates to possible moves list

        southwest_coordinates = self.move_south_west_coordinates(1)

        # add moves to "all moves list"

        all_moves_list = [northwest_coordinates, up_coordinates, northeast_coordinates, left_coordinates,
                          current_coordinate, right_coordinates, southwest_coordinates, down_coordinates,
                          southeast_coordinates]
        print("all moves list:", all_moves_list)

        # filter all moves list to possible moves list if coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        print("possible moves list:", possible_moves_list)
        return possible_moves_list


class BlueGuard(Piece):

    """
    Represents a blue guard. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):

        """
        Initializes a guard piece with a blue color, guard type, number and coordinates.
        """

        super().__init__("blue", "Guard", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class RedGuard(Piece):

    """
    Represents a red guard. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):

        """
        Initializes a guard piece with a red color, guard type, number and coordinates.
        """

        super().__init__("red", "Guard", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class BlueSoldier(Piece):
    """
    Represents a blue soldier piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a soldier piece with a blue color, soldier type, number and coordinates.
        """

        super().__init__("blue", "Soldier", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        print("right_coordinates:", right_coordinates)

        # add moves to possible moves list

        possible_moves_list = [current_coordinate, up_coordinates, left_coordinates, right_coordinates]

        # add more moves to possible moves list if soldier is inside the palace

        # if at d3, can move northeast

        if current_coordinate == "d3":

            northeast_coordinates = self.move_north_east_coordinates(1)
            possible_moves_list.append(northeast_coordinates)

        # if at f3, can move northwest

        if current_coordinate == "f3":

            northwest_coordinates = self.move_north_west_coordinates(1)
            possible_moves_list.append(northwest_coordinates)

        # if at e2, can move northeast and northwest

        if current_coordinate == "e2":

            # add northeast coordinates to possible moves list

            northeast_coordinates = self.move_north_east_coordinates(1)
            possible_moves_list.append(northeast_coordinates)

            # add northwest coordinates to possible moves list

            northwest_coordinates = self.move_north_west_coordinates(1)
            possible_moves_list.append(northwest_coordinates)

        print("possible moves list:", possible_moves_list)
        return possible_moves_list


class RedSoldier(Piece):
    """
    Represents a red soldier piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a soldier piece with a red color, soldier type, number and coordinates.
        """

        super().__init__("red", "Soldier", number, coordinates)

    def get_possible_moves(self):
        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        print("current coordinate:", current_coordinate)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        print("down_coordinates:", down_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        print("right_coordinates:", right_coordinates)

        # add moves to a possible moves list

        possible_moves_list = [current_coordinate, down_coordinates, left_coordinates, right_coordinates]

        # add more moves to the possible moves list if soldier is inside the palace

        # if at d8, can move southeast

        if current_coordinate == "d8":
            southeast_coordinates = self.move_south_east_coordinates(1)
            possible_moves_list.append(southeast_coordinates)

        # if at f8, can move southwest

        if current_coordinate == "f8":
            southwest_coordinates = self.move_south_west_coordinates(1)
            possible_moves_list.append(southwest_coordinates)

        # if at e9, can move southeast and southwest

        if current_coordinate == "e9":

            # add southeast coordinates to possible moves list

            southeast_coordinates = self.move_south_east_coordinates(1)
            possible_moves_list.append(southeast_coordinates)

            # add southwest coordinates to possible moves list

            southwest_coordinates = self.move_south_west_coordinates(1)
            possible_moves_list.append(southwest_coordinates)

        print("possible moves list:", possible_moves_list)
        return possible_moves_list


class BlueHorse(Piece):

    """
    Represents a blue horse piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a horse piece with a blue color, horse type, number and coordinates.
        """

        super().__init__("blue", "Horse", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class RedHorse(Piece):

    """
    Represents a red horse piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a horse piece with a red color, horse type, number and coordinates.
        """

        super().__init__("red", "Horse", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class BlueElephant(Piece):

    """
    Represents a blue elephant piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes an elephant piece with a blue color, elephant type, number and coordinates.
        """

        super().__init__("blue", "Elephant", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class RedElephant(Piece):

    """
    Represents a red elephant piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes an elephant piece with a red color, elephant type, number and coordinates.
        """

        super().__init__("red", "Elephant", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class BlueChariot(Piece):

    """
    Represents a blue chariot piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a chariot piece with a blue color, chariot type, number and coordinates.
        """

        super().__init__("blue", "Chariot", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class RedChariot(Piece):

    """
    Represents a red chariot piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a chariot piece with a red color, chariot type, number and coordinates.
        """

        super().__init__("red", "Chariot", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class BlueCannon(Piece):

    """
    Represents a blue cannon piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a cannon piece with a blue color, cannon type, number and coordinates.
        """

        super().__init__("blue", "Cannon", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class RedCannon(Piece):

    """
    Represents a red cannon piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a cannon piece with a red color, cannon type, number and coordinates.
        """

        super().__init__("red", "Cannon", number, coordinates)

    def check_move(self, current_coordinate, target_coordinate):
        """
        Checks the piece's possible moves from the current_coordinate and makes sure that the target_coordinate is a
        legal move.
        """

        pass


class Player:

    """
    Represents a player in the game. Player class responsibilities include naming each player and keeping track of the
    current player. Has getters for the player name and is_current_player boolean. Communicates with the Board class to
    place the pieces at the desired coordinates, and with the JanggiGame class to determine who the current player is
    and alternate turns.
    """

    def __init__(self, name):
    # def __init__(self, name, is_current_player=None):

        """
        Players have private properties for their name and is_current_player boolean.
        """

        self._name = name
        # self._is_current_player = is_current_player

    def get_name(self):

        """
        Returns the player's name.
        """

        return self._name

    # def get_is_current_player(self):
    #
    #     """
    #     Returns True if the player is the current player, and False if the player is not the current player.
    #     """
    #
    #     return self._is_current_player


class JanggiGame:

    """
    Represents the Janggi game. Janggi game class responsibilities include creating the board and players, alternating
    turns between the players, validating and processing moves, managing the game state and looking for a winning board
    position, and managing "in check" status of the players. The Janggi class communicates with the Board class to
    change the board positions and look for winning board states, the Player class to manage turns and "in check" status
    , and the derived Piece classes to determine if a move is legal or not.

    """

    def __init__(self):

        """
        Initializes the game with an unfinished game state, creates the board and creates the two players.
        """

        self._game_state = "UNFINISHED"

        self._board = [["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"],
                      ["_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______", "_______"]]

        self._coordinate_conversion_dict = {
            "a1": [0, 0],
            "b1": [0, 1],
            "c1": [0, 2],
            "d1": [0, 3],
            "e1": [0, 4],
            "f1": [0, 5],
            "g1": [0, 6],
            "h1": [0, 7],
            "i1": [0, 8],
            "a2": [1, 0],
            "b2": [1, 1],
            "c2": [1, 2],
            "d2": [1, 3],
            "e2": [1, 4],
            "f2": [1, 5],
            "g2": [1, 6],
            "h2": [1, 7],
            "i2": [1, 8],
            "a3": [2, 0],
            "b3": [2, 1],
            "c3": [2, 2],
            "d3": [2, 3],
            "e3": [2, 4],
            "f3": [2, 5],
            "g3": [2, 6],
            "h3": [2, 7],
            "i3": [2, 8],
            "a4": [3, 0],
            "b4": [3, 1],
            "c4": [3, 2],
            "d4": [3, 3],
            "e4": [3, 4],
            "f4": [3, 5],
            "g4": [3, 6],
            "h4": [3, 7],
            "i4": [3, 8],
            "a5": [4, 0],
            "b5": [4, 1],
            "c5": [4, 2],
            "d5": [4, 3],
            "e5": [4, 4],
            "f5": [4, 5],
            "g5": [4, 6],
            "h5": [4, 7],
            "i5": [4, 8],
            "a6": [5, 0],
            "b6": [5, 1],
            "c6": [5, 2],
            "d6": [5, 3],
            "e6": [5, 4],
            "f6": [5, 5],
            "g6": [5, 6],
            "h6": [5, 7],
            "i6": [5, 8],
            "a7": [6, 0],
            "b7": [6, 1],
            "c7": [6, 2],
            "d7": [6, 3],
            "e7": [6, 4],
            "f7": [6, 5],
            "g7": [6, 6],
            "h7": [6, 7],
            "i7": [6, 8],
            "a8": [7, 0],
            "b8": [7, 1],
            "c8": [7, 2],
            "d8": [7, 3],
            "e8": [7, 4],
            "f8": [7, 5],
            "g8": [7, 6],
            "h8": [7, 7],
            "i8": [7, 8],
            "a9": [8, 0],
            "b9": [8, 1],
            "c9": [8, 2],
            "d9": [8, 3],
            "e9": [8, 4],
            "f9": [8, 5],
            "g9": [8, 6],
            "h9": [8, 7],
            "i9": [8, 8],
            "a10": [9, 0],
            "b10": [9, 1],
            "c10": [9, 2],
            "d10": [9, 3],
            "e10": [9, 4],
            "f10": [9, 5],
            "g10": [9, 6],
            "h10": [9, 7],
            "i10": [9, 8],

        }

        # create an alive pieces list

        self._alive_pieces_list = []
        # self._removed_pieces_list = []

        # create and place game pieces, then add to alive pieces list

        self._blue_general = BlueGeneral(1, "e9")
        self.place_piece(self._blue_general, "e9")
        self._alive_pieces_list.append(self._blue_general)

        self._red_general = RedGeneral(1, "e2")
        self.place_piece(self._red_general, "e2")
        self._alive_pieces_list.append(self._red_general)

        self._blue_guard1 = BlueGuard(1, "d10")
        self.place_piece(self._blue_guard1, "d10")
        self._alive_pieces_list.append(self._blue_guard1)

        self._blue_guard2 = BlueGuard(2, "f10")
        self.place_piece(self._blue_guard2, "f10")
        self._alive_pieces_list.append(self._blue_guard2)

        self._red_guard1 = RedGuard(1, "d1")
        self.place_piece(self._red_guard1, "d1")
        self._alive_pieces_list.append(self._red_guard1)
        self._red_guard2 = RedGuard(2, "f1")
        self.place_piece(self._red_guard2, "f1")
        self._alive_pieces_list.append(self._red_guard2)

        self._blue_soldier1 = BlueSoldier(1, "a7")
        self.place_piece(self._blue_soldier1, "a7")
        self._alive_pieces_list.append(self._blue_soldier1)
        self._blue_soldier2 = BlueSoldier(2, "c7")
        self.place_piece(self._blue_soldier2, "c7")
        self._alive_pieces_list.append(self._blue_soldier2)
        self._blue_soldier3 = BlueSoldier(3, "e7")
        self.place_piece(self._blue_soldier3, "e7")
        self._alive_pieces_list.append(self._blue_soldier3)
        self._blue_soldier4 = BlueSoldier(4, "g7")
        self.place_piece(self._blue_soldier4, "g7")
        self._alive_pieces_list.append(self._blue_soldier4)
        self._blue_soldier5 = BlueSoldier(5, "i7")
        self.place_piece(self._blue_soldier5, "i7")
        self._alive_pieces_list.append(self._blue_soldier5)

        self._red_soldier1 = RedSoldier(1, "a4")
        self.place_piece(self._red_soldier1, "a4")
        self._alive_pieces_list.append(self._red_soldier1)
        self._red_soldier2 = RedSoldier(2, "c4")
        self.place_piece(self._red_soldier2, "c4")
        self._alive_pieces_list.append(self._red_soldier2)
        self._red_soldier3 = RedSoldier(3, "e4")
        self.place_piece(self._red_soldier3, "e4")
        self._alive_pieces_list.append(self._red_soldier3)
        self._red_soldier4 = RedSoldier(4, "g4")
        self.place_piece(self._red_soldier4, "g4")
        self._alive_pieces_list.append(self._red_soldier4)
        self._red_soldier5 = RedSoldier(5, "i4")
        self.place_piece(self._red_soldier5, "i4")
        self._alive_pieces_list.append(self._red_soldier5)

        self._blue_horse1 = BlueHorse(1, "c10")
        self.place_piece(self._blue_horse1, "c10")
        self._alive_pieces_list.append(self._blue_horse1)
        self._blue_horse2 = BlueHorse(2, "h10")
        self.place_piece(self._blue_horse2, "h10")
        self._alive_pieces_list.append(self._blue_horse2)
        self._red_horse1 = RedHorse(1, "c1")
        self.place_piece(self._red_horse1, "c1")
        self._alive_pieces_list.append(self._red_horse1)
        self._red_horse2 = RedHorse(2, "h1")
        self.place_piece(self._red_horse2, "h1")
        self._alive_pieces_list.append(self._red_horse2)

        self._blue_elephant1 = BlueElephant(1, "b10")
        self.place_piece(self._blue_elephant1, "b10")
        self._alive_pieces_list.append(self._blue_elephant1)
        self._blue_elephant2 = BlueElephant(2, "g10")
        self.place_piece(self._blue_elephant2, "g10")
        self._alive_pieces_list.append(self._blue_elephant2)
        self._red_elephant1 = RedElephant(1, "b1")
        self.place_piece(self._red_elephant1, "b1")
        self._alive_pieces_list.append(self._red_elephant1)
        self._red_elephant2 = RedElephant(2, "g1")
        self.place_piece(self._red_elephant2, "g1")
        self._alive_pieces_list.append(self._red_elephant2)

        self._blue_chariot1 = BlueChariot(1, "a10")
        self.place_piece(self._blue_chariot1, "a10")
        self._alive_pieces_list.append(self._blue_chariot1)
        self._blue_chariot2 = BlueChariot(2, "i10")
        self.place_piece(self._blue_chariot2, "i10")
        self._alive_pieces_list.append(self._blue_chariot2)
        self._red_chariot1 = RedChariot(1, "a1")
        self.place_piece(self._red_chariot1, "a1")
        self._alive_pieces_list.append(self._red_chariot1)
        self._red_chariot2 = RedChariot(2, "i1")
        self.place_piece(self._red_chariot2, "i1")
        self._alive_pieces_list.append(self._red_chariot2)

        self._blue_cannon1 = BlueCannon(1, "b8")
        self.place_piece(self._blue_cannon1, "b8")
        self._alive_pieces_list.append(self._blue_cannon1)
        self._blue_cannon2 = BlueCannon(2, "h8")
        self.place_piece(self._blue_cannon2, "h8")
        self._alive_pieces_list.append(self._blue_cannon2)
        self._red_cannon1 = RedCannon(1, "b3")
        self.place_piece(self._red_cannon1, "b3")
        self._alive_pieces_list.append(self._red_cannon1)
        self._red_cannon2 = RedCannon(2, "h3")
        self.place_piece(self._red_cannon2, "h3")
        self._alive_pieces_list.append(self._red_cannon2)

        self.display_board()

        self._player1 = Player("blue")
        self._player2 = Player("red")
        self._current_player = "blue"


        # self.make_move("a7", "a6")
        # self.make_move("a4", "a5")
        # self.make_move("a6", "a5")

        # print(self._red_general.get_coordinates())
        # self._red_general.get_possible_moves()
        # self._red_general.set_coordinates("f3")
        # self._red_general.get_possible_moves()

        # print(self._blue_general.get_coordinates())
        # self._blue_general.get_possible_moves()
        # self._blue_general.set_coordinates("d8")
        # self._blue_general.get_possible_moves()

        # self._red_soldier3.set_coordinates("e9")
        # self._red_soldier3.get_possible_moves()

        # self._blue_soldier3.set_coordinates("f3")
        # self._blue_soldier3.get_possible_moves()

        # possible_moves = self._red_soldier3.get_possible_moves()
        # self.get_valid_moves(possible_moves)
        # possible_moves = self._blue_soldier5.get_possible_moves()
        # self.get_valid_moves(possible_moves)

    def get_game_state(self):

        """
        Returns the current game state.
        """

        return self._game_state

    def display_board(self):

        """
        Displays the board.
        """

        for column in self._board:
            for row in column:

                print(row, end=" ")
                # 'end=""' changes the new line of print to an empty space

            print()
            # 'print()' creates a new line after each row

    def convert_coordinates(self, coordinates):

        """
        Converts the game board coordinates to the actual coordinates on the board and returns the actual coordinates.
        """

        for key in self._coordinate_conversion_dict:
            if key == coordinates:
                return self._coordinate_conversion_dict[key]

    def capture_piece(self, piece_coordinates):

        """
        Removes the piece at the piece coordinates in the parameter
        """

        # get piece

        piece = self.get_piece_from_coordinate(piece_coordinates)

        # remove piece from alive pieces list

        self._alive_pieces_list.remove(piece)
        print("piece:", piece, "removed from alive pieces list, which is now:", self._alive_pieces_list)

        # get the piece's current coordinates

        current_coordinate = piece.get_coordinates()

        # convert current coordinate into actual coordinates

        actual_current_coordinate = self.convert_coordinates(current_coordinate)

        # remove piece from board

        self._board[actual_current_coordinate[0]][actual_current_coordinate[1]] = "_______"
        self.display_board()


    def place_piece(self, piece, target_coordinate):

        """
        Places the game piece in the parameter at the target coordinate in the parameter.
        """

        # get the piece's current coordinates

        current_coordinate = piece.get_coordinates()

        # convert current coordinate into actual coordinates

        actual_current_coordinate = self.convert_coordinates(current_coordinate)

        # convert target coordinate into actual coordinates

        actual_target_coordinate = self.convert_coordinates(target_coordinate)

        # remove piece from current coordinate

        self._board[actual_current_coordinate[0]][actual_current_coordinate[1]] = "_______"

        # place piece at target coordinate

        self._board[actual_target_coordinate[0]][actual_target_coordinate[1]] = piece

        # update piece's coordinates

        piece.set_coordinates(target_coordinate)

    def is_coordinate_in_range(self, coordinate):
        """
        Returns True that the coordinate in the parameter is in range, if the letter in its x-value is from "a" to "i"
        and the number in its y-value is from 1 to 10, otherwise returns False.
        """

        for key in self._coordinate_conversion_dict:
            if key == coordinate:
                return True

        return False

        # # we explicitly state the alphabet range
        # alphabet_range = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        #
        #
        # # if the x value of the coordinate is in the alphabet range, and the int cast form of the y value of the
        # # coordinate is from 1 to 10, then return True
        # if list(coordinate)[0] in alphabet_range:
        #     if int(list(coordinate)[1]) in range(1, 11):
        #         return True
        #
        # # Otherwise return False
        # return False

    def get_piece_from_coordinate(self, current_coordinate):

        """
        Returns the board piece at the current coordinate.
        """

        for piece in self._alive_pieces_list:
            if piece.get_coordinates() == current_coordinate:
                return piece

    def get_valid_moves(self, possible_moves_list):

        """
        Returns a list of valid moves, or moves that are inside the board, from the possible moves list in the
        parameter.
        """

        valid_moves_list = []

        for coordinate in possible_moves_list:
            if self.is_coordinate_in_range(coordinate):
                valid_moves_list.append(coordinate)

        print("valid moves list:", valid_moves_list)
        return valid_moves_list

    def is_target_move_valid(self, valid_moves_list, target_coordinate):

        """
        Returns True if the target coordinate in the parameter is inside the valid moves list in the parameter,
        otherwise returns False.
        """

        for valid_move in valid_moves_list:
            if valid_move == target_coordinate:
                return True

        return False

    def switch_players(self):

        """
        Switch the current player for the other player.
        """

        print("current player's color:", self._current_player)
        if self._current_player == "blue":
            self._current_player = "red"
        elif self._current_player == "red":
            self._current_player = "blue"
        print("after switch, current player's color:", self._current_player)


    def is_in_check(self, player_name):

        """
        Checks all the possible moves of the player with the player_name in the parameter to see if any of them lead to
        a "check" status. Returns True if the player is in check, or False otherwise.
        """

        pass

    def make_move(self, from_coordinate, to_coordinate):

        """
        Checks to see if a move from the from_coordinate to the to_coordinate is viable. If the piece is owned by the
        current player, if the move is legal, and if the game is not over, then the move is carried out, which captures
        any opponent piece on the to_coordinate, updates the game status, updates the current player, and returns True.
        If the move is invalid, returns False.
        """

        # get from_piece from the from coordinate and to_piece from the to_coordinate

        from_piece = self.get_piece_from_coordinate(from_coordinate)
        to_piece = self.get_piece_from_coordinate(to_coordinate)
        print("from piece:", from_piece, "and to piece:", to_piece)

        # check to see if piece is owned by current player

        if from_piece.get_color() == self._current_player:
            print("piece's color:", from_piece.get_color(), "matches the current player's name:", self._current_player)

            possible_moves = from_piece.get_possible_moves()
            valid_moves = self.get_valid_moves(possible_moves)

            # check if move is a valid coordinate

            if self.is_target_move_valid(valid_moves, to_coordinate):
                print("to coordinate:", to_coordinate, "is a coordinate inside the valid moves list:", valid_moves)

                # check if to_coordinate isn't occupied, or if it is occupied it's not by an ally piece

                if to_piece is None or (to_piece is not None and to_piece.get_color() != self._current_player):
                    print("to_piece:", to_piece, "is None or is not None and its color [we can't get color of possible "
                          "None type] is not equal to current player's color:", self._current_player)

                    # check if game is over

                    if self.get_game_state() == "UNFINISHED":
                        print("game not over yet, game state:", self.get_game_state())

                        # check if there is an opponent's piece at the to_coordinate

                        if to_piece is not None:
                            print("to_piece:", to_piece, "is not None")

                            if to_piece.get_color() != self._current_player:
                                print("to_piece's color:", to_piece.get_color(), " is not equal to the current player's"
                                      " color:", self._current_player)

                                # capture opponent's piece

                                self.capture_piece(to_coordinate)

                        # move piece

                        self.place_piece(from_piece, to_coordinate)
                        print("piece:", from_piece, "placed at new coordinate:", from_piece.get_coordinates())
                        self.display_board()

                        # update game status code (check for checkmate code here)

                        # switch current player

                        self.switch_players()

                        print("move successful and returning True")
                        return True

        print("move failed and returning False")
        return False


game = JanggiGame()
# board = Board()





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
# pieces move, but not sure how to do that right now. Let's do a bit of brainstorming, what properties do all the pieces
# have in common? They all have a name, location (unless beginning of game), movement pattern. I think these are the 3
# main things right? Alright, let's start doing the piece class and its derivatives. Ok, so let's say the pieces all
# have those private properties, are they going to be parameters in the init? Yeah, I think so, I mean, we want all the
# standard parameters in there, so maybe just name and location? Kinda confused how we'd implement their movement
# pattern as a parameter. Let's just start with the name and location I guess. Looking at the inheritance module, it
# seems we mostly want to give each kind of piece its own init function and override the parent init, so maybe we can
# put the movement in there? Or maybe the movement is a function and we define it for the class? This seems like a
# better plan. Looking at the chess code, we notice that they also have properties of color and type, which seem like
# they can be useful, so we should add those. I'm thinking one of the things we want to check, for example, whether a
# cannon takes another cannon, because that move is illegal, so it's a good idea to know the type data of a piece. They
# also implemented the movement in a function, so we'll try to do that as well. They actually didn't use coordinates
# as a property, but we're gonna keep that for now, because we think it could be useful. Don't see any getters/setters
# either, which seems weird, but maybe we don't need them. From the module, we can redefine the __init__ of the derived
# classes, or we can use "super().__init__(parameters)" to use the superclass' init function. Hmmm.. there are multiple
# pieces of the same type on the board, so we'll need a way to differentiate them. It looks like they created an n
# variable in the class, and ticked it up everytime a piece is made, so I think we should use that.

# I'm a little confused why we have to differentiate between blue and red generals. Can't we just have one general class
# and one's color be blue and the other be red? I think the problem is that each color has certain movements, so we DO
# have to differentiate them because the blue and red generals don't move in the same coordinates. Ok, we got both
# generals down, and put in getters/setters for all the private attributes, and was able to return their names, so that
# seems to be working fine. Now let's go on and all all the other pieces, before we start working on their movement
# functions. As we copy pasted the getters and setters, we realized that that's why we have the Piece superclass, to put
# all these common functions for the pieces in, so we removed all the getters and setters from our derived classes and
# put them in the Piece superclass.

# Alright, we have all our piece classes, and we've created all the piece objects in the Board class, now let's place
# each piece object at the correct starting point. Hmmm... we first need to figure out where all the coordinates on the
# board actually go. We need to figure out basically all the [x,y] coordinates on the computer board, then convert those
# coordinates into standard coordinate format, then finally convert the standard coordinate format to this coordinate
# format ["A-I", 1-10]. Now that we're thinking about this, it will probably makes things a lot easier if we separated
# the x and y coordinates of each piece into its own private property. Afterwards, we can place the pieces on the proper
# coordinates.

# Ok, so let's move the general around and see where he is placed. First of all, [5,5] should be right in the middle.
# Alright, so from placing multiple coordiantes, in this manner [][], we see that [0,0] starts at the upper left of the
# board, and any increase in the x coordinate moves down, up to 9 down, and any increase in the y coordinate moves it
# across, up to 8 across (this is backwards from the standard coordinate system, where x goes across and y goes up).
# Alright, so how are we going to convert these coordinates? We want to convert to the standard system so we know what
# we're doing, but then the position notation for the actual game is [A-I][1-10]. We can read from the letter and number
# notation just fine, so let's just convert the current computer system into the letter number rotation. There are 2
# data points, so I think we should be using a dictionary. Furthermore, the first value, the "key" value, should be the
# letter number notation, then the second value, the "value" value, is its coordinates in the computer coordinate system
# . Let's put the coordinate_conversion_dictionary in our board, putting the values in by hand.

# Alright, so we've converted the letter number coordinates to the computer's coordinate system via the coordinate
# conversion dictionary, so now what? We want to place our pieces, but how are we going to use the conversion dictionary
# to place the pieces? If we want a1, we can't just put a1 into the parameter for the coordinates, we're going to have
# to put the conversion code inside each piece, so probably in the piece class we can convert the coordinates.

# Let's figure out when we want to convert the coordinates, because for the most part, we want the coordinate of the
# pieces in letter number notation. Well, let's try to place our pieces that we created in the board class. Let's start
# with the bluegeneral, who should go on e9. So what we want, is a convert coordinates function, but the question now is
# so we want that in the board class, or our game class? We feel like this is more of a Board class issue, so let's keep
# it in the board class for now. So we created the convert coordinates function, but now we want to call it inside the
# place piece function I think, so let's create the place_piece function. Wow, we created the convert method, and the
# place piece method, and it worked out beautifully, we were expecting that to not place the piece correctly (maybe we
# are just paranoid from all the assembly code failing first try).

# Alright, we've placed all the pieces, and they show up on the board as their color, type, and number concatenated
# names, which looks good and is very identifiable. However, this board is not aligned and looks very messy. I'm not
# we can see moves on this current board, bc it's not properly aligned. We're thinking maybe we can use a list for each
# object, and that might line it up, but we're gonna have to change not only the initial board, but the coordinates
# and its conversion system too, which is a lot of work. Let's work with this and see how the pieces look, if we can
# determine the moves like this, bc it is a lot of work to uphaul our data structure.

# So, we've created the game board, created the pieces, and placed them all. Now what? I think we want to start working
# on the Player class and the Game class itself. Wait a minute, we just had an idea. What if we make all names the same
# length? Then the display would show up perfectly. How do we do that? Well, all the numbers are 1 character so that's
# a good start. We can change red and blue to "red" and "blu" so that both colors only have 3 characters. Then we can
# take just the first 3 characters of all the types, which gives us a name of 7 characters, yeah, this might work. Wow,
# that worked out amazingly. It's amazing what a little break can do for the brainstorming.

# Alright, so we need to create this Player class. What is the class going to handle? It's gonna differentiate between
# the red and blue players. It's going to keep track of the turns. That's all we can think of for now. I'm not sure how
# we want to incorporate the current player into the player class. I mean, if we make it a private property, then both
# player objects have the current player property, which is weird right? Or, we can set it up to be a boolean property?
# Yeah, if we make it a boolean, we can check if the current player property is true or false. Yeah, let's try that,
# that sounds good. I think the player class is fine for now. We have the name and the is_current_player boolean, which
# just might be all we need.

# Now, let's do the last class, the JanngiGame class. Alright, that worked out really well again. We created the board
# from the game class, and let the board place the pieces. We created the two players as well. Alright, now what? Maybe
# we should submit our halfway report? It might be a good idea, but I'm not sure that we are halfway lol, but we do
# have all the classes now.

# That was pretty annoying and took longer than we thought. Alright, now, we did write some docstrings for the methods
# that we still need to implement, so we should start working on those, but which one first? I like figuring out the
# piece movements first, it's a nice little segway into the make move function and the function for calculating check
# mates.

# I think we want to start with the General's movements because they seem pretty simple. Looking at it, we just realized
# that we haven't defined the palace, and the palace actually has different movement rules (ugh). I guess we can just
# check the general's, or whatever the piece we're looking at, movement and assign specific coordinates to be equal to
# the palace, to differentiate it from the other coordinates. For example, we can check if the movement is in the range
# of "d8 to d10, e8 to e10, and f8 to f10," which are all the coordinates for the palace. Let's actually step away from
# this a bit, and do the easiest movements first. I'm thinking it's the soldiers. What are the characteristics of the
# soldier's movement? There normal movements are up, left, or right (they can't go backwards). Once they reach the end
# of the board, they can only move sideways. Lastly, while in the palace (this is only the opponent's palace because
# they can't go back into their own palace), they can move diagonally forward (still no backwards, but diagonally
# allowed in the palace).

# can we take the current coordinates and just theoretically calculate the possible coordinates? ok, so the
# current coordinates are "e7", so moving up is "e6", which is list(coordinates)[1]-1. To move to the left is
# , we need to decrease the alphabet by a letter. I'm not sure how to do this. Stackoverflow says there is a
# "chr" function that we can use, in this manner:
# >> > chr(ord('c') + 1) = "d"
# Let's try this code out in the console and see if it even works. Ok, so this does work. The "ord" function
# apparently receives the Unicode character and the "chr" function produces them.
# chr(ord("e")-1), good, this code works to get the letter d. So what is the formula for this?
# ok, so let's try this out. We are at "e7" and we want the coordinates to move up. To move up, we need to
# change subtract one from the y part of the coordinate, so using the move_valid function parameters, we want
# to do this: list(current_cordinate)[1]-1 , which we set to be the y value of the up coordinate, and the x
# value stays the same. Then, to move left, we need to decrement 1 character in the alphabet. Using the
# parameter in the function, this would code out as: chr(ord(list(current_coordinate)[0])-1), which we set equal
# to the x value of the left coordinate, and they y value stays the same. To move to the right, we increment the
# letter in x, and leave the number in y the same. Alright, we need to code this out.

# alright, we wrote the code, but it was very annoying to test it. Creating the pieces inside the board class was a bad
# idea, because we can't access the pieces, so we switched it out and created all the pieces in the game class, just so
# we could call "is_move_valid" to see if it worked, which luckily it did, but it was very annoying when we tried the
# code in the python console. It gave us a missing parameter error, but we had the parameter there. Anyways, using our
# code, we go the correct coordinate of the up coordinate, which was e6. I think the change to creating the pieces in
# the game class was correct. We want all the relevant objects in the game class so that we can call them and their
# functions. Let's finish writing the coordinates for left and right, and update the code to create all the pieces in
# in the game class.

# Alright, so we've managed to code the simple coordinates for up, left, and right for a solider. What else needs to be
# done? Well, before we can say that those are valid coordinates, we have to check the x and y values. So, what are we
# checking? We need to check if the x value is between "a" to "i" and that the y value is between 1 and 10 (string form
# or int form, whichever is easier). If they are not, then the move is out of bounds, and we reject that possible
# coordinate as a valid coordinate. We want to add all these coordinates into a list of valid coordinates, then we can
# iterate through the list and see if the target coordinate is in the valid coordinates list, and if so, then the move
# is valid (wow, so complicated).

# So we want to do a is_coordinate_inside_range function, but not sure where to put it? This is one where we want to
# use on all the derived pieces, so it should be in the Piece superclass. Ugh, we were testing our is coordinate inside
# range function and realized that it wasn't working. We looked over our alphabet range and we had it like this:
# alphabet_range = ["a,b,c,d,e,f,g,h,i"], but it should be like this: alphabet_range = ["a", "b", "c", "d", "e", "f",
# "g", "h", "i"]. We've made this mistake several times already and it's kinda frustrating to keep making it.
# Furthermore, the number range check in our code was also wrong. We forgot that the number is in string form, so when
# we checked it vs a "range(1,11)", it said it wasn't in range, but we needed to int cast the number because it was in
# string form. The function was relatively simple, but failed at both checks lol.

# So we defined the is_move_valid and is_coordinate_inside_range functions, but we still aren't done with the Soldier
# class. We need to account for the soldier's movement change inside the palace, and then we have to check the valid
# coordinates list and see if the target coordinate is in it, and if so, return that the move is valid, otherwise return
# that it isn't valid. Actually, as we shut it Python off for the day, we realized that all the possible coordinates are
# actually already in the coordinate_conversion_dict, so we just need to make sure the possible matches one of the keys
# in the dictionary to see if the coordinate is inside range. Hmm... we're having issues accessing the coordinate
# conversion dict in the Board class, even after a getter function. Now that we think about it, putting this check
# the Piece class doesn't make that much sense. Should we move it to the game class where we should have access to the
# dictionary (shouldn't the game class have access to everything?)?

# Looking over things, I think there should actually be a big revamp. The convert coordinates and the place piece
# functions, since we want to move the converted coordiantes dicitonary, should follow this dictionary, so they should
# all be inside the game class, so this board class is actually pretty bare if we change it, which I guess isn't a big
# deal? Going even deeper, we realized that we can't access the board outside of the game's init function, where it's
# defined. It actually doesn't make sense to create, and the players as well, inside their own classes. The private
# objects should all be created inside the game class, so that we can access them, otherwise we can't access their
# properties and call their functions. Alright, so let's revamp it like this now. If we remove all these things from
# the board class, do we even need the board class? As it is right now, we don't. If we remove the Board class creating
# its own board, which now that we think about it, is a bad idea since we can't access that object. Yeah, I think for
# now, we will scrap the board class and just create the board inside the game class.

# There is one issue we're seeing with moving everything to the game class, and that is the derived Piece classes can't
# access the is coordinate in range method, so we really want to access that method outside of the object, which makes
# more intuitive sense. Objects shouldn't check themselves whether a move is valid, that seems like something the game
# logic should be doing so... why don't each piece class calculate its possible moves, then give that as a parameter
# to the game class to validate whether the moves are in range, then determine if a target coordinate is part of a moves
# valid moves. More specifically, when the player wants to move a piece from its current coordinate to the target
# coordinate, we call that pieces "get_possible_moves" function, which will return a list of all its possible moves. We
# take that list as a parameter and filter the list with a "get_valid_moves" function, which will refine the list into
# coordinates that are within range of the board and return a list of valid moves, then we can compare the list of valid
# coordinates to the target list, and if the target coordinate is in the valid moves list, then the move is executed. OK
# so how does this relate to the make move function that we need to implement? So, the make move function has parameters
# for the current coordinate and the target coordinate (no piece parameter). How do we combine all these functions to
# incorporate the make move function. The first thing we need to do is find the piece on the current coordinates. How
# do we do that? One way is to have a list of the current alive pieces, then we can iterate thought that list, and for
# each piece, get its current coordinates and see if one matches the current coordinate of the make move function. We
# can return this object so that it can be moved by the place piece function. Alright, so let's code that now.

# Alright, so we were able to code that pretty quickly. Now what. We have the returned piece from the current coordinate
# of the make move function, now we need to determine the possible moves of that piece. Ok, our get possible moves from
# the game piece is working and returning the possible moves list. Now what. We need to get a list of valid moves, so
# let's create that function which takes in the possible moves list as a parameter. Ok, we have the valid moves list now
# so we need to determine if the target coordinate is in the valid moves list. As we were testing the new "is target
# move valid" function, we realized that if they move to the same spot as they are currently on, that is still a valid
# move because you can just pass the turn, so we need to make sure, that the current coordinate is always a valid move.

# Ok, I think we've implemented all the necessary checking moves logic. Now let's write it into the make move function
# and try to move a piece and see what happens. Lol, we need to see if the piece is owned by the current player, but
# I don't like the way our current player is set up, as a property of the players. Let's change it to a private property
# of the game. Alright, we're able to place the piece from the make move function. There are a lot of situations to test
# here, so we need to do that later, but for now, we've noticed that piece that we moved is both in the current spot
# and the new spot. Are we moving pieces wrong? Maybe instead of moving the piece, we change its current coordinates?
# Lol, changing the pieces current coordinates, while we do think it is necessary, just updates it coordinates property
# but the piece is still there. How do we remove the old piece? I mean, we can put it somewhere else, like in a removed
# pieces list, but that seems pretty bad? It's still technically exists. Well, we goggled it and couldn't find anything,
# so I guess we'll just implement a removed pieces list. Lol, that didn't work. Actually, I think we can remove a piece
# just by replacing that coordiante with the original thing, which was a string of 7 underscores. Ok, good, that worked.

# One thing of note that we were thinking about yesterday. Currently the place piece function just places the piece, but
# it does not update the pieces coordinates, so make sure we write another function to update the pieces coordiantes, or
# update it inside of place piece itself. Yeah, we fixed it by adding a set coordinates to the Piece superclass,and just
# setting the coordinate to the target coordinate after placing the piece.

# We still need to finish all aspects of the make move function (returning of True or False, updating the game status
# and player turns after a successful move), then we need to test each if statement to make sure they are working
# properly. Do we want to update our midway progress report? We've made quite a few significant changes. Maybe by the
# end of the day?

# So, we need to check if there's an opponent's piece on the board that we want to capture. What happens if we call our
# get piece from coordinate and there is no piece, does it give us an error, or return None? Ok, good, when there is no
# piece, it returns None instead of giving an exception error, so we can work with that. We tried the game out and we
# can't capture our own units, so if our unit is in the spot we want to move to, we can't make that move. This needs
# to be in the make move function. Ugh, we are calling get color for the None type and getting an attribute error, we
# need to separate the code for the there being nothing on the to coordinate from the code where there is. Let's go
# through this logic again. If there is no piece on the board, we don't have to check the color and we don't have to
# capture any piece. If there is a piece on the board, we have to check and see if it's an ally or opponent. If it's an
# ally, the move is not valid, if it's an opponent and everything else is ok, then before the move gets executed we have
# to capture the opponent's piece. So when exactly do we need to check if there is a piece on the to_coordinate? Before
# the move can be validated, we need to know if there is an ally on the to_coordinate. Wow, apparently we coded it
# correctly, but the issue was the print statement trying to call the color of the None type causing a attribute error.
# We need to read the errors more carefully. It was weird because the rest of the code kept running, I guess because
# Python knows it was just an insignificant print error?

# Alright, I think we finally implemented the check to see if an ally in on the to coordinate. Now, we're still not done
# with the make move function. We still need to update the game state, update current player, and return True, else
# return False. Ok, so we're testing the make move function and we pasted the moves of the blue soldiers into the red
# soldier, but we soon found out, they don't move the same way. The blue soldier can up, relative to the board, but the
# red soldier, actually moves down, relative to the board, so we have to modify the red soldier's movement slightly. OK
# so we were able to move the blue and red soldiers into each other, and capture the red soldier, while alternating
# turns.

# So currently we only have one requirement from the assignment we haven't done, and that's the "is_in_check" function,
# which we want to save for later until the end where we do the checkmate function as well. For now, I think we want to
# implement and test each piece type's movements at a time, then do the is in check function, then code the check for
# checkmate at the end of each turn.

# Now that we've looked back at soldier movement, we realized we aren't completely done. We still have to code the
# soldier movement inside the palace. Alright, so inside the palace they can move diagonally forward (still can't go
# backwards). Let's add an if statement after all the current movement, for the special palace movement, and add those
# coordinates, if the soldier current coordinates are inside the palace, which for the blue soldier, is d1-d3, e1-e3,
# and f1-f3, and for the red soldier, it's d8-d10, e8-e10, and f8-f10. Alright, I think this shouldn't be too bad. Let's
# code it. Now that we're doing this, it's kinda annoying. Moving up is always the same, moving to the right is always
# the same, moving to the left is always the same, can we create a function to use that we don't have to keep retyping
# the movement code everytime. Not only is it a headache to think about, we seen that we've already done it before, so
# it just seems super unnecessary. Let's try to write a move up function in the Piece superclass.

# I think that worked really well. We have a parameter for the "up_amount", and this is calculated the same for all up
# movements, so it's gonna be a very useful function. Let's write the left, right, and down functions in the Piece class
# then update the current soldier code to incorporate the new functions, and finally use the new functions to create
# movement for the soldier's in palace movements.

# Alright, we've coded the 4 orthogonal directions, now we need to implement them in the current class. Ok, so we got
# them incorporated into the blue soldier class, oh, we need to do the red soldier class too. Ok, we just copy pasted
# the blue soldier code and switched out the up coordinate for down coordinates, so much easier when its modular. OK,
# now we need to code the blue soldiers in palace movements. Actually, let's code the diagonal movements, from the top
# of our head, we can think of 3 types of pieces that use this singular diagonal movement. Ok, so we were able to add
# all the diagonal movements, with a parameter for multiple diagonal moves. Now, let's add the movement for the blue,
# then red soldier, in the palace, and test the diagonal moves for valid moves and the other function after that. Dammit
# this soldier movement within the palace is confusing, but after looking at a couple different diagrams, I think we
# understand now. There are only 4 coordinates where the soldier can move diagonally, even though there are 9
# coordinates inside the palace, those 4 coordinates being... Actually, we double checked, and there are only 3 spots
# where they can move diagonally, those being d3, f3, and e2.

# Alright, so let's test this out. We're gonna need to change the current coordinates of a piece first, then we can run
# the tests. Let's use our bluesoldier3 here and check it. Alright, all the blue soldier tests are good. Now let's add
# the redsoldier palace code, and run the tests. RedSoldier palace coordinates are d8, f8, or e9. Alright, we've added
# the palace movements for both the red and blue soldiers, not bad.

# Let's go ahead and code the general and the guard movements, because they are very similar, and use our Piece class
# movements already. Alright, so the general can move up, down, left, right, and diagonally, but the target coordinate
# needs to be inside the palace. Hmmm... so how do we code the palace restriction? Ok, so we're thinking more about the
# movement restrictions. Currently we have a function to check if the movements are inside the board, which is in the
# game class. But we're thinking, we can just keep it in the piece class, since each piece knows there movements? Like
# for the general movements, it has to be inside the palace, but our game code for the is valid move function just
# checks if the coordinates are inside the board, which for the general, he can't move outside the palace, so this check
# is not required here. Basically, we should be having the pieces calculate all their movement logic, is what it is.
# Alright, so for the blue general, we put his move restriction inside the get possible moves function, without a
# secondary function to check if the moves are on the board, because he can't go off the board... wait a min, he can go
# off the board lol. Yeah, he can go off the board, if he moves to the bottom, he can, so we still need to check if it's
# inside the board, but we already checked that, because we checked if his move is inside the palace, which is inside
# the board. Let's test the general code for 2 border spots to make sure it's working, then recode our blue and red
# soldiers to check if their coordinates are inside the board inside their possible moves function. Alright, the code
# seems to be working for the blue general. Let's copy the code into the red general before we fix the soldier code.
# Alright, red general looks fine, let's recode the blue and red soldier. Dammit, we can't do this. We just realized, we
# can't access the converted coordinates dict because it is a private data in the game class.

# we need to code the guard movements, which are exactly like the general's movements.