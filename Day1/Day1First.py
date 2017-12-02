class DigitSummer:
    def sum_digits(self, digits):
        digits_as_string = str(digits)

        sum = 0

        for current_index in range(len(digits_as_string)):
            first_index = 0

            if current_index == len(digits_as_string) - 1:
                next_index = first_index
            else:
                next_index = current_index + 1

            if digits_as_string[current_index] == digits_as_string[next_index]:
                sum += int(digits_as_string[current_index])

        return sum
