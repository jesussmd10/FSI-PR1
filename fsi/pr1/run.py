# Search methods

import search
import time


ab = search.GPSProblem('A', 'B'
                       , search.romania)

# Ejecutar y mostrar resultados para cada algoritmo
print("Búsqueda por Amplitud (BFS):")
solution_bfs = search.breadth_first_graph_search(ab)
if solution_bfs:
    print("Ruta:", [node.state for node in solution_bfs.path()])
    print("Costo total:", solution_bfs.path_cost)
else:
    print("No se encontró una solución con BFS.")

print("\nBúsqueda por Profundidad (DFS):")
solution_dfs = search.depth_first_graph_search(ab)
if solution_dfs:
    print("Ruta:", [node.state for node in solution_dfs.path()])
    print("Costo total:", solution_dfs.path_cost)
else:
    print("No se encontró una solución con DFS.")

# Búsqueda por Ramificación y Acotación
print("\nBúsqueda por Ramificación y Acotación (Branch and Bound):")
solution_bb = search.branch_and_bound(ab)
if solution_bb:
    print("Ruta:", [node.state for node in solution_bb.path()])
    print("Costo total:", solution_bb.path_cost)
else:
    print("No se encontró una solución con Branch and Bound.")

# Búsqueda por Ramificación y Acotación con Heurística
print("\nBúsqueda por Ramificación y Acotación con Heurística:")
solution_bb_h = search.branch_and_bound_with_heuristic(ab)
if solution_bb_h:
    print("Ruta:", [node.state for node in solution_bb_h.path()])
    print("Costo total:", solution_bb_h.path_cost)
else:
    print("No se encontró una solución con Branch and Bound con Heurística.")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
