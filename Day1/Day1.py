class DigitSummer:
    def __init__(self):
        self.__first_index = 0
        self.__current_index = 0
        self.__last_index = 0
        self.__number_of_digits = 0

    def sum_digits(self, digits, challenge_part):
        digits_as_string = str(digits)

        sum = 0

        self.__number_of_digits = len(digits_as_string)
        self.__last_index = self.__number_of_digits - 1

        for self.__current_index in range(self.__last_index + 1):
            next_index = self.get_next_index(challenge_part)

            if digits_as_string[self.__current_index] == digits_as_string[next_index]:
                sum += int(digits_as_string[self.__current_index])

        return sum

    def get_next_index(self, challenge_part):
        if challenge_part == 1:
            if self.__current_index == self.__last_index:
                return self.__first_index
            else:
                return self.__current_index + 1

        if challenge_part == 2:
            comparison_offset = int(self.__number_of_digits / 2)

            potential_next_index = self.__current_index + comparison_offset

            if potential_next_index > self.__last_index:
                # loop around to the front of the array and keep going
                return potential_next_index - self.__number_of_digits
            else:
                return potential_next_index
