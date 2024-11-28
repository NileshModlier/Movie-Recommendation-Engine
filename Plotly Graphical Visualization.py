import plotly.graph_objects as go
from py2neo import Graph

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Delhihouse$34"))

# Execute the Cypher query to get the data
query = "MATCH (m:Movie)-[:SIMILAR_TO]-(rec:Movie) RETURN m.title AS movie, rec.title AS recommendation"
data = graph.run(query).data()
print(data)  # Add this line to see the fetched data
# Extract nodes and edges from the data
nodes = set()
edges = []
for record in data:
    movie = record['movie']
    recommendation = record['recommendation']
    nodes.add(movie)
    nodes.add(recommendation)
    edges.append((movie, recommendation))

# Create a mapping of node names to indices
node_indices = {node: i for i, node in enumerate(nodes)}

# Create edge traces
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=1, color='#888'),
    hoverinfo='none',
    mode='lines'
)

for edge in edges:
    x0, y0 = node_indices[edge[0]], node_indices[edge[0]]
    x1, y1 = node_indices[edge[1]], node_indices[edge[1]]
    edge_trace['x'] += [x0, x1, None]
    edge_trace['y'] += [y0, y1, None]

# Create node traces
node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers+text',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        )
    )
)

for node in nodes:
    x, y = node_indices[node], node_indices[node]
    node_trace['x'] += [x]
    node_trace['y'] += [y]
    node_trace['text'] += [node]

# Create the figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='<br>Movie Recommendations Network',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[dict(
                        text="Visualization of Movie Recommendations",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 )],
                    xaxis=dict(showgrid=False, zeroline=False),
                    yaxis=dict(showgrid=False, zeroline=False))
                )

# Show the figure
fig.show()
