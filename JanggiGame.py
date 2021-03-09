# Author: Bobby Nguyen
# Date: 2/26/21
# Description: Janggi game halfway progress report


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
        # self._previous_coordinate = None

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

    def get_previous_coordinate(self):

        """
        Returns the piece's previous coordinate.
        """

        return self._previous_coordinate

    def set_previous_coordinate(self, coordinate):

        """
        Sets the piece's previous coordinate equal to the coordinate in the parameter.
        """

        self._previous_coordinate = coordinate

    def move_up_coordinates(self, up_amount):

        """
        Returns the resultant coordinate after moving up an up_amount number of spaces from the parameter.
        """

        # to move up, we need to subtract one from y-coordinates value

        # get current coordinate

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get new x coordinate

        x = current_coordinate[0]
        # print("x:", x)

        # get new y coordinate

        y = int(current_coordinate[1:]) - up_amount
        # print("y:", y)

        # if len(list(current_coordinate)) == 2:
        #     y = int(list(current_coordinate)[1]) - up_amount
        #     print("y:", y)
        # elif len(list(current_coordinate)) == 3:
        #     y = int(list(current_coordinate)[1]+list(current_coordinate)[2]) - up_amount
        #     print("y:", y)

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

        x = current_coordinate[0]
        # x = list(current_coordinate)[0]
        # print("x:", x)

        # get new y coordinate

        y = int(current_coordinate[1:]) + down_amount
        # y = int(list(current_coordinate)[1]) + down_amount
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

        y = current_coordinate[1:]
        # y = list(current_coordinate)[1]
        # print("y:", y)

        # get x coordinate

        x = chr(ord(current_coordinate[0]) - left_amount)
        # x = chr(ord(list(current_coordinate)[0])-left_amount)
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

        y = current_coordinate[1:]
        # y = list(current_coordinate)[1]
        # print("y:", y)

        # get x coordinate

        x = chr(ord(current_coordinate[0]) + right_amount)
        # x = chr(ord(list(current_coordinate)[0])+right_amount)
        # print("x:", x)

        # get left coordinate

        right_coordinate = x + y
        # print("right_coordinate:", right_coordinate)
        return right_coordinate

    def move_north_east_coordinates(self, north_east_amount, current_coordinate=None):
    # def move_north_east_coordinates(self, north_east_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate northeast a north_east_amount of
        spaces in the parameter.
        """

        # x increments by a north_east_amount of letters, y decrements by a north_east_amount

        # get current coordinate

        if current_coordinate is None:
            current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(current_coordinate[1:]) - north_east_amount)
        # y = str(int(list(current_coordinate)[1])-north_east_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(current_coordinate[0]) + north_east_amount)
        # x = chr(ord(list(current_coordinate)[0])+north_east_amount)
        # print("x:", x)

        # get northeast coordinate

        north_east_coordinate = x + y
        # print("north_east_coordinate:", north_east_coordinate)
        return north_east_coordinate

    def move_north_west_coordinates(self, north_west_amount, current_coordinate=None):
    # def move_north_west_coordinates(self, north_west_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate northwest a north_west_amount of
        spaces in the parameter.
        """

        # x decrements by a north_west_amount of letters, y decrements by a north_west_amount

        # get current coordinate

        if current_coordinate is None:
            current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(current_coordinate[1:]) - north_west_amount)
        # y = str(int(list(current_coordinate)[1])-north_west_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(current_coordinate[0]) - north_west_amount)
        # x = chr(ord(list(current_coordinate)[0])-north_west_amount)
        # print("x:", x)

        # get northwest coordinate

        north_west_coordinate = x + y
        # print("north_west_coordinate:", north_west_coordinate)
        return north_west_coordinate

    def move_south_west_coordinates(self, south_west_amount, current_coordinate=None):
    # def move_south_west_coordinates(self, south_west_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate southwest a south_west_amount of
        spaces in the parameter.
        """

        # x decrements by a south_west_amount of letters, y increments by a south_west_amount

        # get current coordinate

        if current_coordinate is None:
            current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(current_coordinate[1:]) + south_west_amount)
        # y = str(int(list(current_coordinate)[1])+south_west_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(current_coordinate[0]) - south_west_amount)
        # x = chr(ord(list(current_coordinate)[0])-south_west_amount)
        # print("x:", x)

        # get southwest coordinate

        south_west_coordinate = x + y
        # print("south_west_coordinate:", south_west_coordinate)
        return south_west_coordinate

    def move_south_east_coordinates(self, south_east_amount, current_coordinate=None):
    # def move_south_east_coordinates(self, south_east_amount):

        """
        Returns the coordinates after the piece moves from its current coordinate southeast a south_east_amount of
        spaces in the parameter.
        """

        # x increments by a south_east_amount of letters, y increments by a south_east_amount

        # get current coordinate

        if current_coordinate is None:
            current_coordinate = self.get_coordinates()

        # get y coordinate

        y = str(int(current_coordinate[1:]) + south_east_amount)
        # y = str(int(list(current_coordinate)[1])+south_east_amount)
        # print("y:", y)

        # get x coordinate

        x = chr(ord(current_coordinate[0]) + south_east_amount)
        # x = chr(ord(list(current_coordinate)[0])+south_east_amount)
        # print("x:", x)

        # get southeast coordinate

        south_east_coordinate = x + y
        # print("south_east_coordinate:", south_east_coordinate)
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
        # print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        # print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        # print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        # print("right_coordinates:", right_coordinates)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        # print("down_coordinates:", down_coordinates)

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
        # print("all moves list:", all_moves_list)

        # filter all moves list to possible moves list if coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        # print("possible moves list:", possible_moves_list)
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
        # print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        # print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        # print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        # print("right_coordinates:", right_coordinates)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        # print("down_coordinates:", down_coordinates)

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
        # print("all moves list:", all_moves_list)

        # filter all moves list to possible moves list if coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        # print("possible moves list:", possible_moves_list)
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

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d8", "d9", "d10", "e8", "e9", "e10", "f8", "f9", "f10"]

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        # print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        # print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        # print("right_coordinates:", right_coordinates)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        # print("down_coordinates:", down_coordinates)

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
        # print("all moves list:", all_moves_list)

        # filter all moves list to possible moves list if coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class RedGuard(Piece):

    """
    Represents a red guard. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):

        """
        Initializes a guard piece with a red color, guard type, number and coordinates.
        """

        super().__init__("red", "Guard", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        # print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        # print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        # print("right_coordinates:", right_coordinates)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        # print("down_coordinates:", down_coordinates)

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
        # print("all moves list:", all_moves_list)

        # filter all moves list to possible moves list if coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


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
        # print("current coordinate:", current_coordinate)

        # get move up coordinates

        up_coordinates = self.move_up_coordinates(1)
        # print("up_coordinates:", up_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        # print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        # print("right_coordinates:", right_coordinates)

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

        # print("possible moves list:", possible_moves_list)
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
        # print("current coordinate:", current_coordinate)

        # get move down coordinates

        down_coordinates = self.move_down_coordinates(1)
        # print("down_coordinates:", down_coordinates)

        # get move left coordinates

        left_coordinates = self.move_left_coordinates(1)
        # print("left_coordinates:", left_coordinates)

        # get move right coordinates

        right_coordinates = self.move_right_coordinates(1)
        # print("right_coordinates:", right_coordinates)

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

        # print("possible moves list:", possible_moves_list)
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

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get move up and northwest coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_coordinates = self.move_north_west_coordinates(1, up_coordinates)
        # print("up_and_northwest_coordinates:", up_and_northwest_coordinates)

        # get move up and northeast coordinates

        up_and_northeast_coordinates = self.move_north_east_coordinates(1, up_coordinates)
        # print("up_and_northeast_coordinates:", up_and_northeast_coordinates)

        # get move down and southwest coordinates

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_coordinates = self.move_south_west_coordinates(1, down_coordinates)
        # print("down_and_southwest_coordinates:", down_and_southwest_coordinates)

        # get move down and southeast coordinates

        down_and_southeast_coordinates = self.move_south_east_coordinates(1, down_coordinates)
        # print("down_and_southeast_coordinates:", down_and_southeast_coordinates)

        # get move left and southwest coordinates

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_coordinates = self.move_south_west_coordinates(1, left_coordinates)
        # print("left_and_southwest_coordinates:", left_and_southwest_coordinates)

        # get move left and northwest coordinates

        left_and_northwest_coordinates = self.move_north_west_coordinates(1, left_coordinates)
        # print("left_and_northwest_coordinates:", left_and_northwest_coordinates)

        # get move right and southeast coordinates

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_coordinates = self.move_south_east_coordinates(1, right_coordinates)
        # print("right_and_southeast_coordinates:", right_and_southeast_coordinates)

        # get move right and northeast coordinates

        right_and_northeast_coordinates = self.move_north_east_coordinates(1, right_coordinates)
        # print("right_and_northeast_coordinates:", right_and_northeast_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_coordinates, up_and_northeast_coordinates,
                               down_and_southwest_coordinates, down_and_southeast_coordinates,
                               left_and_southwest_coordinates, left_and_northwest_coordinates,
                               right_and_southeast_coordinates, right_and_northeast_coordinates]

        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class RedHorse(Piece):

    """
    Represents a red horse piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a horse piece with a red color, horse type, number and coordinates.
        """

        super().__init__("red", "Horse", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get move up and northwest coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_coordinates = self.move_north_west_coordinates(1, up_coordinates)
        # print("up_and_northwest_coordinates:", up_and_northwest_coordinates)

        # get move up and northeast coordinates

        up_and_northeast_coordinates = self.move_north_east_coordinates(1, up_coordinates)
        # print("up_and_northeast_coordinates:", up_and_northeast_coordinates)

        # get move down and southwest coordinates

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_coordinates = self.move_south_west_coordinates(1, down_coordinates)
        # print("down_and_southwest_coordinates:", down_and_southwest_coordinates)

        # get move down and southeast coordinates

        down_and_southeast_coordinates = self.move_south_east_coordinates(1, down_coordinates)
        # print("down_and_southeast_coordinates:", down_and_southeast_coordinates)

        # get move left and southwest coordinates

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_coordinates = self.move_south_west_coordinates(1, left_coordinates)
        # print("left_and_southwest_coordinates:", left_and_southwest_coordinates)

        # get move left and northwest coordinates

        left_and_northwest_coordinates = self.move_north_west_coordinates(1, left_coordinates)
        # print("left_and_northwest_coordinates:", left_and_northwest_coordinates)

        # get move right and southeast coordinates

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_coordinates = self.move_south_east_coordinates(1, right_coordinates)
        # print("right_and_southeast_coordinates:", right_and_southeast_coordinates)

        # get move right and northeast coordinates

        right_and_northeast_coordinates = self.move_north_east_coordinates(1, right_coordinates)
        # print("right_and_northeast_coordinates:", right_and_northeast_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_coordinates, up_and_northeast_coordinates,
                               down_and_southwest_coordinates, down_and_southeast_coordinates,
                               left_and_southwest_coordinates, left_and_northwest_coordinates,
                               right_and_southeast_coordinates, right_and_northeast_coordinates]

        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class BlueElephant(Piece):

    """
    Represents a blue elephant piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes an elephant piece with a blue color, elephant type, number and coordinates.
        """

        super().__init__("blue", "Elephant", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get move up and northwest twice coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, up_coordinates)
        # print("up_and_northwest_twice_coordinates:", up_and_northwest_twice_coordinates)

        # get move up and northeast twice coordinates

        up_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, up_coordinates)
        # print("up_and_northeast_twice_coordinates:", up_and_northeast_twice_coordinates)

        # get move down and southwest twice coordinates

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, down_coordinates)
        # print("down_and_southwest_twice_coordinates:", down_and_southwest_twice_coordinates)

        # get move down and southeast twice coordinates

        down_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, down_coordinates)
        # print("down_and_southeast_twice_coordinates:", down_and_southeast_twice_coordinates)

        # get move left and southwest twice coordinates

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, left_coordinates)
        # print("left_and_southwest_twice_coordinates:", left_and_southwest_twice_coordinates)

        # get move left and northwest twice coordinates

        left_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, left_coordinates)
        # print("left_and_northwest_twice_coordinates:", left_and_northwest_twice_coordinates)

        # get move right and southeast twice coordinates

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, right_coordinates)
        # print("right_and_southeast_twice_coordinates:", right_and_southeast_twice_coordinates)

        # get move right and northeast twice coordinates

        right_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, right_coordinates)
        # print("right_and_northeast_twice_coordinates:", right_and_northeast_twice_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_twice_coordinates, up_and_northeast_twice_coordinates,
                               down_and_southwest_twice_coordinates, down_and_southeast_twice_coordinates,
                               left_and_southwest_twice_coordinates, left_and_northwest_twice_coordinates,
                               right_and_southeast_twice_coordinates, right_and_northeast_twice_coordinates]

        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class RedElephant(Piece):

    """
    Represents a red elephant piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes an elephant piece with a red color, elephant type, number and coordinates.
        """

        super().__init__("red", "Elephant", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # get move up and northwest twice coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, up_coordinates)
        # print("up_and_northwest_twice_coordinates:", up_and_northwest_twice_coordinates)

        # get move up and northeast twice coordinates

        up_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, up_coordinates)
        # print("up_and_northeast_twice_coordinates:", up_and_northeast_twice_coordinates)

        # get move down and southwest twice coordinates

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, down_coordinates)
        # print("down_and_southwest_twice_coordinates:", down_and_southwest_twice_coordinates)

        # get move down and southeast twice coordinates

        down_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, down_coordinates)
        # print("down_and_southeast_twice_coordinates:", down_and_southeast_twice_coordinates)

        # get move left and southwest twice coordinates

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, left_coordinates)
        # print("left_and_southwest_twice_coordinates:", left_and_southwest_twice_coordinates)

        # get move left and northwest twice coordinates

        left_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, left_coordinates)
        # print("left_and_northwest_twice_coordinates:", left_and_northwest_twice_coordinates)

        # get move right and southeast twice coordinates

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, right_coordinates)
        # print("right_and_southeast_twice_coordinates:", right_and_southeast_twice_coordinates)

        # get move right and northeast twice coordinates

        right_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, right_coordinates)
        # print("right_and_northeast_twice_coordinates:", right_and_northeast_twice_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_twice_coordinates, up_and_northeast_twice_coordinates,
                               down_and_southwest_twice_coordinates, down_and_southeast_twice_coordinates,
                               left_and_southwest_twice_coordinates, left_and_northwest_twice_coordinates,
                               right_and_southeast_twice_coordinates, right_and_northeast_twice_coordinates]

        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class BlueChariot(Piece):

    """
    Represents a blue chariot piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a chariot piece with a blue color, chariot type, number and coordinates.
        """

        super().__init__("blue", "Chariot", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # create moves lists and move dictionary

        possible_moves_list = [current_coordinate]
        move_dictionary = {}
        up_list = []
        left_list = []
        right_list = []
        down_list = []

        # define boundaries

        top_boundary = 1
        bottom_boundary = 10
        left_boundary = ord("a")
        right_boundary = ord("i")

        # calculate number of spaces from boundaries

        up_spaces = int(current_coordinate[1:]) - top_boundary
        down_spaces = abs(int(current_coordinate[1:]) - bottom_boundary)
        right_spaces = abs(ord(current_coordinate[0]) - right_boundary)
        left_spaces = ord(current_coordinate[0]) - left_boundary
        # print("up_spaces:", up_spaces, "down_spaces:", down_spaces, "right_spaces:", right_spaces, "left_spaces:",
        #       left_spaces)

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            # print("up_coordinates:", up_coordinates)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            # print("left_coordinates:", left_coordinates)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            # print("right_coordinates:", right_coordinates)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            # print("down_coordinates:", down_coordinates)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2, can move northeast, northwest, southeast, or southwest

        elif current_coordinate == "e2" or current_coordinate == "e9":

            # get all coordinates

            northeast_coordinates = self.move_north_east_coordinates(1)
            northwest_coordinates = self.move_north_west_coordinates(1)
            southeast_coordinates = self.move_south_east_coordinates(1)
            southwest_coordinates = self.move_south_west_coordinates(1)

            # add all coordinates

            northeast_list = [northeast_coordinates]
            move_dictionary["northeast_list"] = northeast_list
            northwest_list = [northwest_coordinates]
            move_dictionary["northwest_list"] = northwest_list
            southeast_list = [southeast_coordinates]
            move_dictionary["southeast_list"] = southeast_list
            southwest_list = [southwest_coordinates]
            move_dictionary["southwest_list"] = southwest_list

        # if at d1, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        # print("possible moves list:", possible_moves_list)
        return possible_moves_list

class RedChariot(Piece):

    """
    Represents a red chariot piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a chariot piece with a red color, chariot type, number and coordinates.
        """

        super().__init__("red", "Chariot", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # create moves lists and move dictionary

        possible_moves_list = [current_coordinate]
        move_dictionary = {}
        up_list = []
        left_list = []
        right_list = []
        down_list = []

        # define boundaries

        top_boundary = 1
        bottom_boundary = 10
        left_boundary = ord("a")
        right_boundary = ord("i")

        # calculate number of spaces from boundaries

        up_spaces = int(current_coordinate[1:]) - top_boundary
        down_spaces = abs(int(current_coordinate[1:]) - bottom_boundary)
        right_spaces = abs(ord(current_coordinate[0]) - right_boundary)
        left_spaces = ord(current_coordinate[0]) - left_boundary
        # print("up_spaces:", up_spaces, "down_spaces:", down_spaces, "right_spaces:", right_spaces, "left_spaces:",
        #       left_spaces)

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            # print("up_coordinates:", up_coordinates)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            # print("left_coordinates:", left_coordinates)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            # print("right_coordinates:", right_coordinates)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            # print("down_coordinates:", down_coordinates)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2, can move northeast, northwest, southeast, or southwest

        elif current_coordinate == "e2" or current_coordinate == "e9":

            # get all coordinates

            northeast_coordinates = self.move_north_east_coordinates(1)
            northwest_coordinates = self.move_north_west_coordinates(1)
            southeast_coordinates = self.move_south_east_coordinates(1)
            southwest_coordinates = self.move_south_west_coordinates(1)

            # add all coordinates

            northeast_list = [northeast_coordinates]
            move_dictionary["northeast_list"] = northeast_list
            northwest_list = [northwest_coordinates]
            move_dictionary["northwest_list"] = northwest_list
            southeast_list = [southeast_coordinates]
            move_dictionary["southeast_list"] = southeast_list
            southwest_list = [southwest_coordinates]
            move_dictionary["southwest_list"] = southwest_list

        # if at d1, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class BlueCannon(Piece):

    """
    Represents a blue cannon piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a cannon piece with a blue color, cannon type, number and coordinates.
        """

        super().__init__("blue", "Cannon", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # create moves lists and move dictionary

        possible_moves_list = [current_coordinate]
        move_dictionary = {}
        up_list = []
        left_list = []
        right_list = []
        down_list = []

        # define boundaries

        top_boundary = 1
        bottom_boundary = 10
        left_boundary = ord("a")
        right_boundary = ord("i")

        # calculate number of spaces from boundaries

        up_spaces = int(current_coordinate[1:]) - top_boundary
        down_spaces = abs(int(current_coordinate[1:]) - bottom_boundary)
        right_spaces = abs(ord(current_coordinate[0]) - right_boundary)
        left_spaces = ord(current_coordinate[0]) - left_boundary
        # print("up_spaces:", up_spaces, "down_spaces:", down_spaces, "right_spaces:", right_spaces, "left_spaces:",
        #       left_spaces)

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            # print("up_coordinates:", up_coordinates)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            # print("left_coordinates:", left_coordinates)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            # print("right_coordinates:", right_coordinates)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            # print("down_coordinates:", down_coordinates)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2, can move northeast, northwest, southeast, or southwest

        elif current_coordinate == "e2" or current_coordinate == "e9":

            # get all coordinates

            northeast_coordinates = self.move_north_east_coordinates(1)
            northwest_coordinates = self.move_north_west_coordinates(1)
            southeast_coordinates = self.move_south_east_coordinates(1)
            southwest_coordinates = self.move_south_west_coordinates(1)

            # add all coordinates

            northeast_list = [northeast_coordinates]
            move_dictionary["northeast_list"] = northeast_list
            northwest_list = [northwest_coordinates]
            move_dictionary["northwest_list"] = northwest_list
            southeast_list = [southeast_coordinates]
            move_dictionary["southeast_list"] = southeast_list
            southwest_list = [southwest_coordinates]
            move_dictionary["southwest_list"] = southwest_list

        # if at d1, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class RedCannon(Piece):

    """
    Represents a red cannon piece. Responsibilities and communications are exactly like that of the Piece superclass.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a cannon piece with a red color, cannon type, number and coordinates.
        """

        super().__init__("red", "Cannon", number, coordinates)
        self._move_up_list = []
        self._move_down_list = []
        self._move_right_list = []
        self._move_left_list = []

    def get_move_up_list(self):

        """
        Returns the move up list.
        """

        return self._move_up_list

    def get_move_down_list(self):

        """
        Returns the move up list.
        """

        return self._move_down_list

    def get_move_right_list(self):

        """
        Returns the move up list.
        """

        return self._move_right_list

    def get_move_left_list(self):

        """
        Returns the move up list.
        """

        return self._move_left_list

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()
        # print("current coordinate:", current_coordinate)

        # create moves lists and move dictionary

        possible_moves_list = [current_coordinate]
        move_dictionary = {}
        up_list = []
        left_list = []
        right_list = []
        down_list = []

        # define boundaries

        top_boundary = 1
        bottom_boundary = 10
        left_boundary = ord("a")
        right_boundary = ord("i")

        # calculate number of spaces from boundaries

        up_spaces = int(current_coordinate[1:]) - top_boundary
        down_spaces = abs(int(current_coordinate[1:]) - bottom_boundary)
        right_spaces = abs(ord(current_coordinate[0]) - right_boundary)
        left_spaces = ord(current_coordinate[0]) - left_boundary
        # print("up_spaces:", up_spaces, "down_spaces:", down_spaces, "right_spaces:", right_spaces, "left_spaces:",
        #       left_spaces)

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            # print("up_coordinates:", up_coordinates)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            # print("left_coordinates:", left_coordinates)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            # print("right_coordinates:", right_coordinates)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            # print("down_coordinates:", down_coordinates)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2, can move northeast, northwest, southeast, or southwest

        elif current_coordinate == "e2" or current_coordinate == "e9":

            # get all coordinates

            northeast_coordinates = self.move_north_east_coordinates(1)
            northwest_coordinates = self.move_north_west_coordinates(1)
            southeast_coordinates = self.move_south_east_coordinates(1)
            southwest_coordinates = self.move_south_west_coordinates(1)

            # add all coordinates

            northeast_list = [northeast_coordinates]
            move_dictionary["northeast_list"] = northeast_list
            northwest_list = [northwest_coordinates]
            move_dictionary["northwest_list"] = northwest_list
            southeast_list = [southeast_coordinates]
            move_dictionary["southeast_list"] = southeast_list
            southwest_list = [southwest_coordinates]
            move_dictionary["southwest_list"] = southwest_list

        # if at d1, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        # print("possible moves list:", possible_moves_list)
        return possible_moves_list


class Player:

    """
    Represents a player in the game. Player class responsibilities include naming each player and keeping track of the
    current player. Has getters for the player name and is_current_player boolean. Communicates with the Board class to
    place the pieces at the desired coordinates, and with the JanggiGame class to determine who the current player is
    and alternate turns.
    """

    def __init__(self, name):

        """
        Players have private properties for their name and is_current_player boolean.
        """

        self._name = name
        # self._first_move_has_been_made = False
        # self._is_current_player = is_current_player

    def get_name(self):

        """
        Returns the player's name, which is also it's color.
        """

        return self._name


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

        # # create testing moves boolean
        #
        # self._testing_moves = False

        # create and place game pieces, then add to alive pieces list

        self._blue_general = BlueGeneral(1, "e9")
        # print(self._blue_general.get_previous_coordinate())
        self.place_piece(self._blue_general, "e9")
        # print(self._blue_general.get_previous_coordinate())
        # self.place_piece(self._blue_general, "c3")
        # print(self._blue_general.get_previous_coordinate())
        # self.place_piece(self._blue_general, "d5")
        # print(self._blue_general.get_previous_coordinate())
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

        # self.display_board()

        self._blue_player = Player("blue")
        self._red_player = Player("red")
        self._current_player = self._blue_player

        self.place_piece(self._red_horse1, "a2")
        self.place_piece(self._red_soldier3, "a3")
        self.place_piece(self._red_general, "e1")
        self.place_piece(self._blue_soldier3, "d3")
        self.place_piece(self._blue_soldier4, "f3")
        self.place_piece(self._red_cannon1, "b2")
        self.place_piece(self._blue_chariot1, "f6")
        self.place_piece(self._red_guard1, "b3")
        self.place_piece(self._red_guard2, "i3")
        self.place_piece(self._red_cannon1, "d1")
        self.place_piece(self._red_cannon2, "f1")
        self.place_piece(self._red_elephant1, "b2")

        self.display_board()

        self.make_move("f6", "f5")
        self._current_player = self._blue_player
        self.make_move("f5", "e5")

        # self.place_piece(self._red_guard1, "b2")
        # self.place_piece(self._red_elephant1, "d1")
        # self.place_piece(self._red_guard1, "b1")
        # self.place_piece(self._blue_soldier3, "e8")
        # self.place_piece(self._red_general, "e1")
        # self.place_piece(self._red_soldier3, "a3")
        # self.place_piece(self._red_soldier2, "b2")
        # self.place_piece(self._blue_soldier2, "d3")
        # self.place_piece(self._blue_soldier4, "f3")
        # self.place_piece(self._blue_elephant1, "h5")

        # self._alive_pieces_list.remove(self._red_chariot1)
        # self._alive_pieces_list.remove(self._red_chariot2)
        # self._alive_pieces_list.remove(self._blue_chariot1)
        # self._alive_pieces_list.remove(self._blue_chariot2)
        # self._alive_pieces_list.remove(self._red_cannon1)
        # self._alive_pieces_list.remove(self._red_cannon2)
        # self._alive_pieces_list.remove(self._blue_cannon1)
        # self._alive_pieces_list.remove(self._blue_cannon2)
        #
        # self.display_board()
        #
        # self.make_move("h5", "e7")
        # self._current_player = self._blue_player
        # self.make_move("e7", "c4")
        # self._current_player = self._blue_player

        # self.display_board()
        # print("redCan1 at:", self._red_cannon1.get_coordinates())
        # print("alive pieces list:", self._alive_pieces_list)


        # self.make_move("f5", "f4")
        # self._current_player = self._blue_player
        # self.make_move("f4", "e4")

        # print(self._blue_chariot1.get_possible_moves())

        # self.place_piece(self._red_guard1, "a3")
        # self.place_piece(self._red_guard2, "i3")
        # self.place_piece(self._red_general, "e3")
        # self.place_piece(self._blue_soldier3, "e6")
        # self._game_state = "RED_WON"
        # self.place_piece(self._red_soldier3, "e6")

        # possible_moves = self._blue_soldier3.get_possible_moves()
        # print(self.get_valid_moves(self._blue_soldier3, possible_moves))

        # self.make_move("e6", "e5")
        # self._current_player = self._blue_player
        # self.make_move("e5", "e4")
        # opponent = self.get_opponent_of_current_player()
        # print(self.move_results_in_check("e5", "e4", opponent.get_name()))
        # print(self.move_results_in_check("e5", "e4", self._current_player.get_name()))
        # print(self.move_results_in_check("e7", "f7", self._current_player.get_name()))
        # print(self.move_results_in_check("e7", "e6", self._current_player.get_name()))
        # print(self._current_player)
        # self.make_move("e7", "e7")
        # print(self._current_player)
        # self.make_move("e7", "f7")
        # self.make_move("f7", "f6")
        # self.make_move("e7", "e6")
        # self.make_move("e6", "e5")

        # self.place_piece(self._red_soldier3, "c3")
        # self.place_piece(self._blue_soldier3, "e4")
        # self.place_piece(self._red_general, "e1")
        # self.make_move("e1", "e2")
        # self._current_player = self._red_player
        # self.place_piece(self._blue_soldier3, "e5")
        # self.make_move("e2", "e3")

    def get_game_state(self):

        """
        Returns the current game state.
        """

        return self._game_state

    def get_opponent_of_current_player(self):

        """
        Returns the opponent of the current player.
        """

        if self._current_player.get_name() == "red":
            opponent = self._blue_player
        elif self._current_player.get_name() == "blue":
            opponent = self._red_player

        return opponent

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

        # save current coordinate as previous coordinate

        # print("piece's previous coordinate currently:", piece.get_previous_coordinate())
        # piece.set_previous_coordinate(current_coordinate)
        # print("after setting previous coordinate to current coordinate:", current_coordinate, "previous coordinate "
        #       "now:", piece.get_previous_coordinate())

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

    def coordinate_is_on_board(self, coordinate):
        """
        Returns True if the coordinate in the parameter is on the board, otherwise returns False.
        """

        for key in self._coordinate_conversion_dict:
            if key == coordinate:
                return True

        return False

    def get_piece_from_coordinate(self, coordinate):

        """
        Returns the board piece at the coordinate in the parameter.
        """

        for piece in self._alive_pieces_list:
            if piece.get_coordinates() == coordinate:
                return piece

    def horse_is_blocked(self, piece, target_coordinate):

        """
        Returns true if the horse's orthogonal movement is blocked, and False otherwise.
        """

        # get current coordinates

        current_coordinates = piece.get_coordinates()

        # if moving up

        if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 2:
            # print("current y:", current_coordinates[1:], "minus target y:", target_coordinate[1:], "= 2")

            up_coordinate = piece.move_up_coordinates(1)
            # print("up_coordinate:", up_coordinate)

            # if there's a piece at the up coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(up_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move up coordinate:", up_coordinate)
                return True

        # if moving down

        elif int(current_coordinates[1:]) - int(target_coordinate[1:]) == -2:
            # print("current y:", current_coordinates[1:], "minus than target y:", target_coordinate[1:], "= -2")

            down_coordinate = piece.move_down_coordinates(1)
            # print("down_coordinate:", down_coordinate)

            # if there's a piece at the down coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(down_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move down coordinate:",
                #       down_coordinate)
                return True

        # if moving left

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 2:
            # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
            #       ord(target_coordinate[0]), "= 2")

            left_coordinate = piece.move_left_coordinates(1)
            # print("left_coordinate:", left_coordinate)

            # if there's a piece at the left coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(left_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move left coordinate:",
                #       left_coordinate)
                return True

        # if moving right

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -2:

            # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
            #       ord(target_coordinate[0]), "= -2")

            right_coordinate = piece.move_right_coordinates(1)

            # print("right_coordinate:", right_coordinate)

            # if there's a piece at the right coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(right_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move right coordinate:",
                #       right_coordinate)
                return True

        # none of the horse's orthogonal movement is blocked, so return False

        return False

    def elephant_is_blocked(self, piece, target_coordinate):

        """
        Returns true if the elephant's orthogonal movement is blocked, and False otherwise.
        """

        # get current coordinates

        current_coordinates = piece.get_coordinates()

        # if moving up

        if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 3:
            # print("current y:", current_coordinates[1:], "minus target y:", target_coordinate[1:], "= 3")

            up_coordinate = piece.move_up_coordinates(1)
            # print("up_coordinate:", up_coordinate)

            # if there's a piece at the up coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(up_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move up coordinate:", up_coordinate)
                return True

            # if there isn't a piece at the up coordinate

            elif self.get_piece_from_coordinate(up_coordinate) is None:
                # print("There is no blocking piece at the initial up coordinate:", up_coordinate, "now checking first "
                #       "diagonal")

                # check up and northwest coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= 2")

                    up_and_northwest_coordinate = piece.move_north_west_coordinates(1, up_coordinate)

                    # if there's a piece at the up and northwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(up_and_northwest_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary up and northwest coordinate:",
                        #       up_and_northwest_coordinate)
                        return True

                # check up and northeast coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= -2")

                    up_and_northeast_coordinate = piece.move_north_east_coordinates(1, up_coordinate)

                    # if there's a piece at the up and northeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(up_and_northeast_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary up and northeast coordinate:",
                        #       up_and_northeast_coordinate)
                        return True

        # if moving down

        elif int(current_coordinates[1:]) - int(target_coordinate[1:]) == -3:
            # print("current y:", current_coordinates[1:], "minus than target y:", target_coordinate[1:], "= -3")

            down_coordinate = piece.move_down_coordinates(1)
            # print("down_coordinate:", down_coordinate)

            # if there's a piece at the down coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(down_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move down coordinate:",
                #       down_coordinate)
                return True

            # if there isn't a piece at the down coordinate

            elif self.get_piece_from_coordinate(down_coordinate) is None:
                # print("There is no blocking piece at the initial down coordinate:", down_coordinate, "now checking "
                #       "first diagonal")

                # check down and southwest coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= 2")

                    down_and_southwest_coordinate = piece.move_south_west_coordinates(1, down_coordinate)

                    # if there's a piece at the down and southwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(down_and_southwest_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary down and southwest coordinate:",
                        #       down_and_southwest_coordinate)
                        return True

                # check down and southeast coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= -2")

                    down_and_southeast_coordinate = piece.move_south_east_coordinates(1, down_coordinate)

                    # if there's a piece at the down and southeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(down_and_southeast_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary down and southeast coordinate:",
                        #       down_and_southeast_coordinate)
                        return True

        # if moving left

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 3:
            # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
            #       ord(target_coordinate[0]), "= 3")

            left_coordinate = piece.move_left_coordinates(1)
            # print("left_coordinate:", left_coordinate)

            # if there's a piece at the left coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(left_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move left coordinate:",
                #       left_coordinate)
                return True

            # if there isn't a piece at the left coordinate

            elif self.get_piece_from_coordinate(left_coordinate) is None:
                # print("There is no blocking piece at the initial left coordinate:", left_coordinate, "now checking "
                #       "first diagonal")

                # check left and southwest coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == -2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= -2")

                    left_and_southwest_coordinate = piece.move_south_west_coordinates(1, left_coordinate)

                    # if there's a piece at the left and southwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(left_and_southwest_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary left and southwest coordinate:",
                        #       left_and_southwest_coordinate)
                        return True

                # check left and northwest coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= 2")

                    left_and_northwest_coordinate = piece.move_north_west_coordinates(1, left_coordinate)

                    # if there's a piece at the left and northwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(left_and_northwest_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary left and northwest coordinate:",
                        #       left_and_northwest_coordinate)
                        return True

        # if moving right

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -3:

            # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
            #       ord(target_coordinate[0]), "= -3")

            right_coordinate = piece.move_right_coordinates(1)

            # print("right_coordinate:", right_coordinate)

            # if there's a piece at the right coordinate, then the move is blocked and return False

            if self.get_piece_from_coordinate(right_coordinate) is not None:
                # print("There is a piece blocking", piece.get_name(), "initial move right coordinate:",
                #       right_coordinate)
                return True

            # if there isn't a piece at the right coordinate

            elif self.get_piece_from_coordinate(right_coordinate) is None:
                # print("There is no blocking piece at the initial right coordinate:", right_coordinate, "now checking "
                #                                                                                        "first diagonal")

                # check right and southeast coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == -2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= -2")

                    right_and_southeast_coordinate = piece.move_south_east_coordinates(1, right_coordinate)

                    # if there's a piece at the right and southeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(right_and_southeast_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary right and southeast coordinate:"
                        #       , right_and_southeast_coordinate)
                        return True

                # check right and northeast coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 2:
                    # print("current x number value:", ord(current_coordinates[0]), "minus target x number value:",
                    #       ord(target_coordinate[0]), "= 2")

                    right_and_northeast_coordinate = piece.move_north_east_coordinates(1, right_coordinate)

                    # if there's a piece at the right and northeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(right_and_northeast_coordinate) is not None:
                        # print("There is a piece blocking", piece.get_name(), "secondary right and northeast coordinate:"
                        #       , right_and_northeast_coordinate)
                        return True

        # none of the horse's orthogonal movement is blocked, so return False

        return False

    def get_valid_chariot_moves(self, chariot_piece, possible_moves_list):

        """
        Returns a valid moves list for the chariot_piece in the parameter to the to_coordinate in the parameter.
        """

        # get current coordinate

        current_coordinate = chariot_piece.get_coordinates()

        # create valid chariot moves list with current coordinate and empty move_list

        valid_chariot_moves_list = [current_coordinate]

        move_dictionary = possible_moves_list[1]
        # print("move dictionary:", move_dictionary)

        # print("move dictionary:", move_dictionary)
        for key in move_dictionary:

            # print(key)
            valid_moves = self.get_filtered_chariot_possible_moves(chariot_piece, move_dictionary[key])
            # print(move_dictionary[key])
            # print("valid moves:", valid_moves)
            for coordinate in valid_moves:
                valid_chariot_moves_list.append(coordinate)

        return valid_chariot_moves_list

    def get_filtered_chariot_possible_moves(self, chariot_piece, move_list):

        """
        Returns a valid move list for the chariot piece in the parameter from the possible moves in the move list in
        the parameter.
        """

        valid_move_list = []
        # print("move list in chariot moves:", move_list)

        for coordinate in move_list:

            # if there's a piece at the coordinate

            piece_at_coordinate = self.get_piece_from_coordinate(coordinate)
            if piece_at_coordinate is not None:
                # print("There is a piece:", piece_at_coordinate, "at coordinate:", coordinate)

                # if the piece is an enemy piece, then the current coordinate is valid, but the rest of the
                # coordinates are not valid, so return the valid chariot moves list

                if piece_at_coordinate.get_color() != chariot_piece.get_color():
                    valid_move_list.append(coordinate)
                    # print("Piece:", piece_at_coordinate, "is an enemy piece so coordinate:", coordinate, "is valid "
                    #       "but rest of coordinates invalid")
                    return valid_move_list

                # if the piece is an ally piece, then the current coordinate and the rest of the coordinates are not
                # valid, so return the valid chariot moves list

                # print("Piece:", piece_at_coordinate, " is ally piece so coordinate:", coordinate, "and rest of "
                #       "coordinates are not valid so returning valid_moves_list:", valid_move_list)
                return valid_move_list

            # if there's no piece at the coordinate, then it is a valid move

            if piece_at_coordinate is None:
                valid_move_list.append(coordinate)
                # print("There is no piece at coordinate:", coordinate, "so added coordinate to valid chariot moves list:"
                #       , valid_move_list, "and going to next coordinate")

        return valid_move_list

    def get_valid_cannon_moves(self, cannon_piece, possible_moves_list):

        """
        Returns a valid moves list for the cannon_piece in the parameter to the to_coordinate in the parameter.
        """

        # get current coordinate

        current_coordinate = cannon_piece.get_coordinates()

        # create valid chariot moves list with current coordinate and empty move_list

        valid_cannon_moves_list = [current_coordinate]

        move_dictionary = possible_moves_list[1]
        # print("move dictionary:", move_dictionary)

        # print("move dictionary:", move_dictionary)
        for key in move_dictionary:

            # print(key)
            valid_moves = self.get_filtered_cannon_possible_moves(cannon_piece, move_dictionary[key])
            # print(move_dictionary[key])
            # print("valid moves:", valid_moves)
            for coordinate in valid_moves:
                valid_cannon_moves_list.append(coordinate)

        return valid_cannon_moves_list

    def get_filtered_cannon_possible_moves(self, cannon_piece, move_list):

        """
        Returns a valid move list for the cannon piece in the parameter from the moves in the possible moves
        list in the parameter.
        """

        valid_move_list = []
        piece_to_jump = False

        for coordinate in move_list:
            # print("coordinate in possible moves list:", coordinate)

            # if there's a piece at the coordinate

            piece_at_coordinate = self.get_piece_from_coordinate(coordinate)
            if piece_at_coordinate is not None:
                # print("There is a piece:", piece_at_coordinate, "at coordinate:", coordinate)

                # if the piece is a cannon then don't add the current coordinate, but do return the current valid cannon
                # moves list

                if piece_at_coordinate.get_type() == "Cannon":
                    # print("Piece at coordinate:", piece_at_coordinate, "is of cannon type:",
                    #       piece_at_coordinate.get_type(), "so returning current valid cannon moves list:",
                    #       valid_move_list)
                    return valid_move_list

                if piece_to_jump:

                    # if the piece to jump boolean is True and the piece is an enemy piece, add the current coordinate
                    # and return the valid cannon moves list

                    if piece_at_coordinate.get_color() != cannon_piece.get_color():
                        valid_move_list.append(coordinate)
                        # print("Piece:", piece_at_coordinate, "is an enemy piece so coordinate:", coordinate, "is valid "
                        #       "but rest of coordinates invalid")
                        return valid_move_list

                    # if the piece to jump boolean is True and the piece is an ally piece, don't add the current
                    # coordinate, then return the valid cannon moves list

                    else:
                        # print("Piece:", piece_at_coordinate, "is an ally piece so coordinate:", coordinate, "and rest "
                        #       "of coordinates invalid")
                        return valid_move_list

                # if the piece to jump boolean is False, then don't add the current coordinate, update the piece to jump
                # to True, and continue to the next coordinate

                elif piece_to_jump is False:
                    # print("piece to jump is:", piece_to_jump, "so changing piece to jump to True.")
                    piece_to_jump = True

            # if there's no piece at the coordinate and piece to jump is False, then it's not a valid coordinate, so
            # just move on to the next one

            if piece_at_coordinate is None:
                # print("no piece at coordinate")
                if piece_to_jump:
                    # print("no piece at coordinate and piece to jump is true so adding coordinate to valid moves list")
                    valid_move_list.append(coordinate)

        return valid_move_list

    def coordinate_not_blocked(self, piece, target_coordinate):

        """
        If the target coordinate in the parameter is not blocked by an ally of the piece in the parameter, then return
        True, otherwise return False.
        """

        # get piece's color

        color = piece.get_color()
        # print("color:", color, "piece:", piece)

        # get piece at target coordinate

        piece_at_target = self.get_piece_from_coordinate(target_coordinate)
        # print("piece at target:", piece_at_target)

        # if piece is a horse

        if piece.get_type() == "Horse":
            # print("piece type is:", piece.get_type())

            if self.horse_is_blocked(piece, target_coordinate):
                return False

        if piece.get_type() == "Elephant":
            # print("piece type is:", piece.get_type())

            if self.elephant_is_blocked(piece, target_coordinate):
                return False

        if piece_at_target is not None:
            # print("there is a piece:", piece_at_target, "at target coordinate")

            # if the piece at the target coordinate's color equals the current pieces color
            if piece_at_target.get_color() == color:
                # print("the piece at the target coordinate has the same color as the current piece, move blocked by "
                #       "ally")

                # return False that the target coordinate not blocked by an ally
                return False

        # If there is no piece at the target coordinate, or if the piece is an enemy piece, then return True
        # print("There is no piece at the target coordinate, or the piece belongs to the enemy")
        return True

    def get_valid_moves(self, piece, possible_moves_list):
    # def get_valid_moves(self, piece, possible_moves_list, to_coordinate=None):

        """
        Returns a list of valid moves from the possible moves list in the parameter. Checks first to see if the
        coordinate inside the possibles moves list are on the board, then checks whether there is an ally at the
        coordinate, then checks if the move would leave the current player's general in check.
        """

        # valid move list always starts with the current coordinate

        valid_moves_list = [piece.get_coordinates()]

        # validate moves for chariots differently

        if piece.get_type() == "Chariot":
            # return self.get_valid_chariot_moves(piece, possible_moves_list, to_coordinate)
            return self.get_valid_chariot_moves(piece, possible_moves_list)

        if piece.get_type() == "Cannon":
            # return self.get_valid_cannon_moves(piece, possible_moves_list, to_coordinate)
            return self.get_valid_cannon_moves(piece, possible_moves_list)

        for coordinate in possible_moves_list:
            if self.coordinate_is_on_board(coordinate):
                if self.coordinate_not_blocked(piece, coordinate):
                    # if not self.move_results_in_check(piece.get_coordinates(), coordinate, piece.get_color()):
                    #     valid_moves_list.append(coordinate)
                    valid_moves_list.append(coordinate)

        # print("valid moves list:", valid_moves_list)
        return valid_moves_list

    def target_coordinate_in_valid_moves_list(self, valid_moves_list, target_coordinate):

        """
        Returns True if the target coordinate in the parameter is inside the valid moves list in the parameter,
        otherwise returns False.
        """

        # return False if the valid moves list is empty

        if not valid_moves_list:
            # print("valid moves list:", valid_moves_list, "is empty and returning False that target coordinate is not "
            #                                              "inside valid moves list")
            return False

        for coordinate in valid_moves_list:
            if coordinate == target_coordinate:
                # print("Target coordinate:", target_coordinate, "in valid moves list:", valid_moves_list)
                return True

        # print("Target coordinate:", target_coordinate, "not in valid moves list:", valid_moves_list, "so returning "
        #       "False that move is invalid")
        return False

    def switch_players(self):

        """
        Switch the current player for the other player.
        """

        # print("current player:", self._current_player.get_name())
        if self._current_player == self._blue_player:
            self._current_player = self._red_player
        elif self._current_player == self._red_player:
            self._current_player = self._blue_player
        # print("after switch, current player:", self._current_player.get_name())

    def is_in_check(self, player_name):

        """
        Checks all the possible moves of the opponent of the player with the player_name in the parameter to see if any
        of them puts the player into a "check" status. Returns True if the player is in check, or False otherwise.
        """

        print("CHECKING FOR CHECK")

        # get player_name's opponent and general's coordinates

        if player_name == "red":
            opponent = self._blue_player
            to_coordinate = self._red_general.get_coordinates()
        elif player_name == "blue":
            opponent = self._red_player
            to_coordinate = self._blue_general.get_coordinates()

        # check every possible move of every alive piece that opponent has

        # get all alive pieces of opponent

        for piece in self._alive_pieces_list:

            # if it's an opponent's piece

            if piece.get_color() == opponent.get_name():

                # get piece's valid moves

                possible_moves = piece.get_possible_moves()
                valid_moves = self.get_valid_moves(piece, possible_moves)
                # valid_moves = self.get_valid_moves(piece, possible_moves, to_coordinate)

                # if the general's coordinates are in the valid moves list, then the general is in check

                if self.target_coordinate_in_valid_moves_list(valid_moves, to_coordinate):
                    # print("PIECE:", piece, "AT COORDINATE:", piece.get_coordinates(), "CAN CHECK THE GENERAL OF:",
                    #       player_name, "AT THE GENERAL'S COORDINATES:", to_coordinate)
                    return True

        # print("NONE OF THE PIECES OF:", opponent.get_name(), "CAN CHECK THE GENERAL OF:", player_name,
        #       "AT THE GENERAL'S COORDINATES:", to_coordinate)
        return False


    # def move_is_possible(self, from_coordinate, to_coordinate):
    #
    #     """
    #     Checks to see if a move from the from_coordinate to the to_coordinate is possible. If the piece is owned by the
    #     current player, if the move is legal, and if the game is not over, then the move is possible and returns True,
    #     otherwise returns False.
    #     """
    #
    #     # get from_piece from the from coordinate and to_piece from the to_coordinate
    #
    #     from_piece = self.get_piece_from_coordinate(from_coordinate)
    #     # to_piece = self.get_piece_from_coordinate(to_coordinate)
    #     # print("from piece:", from_piece, "and to piece:", to_piece)
    #
    #     # # check if a piece at from coordinate
    #     #
    #     # if from_piece is not None:
    #     #
    #     #     # check to see if from piece is owned by current player
    #     #
    #     #     if from_piece.get_color() == self._current_player.get_name():
    #     #         print("piece's color:", from_piece.get_color(), "matches the current player's color:",
    #     #               self._current_player.get_name())
    #
    #     possible_moves = from_piece.get_possible_moves()
    #     valid_moves = self.get_valid_moves(from_piece, possible_moves, to_coordinate)
    #
    #     if self.target_coordinate_in_valid_moves_list(valid_moves, to_coordinate):
    #
    #         # print(from_piece, "CAN CHECK GENERAL:", self.get_piece_from_coordinate(to_coordinate), "AT TO_COORDINATE:"
    #         #       , to_coordinate, "SO RETURNING TRUE THAT MOVE IS POSSIBLE")
    #         # print("move is possible and returning True")
    #         return True
    #
    #     # print(from_piece, "can't check general:", self.get_piece_from_coordinate(to_coordinate), "at to_coordinate:",
    #     #       to_coordinate, "so returning False that move is not possible")
    #     return False

    def player_is_checkmated(self, player_name):

        """
        Returns True if the general owned by the player with the player_name in the parameter is checkmated, otherwise
        returns False.
        """

        print("CHECKING FOR CHECKMATE")

        # get the player's general

        for piece in self._alive_pieces_list:
            if piece.get_type() == "General":
                if piece.get_color() == player_name:
                    general = piece

        # get the general's valid moves

        possible_moves = general.get_possible_moves()
        general_valid_moves = self.get_valid_moves(general, possible_moves)

        # for each coordinate in valid moves, set the general's coordinates equal to it and see if they all lead to
        # checks, and if so, then the player is checkmated

        current_coordinate = general.get_coordinates()

        for coordinate in general_valid_moves:

            if not self.move_results_in_check(current_coordinate, coordinate, player_name):

            # general.set_coordinates(coordinate)
            # if not self.is_in_check(player_name):
                print("GENERAL:", general.get_name(), "IS NOT IN CHECK AT THIS COORDINATE:", coordinate, "SO RETURNING"
                      " FALSE AND THE GENERAL IS NOT CHECKMATED")
                # general.set_coordinates(current_coordinate)
                # self._alive_pieces_list.append(piece_at_coordinate)
                return False

        for piece in self._alive_pieces_list:

            # get all ally pieces

            if piece.get_color() == player_name:

                piece_possible_moves = piece.get_possible_moves()
                piece_valid_moves = self.get_valid_moves(piece, piece_possible_moves)

                for coordinate in piece_valid_moves:

                    # check each piece's valid coordinates to see if every move results in check, if one move doesn't,
                    # then there is no checkmate

                    if not self.move_results_in_check(piece.get_coordinates(), coordinate, player_name):
                        print("PIECE:", piece.get_name(), "AT THIS COORDINATE:", piece.get_coordinates(), "moving to:",
                              coordinate, "LEAVES THE GENERAL NOT IN CHECK, SO THERE IS NO CHECKMATE")
                        return False


        # general.set_coordinates(current_coordinate)
        # self._alive_pieces_list.append(piece_at_coordinate)
        print("GENERAL:", general.get_name(), "IS IN CHECK AT EVERY COORDINATE IN VALID MOVES LIST:",
              general_valid_moves, "AND EVERY ALLY PIECE'S MOVE LEADS TO A CHECK, SO THE GENERAL IS CHECKMATED")
        return True

    # def simulate_move(self, from_coordinate, to_coordinate):
    #
    #     """
    #     Simulates the movement of the piece at the from coordinate in the parameter to the to coordinate in the
    #     parameter.
    #     """
    #
    #     pass

    # def move_results_in_check(self, from_coordinate, to_coordinate, player_name, recursion_counter):
    def move_results_in_check(self, from_coordinate, to_coordinate, player_name):
    # def move_results_in_check(self, from_coordinate, to_coordinate):

        """
        Returns True if a move from the from coordinate in the parameter to the to coordinate in the parameter results
        in the player with the player name in the parameter having their general in check, otherwise returns False.
        """

        # # base case for recursive function
        #
        # if recursion_counter == 0:
        #     print("recursion counter:", recursion_counter, "at 0 and leaving move results in check function")
        #     return
        #
        # # start by decrementing the recursion counter
        #
        # recursion_counter -= 1

        # get the pieces at the to and from coordinates

        to_piece = self.get_piece_from_coordinate(to_coordinate)
        from_piece = self.get_piece_from_coordinate(from_coordinate)

        # get other player's name

        if player_name == "red":
            other_player_name = self._blue_player.get_name()
        elif player_name == "blue":
            other_player_name = self._red_player.get_name()

        # if there is a piece at the to coordinate, then capture it, then place the from piece at the to coordinate

        if to_piece is not None:

            # if to piece isn't from piece, so it's not a pass turn

            if to_piece.get_name() != from_piece.get_name():

                print("There is a piece:", to_piece.get_name(), "at the to coordinate:", to_coordinate, "and they "
                      "aren't the same piece as other piece:", from_piece.get_name(), "so capturing it.")

                self.capture_piece(to_coordinate)
        self.place_piece(from_piece, to_coordinate)

        # # get the player's name
        #
        # player_name = from_piece.get_color()

        # call is in check to see if the player's general is in check; if in check, return True, otherwise return False

        if self.is_in_check(player_name):
            print("Move from:", from_coordinate, "with from piece:", from_piece, "to:", to_coordinate, "with to piece:",
                  to_piece, "leaves", player_name, "general in check")

            # # if move results in player's general being in check, then make sure move doesn't leave mover's general in
            # # check
            #
            # if not self.is_in_check(other_player_name):
            #     print("Move from:", from_coordinate, "with from piece:", from_piece, "to:", to_coordinate,
            #           "with to piece:", to_piece, "leaves", player_name, "general in check but does not leave the",
            #           other_player_name, "general in check.")

                # # undo the move and capture before leaving function
                #
                # self.place_piece(from_piece, from_coordinate)
                # if to_piece is not None:
                #     if to_piece.get_name() != from_piece.get_name():
                #         print("Reversing simulated move by putting back the from piece:", from_piece, "and adding the to "
                #                                                                                       "piece:", to_piece,
                #               "back to the alive pieces list:", self._alive_pieces_list)
                #
                #         self._alive_pieces_list.append(to_piece)
                #         self.place_piece(to_piece, to_coordinate)
                #         self.display_board()
                #
                # return True

            # undo the move and capture before leaving function

            self.place_piece(from_piece, from_coordinate)
            if to_piece is not None:
                if to_piece.get_name() != from_piece.get_name():

                    print("Reversing simulated move by putting back the from piece:", from_piece, "and adding the to "
                          "piece:", to_piece, "back to the alive pieces list:", self._alive_pieces_list)

                    self._alive_pieces_list.append(to_piece)
                    self.place_piece(to_piece, to_coordinate)
                    self.display_board()

            return True

        # print("Move from:", from_coordinate, "to:", to_coordinate, "does not leave", player_name, "player in check")

        # undo the move and capture before leaving function

        self.place_piece(from_piece, from_coordinate)
        if to_piece is not None:
            if to_piece.get_name() != from_piece.get_name():

                print("Reversing simulated move by putting back the from piece:", from_piece, "and adding the to piece:"
                      , to_piece, "back to the alive pieces list:", self._alive_pieces_list)

                self._alive_pieces_list.append(to_piece)
                self.place_piece(to_piece, to_coordinate)

        return False

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
        print("Attempting move from:", from_coordinate, "to:", to_coordinate, "with from piece:", from_piece, "and to "
              "piece:", to_piece)

        # check if there isn't a piece at the from coordinate

        if from_piece is None:
        # if from_piece is not None:

            print("There is no piece:", from_piece, "at the from coordinate:", from_coordinate, "so move failed")
            return False

            # print("There is a piece:", from_piece, "at the from coordinate:", from_coordinate)

        # check to see if the from piece is not owned by current player

        if from_piece.get_color() != self._current_player.get_name():
            print("piece's color:", from_piece.get_color(), "doesn't match the current player's color:",
                  self._current_player.get_name(), "so move failed")
            return False

        possible_moves = from_piece.get_possible_moves()
        # print("possible moves:", possible_moves)
        valid_moves = self.get_valid_moves(from_piece, possible_moves)
        # valid_moves = self.get_valid_moves(from_piece, possible_moves, to_coordinate)
        # print("valid moves:", valid_moves)

        # check if target coordinate not in valid moves list

        if not self.target_coordinate_in_valid_moves_list(valid_moves, to_coordinate):
            print("to coordinate:", to_coordinate, "is not a coordinate inside the valid moves list:", valid_moves,
                  "so move failed")
            return False

        # check if the move leaves the current player's general in check

        if self.move_results_in_check(from_coordinate, to_coordinate, self._current_player.get_name()):
        # if self.move_results_in_check(from_coordinate, to_coordinate):
            print("move from:", from_coordinate, "to:", to_coordinate, "leaves the current player's general in check,"
                                                                       " so move failed")
            return False

        # check if the game is over

        if self.get_game_state() != "UNFINISHED":
            print("Game is already over, game state:", self.get_game_state(), "so move failed")
            return False

        # if from coordinate and to coordinate are the same, then the player is passing their turn, so
        # return True but don't do anything else besides switching the players

        if to_coordinate == from_coordinate:

            print("To coordinate:", to_coordinate, "and from coordinate:", from_coordinate, "are the "
                  "same, so current player passed their turn, switching players and returning a "
                  "successful move")
            self.switch_players()
            return True

        # check if there is an opponent's piece at the to_coordinate

        if to_piece is not None:
            # print("to_piece:", to_piece, "is enemy at to coordinate so capturing")

            self.capture_piece(to_coordinate)

        # move piece

        self.place_piece(from_piece, to_coordinate)
        # print("piece:", from_piece, "placed at new coordinate:", from_piece.get_coordinates())
        self.display_board()

        # if there is checkmate, end the game

        opponent_name = self.get_opponent_of_current_player().get_name()
        if self.player_is_checkmated(opponent_name):
            print("game is over")
            return
            # end game code

        # check for check

        if self.is_in_check(opponent_name):
            print(opponent_name, "player is in check!")

        # switch current player

        self.switch_players()

        print("move successful and returning True")
        return True


game = JanggiGame()





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

# we need to code the guard movements, which are exactly like the general's movements. As we were sleeping last night,
# we went back and forth between how to code the piece's movement. Currently we have the game class check to see if the
# possible moves are inside the board, but once again, why can't the piece do this, since it is already checking its
# possible moves on the board. We can add code in the Piece superclass to check if the coordinates are inside the board
# then and if there is a friendly piece blocking our target, since both of these lead to invalid moves. So, maybe the
# piece can initially calculate the "all moves list," which is all the moves possible by their movement, then it can
# calculate the "possible moves list", which weeds out the coordinates outside the board and ones in which the target
# coordinate is blocked by an ally piece. These sub functions can fall under a bigger "get_valid_moves" function, which
# is also inside the Piece superclass. Then, when we call "make move" we just have to "get the valid moves" and make
# sure the target coordinate is inside the "valid moves list". Alright, so we can put the converted coordinates dict
# inside the Piece class, or we can pass it as a parameter from the game class. Let's just write out a simple code for
# detecting if inside range, which we've already done.

# Alright, so we restructured the code a bit. Only the possible moves are in the pieces class, and the rest of the code
# is in the game logic, because we need access to all the game logic methods, and we don't have those in the derived
# piece classes. Let's test the coordinate is on board, coordinate not blocked by ally, and get valid moves functions
# that we modified to make sure they work. Then we want to change the switch player method to be from the player class,
# bc we do have access to the player objects to call the Player class functions. Wow, our coordinate not blocked by ally
# function was giving an error, and after debugging with print statements, we realized that we had added a return
# statement to the "get piece from coordinate" function, which now returned "piece not found". Before, when we left it
# blank, it returned None, so when our statements was checking if the piece was None, it was no longer None, so it went
# to the next if statement and called get.color on no object. Yikes, that was a weird error. Alright, so we go to test
# the get valid moves function, and it seemed to work. There was an issue of the current coordinate not showing up in
# the valid moves, so now we start all the valid move lists inside the function with the piece's current coordinates.

# Alright, now let's change the switch player function to be in the player class. Lol, trying to do it the other way, in
# the player class, just doesn't make sense. It made sense last night when we were brainstorming things, but now was we
# are doing it, this current way is the best way we can think of yet. Alright, now let's make sure our make move
# function works / if it needs to be updated after our new functions. Ok, I think we've made it work. While testing
# the make move function, we stumbled on the issue of the from coordinate not having a piece, which we did not account
# for. We got the very familiar attribute Error saying that we couldn't call the get color method from the None object,
# which we fixed by first checking if there is a from piece. We definitely want to do more thorough testing of the make
# move function after we're done.

# Ok, back to what we were trying to do before we had to change our code. Let's code the guard movements now. Alright,
# so what can a guard do? Well, apparently guards can go wherever the general goes, so I think we pretty much copy paste
# the code right? Let's check our Piece superclass and general code to make sure nothing needs to be changed from our
# changes. Lol, that was a lot easier than we thought, we just pasted the blue general and red general codes into the
# blue and red guard. Now, how do we want to test this? I think we can test the guards to move up to a blank space,
# diagonally into a general, and sideways into a bluehorse. Ok, we noticed very quickly that our coordinates were off,
# and didnt understand why f10 was being converted into f0 after the y should've been just 1 value less, and we went
# into our code and saw that we were just extracting the 2nd string of the coordinate, but we want the third coordinate
# as well, so why not use [1:] for a slice of the second to the end? Yes, we can use a slice, but we have to slice
# strings, so it's actually good just to use a slice of "current coordinate" (we don't have to call list on it to create
# a list first, actually we don't have to call list before either, we can just call a string at 0 to get the first value
# lol. Let's change that. Alright, we went and changed all our movements to be slices of strings, we forgot we don't
# have to call list on strings because strings can already be accessed as a list lol. Alright, so it looks like the
# guard movements are updated, let's go back and make sure our soldier moves are correct though after the changes.

# Ok, let's code horse and elephants, then chariots and cannons. Alright, what is the movement of the horse? Horses move
# one spot othogonally and 1 diagonally, but if the orthogonal move is blocked the whole move is blocked. Blocked by
# allies and opponents or just opponents? From some of the diagrams online, it seems like both the ally pieces and the
# enemy pieces can blocked your movement, which should be pretty easy to code? So... the movement looks like this... in
# an up move, we can move one spot up (but make sure that spot isn't occupied, or it's blocked), then if it's not
# blocked, we can move it in 2 diagonal directions, northeast and northwest if moving up. Alright, so we want to do the
# up and northwest move, but how do we check if the spot is occupied? The retrieval of the piece on the board is from
# the game class, so how would we check if the target coordinate has a piece? Currently we check with the "get piece
# from coordinate" function, which is in the game class. Why don't we check after the fact? Can we do that? Can we pass
# the possible moves into a function that can check for these blocks? Hmmm our current "coordiante not blocked by ally"
# function only checks if there is an ally there. I mean we can write another function, but then we'd have to use
# different checks depending on if we're checking if the move is blocked by an ally or any piece. Ideally we want to get
# the possible moves from the piece class itself. Wow, our brain is not really functioning right now, not good. We're
# gonna have to slog through this.

# Let's take a look at the horse in the gameboard and maybe see if we can't come up with anything. Ideally we want to
# weed out the blocked moves before possible moves, but how do we check the board without access to the game class? It
# says its prefereable to use a module, or we can make it a static method with "@staticmethod", so I guess we'll do that
# even though it isn't preferred. Lol, we can't access self._active_pieces_list with the static method. I think we're
# gonnna have to rewrite our target coordinate is blocked function to account for multiple blocks. Before we do this, we
# need to see what the other moves do to consider how we want to set the parameters; how many blocks are possible.
# Alright, so horse and elephants have the same blocking restriction, at the initial orthogonal move. Chariots can move
# as many places horizontally or vertically as they want (also diagonally inside palace), but they can't jump over a
# piece, so.. they are blocked by allies, but not by the enemy. If the enemy is on that block, they can take the enemy.
# If the enemy is blocking the target coordinate, then the enemy blocks that move. Cannons move like chariots, but they
# need to jump a piece to move.

# Alright, back to horses. So, since the blocking is handled in the game class method, we won't be dealing with it right
# now, but we do need to determine all the possible moves the horse can make. Right now, our move up coordinate function
# returns a coordiante, then our move diagonal function returns a coordinate, and both don't take parameters, which is
# not good for coding the horse's movement. What we want is to get the move up coordinate, then use that coordinate as
# a parameter in the move diagonal coordinate function, so we have a final horse coordinate that is one orthogonal and
# one diagonal movement from its current coordinate. I think in order to do this, we need to have the move coordinates
# optionally take a parameter, at least the diagonal movements need an optional parameter. We can do something like
# setting a current coordinate to None, and then putting in if statement that if the current coordinate is None, then
# the current coordinate is piece.get_current_coordinate(), so that we can set the current coordinate equal to the move
# up coordinate. After we get the horse coordinates like this, we'll have to put extra parameters and if statements in
# the "coordinate is blocked" function to check for the 2 points where the horse can be blocked (at the orthogonal move
# and at its final spot) and to put in if statements to check what piece we are dealing with, and to hardcode the blocks
# for the piece, those pieces being horse, elephant, chariot, and cannons.

# Alright, let's first update the up and diagonal movements in the piece super class. Alright, now let's try to get the
# blue horse's "up_and_northwest coordinate". Ok, so the blue horse possible moves list looks fine, then we updated the
# red and see that it's possible mvoes include b-1, which is "b" "negative" "1", which is actually correct accoring to
# our movements. This isn't necessarily a problem, as this is not a valid coordinate and should be weeded out when we
# run get valid moves. Now let's update the coordinate is blocked function to account for the 2 spots where the horse
# can be blocked. How do we determine the secondary coordinate, considering there are 4 possible secondary coordinates
# that the horse can be blocked at? Well, in pseudocode, we want to check if the horse is moving up, and if so, then
# check the up coordinate, if down, down coordinate, etc. and set this coordinate as the secondary coordiante to check
# for blocks. Can we subtract the target coordinate from the current coordinate to determine which way the movement is?
# For example, if the horse tries to move up, then the y coordinate of the current coordinate is greater than the y
# coordinate of the target coordinate, if moving down, then the y coordinate of the current coordinate is less than the
# y coordinate of the target coordinate. Let's code these for now. Alright, now let's test these before we move on to
# the right and left coordinates. Ok, if we're testing the current red and blue horse up and down movements, there will
# be no blocking of the up and down movements, bc neither have their up or down movement blocked. We test this later by
# moving a unit into a up or down spot, or for now, make sure the valid moves are correct. Lol, we see that a2 is not
# a valid coordinate, so we're trying to figure it out, but... we haven't coded the left and right checks yet, which is
# where a2 is from, THAT'S why it's showing up lol. Alright, let's move something below the red horse so we can block it
# and actually test the code. Yeah, ok, this code IS working. Actually, the valid moves list is missing "a2" now, which
# is weird, why is that? We just blocked the down coordinate... oh.. it thinks a2 is a down movement, since the current
# coordinate is less than the target coordinate... We have to be even more specific. Alright, let's note all the
# differences. Actually, it's not greater than or less than, it's if the difference is 2... that's a move up or move
# down. Ok, so what about left and right movements? The x coordinate increases by 2 letters on a right movement, and
# decrease by 2 letters on a left movement, but I'm not sure we can do this with letters; it was a lot to add and
# subtract numbers. Actually, we can compare letters with the "chr" function, which seems to give the letter in its
# ASCII numerical form. Actually, that's "ord". "Chr" gives us the letter form.

# Alright, I think we've managed to code the blue and red horse movements, and update the coordinate is blocked function
# to check for blocks on the horses, now we need to do the elephants, chariots, and cannons. I think the elephant is
# almost exactly like the horse, but just 1 more diagonal movement. Consider changing the horse checks (and the further
# piece checks) into their functions and we can just call boolean functions on them, such as a "horse not blocked"
# function. Ok, I think we converted the horse not blocked function successfully, let's test a couple of things before
# moving on. I think that is good. We just copy pasted the code and changed around some True False values to match the
# boolean values. Let's do the elephant code now, using the horse code as a template. Ok, before we do the elephant is
# blocked function, we need to code the elephant's movement first.

# Let's code the elephant's movement, which is very similar to the horse, then update the elephant is blocked function.
# Alright, so the elepahnt moves one spot orthogonally and 2 spots diagonally, so it actually has an additional spot
# to check for blockage, during the first diagonal movement. Let's copy in our horse code and go from there. Alright, I
# think we got the elephant movement in there, but this is gonna be tricky, the elephant is blocked function. Because we
# have to deduce a move before the target coordinate to check for blockage, since elephants have 3 spots for blocking.
# Actually, we have about half of the elephant is blocked code done, because the orthogonal movement is the same as the
# horses. However, we need to branch out from the horse and get the orthogonal movement as well. Do we check every
# diagonal to see if there is a blockage. No, we have to determine which way the elephant is going. So, we've split it
# into up, down, left, and right, but within the up movement, we need to figure out if its going northeast or northwest,
# because we don't want to check a diagonal spot where the elephant isn't moving to, that would give us the wrong
# results. Wait a minute, how we do know that the elephant is even moving up? For the horse, it was a difference of 2
# y values, but for the elephant, don't we need to change that value to 3? Yes, first we need to change all the values
# to 3 instead of 2. Alright, that was an easy change because our code is modular. Now, how do we know if it's going
# northwest or northwest when going up, from the current coordinates and target coordinates? Well, we have to check
# the x coordinate of the current and target coordinates. Moving northwest means that the target coordinate's x value
# is 2 less than the current coordinate, so if we subtract the target coordinate from the current coordinate, that's a
# value of positive 2. Similarly, if we are going northeast, then the target coordinate's x value is 2 more than the
# current coordinate, so if we subtract the target coordinate from the current coordinate, we'd get a negative 2. So,
# let's put that into code.

# Alright, so we've code a check for the up movements and the up and northwest and up and northeast movements, now let's
# test this. How do want to do that? Lol, we haven't put the elephant is blocked code into the coordinate is blocked
# code function... lol. The tests for up were pretty complicated, but I think everything worked. Let's translate it to
# down, then do left and right. Alright, so down works, now we need to do left and right. We should save these for
# tomorrow I think, or try to do them now? I really hate stopping halfway, let's see if we can do this. Alright, the
# left looks right, now let's copy it and do the right one. Alright, that looks good, I think everything tested fine
# and it didn't take that long to add the left and right movements since they a lot of similar elements to the up and
# down movements.

# We need to code the chariot and cannon movements, then is in check function and the checkmate function. Alright so
# chariots can move an unlimited number of spaces vertically or horizontally (but we have to limit it to inside the
# board), but they can't jump pieces, so their limit is where the next piece is. Furthermore, they can move diagonally
# inside the palace (we will add palace movements after the initial movements). How do we change the soldier code to
# make the up, down, left, and right coordinates not just one possible coordinate, but many, up to the end of the board
# preferably. Currently we're adding one up movement, so let's just extend that... Oh, we actually we don't have a move
# up amount parameter, but we definitely should for the cannons, so let's add that first and adjust our current code to
# match the change. Oh lol, we already have a up amounts, down amounts, etc. don't even remember when we added that,
# thought it was only for the diagonal movements, so that's good, we don't have to change that. Now, let' use those and
# put in a max value for the orthongal movements. Ok, so if we imagine the chariot on the edge of the board, the max
# movement in one direction is 9 spaces, do we can do 9 spaces for each direction and weed out these possible moves in
# the get valid moves function, or... we can try to create some function that knows how many spaces the chariot can move
# in each direction. How would we do that? Let's look at the game board and take a hypothetical scenario. Looking at the
# board, yeah, I'm seeing the patter. So, from the piece's current coordinates, if we subtract the left boundary x value
# from the x value of the current coordinate, then we get how many spaces it can move left. For example, for blueCha2
# the x value is i and the left boundary is a, so the ord value of i - a, what is that? Using the python console, that
# is an 8, and that is correct, we can move 8 spaces to the left, so the move left amount is from 1 to 8 here. Similarly
# if we want to do the right movement, than it is current x (i) minus the right boundary x (also i), so that is 0, which
# is correct, we can't move right anymore from this spot. Alright, let's start coding. Actually, our current format is
# to start with move up, so let's brainstorm what the code is doing for a move up. So, if we're moving vertically, then
# we want to subtract the current y from the upper y boundary, so 10-1, which is 9, which is correct, that's how many
# spaces we can move up. Similarly, if we want move down, take the current i and subtract it from the boundary, so 10 -
# 10, which is 0. We've noticed a possible issue here. What if we were at i9, so 9-10, which is -1, which means, we have
# to take the abs value of the subtraction, because we can't go -1 spaces down. Alright, so let's code the up and down
# coordinates.

# Alright, the orthonal movement looks good. Now, let's code the diagonal movement inside the palace. From the looks of
# it, they have additional movements at 5 areas within the palaces 9 areas. Alright, so, unlike the current soldier
# palace code, the chariots can move in either palace, which means they have a total of 10 spots on the board where they
# gain increased palace movements, those being d10, f10, e9, d8, f8, d3, f3, e2, d1, f1. I think we want to hardcode
# each of these movements, but first of all, are the diagonal movements unlimited or just 1 space? From one of the move
# diagrams, it seems they can go two spaces to the outer palace edge if on one edge. Alright, let's update the palace
# values and hardcode the additional movements. Ok, now we need to test the possible moves inside the palace, so let's
# move the blue chariot to areas inside the palace and test the possible moves. We've only done the upper palace, but I
# guess we can test it before adding the lower palace. First off, we need to move the redguards and generals so they
# don't block our path. Alright, the upper palace code looks correct, now let's add the lower palace movement
# augmentation. We thought we needed to add a similar section for the blue palace, but since our code is modular, the
# relative movements are exactly the same, so we just need to add the coordinate to the specific correct diagonal
# movements. Alright, the code is looking good, now let's move the code to the red chariot.

# Ok, red chariot loosk good. Let's move on to the cannons now. Wait a minute, we haven't gotten the valid moves yet. We
# need to implement the chariot blocking code and get valid moves, not just the possible moves. Hmm, currently our
# standard blocking code blocks the move if there is an ally at the target coordinate, but now we need to block all
# the rest of the moves in that direction after a block where there is any piece there. So the get valid moves function
# iterates through all the moves in the possible moves list and returns the ones that are firstly, on the board, and
# secondly, not blocked. So we can go down a direction, but once there is a piece there, we need to cut off the rest
# of the moves in that direction. How do check which direction we are going? If we're moving up, then the y value of the
# target coordinate is decreasing, if we're moving down, it's increasing, if we're moving right, the x value is
# increasing,and if we're moving left, the x value is decreasing. Ok, so let's say we pick a direction, say up, then we
# check all the up coordinates, which requires the ranges that we calculated in the possible moves, and if there is a
# piece blocking, then we stop adding the coordinates in that direction. Alright, let's try to code this out for the up
# direction. Actually, I don't think we have to calculate everything, since we already have the target coordinate we
# want to reach, we can just calculate it for the direction that it is moving in. Hmm... we're getting a little confused
# let's run through what our code does again. So, it takes all the possible moves, then it makes sure that the moves are
# inside the board (we already calculated this part, so all the chariot possible are already inside the board) then it
# sees if the move to a spot is blocked, and if so, that move is invalid. So, let's take an example. We have teh blucha2
# at i10, and its possible up moves are from i1 to i9. Now, there are 3 pieces blocking i10 to i1. The opponent's piece
# on i10 is not a real blocked, that is a valid move because we can capture that unit. However, if there is a piece in
# between the captured piece and attacking piece, then we can not make that move. Alright, so let's take this one step
# at a time. We first check the i9, and its not blocked, so we add it to the valid moves. Then we check i8, and its also
# not blocked and gets added. Then we go to i7, and i7 is definitely blocked, because it is an ally piece (not that if
# it was an opponent piece) it is still allowed. Now, if we move to i6, the current code says that is an ok move,
# because there is no piece there, but we need to tell it that since the previous move is blocked, the rest of the moves
# in this direction aren't valid either, so how do we do that? Alright, so in our current code, we have the boundaries
# calculated, so let's also calculate all the possible directional movements. Then, we'll iterate though each movement
# which starts at the smaller value and goes up. If the piece at the target coordinate is an ally piece, we can return
# the function and say that coordiante is blocked. If the piece at the target coordinate is an enemy piece, that target
# is valid, but we need a boolean that says enemy_captured or something, then anywhere past that where there is another
# enemy piece, then those coordinates are blocked. Alright, let's try this code. I don't like how it calculates the
# movement lists everytime. Can we use the movement lists are a parameter? Where would we calculate the movement
# lists? We can calculate it in the piece itself and put getters for it, or we can calculate it in the coordinate not
# blocked function (which seems worse right?), then, we can use those movement lists as parameters in the chariot is
# blocked function. Ok, first of all, we need to put private properties of these lists into the chariot class. Alright
# so we've added private data members for the movement lists in teh blucha1 class, now let's check it with the getters
# and make sure all the lists are correct. Ok, it looks like those showed up fine. We need to copy these into the red
# chariot, then update the chariot is blocked and coordinate not blocked functions to reflect the new functions with
# new list parameters.

# Wait, so what is the code logic in checking the lists again? We will put in code for all the directions, but only
# perform the code for the direction that is calculated from the current coordinate and target coordinate. For each
# direction, we want to go through each move in the move list, starting with the closest (it has to be this order every
# time) and going to the farthest. If we hit a piece, we need to check if it's an ally piece or enemy piece. If it's an
# ally piece, then we can return the function that the move is blocked, and we don't want to keep going with the adding
# valid moves in that direction (I'm not sure how we relate this to get valid moves function). If the move is an enemy
# piece, it is valid, but we change a boolean called "encountered_enemy" to true, so on the next space where we find
# another piece, then that move and further moves are not valid. Let's look over our chariot is blocked, coordinate not
# blocked, and get valid moves function to see how we want to relate this to those functions. Ok, we need to relate the
# coordinate is blocked function with the target coordinate. Let's use a concrete example, actually, we use the one
# we used before, with blucha2 at i10. If we're moving in the up direction, the first move is i9, and we move towards
# i1. Let's say the target coordinate is i1. So we start with i9, and there's no piece there, so it's not blocked, same
# with i8. Then we get to i7, and there's an ally there, which means i7 is not a valid target. Since there is an ally
# at i7, the rest of the coordinates don't need to be checked, because they are blocked. What if the piece was an enemy
# piece? Then, it's not blocked, and we can keep going. So there are no restrictions on i6 and i5, then we get to i4
# and there is another enemy piece. So, for the first piece, if it's an enemy we need to change the "enemy_encountered"
# bool to True, then when we get to this second piece, it doesn't matter what piece it is, if we already encountered an
# enemy along the way, then the rest of the moves are blocked. So basically, we want to have a while statement to keep
# checking each coordinate in the move list, but we will return out False that it is blocked, whenever we encounter the
# first unit. Actually, it doesn't really matter that much whether it's an ally or enemy, if we hit a piece, we can't
# go past that piece. If it's an ally, then we have to stop one space before the ally. If it's an enemy, we have to stop
# at the enemy's coordinate. How do we relate this to the get valid moves function? I think we can't do the same code
# for the chariots as the other pieces, so we want to check them first, by type, and have special code for them, where
# we check the 4 directions, and not every coordinate in the possible moves list. The issue is, if we don't use the
# possible moves list, then we are losing all the possible moves. Wait, just add the moves in the move list as they
# are valid, into the valid moves list. Ok, but don't we need the target coordinate? No, later we check to see if the
# target coordinate is in the valid move list, that's how we check if we can move to the target coordinate, but the
# valid moves list just takes the possible moves and removes all moves not inside the board and all moves that are
# blocked by the piece's movement characteristics. Wait a minute, we don't need a boolean for enemy encountered bc
# we never go past the first piece encountered. We just check to see if there's a piece on the possible moves coordinate
# and if there is, we check if it's an ally or not. If it's an ally, we don't add the current coordinate and return
# the list, if it's an enemy, we add the current coordinate, then return the list. Alright, let's try to test out this
# code and see if we can get valid moves.

# Lol, so we get coordinates that shouldn't be in the valid moves list, only to find out that, we've only coded the
# move up coordinates, and we needed to code the rest. Let's move our redcha1 to a spot where we can test if the move
# up coordiante works or not. We can do bluecha1. It looks like our function for up is working fine. Now let's add down.
# Before we add, let's change this line of code to its own function, with parameters for the piece and direction list.
# Alright, so we did that, and it feels like the list should be a parameter, since that's the only thing different in
# the 4 directions is the list, the rest of the code stays the same. I think this issue is also related to the issue of
# how to determine the direction of the move. We're gonna need the final target coordinate, not the coordinates in the
# move lists, but the target we are trying to go to in make move. So what does make move call? Ok, so we need to carry
# the to coordinate from make move to the get valid moves function, to the get valid chariot moves function, so let's
# add these parameters.

# Alright, so how do we know what direction the chariot is moving? Well, if it's moving up and down, then the x value
# of the coordinate stays the same, while the y changes. Conversely, if it's moving right and left, then the y value
# of the coordinate stays the same, and the x value changes. So I can we can compare the x and y values of the current
# coordinate and the to coordinate. If x is the same, then we know it's vertical movement, and if y is the same, then
# we know it's horizontal movement. If the y change is positive, then it's a movement up, and if the y change is
# negative, then it's a movement down. If the x change is negative, then it's to the right, and if the x change is
# positive, then it's to the left. Alright, let's code this. Is there a case where both the x and y values are the
# same? Yes, when there is no movement. So what do we want to do then? We want to just return the current coordinate
# for the valid moves list. Let's put this situation on top?

# Wow, we're done with our code, but it says current lines unreachable, very annoying. Wow, it had something to do with
# calling "ord" when we didn't need to apparently. Very weird. Alright, we need to test this code. Jesus, we finally
# were able to test all 4 directions for the chariot movements. Now, let's get it to the end and test the make move
# function? We tested the top left corner for the chariot, and it seemed to work. Whew, this part took so much time.
# We still have to add the palace movements to all the chariot related functions, then do the last piece, the cannons.
# Alright, so currently we have the chariots with their orthogonal movements, but we still need to add all the palace
# movements as well right? Let's see the current valid moves and what moves are valid at a palace spot. Ok, so we
# assumed there were only movements along the x or y axis, so the chariots would have either x or y the same, but
# inside the palace, it can move diagonally, so we need to account the move list for that.

# So, inside the palace, the chariots have their coordinates, which can all be checked by a simple coordinate not
# not blocked function, right? It's actually not simple, because there can be a blocker in the middle of all the
# diagonal movements, but no piece at the target coordinate 2 diagonals away, which means the game will think that
# the move is ok when it's not. We still need special block movement for the chariot, should be code it in a chariot
# is blocked and put inside coordinate is blocked or do it in the get valid chariot moves function? I think it needs
# to go in the get valid chariot moves function. Let's copy the possible palace movements first, or should we do what
# we did with the up and down directions and save the palace movements in there own lists? How complicated is this
# palace code? Alright, we've added the additional palace move lists, now let's test to make sure they are correct.

# Alright, so we added the private properties for those lists, and the getters for them in both chariot classes, so
# now what? We need to check the movements. The only movement that is important, is actually the corner movements, so
# e2 and e9 are not necessary. So, we need to differentiate a "palace movement" from a regular movement, and I think
# the difference is if the both x and y values are not the same, so if they are both not the same, we check for their
# current coordinate, and run the same blocking code as for the othogonal movement, but just using the diagonal move
# lists. Alright, I think we added the additional palace movements. Now, let's test it to make sure it works. So, how
# are we going to test this? We want to put the chariot at a palace spot, then see all the possible and valid moves
# to make sure they are correct, then test some make moves to make sure the outputs are all correct. Lol, we're
# catching a lot of errors now. The final error that we see is that, d3 and d10 actually have different coordinates to
# use, so we actually need to separate each palace current coordinate into its own palace move list, then set that
# move list equal to move list. This means we have to change all the diagonal move lists in the red and blue chariot
# , update the getter functions to get those new lists, then update the get valid chariot moves function to use those
# new lists.

# So the question is, do we really need to use the private data members for these lists or can we just calculate it
# them. We wouldn't have to use the getters either. Let's look at how we got them initially in the get possible moves
# section. Alright, we kinda copied and modified the code a little bit, but using the superclass move function is better
# here than using the data parameter lists. Now, let's make sure both the red and blue chariot have the same code, then
# remove the init data members and gettters since we won't be using them. Actually, have we tried to call make move yet?
# Yeah, let's call make move and make sure everything works first. Good, it seemed to work fine. Let's remove the data
# members and getters and make sure both chariots are correct.

# Alright, on to the last piece, the cannons. What are the cannons moves again? Cannons move a lot like chariots. They
# go vertically and horizontally, and also can move diagonally inside the palace. However, there are some extra
# restrictions for cannons. Cannons need to jump a unit to move (the unit can be friend or foe). This means that inside
# the palace, they can only move diagonally if they are on the 4 edge spots and there is a unit in the middle. Cannons
# have jump restrictions as well. They can't jump over an ally or enemy's cannon, and they can't capture an enemy cannon
# (I think we just check and make sure that the first piece they encounter is not a cannon, otherwise return the valid
# moves so far, and if the target coordinate is an enemy cannon, that we return the valid moves excluding that spot).
# Lastly, they can't make the first move.

# Alright, so it seems like the cannons move almost exactly like the chariots, but with some additional restrictions,
# so let's start by copying the blue chariot's code into the blue cannon. So looking at our chariot/cannon code, we
# see that we really aren't using the possible moves, but the possible moves function does populate our orthogonal
# move lists and give us a possible moves list that we put into the get valid moves function, even though getting
# valid moves... wait, don't we just its own get valid moves function? Are we even using the get valid moves function?
# Yeah, we are calling the get valid moves function, but that function calls get valid chariot moves, which doesn't
# use the possible moves at all, but the get valid moves function does have that parameter, so I guess that's fine.
# We still want to call the get possible moves because it does populate our moves, but we don't actually iterate
# through that move list for the chariots and now cannons. We're also noticing that with the chariots and cannons,
# that we've already took out all the off the board moves from our move list, so the valid moves, which is based on
# the target coordinate, are all we need, so basically, we don't even have to calculate the palace moves in the get
# possible moves function, since they are calculated in the get valid chariot moves function. Let's remove those parts
# and test to make sure nothing is broken. Ok, yeah, that changed nothing, so it was good.

# Alright, let's use the blue chariot template and update for the blue cannon. I think most of the updating is actually
# for the yet to be made get valid cannon moves, since the possible moves for the chariots are the same as the cannon,
# we just need to put in the proper move restrictions. For example, we definitely need a first_move_made boolean that
# checks whether a first move has been made, and if not, the cannon has no valid moves (bc it can't make the first move)
# this boolean probably has to be specific for each player as well. Since neither player can move a cannon as their
# first move we're thinking.

# Ok, let's first review the blue chariot code that we copied and make sure the cannon does all those things, then
# create a first move made boolean for each player to track their first move. Ok, so how are we going to test this
# first move has been made boolean. When does it change? When a player makes a move, so more in the game loop right?
# It's in the make move function actually. If it's there first move, we need to check it basically. Alright, so how
# are we going to test this? After creating both players, let's call their get first move booleans. Then, make moves
# with a blue and call both, then make move with red and call both. They should be updated correctly. But first, make
# sure the switch players function works as well. Ok, that all worked. Took a little longer because of the way we have
# current player assigned. It doesn't make sense to have current player as a private member of the player class, but
# we were assigning the curent player a string for their color, instead of the object, so that got kind of confusing.
# We needed to access the current player's color, which is actually their name and can be obtained from get_name, which
# we totally forgot about.

# Alright, so let's now create the get valid cannon moves function and copy the get valid chariot moves function, but
# put in all the movement restrictions. Wow, just changing all the instances of chariots to cannons took like 10 mins
# lol. Let's move the cannon around and make sure we didn't break anything. It hsould move exactly like the chariot.
# Ok, we thought we didnt' check if the chariot can stay still, but we did. However, we noticed a problem "moving" to
# the same spot, we captured the piece, and removed that piece, even though nothing happened. What needs to happen is
# the move return successful, but no moving or capturing happens. Ok, so we put a check for the to and from coordinate
# being the same near the begining of check move, and it just switches the player but doesn't update anything. Actually
# now that we look at it some, if the from piece isn't the current player's, or if the game is over, we don't want to
# switch players. Let's actually move this check before we start capturing pieces and making moves.

# Ok, I think we fixed it. That was a nice little extra detour. Now, what's the first thing we want to implement in the
# get valid cannon moves function? Let's list all the movement restrictions again. The first restriction, and easiest
# and most important, is that they can't make the first move, so check the first move made boolean, and if it's false
# then there are no valid moves for the cannon (return an empty valid moves list). Alright, so I think the checking of
# the first move made boolean is correct now. We still have to update the chariots code to match the cannon codes bc
# of the minor errors we saw.

# Ok, so what's next for the cannon? It's the big one. We need to code the restriction that it needs to jump something,
# but also that that something can't be another cannon. Alright, so let's talk about where we can add the jumping unit
# restriction. There are 2 spots in the get valid cannon moves function; we can do it the move lists, or we can do it
# while iterating through the move list. Currently, we iterate and if there is no piece at the first coordinate, it goes
# into the valid moves list and we move on to the second coordinate. If there is a piece, we check if it's an enemy or
# or ally. An ally piece doesn't get the current coordinate added, and the valid moves list is returned. An enemy piece
# returns the valid moves list with the current coordinate added. So, for this, if we leave the code the same, then we
# need to comb through the valid moves lists and find a piece to jump, which I think is a bad idea. So what about if we
# keep adding the moves into the valid moves list, then if we go to the end and we don't find another piece, then none
# of the moves in that move list are valid (after the loop, if a boolean for there_is_a_piece_to_jump is false, we
# change the list to just the current coordinate [because they can always pass the turn]). If there is a unit in the
# path, then we update the there_is_a_piece_to_jump to True. Actually, within the check for there being a piece, we also
# need to make sure it's type is not Cannon, because we can't jump cannons, so we don't change the piece_to_jump boolean
# if the piece is of a cannon type. So, if the piece is not a cannon type, then what? We check if it's an ally piece or
# an enemy piece. If it's an ally piece, we don't add that current coordinate to the valid moves list, but we keep going
# through the list. What happens in this case? The rest of the moves are valid, up until we find a second piece, then
# there is another piece check. If it's an ally piece, we don't add the current coordinate and return the valid moves.
# If it's an enemy piece, we add the current coordinate, and return the valid moves. But what if this second piece is a
# cannon type, would that change things? If it's an ally cannon, we still don't add the current coordinate. If it's an
# enemy cannon, then things do change. Instead of adding the coordinate and possibly capturing the enemy, since we can't
# capture enemy cannons, we don't add the coordinate but return the the valid moves. Alright, so, let's see where we
# can start coding this. Actually, let's first make sure, cannons can only jump one piece. Reading the wikipedia, we
# also see a couple of things. It says cannons can't make the first move, but it isn't a rule actually. They can't make
# the first move because their movement means there aren't any valid moves in the beginning. This got us to look at the
# board, where we see that, even though they can move down since there is a horse or elephant unit down there, if the
# board ends when there is the first unit to jump, they actually don't have anywhere to go. This means our current code
# would be calculating the valid moves wrong. The valid moves start at the square after the first piece.

# Alright, let's first move the boolean that keeps track of first moves, because that is actually not correct. Ok, so
# we moved all first move boolean aspects, we had actually added quite a few things in there. Now, let's try to code
# the cannon movements. Let's look back at what we're trying to do again and see if we can understand it better. Alright
# so at first, we'll iterate though the correct move list. Outside the loop, we will set a piece_to_jump boolean to
# False, then go through each coordinate. At each coordinate, we check if there is a piece there. If there isn't a piece
# then we move on to the next coordinate. Actually, if there isn't a piece and piece to jump is False, we don't add
# that coordinate. If there isn't a piece but piece to jump is True, then we need to add the coordinate. Alright, so if
# there is a piece, what are we checking? We need to first determine if the piece is of a cannon type, because if it's
# a cannon type, then we can return no valid moves since we can't jump a cannon type. Actually, if the piece is a cannon
# the pass play is still valid, so we still want to return a valid cannon moves list with the current coordinator. The
# question is, does it matter what the status of the piece to jump boolean is? If piece to jump is False, then there's
# no piece to jump, and we can't jump a cannon, so there are no valid moves beside the current coordinate. If the piece
# to jump is true, we can't jump a cannon, or capture an enemy cannon, so we still don't add the current coordinate and
# then return the current valid cannon moves list, so yeah, they both lead to the same thing. Alright, so what happens
# after we check if it's a cannon piece or not? We check if it's an ally piece? Or do we check if the piece to jump
# boolean is true or false. I think we want to check if it's an ally piece. So, if it's an ally piece, then we check if
# the piece to jump boolean is True or not. If it's an ally piece and piece to jump boolean is False, we change the
# boolean, don't add the current coordinate, and move on to the next coordinate. If it's an ally piece and piece to jump
# boolean is True, then this is a second piece in the way, so we don't add the current coordinate and then return the
# valid moves list. Actually, our current code format checks for enemies first, so I think we should do the enemy code.
# So, if the piece is an enemy piece and the piece to jump boolean is True, then it's the second piece, so we add the
# current coordinate and return the valid moves list. If it's an enemy piece and the piece to jump boolean is False,
# then we don't add the current coordinate, but we do change the boolean to True. Actually, I think we want to separate
# the code by boolean, instead of by enemy type, because the booleans do the same thing? So, if piece to jump is True,
# then both ally and enemy is the second piece, but we add the current coordinate if it's an enemy piece. If the piece
# to jump boolean is False, then we change it to true, don't add the current coordinate, and move on to the next
# coordinate. I think we've coded this correctly, but let's try it out. The initial spot is a good testing spot, because
# there are no valid moves at the initial spot.

# Alright, so we tested every possible orthogonal direction for the blue cannon, and they the moves failed, which is
# what we wanted to happen, so it looks good. Now, we have to incorporate the diagonal palace movements, then migrate
# all the blue cannon class code to the red cannon class code. Actually, let's first try to test a valid movement for
# the cannon. Yeah, the current orthogonal movement looks fine. Now, let's look at the diagonal palace movements and see
# what we need to do. Wait a minute, shouldn't the diagonal moves work as is? We aren't changing the diagonal possible
# moves, we are just adding more move requirements, but we've already added the move requirements, let's just move
# pieces around and see what happens. Actually,everything looks correct. For the cannons, the palace movements are
# exactly the same, it's just the blocking restrictions are different, but we've coded the blocking restrictions in the
# get valid cannon moves function already, so we actually don't have to change anything here. Alright, let's migrate the
# code to the red cannon and do some more testing. Alright, the red cannon down movement works good. Now we need to test
# its diagonal movement as well. Ok, we tested a lot here, and they all seemed to work, so that's good. Now what?

# Well, we're finally done with all the piece movements, so we have 2 more functions to do for the program requirements,
# those being the "is in check" function, and the function to check for checkmate at the end of each turn. Ok, so "is
# in check" takes as paramters the color of the player (which is the player name) and returns True if that player is in
# check or False otherwise. What does being in check mean? Lol, right now I guess we aren't thinking properly. What does
# it mean to be in check? This is just for the general's right? Ok, so being in check means that the general can get
# captured by one of the opponent's pieces. Ok, so let's think back to chess. When do ppl get checked. In regular chess,
# after each move, check is checked, but usually the opponent that puts the player into check declares it. So, at the
# end of a player's turn, you have to check if that move put the player in check I guess. So being in check means that
# one of the player's pieces can capture the other player's general.

# Alright, didn't think we'd have to think about it, but all the coding has made us forget how the game is actually
# played. Alright, so after a player's move, we have to check and see if the opponent is in check I'd say. So what does
# it mean to be in check again? If any of the opponent's pieces can capture the other player's general. Alright, let's
# break this down even more. So, the current player finishes his turn, so now we want to check for check. The checking
# for check, is for the current player's opponent, so we get the current player, and we set the opponent equal to the
# not current player. Alright, let's try to code this part first. So, we start with the player in the parameter that we
# want to know is in check. So we have to get that player's opponent, then we check every possible move of every alive
# piece that opponent has, and if any move can capture the player in the parameters general, then they are in check.
# Hmm, we're calling the get valid moves function for every alive piece of the opponent, but... the chariots and cannons
# need a to coordinate, so how do we do that? What is the to coordinate? The to coordinate is the general's coordinate
# isn't it? Yeah, yeah it is! So we do have it. So how do we put it in for some and not for others? Actually, we don't
# want to call the get valid moves, what we want to call, is the make move function, which will tell us if a move can
# be made or not. But, we don't actually want to make a move, so how do we do that? I guess we can just copy the
# function and change it to where it doesn't actually capture any pieces?

# Hmmm... let's think about this for a second. Let's say we have a make move that is just hypothetical, and doesn't
# actually move the units like right now, how would we do this? We get all the alive pieces of the opponent, call a fake
# make move function to the player's general (so the from coordinate is there current coordinate, and the to coordinate
# is the coordinate of the player's general), and if any of them are possible, then the player's general is in check.
# The assignment is pretty specific about the make move function, so yeah, we should probably just copy the make move
# and change it to a check move, basically make the code not capture a unit and switch turns and all that. Alright, we
# see that the check function works, but when it gets to bluCha1, it says move list referenced before assignment, I'm
# thinking because we don't have a movelist yet. We need parameters for valid moves that we didnt' put in... so we have
# to put those in... Actually it wasn't the paramteres, it was us trying to print the move lists for chariots and cannon
# when nothing was generated if the move was a diagonal move that was invalid. We fixed it, and got a full cycle of
# checks that didn't find a check and checks that found a check, so the is in check function seems to be working.

# Now, we need to figure out, when the general is checkmated. So basically, I think this one is simple? We get all the
# valid moves of the general, simulate those moves, then run the is in check function for each simulated spot. If they
# all lead to check, then the general is checkmated and the opponent has won. Actually, we currently don't have a way
# to simulate moves, but we don't have to. What we can do is this... we first get our valid moves of the general, wait,
# how would we do that? It would be at the same time that we do the is in check checks I'd say, or maybe check for
# checkmate is a function with is in check in it... Anyways, so we have the current player, we call get opponent from
# current player to get the opponent, then we need that opponent's general piece, how would we do that? Iterate through
# the alive pieces list and find a match for type general, then color equal to opponent.getcolor(). Then... we run get
# valid moves for the general, and from that get valid moves list, for each coordinate, we set the general to that
# coordinate to simulate movement there, then run the is in check function with the parameter being the opposing player.
# If all are in check, then we can return True that there is a checkmate (from outside the for loop), but if any is not
# in check, then we can return False inside the for loop.

# Alright, so let's first create a checkmate function, something like player_is_checkmated, which will use the is in
# check function, so I actually don't think we want to even use is in check (but we'd like to print out a notice if one
# of the player's is in check). Ok, so how are we going to test checkmate? Well, we need to get a general in checkmate.
# We thought we created a checkmate scenario with bluSol3 in front of redGen1, but it didn't say checkmate. Technically
# this isn't checkmate because the red general can move to the bluSol spot and take him, but we didn't account for the
# fact that the red general can move to a spot and capture the other unit in our code. First, let's use a different
# piece that the redGen can't capture and see if our checkmate code is working properly. Hmmm... it seems to be getting
# valid moves list wrong for bluCha1 when bluCha1 at e4 and redGen at e1, so let's stop debuggin this and go to debug
# that lol. Hmm.. that's weird, so moving it by itself gave us the correct move list. Let's put the check function in
# and see now. So the move list is coming out wrong in the is in check function, probably from inside the move is
# possible function, but we're not sure why. How are we generating the move lists? They are coming from the get possible
# moves function. Ok, it looks like we were appending to the lists in the data members, and appending them more when
# we call it for these check functions, so we added a clear before every loop for these lists before appending again.
# We need to do that with the other chariot, and then cannons as well.

# Ok, we fixed the problem with the data lists accumulating values bc of append and calling the possible moves list
# multiple times, now, what were we even working on lol. Oh yeah, we were trying to get the game to say checkmate, to
# create a checkmate situation to make sure the function worked. Ok, so the way we've currently set up checkmate, it
# is not a real checkmate. The blue chariot at e3, and the red general at e1, although the chariot can get him going up
# the chariot actually can't move diagonally at e3. We had forgotten about this, but the only diagonal movements are at
# d3, f3, e2, d1, and f1 in the red palace. Yep, we double checked it, and that's correct so that's not technically a
# checkmate move either.

# So, we need to find a real checkmate situation, which probably involves more than just one piece to block the general.
# With that said, I think we've identified a problem with our checkmate function. It seems that it's possible for the
# current player to make a move, and put his own general in a checkmate, and we're only coding for the opponent's of
# the current player, so maybe we need to check the current player to make sure they didn't put themselves in check (or
# is this an illegal move?) not sure. Furthermore, when we are hypothetically moving the general, we are just changing
# it's current coordinates. However, if there is an opponent's piece there (valid moves doesn't include ally pieces
# right? we can't remember) then the general would actually capture that piece. So... maybe instead of just setting the
# general's coordinates to that possible position, we can check first if there is an opponent at that position, and if
# so, remove him (maybe by changing his coordinates to something off the board?). A couple of other things we were
# thinking of last night. For one, maybe we can put the move list data parameters in the chariot and cannon classes
# in the possible moves list, via a dictionary, something like [{list1 name: list1, list2 name: list2, etc}], then we
# can still access the lists from the possible moves list and wouldn't need any additional init parameters or getter
# functions (we need to make sure we aren't trying to access these lists when possible moves list is not available,
# otherwise we might still need private data members for the lists). Another thing we thought about is what does it
# actually mean to be a dead unit? That is, if we remove a dead unit from the alive pieces list, then try to find a
# piece at the coordinate where it just was, does it show that a piece is still there? If it does, not only do we have
# to move units out of the alive pieces list when dead, we also need to change their coordinates to something off the
# board, or give them None coordinates and make sure the code only checks the coordinates if they are not None.

# Let's first test the alive dead thing. Let's remove a piece from the board, then call get piece from that unit's
# coordinate and see what it says. Ok, so the coordinates of the dead general are still the same, however, when we call
# get piece from that coordinate, it returns None, so there's no piece at that coordinate, which is correct. Let's make
# sure the get piece from coordinates finds the piece before we remove it. So what does this mean for our checkmate code
# Well, I think if the general goes to a coordinate that has an alive piece, and since allies are already invalid, then
# it must be an enemy piece, so we need to remove that piece from the alive pieces board temporarily, then add it back
# after the checkmate check. Let's test this. First of all, we need to make the checkmate situation happen. Let's move
# the bluechar to e3, redgeneral to e1, and both blue guards to e3 and f3. That should be a checkmate and set off our
# checkmate prints right.

# As we're thinking about this, not only can the general remove the unit that put him in check, but so can other units
# on that team, so how are we supposed to handle that? I think, first of all, the general is prevented from ever moving
# into a check right? Since if they move into a check, the opponent can go to capture it, and it has to be a checkmate?
# Honestly still don't know the rules of this game. Lol, wow, our move kept being unsuccessful and we couldn't
# understand why, but we had made the current player red while the from piece was blue, ugh. Removing all our prints
# made it really hard to track this error.

# Alright, so we were able to get the checkmate code to appear, so the opponent can be checked. Now, let's check this
# by moving away from of our bluSol, which should prevent the checkmate. Alright, so that did work, but I don't think
# checkmate is that simple, once again. Like in our checkmate example, if the general in check's other pieces can block
# the general, then he isn't checkmated. Let's work at the other stuff for now, and we want to google this checkmate to
# see what it actually means, bc we don't know situation we are trying to code for.

# Let's first make sure, when we are moving the general around hypothetically, that if there is an enemy piece there,
# that he takes it temporarily. We don't understand when to remove the piece from the alive pieces list, and when to
# bring it back. Let's forget about this for now, since it is related to checkmate and we're not sure what we want to do
# with checkmate, and look at the data structure of our chariot and cannon moves list. Instead of appening them to the
# move lists in their private data members, let's append a dictionary that can link to those lists inside the possible
# moves list. Let's start with the blue chariot, and try all the code with the blue chariot first. Alright good, it was
# awkard to add the dictionary because we had to get another variable for the list to append to, but once we got it, we
# were able to access the dictionary which was the second item in the possibles moves list (the first being the original
# coordinate) so possible_moves_list[1]["name of key in dictionary"] gave us the correct lists and it has tested fine.
# Let's migrate this code to the red chariot, and then update the blue and red cannons, then update the get valid
# cannon moves function and adjust the get valid moves function to incorporate the possible moves parameter. Alright,
# the red chariot moves were fine, as they should be since we just copy and pasted, but it didn't test for a while bc
# we forgot to switch the current player lol.

# Alright, so I think we did a lot of things we wanted to do today. We wanted to make sure when we removed a piece from
# the alive list, that it wouldn't be found at its coordinates by the get piece from coordinate function, which it did
# not, and we wanted to change the private lists to inside the possibe moves list, which we were able to do with a
# dictionary. However, we were still unable to fully grasp what checkmate means. We know that our current code isn't
# enough, since we keep thinking of exceptions to our checkmate code. We still need to google checkmate to see what it
# all entails, but a couple of questions from yesterday still remain.

# Do we have to check for checkmate for the current player after they move, that is, can the current player move into
# a check/checkmate, or is that an illegal move? In addition, we need to code the general to remove a piece during their
# hypothetical moves in checking for checkmate (removing an enemy piece), but we need to think about it more to see
# where we remove the piece from the alive pieces list, and where we want to return the piece. Also, we haven't gotten
# an answer for what if the general can avoid checkmate by another ally pieces move, bc so far, we've only checked all
# the possible moves of the general, but an ally can save the general as well, and if we have to check all the ally
# movements that can save the general, that's gonna get complicated.

# Going through the Piazza, apparently in the readme it says "a player can't make a move that leaves or puts their
# general in check", so yeah, I guess we don't have to check the current player for checkmate, since it is illegal for
# them to move into a check or leave general in check. We also saw another post that was quite relevant, this one about
# checkmate. The poster says:

# "From my current understanding, if Red is in check, then I have to see if Red's general
# can move, and if that movement would get it out of check. Then if not, if a red piece can capture the threatening
# piece. Then if still not, if a red piece can block anywhere in the path of the threatening piece."

# and a student replied:

# "You might try tracking the source of pieces, the destinations from a source, and the paths to a destination. You
# might also try making a do_move and undo_move method. To see if capturing an attacking piece saves a general from
# check, just call is_in_check again. To see if blocking (moving into the path of a piece) an attacking piece saves a
# general from check, just call is_in_check again."

# Alright, so let's deal with the first answer from Piazza first. A player can't make a move that leaves or puts their
# general in check, which means, we need to check if a move would put that player's general in check as a condition when
# checking if a move is valid, and not add it to the valid moves list if it is. Ok, first of all, how do we simulate a
# move. We know that before, we were just changing a piece's coordinates to simulate movement, but that doesn't fully
# do it does it? We're missing the part where they capture the piece, which is a big part, but is there anything else
# we are missing? I mean, I don't think we can use the make move function, bc the make move function also switches the
# players turn and updates the game status and stuff, so yeah, I don't think that's a good idea. It's gonna have to be
# a different function. So, what happens when a piece "moves" to another spot? Well, the place piece function would do
# all that, and I think that's ok to call, if we just remember the previous coordinate (maybe by creating a previous
# coordinate private member that starts as None and we change during the place piece function? yeah that could work).
# Ok, so we can modify the place piece to place the piece there, and save the previous coordinate (or we can just do
# what we tried to do and save the coordinate in for loop and replace it afterwards but... I think we should implement
# a simulate move function to see if the it leaves the general in check. One question before we do this... If the
# general is already in check, we can't move it into another check spot right? So it's not a valid situation? This is a
# static requirement since it's the same if the general is in check or not in check right? If the general is in check,
# and they move to another spot in check, then they can be captured, but it isn't a legal move because you can only win
# via checkmate. If the general is in check and every other spot creates a check, then it is already checkmate (assuming
# none of the other pieces can remove the checking piece or get in the way).

# Alright, let's first do a simulate move function, then we'll code a function to check if the simulated move results
# in the general being in check, and if so, then it's not a valid move (put it inside all the valid move functions).
# Alright, there is a lot of related things going on here, so let's tackle them one at a time. If we are going to save
# the previous coordinate of each piece, then we need to add a previous coordinate private data member to the piece
# superclass. Ok, so we did that, now let's update the place piece function to keep track of the previous coordinates.
# Ok, we also needed to create getters and setters for previous coordinate, but now let's do a simple test before and
# after placing a unit to make sure the previous coordinate is correct. Ok, it was kind of confusing bc the previous
# coordinate starts at None, but I think we got the function right the first try, it really isn't that complicated. So
# let's do simulate move function now. What exactly do we want our simulate move function to do? It's going to move a
# piece from the from coordinate to the to coordinate, very much like the make move function. Ok, if that's the case,
# does it need to check for valid moves? I mean, technically the move should be valid, so we're going to call this
# inside of the valid move functions, after the move has been validated for its other restrictions, so we don't need to
# validate the moves. Alright, so we'll call place piece to move the the piece, and then what? Then I think we call the
# is in check function to see if that move leaves the that player's general in check, and if so, we want to return False
# that the move is not valid. We might be thinking of 2 different things here, bc if we just want to validate any move
# to make sure it doesn't leave the general in check, we should make this a boolean function, called something like
# "move results in check" and then return True or False based on that. We can actually keep the simulate move function
# as well, but how are we going to call it in the move results in check function? Let's break down what we want a
# simulated move to do as well. We want it to place the piece at the target, then check whatever needs to be checked,
# then reverses the move. What does this mean? If a piece is captured, then it needs to be returned. Then the current
# piece needs to return to its original coordinate as well.

# Alright, let's do one thing at a time and try to write this move results in check function. Alright, so we wrote it,
# and we removed the simulate move function. We put the parts of the simulate move function in the move results in check
# function, so maybe we can take it out and put it in a simulate move functions in the future, but as of right now, we
# don't need that. Now, let's move this function into the end of each valid move check before adding moves. Actually we
# need test the function. Ok, so we need to make a move that leaves the general not in check, and one where the general
# is in check, to see what happens. Alright, let's move the red soldier out of the way and put the red general at e4,
# then e5. Alright, the function seems to be working, at least for the checking part. Now, we also need to make sure
# that the original coordinates and pieces are maintained after the simulated move, so let's do a move to an empty board
# and check the current coordinate of the general before and after the move, then a move to capture the enemy, and check
# the current coordinate of the general before and after move and the coordinate of the piece at the target coordinate
# before and after the move. Alright, there seemed to be a lot of moving pieces in that function, but I think we got it
# right. It checked for check correctly and all the pieces got returned correctly. Now, let's put it into all the valid
# move functions. Alright, so we've put it in the get valid moves function, literally just snuck it in a line, which is
# good, we like it when the code is modular and we can just add pieces easy breezy. Now, we can only test units that
# are not chariots and cannons, since we use a different valid moves for those.

# Let's test the general that we've been testing, and focus on the valid moves for the general. Hmm.. there is a problem
# with our parameters that being there is no to coordinate. We need to call this check actually inside the make move
# function, since it has the same parameter requirements. Ok, so that worked, but it kinda feels like spaghetti code
# since we are calling more move validating functions outside of the functions for them, however, instead of adding it
# to 3 different valid move functions, we just had to add it to check move, so that was more efficient for sure. There
# is one more check situation, and that is while the general is already in check. Wait, but this is still the same
# concept, they can't make a move that leaves the general in check, yeah, I don't this needs to be coded.

# Ok, so for now, we can remove the previous coordinate data parameter from the piece superclass. So the next issue we
# need to address, is that apparently there are 3 different things to check for in checkmate. Not only do we make sure
# that all the general's moves result in check (we haven't finished coding this since we haven't simulated the move in
# this part of the checkmate code yet), but then we have to check to see if any other of the player's pieces can remove
# the piece checking the general (so we'll simulate a move to remove the checking piece, then call is in check to see if
# the general is still in check), then if a piece can block the path of the enemy piece to stop a check (again by
# calling is in check again).

# So yeah, I think we first have to simulate all the moves of the general to make sure they can't get out of check, then
# we simulate all the moves of the rest of the pieces for the player that owns the general, and if all those moves
# result in a check for the general, then the general is checkmated. Hmmm... the last 2 steps, it seems we can combine
# since we are already checking the moves of all the ally pieces.

# Ok, so we were thinking of a couple of things last night. We were thinking about how we weren't really using the other
# classes, before because it was awkward to make another board after creating a board in the board class, but, no it's
# fine, just make a getter function for it and create a board object in the game class, we could give them slightly
# different names to not be too confusing. Same with the Player class, it's ok to create the players if we create getter
# functions for them. If we're talking about objects in this game, then the board, the pieces, and the player's are all
# objects, so they should be in their own classes, so we should make this change. We also realized as we're testing the
# make move function that it's kinda backwards right now. We are finding the one instance where the move is possible
# and returning true, and returning all the other instances as false, but that isn't productive to debugging or putting
# print statements saying what is going on. We should reverse the logic so that we are looking for ways to make the move
# not successful, returning False out of the function, then writing a print statement before that saying why it was
# false so we know what's going on with the moves. We can also use it to notify the user why they can't make a move,
# probably the most important thing. Furthermore, we were considering using the make move function as the function to
# to test moves, instead of the move results in check function, since they should be very close to each other in
# functionality. Can we augment the make move function, or create a test boolean or something, to make a the make move
# function test moves and perform moves? For example, is testing is True, don't switch the players or something like
# that, or we can just put save the important states before the make move and restore them after make move.

# Alright, so let's start by reversing the logic in our make move function so look for return False instead of return
# True. Alright, I think we did that ok, now let's test all the elements of the make move function to make sure
# everything works as we want it to (leave in all the print statements so we can test every situation). First we want to
# test a regular move, then we want to test a move where there is no coordinate at the from coordinate. Actually, for
# now, we do want to comment out the checkmate and check code, bc we aren't really testing those functions and they
# print a lot of print statements. Alright, good, we were able to revamp the make move code in about an hour, so that's
# good. Now what. Let's tackle the problem of using make move or move results in check function to test hypothetical
# moves. The current problems we see with the make move function is that it prints too many things (which I guess we
# can remove the print statements if we know we're testing it, but if those statements are part of actual moves, it
# gets hard to know right) and switches the players around. The problem with the move results in check function is that
# it hasn't implemented all the move restrictions, but does that matter? We are calling the move results in check
# only after getting the valid moves right? So it'll just go through all the valid moves, so it doesn't need to move
# restrictions? Alright, let's look over where move results in check gets called. So, in the make move function, it's
# called after all the move restrictions, with the last one being the to coordinate has to be inside that piece's valid
# moves list, so yeah, we don't need to implement movement restriction for move results in check if it's only called
# inside the make move function. However, in the is in check function, which is used in the player is checkmated
# function we are calling the "move is possible" function, which is basically a move results in check variation. I think
# we are ok to use the make move function, but here's the thing, we have to reverse the things, and actually capture the
# pieces. I think we can do a testing_moves boolean and change the logic in make move to accomodate what we want. Let's
# try it out.

# Ok, so let's think about this. We have a testing_moves boolean, which we will set at initialization to be False. Then,
# when do we turn it True? We want to turn it to true before we start calling simulated make moves. Ok, then when do we
# want to change it back to False. Well, obviously after we are done with the simulated moves, which I guess depends on
# where we call the simulated moves. Ok, I think this part is easier than the next part, which is, how do we incorporate
# the testing moves boolean into our make move code? First, let's go ahead anc create this boolean in the game class.
# Alright, good, so in a test move, what do we want and what do we not want? We're already seeing a problem, that being
# that we create a list of possible moves and valid moves everytime our make move is run, which seems unnecessary? Ok,
# we have to go back and see where we are going to call the test moves first of all. Alright, so looking over the is in
# check function, it basically looks for all the alive pieces of the opponent and tries to move them to the general's
# current coordinates, and any can, then the opponent is in check. So, it does needs to create the possible and valid
# moves for each of the opponent's pieces and run the checks if the move is inside the valid moves list and if it
# doesn't leave that player's general in check. However, there are some things we don't want. It can't check to see if
# its color matches the current color, because they will be making moves on the opponent's turn. It also doesn't need to
# check if the from piece is None, because it is always not none, since we already checked for all the alive pieces. It
# also doesn't need to check if the game is over (you can simulate moves with the game being over), or if the to and
# from coordinate are the same (since they will never be, unless the to piece is on the other player's general lol).
# Actually, this check is to capture the enemy, so it does want to run this check and capture the enemy. Alright, so we
# capture the enemy piece if it's there and place the piece, but we don't switch the player's or check for checkmate or
# check. So yeah, it should be a different function.

# Ok, so we have a good outline of the simulate move function that we want, so how and when are we going to call this
# simulate move function? For the is in check function, we simulate the move to the general, and if it's possible (so
# returns True) then the other player is in check. Can we use our move results in check function here? Actually yeah,
# the move results in check function is exactly what we want, it's just a variaton of the moves is possible function, so
# it actually works in the exact same way. If the from piece can go there, then the general is in check. But whose
# general is it checking? I think the move is possible doesn't really specify a player, but the move results in check
# is talking about the player that owns the piece at the from coordinate, which is a thing that is getting us confused.
# When we check if a move results in check, we check if the player moving that piece leaves their general in check, but
# when we call the "move is possible" function, we are checking that the move is possible, and if so, is in check says
# that the opposing general is in check. Can we use a parameter with the move results in check function that tells it
# which player to check if in check? Alright, we added a player name parameter, now let's see if we can test this to
# see if we can get both player's in check. Ok, yeah, the player parameter works. So what can we do with this? We select
# the correct player in the make move function, and the correct player in the is in check function, to differentiate
# between the player's we are looking to check. So it looks like the is in check function already works fine. We it
# already finds the opponent of the player in the parameter.

# Also, we need to incorporate the move restrictions that we brainstormed for the simulate move function into the move
# results in check function. Ok, so currently we have 3 move functions that all get possible and valid moves, those
# being the make move function, the move results in check function, and the move is possible function. Can we put some
# of these move lists into parameters so we don't keep creating them? Let's see, so make move calls move results in
# check, so we can add a parameter for the valid moves in move results in check. The move results in check function
# calls is in check, but we can't pass any parameters into is in check, and is in check calls move is possible. Do we
# need the move is possible check, why don't we check if the move is possible already in move results in check, then
# just see if it results in check. Resulting in check just simulate movement to the general. Actually, we don't even
# need the move results in check function in the make move function? We just call is in check (but we need to simulate
# the move though), then is in check will simulate more moves to see if that move results in check. Alright, so how many
# move simulations are we actually doing? For make move, we simulate movement when calling move results in check, then
# is in check simulates the movement for all the opponent pieces to see if they can get the general in check, so there
# are 2 rounds of movement simulation. The first movement simulation sees if the move leaves the current player's
# general in check, and if not, then the second movement simulation checks if the first simulated move leaves the
# opponent's general in check. Ok, so what about instead of calling move is possible we call move results in check again
# does that work?

# Lol, the code seemed to create an infinite loop. We are calling move results in check, which calls is in check, which
# calls move results in check, so yeah lol. Ok, actually, we can use a different function, and it doesn't have to be
# the moves is possible function, which basically is just calling the target coordiante inside valid moves list, so we
# can just use that. But we'll need to create possible and valid moves for each valid coordinate.

# Ok, so I think we finally got clarity with the move results in check and move is possible functions, which were very
# similar, by removing the move is possible function. Now, we need to incorporate some of the movement restrictions
# brainstormed in the simulate move function into either the move results in check function, or the is in check function
# so that we don't make any ilegal moves for all the simulated moves. After we figure this out, we need to code the
# checkmate code like the make move code, looking for any False checkmates. The false checkmates being, any of the valid
# moves of the general resulting in not being checked, and also any valid moves of the rest of the pieces resulting in
# not being in check. If every move the general can make results in check, and every move the ally pieces can make
# results in check, then it is checkmate!

# Ok, so let's first see where the simulated coordinates are to see where we need to put in the restrictions. Ok, so it
# looks like all 3 functions (make move, move results in check, and is in check) all rely on is in check, so we can put
# it in there. Since we are already checking the valid moves, just add the additional restriction that the move doesn't
# result in a check? Or is this the infinite loop again lol, not sure. Yeah, we can't call the function A that calls
# function B which calls function A, bc that's an infinite loop. So let's think about this restriction about not being
# able to move to a spot that leaves your general in check. Obviously this requires calling the is in check method. Can
# we change the move results in check method to not use is in check? Lol, I don't think so. Ok, so what is the problem
# again? We need to add an if statement for the simulated moves that if the move leaves the general in check, then it's
# not a valid move. Why don't we call this in the valid moves function? If we call this in the valid moves function,
# then the valid moves don't have to be filtered. This means that every possible move, we check if it leaves the general
# in check? That seems really bad, like really inefficient. Let's think about this just without the context of our
# current code. When would we want to check to see if a move leaves the general in check? We'd have to check it for each
# move right? Or only when the move is attempted? Ideally we only do it when it's attempted, because that's just more
# efficient. Let's go over the moves again. Actually, let's try looking at it like before, filtering it before valid
# moves. Wait, so why can't we put this in valid moves? It is part of the move validation code, let's put it in valid
# moves. Note that chariot and cannons have their own valid moves, but yeah, let's put it inside of these other ones
# and see what happens. Lol, so now we getting recursion error and seeing that our valid moves is calling valid moves
# in the is in check function lol.

# I guess that's where we are stuck now. We can't simulate these moves and put in the move results in check condition
# because it calls the is in check function. What if we remove the move results in check function and just put
# everything inside the is in check function, would that work? What does this mean? We'd have to create a simulate move
# function to simulate the move, then call the is in check function lol. Lmao, this seems to be going around in circles
# and getting pretty frustrating.

# We need to talk out what we want the function to do logically and see if we can't figure it out that way. Alright, so
# what is the make move function doing. We want to check if the a move actually leads to that player's general being in
# check, so I think we can just call is in check here right? We'd have to simulate the move, then call is in check,
# which is basically what move results in check does. Ok, so what's the problem then? The problem is that is in check
# is actually not checking to see if the move leads to that player being in check, basically once we call is in check,
# we also need to call it again to see if that results in the current player being in check, so the function will keep
# calling itself. What if we have 2 different is in check functions? So, for the make move function, we call is in check
# for the current player, so just regular is in check. So if not in check, then we want to check if the opponent is in
# check, so opponent is in check function (here we can also check for checkmate while checking for if in check). They
# are basically checking the same thing, but checkmate keeps going if they are all checks. Let's speak in terms of when
# we need to check if the move leaves the current player in check. I think this is a lot simpler if we just remove the
# moves that leave the current player in check out of the valid moves list. So let's talk this over. The valid moves
# function gets all the possible moves of a unit and returns all the valid moves. Its parameters are the current piece
# , a possible moves list, and the to coordinate, which is optional. So, for the valid moves, we want to iterate though
# each possible move, weed them out for off the board and not blocked moves, then add them to the valid moves list. So
# now we add a third restriction, the move can't leave that player's general in check, into there, and if all is fine
# there, then we add the move. The problem is, our is in check function is actually calculating all the valid moves
# again, so that is an infinite loop. I guess we can get around this if we save the valid moves into a data parameter.
# Let's look at the is in check function again.

# Yeah, I think we've pinpointed the problem, that being that the is in check function, needs to call is in check for
# the valid moves that it creates, so it's a never ending loop. How do we separate checking if a move leaves that player
# general in check, and if the move leaves the opponent's player in check? Let's think about this in terms of the
# checkmate function. So what are we doing in our checkmate function? First we want to get all the valid moves of the
# general, and if they all lead to a check, then we move onto all the moves of the allies, and if they all lead to
# checks, then it is checkmate. This actually seems incredibly simple, the problem is, and still is, we can't seem to
# incorporate this check if the ally is in check before making a move function, because it calls is in check.

# Ok, the real problem seems to be that in order to check to see if a move leaves the general in check, you need to know
# beforehand whether that move leaves the general in check, so it kinda defeats the purpose. Is in check is generating
# moves that need to be checked if they are in check or not, and it should be generating moves that know if they are in
# not going to cause the general to be in check. What does it mean to be in check again? If any of the opponent's moves
# can lead to them capturing you in the next turn. I think if we can somehow get the valid moves to populate with the
# moves leading to the player getting their general checked removed, it would be really good. I guess another way we can
# do that is to call the make move function. If make move is possible, then we check if that leads to... No the problem
# is that the is in check function is using the wrong valid moves list and needs to call itself to get the right list,
# so it just doesn't work. Our best idea is to make the valid moves list a data parameter, but we still need to call
# the is in check method on it, and what if the valid moves aren't populated?

# Man this is getting frustrating. let's code the checkmate function with the is in check we have right now, and redo
# the classes like the way we want, and hopefully tomorrow or later we can figure this out, because it's just not
# happening right now and we feel like we are wasting time. Alright, so, the checkmate function, assuming on is in check
# is working... We get all the valid moves of the general, go through each one, and if any are not in check, return
# False that it is not checkmate. If they are all true, then we go through all the allies pieces, and see if each every
# move from the ally still leads to the general being in check, and if any don't leave in check, then we return False
# that there is no checkmate. We return through after all those if statements, since every move leads to check, then the
# general is in check.

# Hmm.. we're trying to get all the valid moves of each piece, but, we don't actually have a direction for the chariots
# and cannons, so we have to figure that out. I guess we can put in, I mean, what are the directional requirements for
# chariots and cannons? Is there a to coordinate that the chariots or cannons are trying to reach? No, I don't think so,
# which is pretty annoying. We're gonna have to hardcode the chariots and cannons, but for now, let's forget about these
# exceptions and see if the checkmate code even works. Alright, so let's test this iteration. We can't check for
# chariots or cannons though, so I'm not sure if this code is going to run. Ok, we ran into a lot of issues, only to
# that yes, this is not working because we do have to get the valid chariot and cannon moves.

# Alright, so currently we get the valid chariot/cannon moves by first figuring out the direction they are going with
# the to coordinate, then limiting the valid moves list to that, but we don't want to use the to coordinate, bc when we
# are checking the moves of the ally pieces of the general, we want every possible valid move, so we need to calculate
# every possible valid move, so how is this going to work? Currently, our possible moves consist of the current
# coordinate and a dictionary of direction string keys and a value of the direction list. We can add the palace
# coordinates as its own list (we have to check with an if statement, since sometimes they won't have palace coordinates
# ). Then, we just go through each list, and we still use the same movement restrictions, and add all the valid moves
# into a moves list. Alright, we need to try that. Once we do this, we have to do it for the cannons, actually we can
# test it before by just removing all the cannons from the alive list so it doesn't search through those units. Actually
# we can test our current code by getting a horse or elephant to block both spots where the general may be and get it
# checkmate like that.

# The code found so many exceptions to our attempt to checkmate, but I think the current board position is a checkmate
# however, the code just keeps repeating, so we need to see why it's stuck in a loop. After that, we need to figure out
# how to get the correct chariot and cannon movements without a to coordinate, using the same method from the other
# classes and not relying on knowing the direction first. Lol, we get the checkmate to work, but our pieces were
# disappearing. Turns out we put back the from piece, but we also need to put back the to piece that we put back into
# the alive pieces list. We're not sure where the red cannon went, but, the checkmate code did work, so, now we need to
# do it the cannon and chariot valid move lists, but why are we doing this? Bc we want to call is in check from the
# valid move lists function, but the is in check function calls the valid move lists function, so this is actually
# circular logic. The is in check calls valid moves, valid moves calls is in check, and they just keep doing that, so
# that's not gonna work.

# What do we really need to work on right now? Actually, we do need to get the valid moves without a direction, bc we
# can't add the cannon and chariot valid moves right now, since there is no direction. We want them to go to all their
# possible moves. Ok, so we got the lists in their fine, now how are we going to parse through each move list? Let's
# look at how we did it in valid chariot moves. Hmm, we need a way to add all the relevant values in each list, but we
# can't do it as it currently is, because once we call return, the function ends. We can put each key in a separate
# variable, then we have to create a function for that return statement, which will return the list, which we will add
# to the greater list. Wow that was some tricky dictionary manipulation, but I think we got it.

# Let's test it the valid moves created by the new get chariot moves function on several coordinates and make sure they
# that all the values are right, then copy that red chariot code into blue chariot and maybe the cannons as well,
# bc they all have the same possible moves. We can rename the get chariot moves to something better, and we also need
# to break the get valid cannon moves function into a smaller function. After we redo these functions, test the
# checkmate function again with all the pieces alive now to make sure it still works, then see if we can't figure out
# how to incorporate the preventing general from being in check on every move into the is in check function.

# We had a thought in the shower, I think we've solved the is in check problem. So the move results in check funtion,
# we usually always want to call an is in check call again, but... its the is in check from the move results in check
# function, so we want to call move results in check first to see if their general is in check, then we want to call
# it again for the current player to make sure that after the move their general isn't in check. Obviously we want to
# call it anymore for this iteration, so maybe put a recursion_counter parameter that initializes to None that we can
# change to a number, and the base case is when that number is 0. I think in the case of make move, we only check if the
# move leaves the current player in check, and nothing about the general (at least to validate the move), so we need to
# set the recursion loop at 1 so that it does it the first time then stops (need to decrement recursion loop in function
# as well).

# Lol, our first coordinates didn't show the diagonal coordinates, so we thought there was a bug and put in the print
# statements, but no, there was no valid diagonal moves bc the coordinates were blocked. I like how the code now tells
# us the correct moves, but the code was right and we just don't know the actual coordinates lol. Ok, we noticed that
# our center coordinates for the diagonal are wrong, and that's because its all in one list, and when one is deactivated
# then all is, but what we want for the diagonal is 4 different lists, for each direction, so the center list needs to
# change. Lmao, we're testing the cannon moves now and we think we have the wrong valid moves list, to find that it was
# correct again. We can jump another enemy piece as long as enemy in the way, but we thought the enemy past the first
# enemy was blocked lol. Thank god our perception was wrong and not the code.

# Alright, I think we've m anaged to successfully update all the chariot and cannon valid moves, which took about an hr.
# Now what. Alright, we've updated the filtered move names to a little more clear. Now, let's test the checkmate
# function again, but now we have valid chariot and cannon moves so we don't have to remove them from the alive list.
# Ok, so this checkmate code currently works. Now, we want to implement the move results in check recursion. Let's see
# if we can do it.

# Alright, so now we're talking about the move results in check function. Let's think about what we want make move to
# do when it calls it, and what we want it to do in other cases, if they are different. So, in move results in check
# call in the make move function, we are checking to see if the move results in the current player being in check, so
# we just call it normally, and it doesn't need to recur. Alright, how do we set that up, if we're gonna have a
# recursion counter loop parameter? Well, set the parameter to None in the parameter, then we just change it to whatever
# we want when we call make move, which should be 1 to do it just once. So the move results in check always calls itself
# by default. Alright, let's code this. Hmmm.. as we were coding it, we realized that we just need to call is in check
# again, is in check doesn't call itself, so this should be fine. Alright, so how do we test this move results in check
# function? We need to put the generals in a spot where one move puts one general in check, then another spot where one
# move puts the opponent's general in check but leaves the moving player's general in check, which shouldn't be valid.
# I'm thinking that we just call the is in check in the make move function, and not the move results in check, and then
# we don't have need any recursion.

# Ok, let's first think about what we want our functions to do before we do more coding. So, for the make move function
# we want to simulate the move, then check if the simulated move leaves the moving player in check, and we've already
# gotten this code I think, I think it works fine as is. I think the issue is, the checkmate code right, and similarly
# the looking for check code. So, in the make move function, at the end of the function, after we make the move for
# real, we want to check if the opponent is checkmated. So, we first get all the valid moves for their general, then see
# if each result in check. Ok, so this is where we're at right now. We see if each results in check, then if they don't
# we return False out of the function. To clarify, we check if each move results in not a check, and if so, then we
# return False because the general is not checkmated. So what we want to add, is an additional check here. So not only
# does the general need to not be checked. I thinkwe ahve this logic backwards? We wnat to check if they are checkmated,
# right but we do that by making sure all the moves lead to checks, so not only does it need to lead to not a check to
# make it return that checkmate is False. Ok, let's go through this again. So, we're checking each valid move of the
# unit to check whether it leaves the general in check or not. So we want to target the moves that don't leave the
# general in check, and make sure that they don't leave the general in check? What? We are already checking to see if
# the general is in check after each move, so we don't need to check if the move leaves the general in check right? Yeah
# I don't think we need to validate these moves, because they are already validated. Let's test the code as is and see
# what we find. We still need a spot where moving a piece puts the opponent's general in check, and one where moving it
# puts the ohter general in check but the mover's general in check as well, which should be an illegal move. Lol, so we
# thought we had a checkmate situation when the red general is backed up to e1, but not really, because the red guards
# that guard him can go into that spot to block. Let's see if we can't replace guards with cannons.

# Ok, yeah, that worked. I think we are done? Lol. Let's submit to gradescope and see they find any errors.