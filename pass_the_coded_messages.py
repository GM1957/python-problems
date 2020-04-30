l = [3,1,4,1,5,9]
k = 0
def convert(list): 
    res = str(''.join(map(str, list))) 
    return res 

def check(k):
    if(k%3==0):
        return 1
    else:
        return 0   

l.sort(reverse = True)
newl = convert(l)
final_list =[]

if (check(int(newl))==1):
    print(int(newl))

if(check(int(newl))==0):
       temp = list(newl)
       i = 0
       while(i<len(l)):
           victim = temp.pop(i)
           tempu = convert(temp)
           if(check(int(tempu))==1):
               final_list.append(tempu)
           else:
               for j in range(len(temp)):
                   if(int(victim)==temp[j]):
                       temp.pop(j)
                       tempu_to = convert(temp)
                       if(check(int(tempu_to))==1):
                           final_list.append(tempu_to)
           temp = list(newl)
           i = i+1
       final_list.sort(reverse=True)
       print(final_list[0])
