def read(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [float(line.strip()) for line in lines]


def cal_total(filename):
    nums = read(filename)
    return sum(nums)
