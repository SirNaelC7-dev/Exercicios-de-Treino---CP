import math
xum = float(input())
yum = float(input())
xdois = float(input())
ydois = float(input())
subx = xdois - xum 
suby = ydois - yum
potenciax = pow(subx,2)
potenciay = pow(suby,2)
soma=potenciax+potenciay
distancia = math.sqrt(soma)
print('{:.4f}'.format(distancia))






