import math # импортируем матемтику
from math import pi, sqrt, sin, cos, tan, radians #импортируем изменения из библотеки
print("Ввидите радиус круга в см")#принтим текст
a=(input())#ввод радиуса
r=int(a)#перевод значения радиуса
b=2*pi*r#формула длина окружности
c=pi*r*r#формула площади круга 
d=r*2**0.5#формула нахождения вписанного квадрата
e=r*3**0.5#формула вписанного треугольника
f=2*r#формула описанного квадрата
j=r*2*3**0.5#формула описанного треугольника
h=2*r*tan(radians(22.5))#формулаописанного восьмиугольника
k=b/100
g=c/100
print("Длина окружности",b,"см",k,"м")#вывод
print("Площадь круга",c,"см",g,"м")#вывод
print("Сторона вписанного квадрата",d,"") #вывод
print("Сторона равностороннего треугольника",e,"")#вывод
print("Сторона описанного квадрата",f,"")#вывод
print("Сторона описанного треугольника",j,"")#вывод
print("Сторона описанного восьмиугольника",h,"")#вывод
