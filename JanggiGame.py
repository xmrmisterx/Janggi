import random
import time


class Piece:
    """
    Represents all the game pieces on the board. Every game piece has private properties for color, type, number, name,
    and coordinates. Has getter functions to access all of these private properties as well, and a setter function to
    set the coordinates.
    """

    def __init__(self, color, type, number_of_underscores, number, coordinates=None):

        """
        Every piece starts off with private properties for the color, type, number, name and coordinates, which are
        equal to their parameter counterparts.
        """

        self._color = color
        self._type = type
        self._number_of_underscores = number_of_underscores
        self._number = number
        self._name = color + type + str(number) + number_of_underscores
        self._coordinates = coordinates

    def __repr__(self):

        """
        Overrides the object's print method to print out its name to better visualize the board.
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
        Returns the resultant coordinate after moving up an up_amount number of spaces from the current coordinate.
        """

        # to move up, we need to subtract one from y-coordinates value

        # get current coordinate

        current_coordinate = self.get_coordinates()

        # get new x coordinate

        x = current_coordinate[0]

        # get new y coordinate

        y = int(current_coordinate[1:]) - up_amount

        # get up_coordinate

        up_coordinate = x + str(y)
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

        # get new y coordinate

        y = int(current_coordinate[1:]) + down_amount

        # get down_coordinate

        down_coordinate = x + str(y)
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

        # get x coordinate

        x = chr(ord(current_coordinate[0]) - left_amount)

        # get left coordinate

        left_coordinate = x + y
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

        # get x coordinate

        x = chr(ord(current_coordinate[0]) + right_amount)

        # get left coordinate

        right_coordinate = x + y
        return right_coordinate

    def move_north_east_coordinates(self, north_east_amount, current_coordinate=None):

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

        # get x coordinate

        x = chr(ord(current_coordinate[0]) + north_east_amount)

        # get northeast coordinate

        north_east_coordinate = x + y
        return north_east_coordinate

    def move_north_west_coordinates(self, north_west_amount, current_coordinate=None):

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

        # get x coordinate

        x = chr(ord(current_coordinate[0]) - north_west_amount)

        # get northwest coordinate

        north_west_coordinate = x + y
        return north_west_coordinate

    def move_south_west_coordinates(self, south_west_amount, current_coordinate=None):

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

        # get x coordinate

        x = chr(ord(current_coordinate[0]) - south_west_amount)

        # get southwest coordinate

        south_west_coordinate = x + y
        return south_west_coordinate

    def move_south_east_coordinates(self, south_east_amount, current_coordinate=None):

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

        # get x coordinate

        x = chr(ord(current_coordinate[0]) + south_east_amount)

        # get southeast coordinate

        south_east_coordinate = x + y
        return south_east_coordinate


class BlueGeneral(Piece):

    """
    Represents a blue general piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):

        """
        Initializes the general piece with private attributes for a blue color, general type, number and coordinates.
        """

        super().__init__("blue", "General", "_", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d8", "d9", "d10", "e8", "e9", "e10", "f8", "f9", "f10"]

        # get current coordinates

        current_coordinate = self.get_coordinates()

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        left_coordinates = self.move_left_coordinates(1)
        right_coordinates = self.move_right_coordinates(1)
        down_coordinates = self.move_down_coordinates(1)
        northeast_coordinates = self.move_north_east_coordinates(1)
        northwest_coordinates = self.move_north_west_coordinates(1)
        southeast_coordinates = self.move_south_east_coordinates(1)
        southwest_coordinates = self.move_south_west_coordinates(1)

        # add moves to "all moves list"

        all_moves_list = [northwest_coordinates, up_coordinates, northeast_coordinates, left_coordinates,
                          current_coordinate, right_coordinates, southwest_coordinates, down_coordinates,
                          southeast_coordinates]

        # filter all moves list to possible moves list if current coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        return possible_moves_list


class RedGeneral(Piece):

    """
    Represents a red general piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):

        """
        Initializes the general piece with private attributes for a red color, general type, number and coordinates.
        """

        super().__init__("red", "General", "__", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]

        # get current coordinates

        current_coordinate = self.get_coordinates()

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        left_coordinates = self.move_left_coordinates(1)
        right_coordinates = self.move_right_coordinates(1)
        down_coordinates = self.move_down_coordinates(1)
        northeast_coordinates = self.move_north_east_coordinates(1)
        northwest_coordinates = self.move_north_west_coordinates(1)
        southeast_coordinates = self.move_south_east_coordinates(1)
        southwest_coordinates = self.move_south_west_coordinates(1)

        # add moves to "all moves list"

        all_moves_list = [northwest_coordinates, up_coordinates, northeast_coordinates, left_coordinates,
                          current_coordinate, right_coordinates, southwest_coordinates, down_coordinates,
                          southeast_coordinates]

        # filter all moves list to possible moves list if current coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        return possible_moves_list


class BlueGuard(Piece):

    """
    Represents a blue guard. Responsibilities and communications are exactly like that of the Piece superclass, except
    it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):

        """
        Initializes a guard piece with a blue color, guard type, number and coordinates.
        """

        super().__init__("blue", "Guard", "___", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d8", "d9", "d10", "e8", "e9", "e10", "f8", "f9", "f10"]

        # get current coordinates

        current_coordinate = self.get_coordinates()

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        left_coordinates = self.move_left_coordinates(1)
        right_coordinates = self.move_right_coordinates(1)
        down_coordinates = self.move_down_coordinates(1)
        northeast_coordinates = self.move_north_east_coordinates(1)
        northwest_coordinates = self.move_north_west_coordinates(1)
        southeast_coordinates = self.move_south_east_coordinates(1)
        southwest_coordinates = self.move_south_west_coordinates(1)

        # add moves to "all moves list"

        all_moves_list = [northwest_coordinates, up_coordinates, northeast_coordinates, left_coordinates,
                          current_coordinate, right_coordinates, southwest_coordinates, down_coordinates,
                          southeast_coordinates]

        # filter all moves list to possible moves list if current coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        return possible_moves_list


class RedGuard(Piece):

    """
    Represents a red guard. Responsibilities and communications are exactly like that of the Piece superclass, except it
    can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):

        """
        Initializes a guard piece with a red color, guard type, number and coordinates.
        """

        super().__init__("red", "Guard", "____", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # create possible moves list and palace coordinates list

        possible_moves_list = []
        palace_coordinates_list = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]

        # get current coordinates

        current_coordinate = self.get_coordinates()

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        left_coordinates = self.move_left_coordinates(1)
        right_coordinates = self.move_right_coordinates(1)
        down_coordinates = self.move_down_coordinates(1)
        northeast_coordinates = self.move_north_east_coordinates(1)
        northwest_coordinates = self.move_north_west_coordinates(1)
        southeast_coordinates = self.move_south_east_coordinates(1)
        southwest_coordinates = self.move_south_west_coordinates(1)

        # add moves to "all moves list"

        all_moves_list = [northwest_coordinates, up_coordinates, northeast_coordinates, left_coordinates,
                          current_coordinate, right_coordinates, southwest_coordinates, down_coordinates,
                          southeast_coordinates]

        # filter all moves list to possible moves list if current coordinate is inside palace

        for coordinate in all_moves_list:
            if coordinate in palace_coordinates_list:
                possible_moves_list.append(coordinate)

        return possible_moves_list


class BlueSoldier(Piece):
    """
    Represents a blue soldier piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a soldier piece with a blue color, soldier type, number and coordinates.
        """

        super().__init__("blue", "Soldier", "_", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        left_coordinates = self.move_left_coordinates(1)
        right_coordinates = self.move_right_coordinates(1)

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

        return possible_moves_list


class RedSoldier(Piece):
    """
    Represents a red soldier piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a soldier piece with a red color, soldier type, number and coordinates.
        """

        super().__init__("red", "Soldier", "__", number, coordinates)

    def get_possible_moves(self):
        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()

        # get directional movement coordinates

        down_coordinates = self.move_down_coordinates(1)
        left_coordinates = self.move_left_coordinates(1)
        right_coordinates = self.move_right_coordinates(1)

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

        return possible_moves_list


class BlueHorse(Piece):

    """
    Represents a blue horse piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a horse piece with a blue color, horse type, number and coordinates.
        """

        super().__init__("blue", "Horse", "___", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_coordinates = self.move_north_west_coordinates(1, up_coordinates)
        up_and_northeast_coordinates = self.move_north_east_coordinates(1, up_coordinates)

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_coordinates = self.move_south_west_coordinates(1, down_coordinates)
        down_and_southeast_coordinates = self.move_south_east_coordinates(1, down_coordinates)

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_coordinates = self.move_south_west_coordinates(1, left_coordinates)
        left_and_northwest_coordinates = self.move_north_west_coordinates(1, left_coordinates)

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_coordinates = self.move_south_east_coordinates(1, right_coordinates)
        right_and_northeast_coordinates = self.move_north_east_coordinates(1, right_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_coordinates, up_and_northeast_coordinates,
                               down_and_southwest_coordinates, down_and_southeast_coordinates,
                               left_and_southwest_coordinates, left_and_northwest_coordinates,
                               right_and_southeast_coordinates, right_and_northeast_coordinates]

        return possible_moves_list


class RedHorse(Piece):

    """
    Represents a red horse piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a horse piece with a red color, horse type, number and coordinates.
        """

        super().__init__("red", "Horse", "____", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_coordinates = self.move_north_west_coordinates(1, up_coordinates)
        up_and_northeast_coordinates = self.move_north_east_coordinates(1, up_coordinates)

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_coordinates = self.move_south_west_coordinates(1, down_coordinates)
        down_and_southeast_coordinates = self.move_south_east_coordinates(1, down_coordinates)

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_coordinates = self.move_south_west_coordinates(1, left_coordinates)
        left_and_northwest_coordinates = self.move_north_west_coordinates(1, left_coordinates)

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_coordinates = self.move_south_east_coordinates(1, right_coordinates)
        right_and_northeast_coordinates = self.move_north_east_coordinates(1, right_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_coordinates, up_and_northeast_coordinates,
                               down_and_southwest_coordinates, down_and_southeast_coordinates,
                               left_and_southwest_coordinates, left_and_northwest_coordinates,
                               right_and_southeast_coordinates, right_and_northeast_coordinates]

        return possible_moves_list


class BlueElephant(Piece):

    """
    Represents a blue elephant piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes an elephant piece with a blue color, elephant type, number and coordinates.
        """

        super().__init__("blue", "Elephant", "", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, up_coordinates)
        up_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, up_coordinates)

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, down_coordinates)
        down_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, down_coordinates)

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, left_coordinates)
        left_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, left_coordinates)

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, right_coordinates)
        right_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, right_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_twice_coordinates, up_and_northeast_twice_coordinates,
                               down_and_southwest_twice_coordinates, down_and_southeast_twice_coordinates,
                               left_and_southwest_twice_coordinates, left_and_northwest_twice_coordinates,
                               right_and_southeast_twice_coordinates, right_and_northeast_twice_coordinates]

        return possible_moves_list


class RedElephant(Piece):

    """
    Represents a red elephant piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes an elephant piece with a red color, elephant type, number and coordinates.
        """

        super().__init__("red", "Elephant", "_", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get directional movement coordinates

        up_coordinates = self.move_up_coordinates(1)
        up_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, up_coordinates)
        up_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, up_coordinates)

        down_coordinates = self.move_down_coordinates(1)
        down_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, down_coordinates)
        down_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, down_coordinates)

        left_coordinates = self.move_left_coordinates(1)
        left_and_southwest_twice_coordinates = self.move_south_west_coordinates(2, left_coordinates)
        left_and_northwest_twice_coordinates = self.move_north_west_coordinates(2, left_coordinates)

        right_coordinates = self.move_right_coordinates(1)
        right_and_southeast_twice_coordinates = self.move_south_east_coordinates(2, right_coordinates)
        right_and_northeast_twice_coordinates = self.move_north_east_coordinates(2, right_coordinates)

        # add moves to possible moves list

        possible_moves_list = [up_and_northwest_twice_coordinates, up_and_northeast_twice_coordinates,
                               down_and_southwest_twice_coordinates, down_and_southeast_twice_coordinates,
                               left_and_southwest_twice_coordinates, left_and_northwest_twice_coordinates,
                               right_and_southeast_twice_coordinates, right_and_northeast_twice_coordinates]

        return possible_moves_list


class BlueChariot(Piece):

    """
    Represents a blue chariot piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a chariot piece with a blue color, chariot type, number and coordinates.
        """

        super().__init__("blue", "Chariot", "_", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()

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

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3 or d10, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3 or f10, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2 or e9, can move northeast, northwest, southeast, or southwest

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

        # if at d1 or d8, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1 or f8, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        return possible_moves_list


class RedChariot(Piece):

    """
    Represents a red chariot piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a chariot piece with a red color, chariot type, number and coordinates.
        """

        super().__init__("red", "Chariot", "__", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()

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

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3 or d10, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3 or f10, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2 or e9, can move northeast, northwest, southeast, or southwest

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

        # if at d1 or d8, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1 or f8, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        return possible_moves_list


class BlueCannon(Piece):

    """
    Represents a blue cannon piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a cannon piece with a blue color, cannon type, number and coordinates.
        """

        super().__init__("blue", "Cannon", "__", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()

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

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3 or d10, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3 or f10, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2 or e9, can move northeast, northwest, southeast, or southwest

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

        # if at d1 or d8, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1 or f8, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        return possible_moves_list


class RedCannon(Piece):

    """
    Represents a red cannon piece. Responsibilities and communications are exactly like that of the Piece superclass,
    except it can calculate its possible moves with the get possible moves function.
    """

    def __init__(self, number, coordinates):
        """
        Initializes a cannon piece with a red color, cannon type, number and coordinates.
        """

        super().__init__("red", "Cannon", "___", number, coordinates)

    def get_possible_moves(self):

        """
        Gets the piece's possible moves from its current_coordinate and returns a list of its possible moves.
        """

        # get current coordinates

        current_coordinate = self.get_coordinates()

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

        # get move up coordinates

        for move_value in range(1, up_spaces + 1):
            up_coordinates = self.move_up_coordinates(move_value)
            up_list.append(up_coordinates)
        move_dictionary["up_list"] = up_list

        # get move left coordinates

        for move_value in range(1, left_spaces + 1):
            left_coordinates = self.move_left_coordinates(move_value)
            left_list.append(left_coordinates)
        move_dictionary["left_list"] = left_list

        # get move right coordinates

        for move_value in range(1, right_spaces + 1):
            right_coordinates = self.move_right_coordinates(move_value)
            right_list.append(right_coordinates)
        move_dictionary["right_list"] = right_list

        # get move down coordinates

        for move_value in range(1, down_spaces + 1):
            down_coordinates = self.move_down_coordinates(move_value)
            down_list.append(down_coordinates)
        move_dictionary["down_list"] = down_list

        # get palace coordinates
        # if at d3 or d10, can move northeast one or two spaces

        if current_coordinate == "d3" or current_coordinate == "d10":
            northeast_coordinates1 = self.move_north_east_coordinates(1)
            northeast_coordinates2 = self.move_north_east_coordinates(2)
            northeast_list = [northeast_coordinates1, northeast_coordinates2]
            move_dictionary["northeast_list"] = northeast_list

        # if at f3 or f10, can move northwest one or two spaces

        elif current_coordinate == "f3" or current_coordinate == "f10":
            northwest_coordinates1 = self.move_north_west_coordinates(1)
            northwest_coordinates2 = self.move_north_west_coordinates(2)
            northwest_list = [northwest_coordinates1, northwest_coordinates2]
            move_dictionary["northwest_list"] = northwest_list

        # if at e2 or e9, can move northeast, northwest, southeast, or southwest

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

        # if at d1 or d8, can move southeast one or two spaces

        elif current_coordinate == "d1" or current_coordinate == "d8":
            southeast_coordinates1 = self.move_south_east_coordinates(1)
            southeast_coordinates2 = self.move_south_east_coordinates(2)
            southeast_list = [southeast_coordinates1, southeast_coordinates2]
            move_dictionary["southeast_list"] = southeast_list

        # if at f1 or f8, can move southwest one or two spaces

        elif current_coordinate == "f1" or current_coordinate == "f8":

            southwest_coordinates1 = self.move_south_west_coordinates(1)
            southwest_coordinates2 = self.move_south_west_coordinates(2)
            southwest_list = [southwest_coordinates1, southwest_coordinates2]
            move_dictionary["southwest_list"] = southwest_list

        possible_moves_list.append(move_dictionary)
        return possible_moves_list


class Player:

    """
    Represents a player in the game. Player class responsibilities include naming each player and has setters to get the
    name
    """

    def __init__(self, name):

        """
        Players have private properties for their name.
        """

        self._name = name

    def get_name(self):

        """
        Returns the player's name, which is also its color.
        """

        return self._name


class JanggiGame:

    """
    Represents the Janggi game. Janggi game class responsibilities include creating the board and players, alternating
    turns between the players, validating and processing moves, managing the game state and looking for a winning board
    position, and managing "in check" status of the players.

    """

    def __init__(self):

        """
        Initializes the game with an unfinished game state, board, pieces, players, coordinate conversion dictionary,
        and an alive pieces list.
        """

        self._game_state = "UNFINISHED"

        self._board = \
            [["    ", "     |a|     ", "     |b|     ", "     |c|     ", "     |d|     ", "     |e|     ", "     |f|     ", "     |g|     ", "     |h|     ", "     |i|     "],
            ["|1| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|2| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|3| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|4| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|5| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|6| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|7| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|8| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|9| ", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"],
            ["|10|", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________", "_____________"]]

        self._coordinate_conversion_dict = {
            "a1": [1, 1],
            "b1": [1, 2],
            "c1": [1, 3],
            "d1": [1, 4],
            "e1": [1, 5],
            "f1": [1, 6],
            "g1": [1, 7],
            "h1": [1, 8],
            "i1": [1, 9],
            "a2": [2, 1],
            "b2": [2, 2],
            "c2": [2, 3],
            "d2": [2, 4],
            "e2": [2, 5],
            "f2": [2, 6],
            "g2": [2, 7],
            "h2": [2, 8],
            "i2": [2, 9],
            "a3": [3, 1],
            "b3": [3, 2],
            "c3": [3, 3],
            "d3": [3, 4],
            "e3": [3, 5],
            "f3": [3, 6],
            "g3": [3, 7],
            "h3": [3, 8],
            "i3": [3, 9],
            "a4": [4, 1],
            "b4": [4, 2],
            "c4": [4, 3],
            "d4": [4, 4],
            "e4": [4, 5],
            "f4": [4, 6],
            "g4": [4, 7],
            "h4": [4, 8],
            "i4": [4, 9],
            "a5": [5, 1],
            "b5": [5, 2],
            "c5": [5, 3],
            "d5": [5, 4],
            "e5": [5, 5],
            "f5": [5, 6],
            "g5": [5, 7],
            "h5": [5, 8],
            "i5": [5, 9],
            "a6": [6, 1],
            "b6": [6, 2],
            "c6": [6, 3],
            "d6": [6, 4],
            "e6": [6, 5],
            "f6": [6, 6],
            "g6": [6, 7],
            "h6": [6, 8],
            "i6": [6, 9],
            "a7": [7, 1],
            "b7": [7, 2],
            "c7": [7, 3],
            "d7": [7, 4],
            "e7": [7, 5],
            "f7": [7, 6],
            "g7": [7, 7],
            "h7": [7, 8],
            "i7": [7, 9],
            "a8": [8, 1],
            "b8": [8, 2],
            "c8": [8, 3],
            "d8": [8, 4],
            "e8": [8, 5],
            "f8": [8, 6],
            "g8": [8, 7],
            "h8": [8, 8],
            "i8": [8, 9],
            "a9": [9, 1],
            "b9": [9, 2],
            "c9": [9, 3],
            "d9": [9, 4],
            "e9": [9, 5],
            "f9": [9, 6],
            "g9": [9, 7],
            "h9": [9, 8],
            "i9": [9, 9],
            "a10": [10, 1],
            "b10": [10, 2],
            "c10": [10, 3],
            "d10": [10, 4],
            "e10": [10, 5],
            "f10": [10, 6],
            "g10": [10, 7],
            "h10": [10, 8],
            "i10": [10, 9],

        }

        # create an alive pieces list

        self._alive_pieces_list = []

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

        # create players and set current player

        self._blue_player = Player("blue")
        self._red_player = Player("red")
        self._current_player = self._blue_player

        # display board

        self.display_board()

    def get_game_state(self):

        """
        Returns the current game state.
        """

        return self._game_state

    def set_game_state(self, game_state):

        """
        Sets the game state equal to the game state in the parameter.
        """

        self._game_state = game_state

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

                # 'end=""' changes the new line of print to an empty space

                print(row, end=" ")

            # 'print()' creates a new line after each row

            print()
        print()

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

        # get the piece's current coordinates

        current_coordinate = piece.get_coordinates()

        # convert current coordinate into actual coordinates

        actual_current_coordinate = self.convert_coordinates(current_coordinate)

        # remove piece from board

        self._board[actual_current_coordinate[0]][actual_current_coordinate[1]] = "_____________"

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

        self._board[actual_current_coordinate[0]][actual_current_coordinate[1]] = "_____________"

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
        Returns True if the horse's orthogonal movement is blocked, and False otherwise.
        """

        # get current coordinates

        current_coordinates = piece.get_coordinates()

        # if moving up

        if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 2:

            up_coordinate = piece.move_up_coordinates(1)

            # if there's a piece at the up coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(up_coordinate) is not None:
                return True

        # if moving down

        elif int(current_coordinates[1:]) - int(target_coordinate[1:]) == -2:

            down_coordinate = piece.move_down_coordinates(1)

            # if there's a piece at the down coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(down_coordinate) is not None:
                return True

        # if moving left

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 2:

            left_coordinate = piece.move_left_coordinates(1)

            # if there's a piece at the left coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(left_coordinate) is not None:
                return True

        # if moving right

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -2:
            right_coordinate = piece.move_right_coordinates(1)

            # if there's a piece at the right coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(right_coordinate) is not None:
                return True

        # none of the horse's orthogonal movement is blocked, so return False

        return False

    def elephant_is_blocked(self, piece, target_coordinate):

        """
        Returns True if the elephant's orthogonal movement is blocked, and False otherwise.
        """

        # get current coordinates

        current_coordinates = piece.get_coordinates()

        # if moving up

        if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 3:

            up_coordinate = piece.move_up_coordinates(1)

            # if there's a piece at the up coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(up_coordinate) is not None:
                return True

            # if there isn't a piece at the up coordinate

            elif self.get_piece_from_coordinate(up_coordinate) is None:

                # check up and northwest coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 2:
                    up_and_northwest_coordinate = piece.move_north_west_coordinates(1, up_coordinate)

                    # if there's a piece at the up and northwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(up_and_northwest_coordinate) is not None:
                        return True

                # check up and northeast coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -2:
                    up_and_northeast_coordinate = piece.move_north_east_coordinates(1, up_coordinate)

                    # if there's a piece at the up and northeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(up_and_northeast_coordinate) is not None:
                        return True

        # if moving down

        elif int(current_coordinates[1:]) - int(target_coordinate[1:]) == -3:

            down_coordinate = piece.move_down_coordinates(1)

            # if there's a piece at the down coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(down_coordinate) is not None:
                return True

            # if there isn't a piece at the down coordinate

            elif self.get_piece_from_coordinate(down_coordinate) is None:

                # check down and southwest coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 2:
                    down_and_southwest_coordinate = piece.move_south_west_coordinates(1, down_coordinate)

                    # if there's a piece at the down and southwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(down_and_southwest_coordinate) is not None:
                        return True

                # check down and southeast coordinate

                if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -2:
                    down_and_southeast_coordinate = piece.move_south_east_coordinates(1, down_coordinate)

                    # if there's a piece at the down and southeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(down_and_southeast_coordinate) is not None:
                        return True

        # if moving left

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == 3:

            left_coordinate = piece.move_left_coordinates(1)

            # if there's a piece at the left coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(left_coordinate) is not None:
                return True

            # if there isn't a piece at the left coordinate

            elif self.get_piece_from_coordinate(left_coordinate) is None:

                # check left and southwest coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == -2:
                    left_and_southwest_coordinate = piece.move_south_west_coordinates(1, left_coordinate)

                    # if there's a piece at the left and southwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(left_and_southwest_coordinate) is not None:
                        return True

                # check left and northwest coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 2:
                    left_and_northwest_coordinate = piece.move_north_west_coordinates(1, left_coordinate)

                    # if there's a piece at the left and northwest coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(left_and_northwest_coordinate) is not None:
                        return True

        # if moving right

        if ord(current_coordinates[0]) - ord(target_coordinate[0]) == -3:
            right_coordinate = piece.move_right_coordinates(1)

            # if there's a piece at the right coordinate, then the move is blocked and return True

            if self.get_piece_from_coordinate(right_coordinate) is not None:
                return True

            # if there isn't a piece at the right coordinate

            elif self.get_piece_from_coordinate(right_coordinate) is None:

                # check right and southeast coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == -2:
                    right_and_southeast_coordinate = piece.move_south_east_coordinates(1, right_coordinate)

                    # if there's a piece at the right and southeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(right_and_southeast_coordinate) is not None:
                        return True

                # check right and northeast coordinate

                if int(current_coordinates[1:]) - int(target_coordinate[1:]) == 2:
                    right_and_northeast_coordinate = piece.move_north_east_coordinates(1, right_coordinate)

                    # if there's a piece at the right and northeast coordinate, then the move is blocked and return True

                    if self.get_piece_from_coordinate(right_and_northeast_coordinate) is not None:
                        return True

        # none of the elephant's orthogonal movement is blocked, so return False

        return False

    def get_valid_chariot_moves(self, chariot_piece, possible_moves_list):

        """
        Returns a valid moves list for the chariot_piece in the parameter from the possible moves list in the parameter.
        """

        # get current coordinate

        current_coordinate = chariot_piece.get_coordinates()

        # create move_dictionary and valid chariot moves list with current coordinate

        valid_chariot_moves_list = [current_coordinate]
        move_dictionary = possible_moves_list[1]

        # for each list in the move dictionary, filter the possibles moves into valid moves

        for key in move_dictionary:
            valid_moves = self.get_filtered_chariot_possible_moves(chariot_piece, move_dictionary[key])

            # for each coordinate in the valid moves list, add to the valid chariot moves list

            for coordinate in valid_moves:
                valid_chariot_moves_list.append(coordinate)

        return valid_chariot_moves_list

    def get_filtered_chariot_possible_moves(self, chariot_piece, move_list):

        """
        Returns a valid move list for the chariot piece in the parameter from the possible moves in the move list in
        the parameter.
        """

        valid_move_list = []

        # for each coordinate in the possible moves list

        for coordinate in move_list:

            # if there's a piece at the coordinate

            piece_at_coordinate = self.get_piece_from_coordinate(coordinate)
            if piece_at_coordinate is not None:

                # if the piece is an enemy piece, then the current coordinate is valid, but the rest of the
                # coordinates are not valid, so return the valid chariot moves list

                if piece_at_coordinate.get_color() != chariot_piece.get_color():
                    valid_move_list.append(coordinate)
                    return valid_move_list

                # if the piece is an ally piece, then the current coordinate and the rest of the coordinates are not
                # valid, so return the valid chariot moves list

                return valid_move_list

            # if there's no piece at the coordinate, then add to valid move list

            if piece_at_coordinate is None:
                valid_move_list.append(coordinate)

        return valid_move_list

    def get_valid_cannon_moves(self, cannon_piece, possible_moves_list):

        """
        Returns a valid moves list for the cannon_piece in the parameter from the possible moves list in the parameter.
        """

        # get current coordinate

        current_coordinate = cannon_piece.get_coordinates()

        # create move dictionary and valid cannon moves list with current coordinate

        valid_cannon_moves_list = [current_coordinate]
        move_dictionary = possible_moves_list[1]

        for key in move_dictionary:

            # filter the possible cannon moves into valid moves

            valid_moves = self.get_filtered_cannon_possible_moves(cannon_piece, move_dictionary[key])

            # for each coordinate in the valid moves, add them to the valid cannon moves list

            for coordinate in valid_moves:
                valid_cannon_moves_list.append(coordinate)

        return valid_cannon_moves_list

    def get_filtered_cannon_possible_moves(self, cannon_piece, move_list):

        """
        Returns a valid move list for the cannon piece in the parameter from the moves in the possible moves
        list in the parameter.
        """

        # set an empty valid move list and a "piece to jump" boolean variable to False

        valid_move_list = []
        piece_to_jump = False

        for coordinate in move_list:

            # if there's a piece at the coordinate

            piece_at_coordinate = self.get_piece_from_coordinate(coordinate)
            if piece_at_coordinate is not None:

                # if the piece is a cannon then don't add the current coordinate, but do return the current valid cannon
                # moves list

                if piece_at_coordinate.get_type() == "Cannon":
                    return valid_move_list

                if piece_to_jump:

                    # if the piece to jump boolean is True and the piece is an enemy piece, add the current coordinate
                    # and return the valid cannon moves list

                    if piece_at_coordinate.get_color() != cannon_piece.get_color():
                        valid_move_list.append(coordinate)
                        return valid_move_list

                    # if the piece to jump boolean is True and the piece is an ally piece, don't add the current
                    # coordinate, then return the valid cannon moves list

                    else:
                        return valid_move_list

                # if the piece to jump boolean is False, then don't add the current coordinate, update the piece to jump
                # to True, and continue to the next coordinate

                elif piece_to_jump is False:
                    piece_to_jump = True

            # if there's no piece at the coordinate and piece to jump is False, then it's not a valid coordinate, so
            # just move on to the next one

            if piece_at_coordinate is None:
                if piece_to_jump:
                    valid_move_list.append(coordinate)

        return valid_move_list

    def coordinate_not_blocked(self, piece, target_coordinate):

        """
        If the target coordinate in the parameter is not blocked by an ally of the piece in the parameter, then return
        True, otherwise return False.
        """

        # get piece's color

        color = piece.get_color()

        # get piece at target coordinate

        piece_at_target = self.get_piece_from_coordinate(target_coordinate)

        # if piece is a horse and the horse is blocked, then return False that the coordinate is blocked

        if piece.get_type() == "Horse":
            if self.horse_is_blocked(piece, target_coordinate):
                return False

        # if piece is an elephant and the elephant is blocked, then return False that the coordinate is blocked

        if piece.get_type() == "Elephant":
            if self.elephant_is_blocked(piece, target_coordinate):
                return False

        if piece_at_target is not None:

            # if the piece at the target coordinate's color equals the current pieces color

            if piece_at_target.get_color() == color:

                # return False that the target coordinate not blocked by an ally
                return False

        # If there is no piece at the target coordinate, or if the piece is an enemy piece, then return True that the
        # coordinate is not blocked

        return True

    def get_valid_moves(self, piece, possible_moves_list):

        """
        Returns a list of valid moves from the possible moves list in the parameter. Checks first to see if the
        coordinate inside the possibles moves list are on the board, then checks whether there is an ally at the
        coordinate.
        """

        # valid move list always starts with the current coordinate

        valid_moves_list = [piece.get_coordinates()]

        # validate moves for chariots differently

        if piece.get_type() == "Chariot":
            return self.get_valid_chariot_moves(piece, possible_moves_list)

        # validate moves for cannons differently

        if piece.get_type() == "Cannon":
            return self.get_valid_cannon_moves(piece, possible_moves_list)

        for coordinate in possible_moves_list:
            if self.coordinate_is_on_board(coordinate):
                if self.coordinate_not_blocked(piece, coordinate):
                    valid_moves_list.append(coordinate)

        return valid_moves_list

    def target_coordinate_in_valid_moves_list(self, valid_moves_list, target_coordinate):

        """
        Returns True if the target coordinate in the parameter is inside the valid moves list in the parameter,
        otherwise returns False.
        """

        # return False if the valid moves list is empty

        if not valid_moves_list:
            return False

        # if the target coordinate is inside the valid moves list, then it's a valid coordinate and return True

        for coordinate in valid_moves_list:
            if coordinate == target_coordinate:
                return True

        # if the target coordinate is not inside the valid moves list, then it's not a valid coordinate and return False

        return False

    def switch_players(self):

        """
        Switch the current player for the other player.
        """

        if self._current_player == self._blue_player:
            self._current_player = self._red_player
        elif self._current_player == self._red_player:
            self._current_player = self._blue_player

    def is_in_check(self, player_name):

        """
        Checks all the possible moves of the opponent of the player with the player_name in the parameter to see if any
        of them puts the player into a "check" status. Returns True if the player is in check, or False otherwise.
        """

        # get player_name's opponent and general's coordinates

        if player_name == "red":
            opponent = self._blue_player
            to_coordinate = self._red_general.get_coordinates()
        elif player_name == "blue":
            opponent = self._red_player
            to_coordinate = self._blue_general.get_coordinates()

        # get all alive pieces of opponent

        for piece in self._alive_pieces_list:

            # if it's an opponent's piece

            if piece.get_color() == opponent.get_name():

                # get piece's valid moves

                possible_moves = piece.get_possible_moves()
                valid_moves = self.get_valid_moves(piece, possible_moves)

                # if the general's coordinates are in the valid moves list, then the general is in check

                if self.target_coordinate_in_valid_moves_list(valid_moves, to_coordinate):
                    return True

        # none of the pieces can check the general, so return False

        return False

    def player_is_checkmated(self, player_name):

        """
        Returns True if the general owned by the player with the player_name in the parameter is checkmated, otherwise
        returns False.
        """

        for piece in self._alive_pieces_list:

            # get all ally pieces

            if piece.get_color() == player_name:

                piece_possible_moves = piece.get_possible_moves()
                piece_valid_moves = self.get_valid_moves(piece, piece_possible_moves)

                for coordinate in piece_valid_moves:

                    # check each piece's valid coordinates to see if every move results in check, if one move doesn't,
                    # then there is no checkmate

                    if not self.move_results_in_check(piece.get_coordinates(), coordinate, player_name):
                        return False

        # all ally valid moves lead to a general check, so return True that the general is checkmated

        return True

    def move_results_in_check(self, from_coordinate, to_coordinate, player_name):

        """
        Returns True if a move from the from coordinate in the parameter to the to coordinate in the parameter results
        in the player with the player name in the parameter having their general in check, otherwise returns False.
        """

        # get the pieces at the to and from coordinates

        to_piece = self.get_piece_from_coordinate(to_coordinate)
        from_piece = self.get_piece_from_coordinate(from_coordinate)

        # if there is a piece at the to coordinate, then capture it, then place the from piece at the to coordinate

        if to_piece is not None:

            # if to piece isn't from piece, so it's not a pass turn

            if to_piece.get_name() != from_piece.get_name():
                self.capture_piece(to_coordinate)

        self.place_piece(from_piece, to_coordinate)

        # call is in check to see if the player's general is in check; if in check, return True, otherwise return False

        if self.is_in_check(player_name):

            # undo the move and capture before leaving function

            self.place_piece(from_piece, from_coordinate)

            if to_piece is not None:
                if to_piece.get_name() != from_piece.get_name():
                    self._alive_pieces_list.append(to_piece)
                    self.place_piece(to_piece, to_coordinate)

            return True

        # undo the move and capture before leaving function

        self.place_piece(from_piece, from_coordinate)

        if to_piece is not None:
            if to_piece.get_name() != from_piece.get_name():
                self._alive_pieces_list.append(to_piece)
                self.place_piece(to_piece, to_coordinate)

        return False

    def declare_winner(self):

        """
        Declares that the current player is the winner and updates the game state to reflect that there is a winner.
        """

        current_player_name = self._current_player.get_name()
        opponent_name = self.get_opponent_of_current_player().get_name()

        if self._current_player.get_name() == "red":
            self.set_game_state("RED_WON")
        elif self._current_player.get_name() == "blue":
            self.set_game_state("BLUE_WON")

        print(opponent_name, "player is checkmated so", current_player_name, "player has won the game!")

    def make_move(self, from_coordinate, to_coordinate):

        """
        Checks to see if a move from the from_coordinate to the to_coordinate is viable. If the piece is owned by the
        current player, if the move is legal, and if the game is not over, then the move is carried out, which captures
        any opponent piece on the to_coordinate and returns True. If the move is invalid, returns False.
        """

        # get from_piece from the from coordinate and to_piece from the to_coordinate

        from_piece = self.get_piece_from_coordinate(from_coordinate)
        to_piece = self.get_piece_from_coordinate(to_coordinate)

        # check if there isn't a piece at the from coordinate

        if from_piece is None:
            print("Move from", from_coordinate, "to", to_coordinate, "failed because there is no game piece at",
                  from_coordinate + ".")
            return False

        # check to see if the from piece is not owned by current player

        number = from_piece.get_number()
        from_piece_name = from_piece.get_color() + from_piece.get_type() + str(number)
        if from_piece.get_color() != self._current_player.get_name():
            print("Move from", from_coordinate, "to", to_coordinate, "failed because", self._current_player.get_name(),
                  "player does not own", from_piece_name + ".")
            return False

        possible_moves = from_piece.get_possible_moves()
        valid_moves = self.get_valid_moves(from_piece, possible_moves)

        # check if target coordinate not in valid moves list

        if not self.target_coordinate_in_valid_moves_list(valid_moves, to_coordinate):
            print("Move from", from_coordinate, "to", to_coordinate, "failed because", from_piece_name, "can't move to",
                  to_coordinate + ".", "Its valid moves are:", ", ".join(valid_moves) + ".")
            return False

        # check if the move leaves the current player's general in check

        if self.move_results_in_check(from_coordinate, to_coordinate, self._current_player.get_name()):
            print("Move from", from_coordinate, "to", to_coordinate, "failed because it leaves",
                  self._current_player.get_name(), "player's general in check.")
            return False

        # check if the game is over

        if self.get_game_state() != "UNFINISHED":
            if game.get_game_state() == "RED_WON":
                print("Move from", from_coordinate, "to", to_coordinate, "failed because the game is already over and "
                                                                         "red player won.")
            elif game.get_game_state() == "BLUE_WON":
                print("Move from", from_coordinate, "to", to_coordinate, "failed because the game is already over and "
                                                                         "blue player won.")
            return False

        # check if there is an opponent's piece at the to_coordinate, and if so, capture it

        if to_piece is not None:
            self.capture_piece(to_coordinate)

        # return True that move was successful

        return True

    def play_game(self):

        """
        Plays the game by creating a game loop that alternates between the 2 players until there is a winner.
        """

        # introduction to game

        print("Welcome to a game of Janggi. You are the blue player and will compete against the red player.")

        # game loops until one player wins

        while game.get_game_state() == "UNFINISHED":

            print("The current player is", self._current_player.get_name() + ".")

            # If player is blue player, then get blue player's move

            if self._current_player.get_name() == "blue":

                # Get coordinates

                from_coordinate = self.ask_for_coordinates("from")
                to_coordinate = self.ask_for_coordinates("to")

                # If the player keeps the piece at the same coordinate, then they passed their turn

                if to_coordinate == from_coordinate:
                    print(self._current_player.get_name(), "player did not make a move and passed their turn.")
                    self.switch_players()
                    continue

                # If the move is successful

                if self.make_move(from_coordinate, to_coordinate):

                    # display move

                    from_piece = self.get_piece_from_coordinate(from_coordinate)
                    number = from_piece.get_number()
                    from_piece_name = from_piece.get_color() + from_piece.get_type() + str(number)
                    print(self._current_player.get_name(), "player moved their", from_piece_name, "from",
                          from_coordinate, "to", to_coordinate + ".")

                    # move piece

                    self.place_piece(from_piece, to_coordinate)
                    self.display_board()

                    # if there is checkmate, end the game

                    opponent_name = self.get_opponent_of_current_player().get_name()
                    if self.player_is_checkmated(opponent_name):
                        self.declare_winner()
                        return

                    # check for check

                    if self.is_in_check(opponent_name):
                        print(opponent_name, "player is in check!")

                    # switch current player

                    self.switch_players()

                # If the move is not successful, then go back to the beginning of the loop and try another move

                else:
                    continue

            # If player is the computer

            elif self._current_player.get_name() == "red":

                # Create some suspense

                print("The computer is thinking...")
                time.sleep(5)

                # Get move values dictionary

                move_values_dictionary = self.get_move_values_dictionary()

                # Initialize random move made boolean to false

                random_move_made = False

                for key in move_values_dictionary:

                    # if a random move was already made, go to the next turn

                    if random_move_made:
                        break

                    valid_moves_list = move_values_dictionary[key]

                    # if the move values list is empty, go on to a lower value moves list

                    if not move_values_dictionary[key]:
                        continue

                    else:

                        # Make move loop

                        while True:

                            # Get a random coordinate from the valid moves list and create the from and to coordinates

                            random_coordinate_list = random.choice(valid_moves_list)

                            from_coordinate = random_coordinate_list[0]
                            to_coordinate = random_coordinate_list[1]

                            # If move is not successful

                            if not self.make_move(from_coordinate, to_coordinate):

                                # remove move from valid moves list

                                valid_moves_list.remove(random_coordinate_list)

                                # if valid moves list is empty, then break out of loop back to picking the next move
                                # values list

                                if not valid_moves_list:
                                    break

                                # if valid moves list not empty, then continue trying other moves

                                else:
                                    continue

                            # If move is successful

                            else:

                                # display move

                                from_piece = self.get_piece_from_coordinate(from_coordinate)
                                number = from_piece.get_number()
                                from_piece_name = from_piece.get_color() + from_piece.get_type() + str(number)
                                print(self._current_player.get_name(), "player moved their", from_piece_name, "from",
                                      from_coordinate, "to", to_coordinate + ".")

                                # move piece

                                self.place_piece(from_piece, to_coordinate)
                                self.display_board()

                                # if there is checkmate, end the game

                                opponent_name = self.get_opponent_of_current_player().get_name()
                                if self.player_is_checkmated(opponent_name):
                                    self.declare_winner()
                                    return

                                # check for check

                                if self.is_in_check(opponent_name):
                                    print(opponent_name, "player is in check!")

                                # switch current player

                                self.switch_players()

                                # update random move made boolean

                                random_move_made = True
                                break

    def ask_for_coordinates(self, to_or_from_string):

        """
        Asks the player for a coordinate until there is a coordinate on the board, then returns that coordinate. The
        "to or from string" parameter determines which question to ask the player.
        """

        # keep asking for coordinates until the break statement is hit

        while True:

            # If the coordinate is the from coordinate, use this string

            if to_or_from_string == "from":
                coordinate = input("Please select the coordinates of the piece you wish to move, with the x coordinate "
                                   "being a letter from a to i and the y coordinate being a number from 1 to 10. \n")

            # If the coordinate is the to coordinate, then use this string

            elif to_or_from_string == "to":
                coordinate = input("Please select the coordinates of where you want to move to, with the x coordinate "
                                   "being a letter from a to i and the y coordinate being a number from 1 to 10. \n")

            # If the coordinate isn't on the board, then go back to selecting a coordinate

            if coordinate not in self._coordinate_conversion_dict:
                print("That is not a valid coordinate.")
                continue

            # If input is valid, then break the while loop

            else:
                break

        # return the valid coordinate

        return coordinate

    def get_move_values_dictionary(self):

        """
        Returns a dictionary of moves for every red piece that is sorted by move value, which ranges from a 1 to a 5. 5
        value moves result in checkmate, 4 value moves result in check, 3 value moves result in capturing a piece, 2
        value moves are moves that don't capture anything, and 1 value moves are moves that pass the turn.
        """

        # start with our move values dictionary

        move_values_dictionary = {
            5: [],
            4: [],
            3: [],
            2: [],
            1: [],
        }

        # get all the red pieces

        alive_red_pieces_list = []
        for piece in self._alive_pieces_list:
            if piece.get_color() == "red":
                alive_red_pieces_list.append(piece)

        # get valid moves for the alive red pieces

        for from_piece in alive_red_pieces_list:
            possible_moves = from_piece.get_possible_moves()
            valid_moves = self.get_valid_moves(from_piece, possible_moves)

            # simulate each valid move

            from_coordinate = from_piece.get_coordinates()
            for to_coordinate in valid_moves:

                to_piece = self.get_piece_from_coordinate(to_coordinate)
                enemy_captured = False

                # if from coordinate and to coordinate are the same, then it's a passed turn and the move value is 1

                if from_coordinate == to_coordinate:

                    # add the coordinates to move values dictionary with a move value of 1 and continue to next
                    # coordinate

                    move_values_dictionary[1].append([from_coordinate, to_coordinate])
                    continue

                # if there is a piece at the to coordinate, then capture it, then place the from piece at the to
                # coordinate

                if to_piece is not None:

                    # if to piece isn't from piece, meaning it's not a passed turn

                    if to_piece.get_name() != from_piece.get_name():

                        # capture enemy and update enemy captured boolean

                        self.capture_piece(to_coordinate)
                        enemy_captured = True

                self.place_piece(from_piece, to_coordinate)

                # if the blue player's general is checkmated then add a move value of 5

                if self.player_is_checkmated("blue"):
                    move_values_dictionary[5].append([from_coordinate, to_coordinate])

                # if the blue player's general is in check

                elif self.is_in_check("blue"):
                    move_values_dictionary[4].append([from_coordinate, to_coordinate])

                # if an enemy was captured then add a move value of 3

                elif enemy_captured:
                    move_values_dictionary[3].append([from_coordinate, to_coordinate])

                # all other moves have a move value of 2

                else:
                    move_values_dictionary[2].append([from_coordinate, to_coordinate])

                # undo the move and capture

                self.place_piece(from_piece, from_coordinate)

                if to_piece is not None:
                    if to_piece.get_name() != from_piece.get_name():
                        self._alive_pieces_list.append(to_piece)
                        self.place_piece(to_piece, to_coordinate)

        return move_values_dictionary


game = JanggiGame()
game.play_game()


