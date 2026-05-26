list=[1,2,3,4,5,6,7,8,9]


def maximum(nums):
    # print(max(nums))
    maxi=0
    for i in nums:
        if maxi<i:
            maxi=i
    print(maxi)
maximum(list)


# for i in range(0,len(list)):
#     print(list[i])