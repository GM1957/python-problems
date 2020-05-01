l = [3, 1, 4, 1, 5, 5, 9,5,5]
def solution(l):
    # Your code here
    #k = 0
    #result=[]
    def convert(l):
        res = str(''.join(map(str,l)))
        return res 

    def check(k):
        if(k%3==0):
            return 1
        if(k%3 != 0):
            return 2

    l.sort(reverse = True)
    newl = str(convert(l))
    final_list =[]

    if (check(int(newl))==1):
        return(int(newl))
  
    if(check(int(newl))==2):
        temp = list(l)
        i = len(l)-1
        while(i>=0):
            victim = temp.pop(i)
            tempu = convert(temp)
            if(check(int(tempu))==1):
                final_list.append(tempu)
                final_list.sort(reverse=True)
                return(int(final_list[0]))  
                
               
            if(check(int(tempu))==2):
                for j in range(len(temp)-1):
                    if(int(victim)==int(temp[j])):
                        temp.pop(j)
                        tempu_to = str(convert(temp))
                        if(check(int(tempu_to))==1):
                            final_list.append(tempu_to)
                            final_list.sort(reverse=True)
                            return(int(final_list[0]))  
                        
            temp = list(l)
            i = i-1
        
    return 0 


print(solution(l))    
