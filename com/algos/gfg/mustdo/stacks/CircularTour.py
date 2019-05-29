'''
Problem statement:
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.

Your task is to complete the function tour() which returns an integer denoting the first point from where a truck will '
be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity).

Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.
'''


def tour(lis, n):

    start_station, left_over_petrol, deficit = 0, 0, 0
    for i in range(n):
        left_over_petrol += lis[i][0] - lis[i][1]

        if left_over_petrol < 0:
            start_station = i + 1
            deficit += left_over_petrol
            left_over_petrol = 0

    return start_station if deficit + left_over_petrol > 0 else -1


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        stations = int(input())
        arr=list(map(int, input().strip().split()))
        lis = []
        for i in range(1, 2 * stations, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(tour(lis, stations))
