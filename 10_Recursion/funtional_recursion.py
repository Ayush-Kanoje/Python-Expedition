# Funtional Recursion: Means funtion return something instead of printing


# Q. Return SUM of N natural no

# def sumfun(sum,i,n):
#     if i > n:
#         print(sum)
#         return

#     sumfun(sum+i,i+1,n)


def sumfun(num):
    if num == 1:
        return 1

    return num+sumfun(num-1)

x = sumfun(10)

print(x)