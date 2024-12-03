import re

MULTIPLE_REGEX = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
DO_REGEX = re.compile(r"do\(\)")
DONT_REGEX = re.compile(r"don't\(\)")


def main():
    with open("input.txt") as f:
        content = f.read()

    matches = MULTIPLE_REGEX.findall(content)
    total = sum(int(x) * int(y) for x, y in matches)

    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", content)

    enabled = True
    total_enabled = 0

    for instr in instructions:
        if DO_REGEX.match(instr):
            enabled = True
            
        elif DONT_REGEX.match(instr):
            enabled = False
        elif MULTIPLE_REGEX.match(instr) and enabled:
            x, y = MULTIPLE_REGEX.match(instr).groups()
            total_enabled += int(x) * int(y)

    print(total, total_enabled)
    return total, total_enabled


if __name__ == '__main__':
    main()
