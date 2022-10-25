# -*- coding: cp1250 -*-
# Heap
# Created by Bc. Petr Novák, 2015/04
# Faculty of Environmental Sciences
# Czech University of Life Sciences Prague 

'''
Modul "halda.py" seřadí seznam do haldy s největším číslem na začátku a 
pomocí funkce cr_list lze vytvořit seřazený seznam hodnot.
'''

# Vytvoří binární haldu ze seznamu
def cr_heap (seznam, index=2):
    heap=[]
    for i in seznam:
        inz_el (heap, i, index)
    return heap

# Přidá prvek na konec seznamu a nechá ho proskákat haldou
def inz_el (sez, x, index=2):
    sez.append (x)
    # Index vloženého čísla
    j = len(sez)   
    while j > 1:
        # Index nahrazeného prvku
        p = j / 2  
        # Porovná vložený prvek a jeho nadřazený a případně je vymění
        if isinstance(sez[p-1],int):
            if sez[j-1] > sez[p-1]: 
                d = sez[j-1]
                sez[j-1] = sez[p-1]
                sez[p-1] = d
                # Posun v haldě na předchůdce
                j = p  
            else:                       
                break
        else:
            if sez[j-1][index] > sez[p-1][index]: 
                d = sez[j-1]
                sez[j-1] = sez[p-1]
                sez[p-1] = d 
                # Posun v haldě na předchůdce
                j = p  
            else:                       
                break
            
# Odstraní prvek z vrcholu haldy a nahradí ho dalším nejvyšším číslem           
def ret_max (heap, index=2):
    # Přesune poslední prvek haldy na vrchol
    heap[0] = heap[-1]  
    del heap [-1]       
    # Index posledního čísla
    j = len(heap)-1     
    # Index porovnávaného čísla
    i = 0               
    # Platí pro haldu obsahující více, než jedno číslo
    while j > 0: 
        # Index následníka       
        n = 2*(i+1)-1   
        if n<len(heap):
            if isinstance(heap[n] and heap[i],int):
                # Kontrola zda existují oba následníci
                if n < j:
                    # Vybere ten větší
                    if heap [n+1] > heap [n]:
                        n = n+1
                # Je-li číslo menší než následník, tak se vymění
                if heap[i] < heap[n]:
                    d = heap[n]
                    heap[n] = heap[i]
                    heap[i] = d
                    # Posun v haldě na následníka
                    i = n   
                else:
                    break
            else:
                # Kontrola zda existují oba následníci
                if n < j:
                    # Vybere ten větší
                    if heap [n+1][index] > heap [n][index]:
                        n = n+1
                # Je-li číslo menší než následník, tak se vymění
                if heap[i][index] < heap[n][index]:
                    d = heap[n]
                    heap[n] = heap[i]
                    heap[i] = d
                    # Posun v haldě na následníka
                    i = n   
                else:
                    break                      
        else:
            break

# Funkce pro vytvoření seřazeného seznamu z existující seřazené haldy
def cr_list (heap):
    ssez = []
    # Je-li v haldě alespoň jediná položka
    while len (heap)>0:
        # vloží největší číslo z haldy na konec seznamu         
        ssez.append (heap[0])   
        # a vrátí maximum na začátek haldy
        ret_max (heap)          
    return ssez

