'''
Created on 15/02/2018

@author: 

XXX: http://codeforces.com/problemset/problem/913/B
'''

import logging
import sys
from collections import namedtuple
from sys import stdin

nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

class nodot():
    def __init__(self, idx):
        self.idx = idx
        self.es_hoja = False
        self.hijos = []
    def __repr__(self):
        return "{}:{}:{}".format(self.idx, self.es_hoja, list(map(lambda x:x.idx, self.hijos)))

def chriscaca_sputa_es_valido(nodo):
    hijos_hoja_cnt = 0
    if not nodo:
        return True
    hijos_hoja_cnt = len(list(filter(lambda nd:nd.es_hoja, nodo.hijos)))
    
    assert nodo.es_hoja or len(nodo.hijos)
    
    return nodo.es_hoja or hijos_hoja_cnt > 2

def chriscaca_sputa_es_hoja(nodo):
    if nodo:
        nodo.es_hoja = not len(nodo.hijos)
        logger_cagada.debug("q pedo {}".format(nodo))

def chriscaca_sputa_core(lista_adjacencia):
    list(map(chriscaca_sputa_es_hoja, lista_adjacencia))
    logger_cagada.debug("la lista de mierda  a {}".format(lista_adjacencia))
    
    return all(map(lambda nodo:chriscaca_sputa_es_valido(nodo), lista_adjacencia))

def caca_comun_lee_linea_como_num():
    return int(stdin.readline().strip())

def caca_comun_lee_linea_como_monton_de_numeros():
    return list(map(int, stdin.readline().strip().split(" ")))

def chriscaca_sputa_main():
    nodo_cnt = caca_comun_lee_linea_como_num()
    lista_caca = [None]
    for nodo_idx in range(1, nodo_cnt + 1):
        nodon = nodot(nodo_idx)
        lista_caca.append(nodon)
    
    for nodo_idx in range(2, nodo_cnt + 1):
        padre_idx = caca_comun_lee_linea_como_num()
        padre = lista_caca[padre_idx]
        padre.hijos.append(lista_caca[nodo_idx])
    
    logger_cagada.debug("la lista de mierda {}".format(lista_caca))
    
    fuck = chriscaca_sputa_core(lista_caca)
    logger_cagada.debug("puta {}".format(fuck))
    if fuck:
        print("Yes")
    else:
        print("No")
        
        
if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        chriscaca_sputa_main()
