import re
class ready():
    def com(self,a,b):
        if a==b:
            return str(1)
        elif a>b:
            l=a//b
            rzi=a-b*l
            if rzi==0:
                flag=0
            else:
                flag=1
            return str(l)+' '+(str(rzi)+'/'+str(b))*flag
        else:
            return str(a)+'/'+str(b)
## 控制输出
    def MPR(self,u,v):
        k=0
        while 1 :
            if u % 2 !=0 or v % 2 !=0:
                break
            else:
                u=u/2
                v=v/2
                k+=1



        if v>u:
            u,v=v,u
        while 1 :
            if u==v:
                break
            m=u-v
            u=max([m,v])
            v=min([m,v])

            

        return int(v*2**k)

## 计算最大公因数，为化简做准备
        
    def __init__(self,text):
        result=re.findall(r'(\d+)/(\d+)',text)
        if result != []:
            need=list(result[0])
            self.zi=int(need[0])
            self.mu=int(need[1])
        else:
            self.zi=int(text)
            self.mu=1
    
## 将字符串转化成分子和分母（整数）


class fra(ready):
    def __init__(self,fraction):
        super().__init__(fraction)

    def __add__(self,f1):
        if self.mu==f1.mu:
            return [self.zi+f1.zi,self.mu]
        else:
            return [(self.zi)*f1.mu+f1.zi*self.mu,self.mu*f1.mu]
## +
    def __sub__(self,f2):
        if self.mu==f2.mu:
            return [self.zi-f2.zi,self.mu]
        else:
            return [(self.zi)*f2.mu-f2.zi*self.mu,self.mu*f2.mu]
## -
    def __mul__(self,f3):
        return [self.zi*f3.zi,self.mu*f3.mu]
## *
    def __truediv__(self,f4):
        return [self.zi*f4.mu,self.mu*f4.zi]
## /04

a=input('输入第一个分数：\n')
b=input('输入第二个分数：\n')
uu=fra(a)
uu1=fra(b)
uu2=uu*uu1
gg=fra(a).MPR(uu2[0],uu2[1])
#print(str(uu2[0]/gg)+'/'+str(uu2[1]/gg))
result=fra(a).com(int(uu2[0]/gg),int(uu2[1]/gg))
print(' ')
print('结果是')
print(result)

