from graphviz import Digraph

dot = Digraph()

# Adding nodes
dot.node('Kate', 'Kate Windsor (nacida Middleton)')
dot.node('Guillermo', 'Guillermo de Gales')
dot.node('Carlos', 'Carlos (Windsor) de Gales')
dot.node('Diana', 'Diana de Gales (nacida Spencer)')

# Adding edges
dot.edge('Kate', 'Guillermo', label='casados')
dot.edge('Guillermo', 'Carlos', label='hijo')
dot.edge('Guillermo', 'Diana', label='hijo')

# Render the diagram
dot.render('family_tree', format='png', view=True)