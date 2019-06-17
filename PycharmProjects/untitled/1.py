# code = 'utf- 8'
'''

3
3
helloworld
acbde
hdlrowolle
2
helloworld
worldhello
2
abcde
acbde
'''



# a,b = s.strip().split(',')
t = int(input().strip())
for _ in range(t):

    n = int(input().strip())
    s1 = input().strip()
    s2_list = []
    for j in range(n-1):
        s2 = input().strip()
        s2_list.append(s2)
    i = 0
    list2 = []
    while i <= len(s1):
        list1 = list(s1)
        temp = list1.pop(0)
        list1.append(temp)
        list2 = list1[::-1]
        temp_s1 = "".join(list1)
        temp_s2 = "".join(list2)
        s1 = temp_s1
        if temp_s1 in s2_list or temp_s2 in s2_list:
            print('Yeah')
            break
        else:
            i = i+1
            if i == len(s1):
                print('sad')
                break
            continue



