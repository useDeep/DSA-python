# def singleNumber(nums) -> int:
#     nums.sort()
#     for i in nums:
#         x= i
#         nums.remove(i)
#         mid= len(nums)//2

#         if (nums[mid]== i):
#             nums.remove[i]
#             nums.remove[i]

#         elif(nums[mid]> i):
#             nums= nums[0: mid]
#             singleNumber(nums)
#         elif(nums[mid]< i):
#             nums= nums[mid: len(nums)]
#             singleNumber(nums)
#         else:
#             return x


# nums= [30000,500,100,30000,100,30000,100]
# singleNumber(nums)

class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

a1= A()
a1.feature1()
a1.feature2()
b1= B()
b1.feature1()
