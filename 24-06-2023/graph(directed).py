class graph:
    def __init__(self,no_of_node,directed=True):
        self.m_no_of_node=no_of_node
        self.m_node=range(self.m_no_of_node)
        self.m_direct=directed
        self.adjlist={node:set() for node in self.m_node}
    def addedge(self,node1,node2,weight=1):
        self.adjlist[node1].add((node2,weight))
        if not self.m_direct:
            self.adjlist[node2].add((node1,weight)) 
    def printadjlist(self):
        for key in self.adjlist.keys():
            print("node",key,":",self.adjlist[key])
g=graph(5)
g.addedge(0,0,25)
g.addedge(0,1,5)
g.addedge(0,2,3)
g.addedge(1,3,1)
g.addedge(1,4,15)
g.addedge(4,3,11)
g.addedge(4,2,7)
g.printadjlist()