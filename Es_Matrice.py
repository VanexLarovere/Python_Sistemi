import networkx as nx
import matplotlib.pyplot as plt

def dizionario(matrice):       
    #nr = len([x for x in matrice if x != '\t'])
    nr = len(matrice)
    dizR = {i = [] for i in range(nr)}
    for i in range(nr):
        for j in range(nr):
            if matrice[i][j] == 1: #Chiedere perché è uguale a 1
                dizR[i].append(j)
    print(dizR)

def drawGraph(graph):
    G = nx.Graph(graph)

    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, font_color='black', font_family='Arial')
    plt.show()

def prettyPrint(matrice, separatore=' '):
    for riga in matrice:
        rigaStr = [str(x) for x in riga]
        print(separatore.join(rigaStr))

def createGraphFromMatrix(matriceAdiacenza):
    graph = {}
    nNodi = len(matriceAdiacenza)

    for i in range(nNodi):
        graph[i] = [j for j, valore in enumerate(matriceAdiacenza[i]) if valore == 1]

    return graph

def main():

    matriceAdiacenza = [
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]

    dizionario(matriceAdiacenza)

    prettyPrint(matriceAdiacenza)

    d = createGraphFromMatrix(matriceAdiacenza)
    print("\nGrafo creato:")
    print(d)

    # Disegna il grafo creato
    drawGraph(d)

if _name_ == '_main_':
    main()

#DEFINIRE UNA MAPPA PER IL ROBOT