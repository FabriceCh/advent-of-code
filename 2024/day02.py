from utils import read_file

# part 1
ar = read_file("2024/input")
# ar = [
#     "7 6 4 2 1",
#     "1 2 7 8 9",
#     "9 7 6 2 1",
#     "1 3 2 4 5",
#     "8 6 4 4 1",
#     "1 3 6 7 9",
# ]

reports = [[int(i) for i in line.split(" ")] for line in ar]


def evaluate_report(report: list) -> tuple[bool, int]:
    is_increasing = True
    if report[0] > report[1]:
        is_increasing = False
    for i in range(len(report) - 1):
        if is_increasing:
            if report[i] > report[i + 1]:
                return False, i + 1
        else:
            if report[i] < report[i + 1]:
                return False, i + 1
        difference = abs(report[i] - report[i + 1])
        if difference > 3 or difference == 0:
            return False, i + 1
    return True, -1


count = 0

for report in reports:
    ans = evaluate_report(report)
    count += ans[0]
print(count)

# part 2
count = 0
for report in reports:
    safe, index = evaluate_report(report)
    if not safe:
        dampened_report = report.copy()
        dampened_report.pop(index)
        safe, _ = evaluate_report(dampened_report)
        if not safe:
            dampened_report = report.copy()
            dampened_report.pop(index - 1)
            safe, _ = evaluate_report(dampened_report)
            if not safe:
                dampened_report = report.copy()
                dampened_report.pop(index - 2)
                safe, _ = evaluate_report(dampened_report)
    count += safe
print(count)
