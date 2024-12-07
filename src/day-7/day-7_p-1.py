def read_input(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    equations = []
    for line in lines:
        target, numbers = line.strip().split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))
    return equations


def evaluate_with_pruning(numbers, target, current_value, index): # recursion
    if index == len(numbers):
        return current_value == target

    # Stop exploring if the current value exceeds the target
    if current_value > target:
        return False # careful if ones exist since adding can result in bigger then multiplying
                     # but it seems theres no cases where it happens.

    if evaluate_with_pruning(numbers, target, current_value + numbers[index], index + 1):
        return True

    if evaluate_with_pruning(numbers, target, current_value * numbers[index], index + 1):
        return True

    return False


def evaluate_equation(target, numbers):
    return evaluate_with_pruning(numbers, target, numbers[0], 1)


def calculate_total_calibration_result(equations):
    total_calibration_result = 0

    for target, numbers in equations:
        if evaluate_equation(target, numbers):
            total_calibration_result += target

    return total_calibration_result


input_file = "src\day-7\input.txt"
equations = read_input(input_file)
result = calculate_total_calibration_result(equations)
print(result)
