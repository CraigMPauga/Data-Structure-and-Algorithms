# Uses python3
import sys

def get_change(m):
    count = get_count(m)
    return count

def get_count(m):
    count =0
    while m>0:
        if m>=10:
            m=m-10
            count += 1
        elif m>4 and m<10:
            m=m-5
            count +=1
        else:
            m=m-1
            count+=1

    return count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
