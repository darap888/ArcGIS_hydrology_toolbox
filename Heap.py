# -*- coding: cp1250 -*-
# Heap
# Created by Bc. Petr Nov�k, 2015/04
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

'''
Modul "halda.py" se�ad� seznam do haldy s nejv�t��m ��slem na za��tku a 
pomoc� funkce cr_list lze vytvo�it se�azen� seznam hodnot.
'''

# Vytvo�� bin�rn� haldu ze seznamu
def cr_heap (seznam, index=2):
    heap=[]
    for i in seznam:
        inz_el (heap, i, index)
    return heap

# P�id� prvek na konec seznamu a nech� ho prosk�kat haldou
def inz_el (sez, x, index=2):
    sez.append (x)
    # Index vlo�en�ho ��sla
    j = len(sez)   
    while j > 1:
        # Index nahrazen�ho prvku
        p = j / 2  
        # Porovn� vlo�en� prvek a jeho nad�azen� a p��padn� je vym�n�
        if isinstance(sez[p-1],int):
            if sez[j-1] > sez[p-1]: 
                d = sez[j-1]
                sez[j-1] = sez[p-1]
                sez[p-1] = d
                # Posun v hald� na p�edch�dce
                j = p  
            else:                       
                break
        else:
            if sez[j-1][index] > sez[p-1][index]: 
                d = sez[j-1]
                sez[j-1] = sez[p-1]
                sez[p-1] = d 
                # Posun v hald� na p�edch�dce
                j = p  
            else:                       
                break
            
# Odstran� prvek z vrcholu haldy a nahrad� ho dal��m nejvy���m ��slem           
def ret_max (heap, index=2):
    # P�esune posledn� prvek haldy na vrchol
    heap[0] = heap[-1]  
    del heap [-1]       
    # Index posledn�ho ��sla
    j = len(heap)-1     
    # Index porovn�van�ho ��sla
    i = 0               
    # Plat� pro haldu obsahuj�c� v�ce, ne� jedno ��slo
    while j > 0: 
        # Index n�sledn�ka       
        n = 2*(i+1)-1   
        if n<len(heap):
            if isinstance(heap[n] and heap[i],int):
                # Kontrola zda existuj� oba n�sledn�ci
                if n < j:
                    # Vybere ten v�t��
                    if heap [n+1] > heap [n]:
                        n = n+1
                # Je-li ��slo men�� ne� n�sledn�k, tak se vym�n�
                if heap[i] < heap[n]:
                    d = heap[n]
                    heap[n] = heap[i]
                    heap[i] = d
                    # Posun v hald� na n�sledn�ka
                    i = n   
                else:
                    break
            else:
                # Kontrola zda existuj� oba n�sledn�ci
                if n < j:
                    # Vybere ten v�t��
                    if heap [n+1][index] > heap [n][index]:
                        n = n+1
                # Je-li ��slo men�� ne� n�sledn�k, tak se vym�n�
                if heap[i][index] < heap[n][index]:
                    d = heap[n]
                    heap[n] = heap[i]
                    heap[i] = d
                    # Posun v hald� na n�sledn�ka
                    i = n   
                else:
                    break                      
        else:
            break

# Funkce pro vytvo�en� se�azen�ho seznamu z existuj�c� se�azen� haldy
def cr_list (heap):
    ssez = []
    # Je-li v hald� alespo� jedin� polo�ka
    while len (heap)>0:
        # vlo�� nejv�t�� ��slo z haldy na konec seznamu         
        ssez.append (heap[0])   
        # a vr�t� maximum na za��tek haldy
        ret_max (heap)          
    return ssez

