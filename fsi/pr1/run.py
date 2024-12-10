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

print("===============================================================")

oe = search.GPSProblem('O', 'E'
                       , search.romania)

print("Búsqueda en anchura para OE")
print(search.breadth_first_graph_search(oe).path())

print("Búsqueda en profundidad para OE")
print(search.depth_first_graph_search(oe).path())

print("Búsqueda con ramificación y acotación para OE")
print(search.branch_and_bound_search(oe).path())
print("-----------------------------------------------------------------")
print("Búsqueda con ramificación y acotación con subestimación para OE")
print(search.branch_and_boundWS_search(oe).path())


print("===============================================================")

gz = search.GPSProblem('G', 'Z'
                       , search.romania)

print("Búsqueda en anchura para GZ")
print(search.breadth_first_graph_search(gz).path())

print("-----------------------------------------------------------------")

print("Búsqueda en profundidad para GZ")
print(search.depth_first_graph_search(gz).path())

print("-----------------------------------------------------------------")


print("Búsqueda con ramificación y acotación para GZ")
print(search.branch_and_bound_search(gz).path())

print("-----------------------------------------------------------------")

print("Búsqueda con ramificación y acotación con subestimación para GZ")
print(search.branch_and_boundWS_search(gz).path())

print("===============================================================")

nd = search.GPSProblem('N', 'D'
                       , search.romania)

print("Búsqueda en anchura para ND")
print(search.breadth_first_graph_search(nd).path())

print("-----------------------------------------------------------------")

print("Búsqueda en profundidad para ND")
print(search.depth_first_graph_search(nd).path())

print("-----------------------------------------------------------------")

print("Búsqueda con ramificación y acotación para ND")
print(search.branch_and_bound_search(nd).path())

print("-----------------------------------------------------------------")

print("Búsqueda con ramificación y acotación con subestimación para ND")
print(search.branch_and_boundWS_search(nd).path())

print("===============================================================")

mf = search.GPSProblem('M', 'F'
                       , search.romania)

print("Búsqueda en anchura para MF")
print(search.breadth_first_graph_search(mf).path())

print("-----------------------------------------------------------------")

print("Búsqueda en profundidad para MF")
print(search.depth_first_graph_search(mf).path())

print("-----------------------------------------------------------------")


print("Búsqueda con ramificación y acotación para MF")
print(search.branch_and_bound_search(mf).path())

print("-----------------------------------------------------------------")

print("Búsqueda con ramificación y acotación con subestimación para MF")
print(search.branch_and_boundWS_search(mf).path())

print("===============================================================")
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450