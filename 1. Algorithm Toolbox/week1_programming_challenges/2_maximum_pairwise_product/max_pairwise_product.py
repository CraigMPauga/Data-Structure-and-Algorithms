# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    maxindex1 = -1
    maxindex2 = -1
    max_product = 0
    for i in range(n):
        if maxindex1 == -1 or numbers[maxindex1] < numbers[i]:
            maxindex1 = i
    for j in range(n):
        if ((j != maxindex1) and ((maxindex2 == -1) or (numbers[j] > numbers[maxindex2]))):
            maxindex2 = j

    max_product = numbers[maxindex1] * numbers[maxindex2]    

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
