# Search methods

import search #importa el módulo search

ab = search.GPSProblem('A', 'B'
                       , search.romania)#  definiendo un problema de búsqueda desde el punto 'A' al punto 'B'


print("Comienzo")
print("Búsqueda en anchura")
print(search.breadth_first_graph_search(ab).path())

print("----------------------------------------------")

print("Búsqueda en profundidad")
print(search.depth_first_graph_search(ab).path())

print("----------------------------------------------")

print("Búsqueda con ramificación y acotación")
print(search.branch_and_bound_search(ab).path())#Coge el metodo del fichero search y path muestra el camino encontrado

print("----------------------------------------------")

print("Búsqueda con ramificación y acotación con subestimación")
print(search.branch_and_boundWS_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450