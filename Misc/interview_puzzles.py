#not finished, 2 lazy to tbh, i did them in person okay!!!
class Cup:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filled = 0

    def pour(self, source=None):
        amount = self.filled
        self.filled = 0
        return amount

    def fill(self, amount=None):
        if not amount:
            self.filled = self.capacity
        else:
            self.filled += amount
            if self.filled > self.capacity:
                self.filled = self.capacity

small = Cup(3)
large = Cup(5)

def print_total(*cups):
    total = 0
    fills = [cup.filled for cup in cups]
    print(fills, f'| {sum(fills)}')

small.fill()
large.fill(small.pour())
small.fill()
print_total(small, large)


def compute_clock_angle(time):
    pieces = time.split(":")
    if len(pieces) < 2:
        print("Must be a real time!")
    else:
        try:
            hour = int(pieces[0])
            minutes = int(pieces[1])
            if 23 >= hour >= 0 and 59 >= minutes >= 0:
                hour = hour % 12
            else:
                print("Invalid time!")
                return


            print(hour, minutes)
        except ValueError:
            print("Error! Must be a real time!")


compute_clock_angle("23:00")

if __name__ == '__main__':
    pass












