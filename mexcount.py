# #funtion to search the minimum
# def searchmin(arraytest):
#     setarr = set(arraytest)
#     # search for the max to find the min
   
#     for i in range(0, max(arraytest)+2):
#         if (i in setarr):
#             pass
#         else : return i
        

# # first line  test case
# print('how many test case')
# testcase = int(input())
# # testing loop
# for i in range(0, testcase):
#     print('enter array size')
#     arraysize = int(input())
#     print(arraysize)
#     print('enter array number')
#     arraytest = []
#     #adding number to array
#     for j in range(0, arraysize):
#         numb = int(input())
#         arraytest.append(numb) 
#     chkmin = []
#     for k in range(0, arraysize) :
#         min = searchmin(arraytest)
#         arraytest.pop() # deleting one item
#         chkmin.append(min)
#     setmin =set(chkmin)
#     print(f'the number of diferent mex is {len(setmin)}' )
#     print('the value are : ',setmin)
# kapout a refaire