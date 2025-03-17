import random

for _ in range(100):  # Generate 100 random CPF numbers
    # Generate the first 9 digits randomly
    first_nine_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))

    # Calculate the first verification digit
    reverse_counter_1 = 10
    first_digit_result = sum(int(digit) * reverse_counter_1 for digit, reverse_counter_1 in zip(first_nine_digits, range(10, 1, -1)))
    first_digit = (first_digit_result * 10) % 11
    first_digit = first_digit if first_digit <= 9 else 0

    # Calculate the second verification digit
    first_ten_digits = first_nine_digits + str(first_digit)
    reverse_counter_2 = 11
    second_digit_result = sum(int(digit) * reverse_counter_2 for digit, reverse_counter_2 in zip(first_ten_digits, range(11, 1, -1)))
    second_digit = (second_digit_result * 10) % 11
    second_digit = second_digit if second_digit <= 9 else 0

    # Generate final valid CPF
    generated_cpf = f'{first_nine_digits}{first_digit}{second_digit}'

    print(generated_cpf)
