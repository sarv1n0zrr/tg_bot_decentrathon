#выращиваем бактерии
# def min_bacteria_count(x):
#     result = 0
#
#     while x > 0:
#         if x % 2 == 1:
#             result += 1
#         x //= 2
#
#     return result
#
# # Taking user input
# x = int(input())
# minimum_bacteria = min_bacteria_count(x)
# print(min_bacteria_count(x))
def function(n, k):
    for i in range(n):
        counter = 0
        m = k + i
        if m == k:
            counter += 1
n = int(input())
k = int(input())
print(function())

