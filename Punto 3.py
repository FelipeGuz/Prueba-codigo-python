#-*-coding: utf-8-*-
#Punto 3 A)
def pos_ori():
    print (u"Ingrese la posición en el eje 'X' de KAREL:")
    px= int(input())
    print (u"Ingrese la posición en el eje 'Y' de KAREL:")
    py= int(input())
    print (u"Ingrese la orientación de KAREL:")
    o= raw_input()
    print u"Las cordenadas iniciales de KAREL son (%d,%d), y su orientación es \
%r" %(px,py,o)

#Punto 3 B)
#Para que funcione toca llamar a la función:
arriba=u'arriba'
abajo=u'abajo'
derecha=u'derecha'
izquierda=u'izquierda'

def karel_f(posicionx,posiciony,orientacion,\
         posicionxfinal,posicionyfinal,orientacionfinal):
    px=posicionx
    py=posiciony
    o=str(orientacion)
    pxf=posicionxfinal
    pyf=posicionyfinal
    of=str(orientacionfinal)
    
    turnright=u'turnleft; turnleft; turnleft;'

    mov_x=u'move;'*(abs(pxf-px))
    mov_y=u'move;'*(abs(pyf-py))
    
    if px>=pxf:
        ori2=u'izquierda'
        if o==u'derecha' or o==u'Derecha' or o==u'DERECHA':
            ori=u'turnleft; turnleft;'
        if o==u'arriba':
            ori=u'turnleft;'
        if o==u'abajo':
            ori=turnright
        if o==u'izquierda':
            ori=ori2
    if px<=pxf:
        ori2=u'derecha'
        if o==u'izquierda':
            ori=u'turnleft; turnleft;'
        if o==u'arriba':
            ori=turnright
        if o==u'abajo':
            ori=u'turnleft;'
        if o==u'derecha':
            ori=''
    if py>=pyf:
        ori3=u'abajo'
        if ori2==u'izquierda':
            ori_m='turnleft;'
        if ori2==u'derecha':
            ori_m=turnright
        if of==u'arriba':
            ori_f=u'turnleft; turnleft;'
        if of==u'derecha':
            ori_f=u'turnleft;'
        if of==u'izquierda':
            ori_f=turnright
        if of==u'abajo':
            ori_f=''
    if py<=pyf:
        ori3=u'arriba'
        if ori2==u'izquierda':
            ori_m=turnright
        if ori2=='derecha':
            ori_m='turnleft;'
        if of==u'derecha':
            ori_f=turnrigth
        if of==u'abajo':
            ori_f=u'turnleft; turnleft;'
        if of==u'izquierda':
            ori_f=u'turnleft;'
        if of==u'arriba':
            ori_f=''
    string=u'''
BEGINNING-OF-PROGRAM\n    BEGINNING-OF-EXECUTION\n        %s\n        \
%s\n        %s\n        %s\n        %s\n        turnoff\n    \
END-OF-EXECUTION\nEND-OF-PROGRAM\n
''' %(ori,mov_x,ori_m,mov_y,ori_f)

    print string
    
    

#Punto 3 C)
#Para que funcione toca llamar a la función 'karel()':
    
def karel():
    #Elementos ingresados por el usuario.
    print (u"Ingrese la posición inicial en el eje 'X' de KAREL:")
    px= int(input())
    print (u"Ingrese la posición inicial en el eje 'Y' de KAREL:")
    py= int(input())
    print (u"Ingrese la orientación inicial de KAREL (arriba,abajo,derecha,\
izquierda):")
    o= raw_input()
    print (u"Ingrese la posición final en el eje 'X' de KAREL:")
    pxf= int(input())
    print (u"Ingrese la posición final en el eje 'Y' de KAREL:")
    pyf= int(input())
    print (u"Ingrese la orientación final de KAREL (arriba,abajo,derecha,\
izquierda):")
    of= raw_input()

    turnright=u'turnleft; turnleft; turnleft;'

    #Movimiento de KAREL, cordenada final menos la inicial. 
    mov_x=u'move;'*(abs(pxf-px))
    mov_y=u'move;'*(abs(pyf-py))

    #Orientación de KAREL.
    if px>=pxf:
        ori2=u'izquierda'
        if o==u'derecha':
            ori=u'turnleft; turnleft;'
        if o==u'arriba':
            ori=u'turnleft;'
        if o==u'abajo':
            ori=turnright
        if o==u'izquierda':
            ori=''
    if px<=pxf:
        ori2=u'derecha'
        if o==u'izquierda':
            ori=u'turnleft; turnleft;'
        if o==u'arriba':
            ori=turnright
        if o==u'abajo':
            ori=u'turnleft;'
        if o==u'derecha':
            ori=''
    if py>=pyf:
        ori3=u'abajo'
        if ori2==u'izquierda':
            ori_m='turnleft;'
        if ori2==u'derecha':
            ori_m=turnright
        if of==u'arriba':
            ori_f=u'turnleft; turnleft;'
        if of==u'derecha':
            ori_f=u'turnleft;'
        if of==u'izquierda':
            ori_f=turnright
        if of==u'abajo':
            ori_f=''
    if py<=pyf:
        ori3=u'arriba'
        if ori2==u'izquierda':
            ori_m=turnright
        if ori2=='derecha':
            ori_m='turnleft;'
        if of==u'derecha':
            ori_f=turnright
        if of==u'abajo':
            ori_f=u'turnleft; turnleft;'
        if of==u'izquierda':
            ori_f=u'turnleft;'
        if of==u'arriba':
            ori_f=''
    string=u'''
BEGINNING-OF-PROGRAM\n    BEGINNING-OF-EXECUTION\n        %s\n        \
%s\n        %s\n        %s\n        %s\n        turnoff\n    \
END-OF-EXECUTION\nEND-OF-PROGRAM\n
''' %(ori,mov_x,ori_m,mov_y,ori_f)
            
    print '%s' %string
    
    
    
def Prueba(numero):
    numero = 0
    fot i in range(5):
        numero = i +numero
        print numero
        
          
    


        









    
        
        
    
