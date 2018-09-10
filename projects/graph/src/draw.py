import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, Label, ColumnDataSource

from graph import Graph


def main():
    graph = Graph()

    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    print(graph.vertices)

    N = len(graph.vertices)
    node_indices = list(graph.vertices)

    plot = figure(title='Graph Layout Demonstration', x_range=(-1,10), y_range=(-1,10),
                  tools='', toolbar_location=None)

    graph_renderer = GraphRenderer()

    graph_renderer.node_renderer.data_source.add(node_indices, 'index')
    graph_renderer.node_renderer.data_source.add(['red'] * N, 'color')
    graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

    start_indices = []
    end_indices = []

    for vertex in graph.vertices:
        for edge in graph.vertices[vertex]:
            start_indices.append(vertex)
            end_indices.append(edge)

    graph_renderer.edge_renderer.data_source.data = dict(
        start=start_indices,
        end=end_indices)


    ### start of layout code
    vertex_values = [v for v in graph.vertices]
    x = [2 * (i // 3) for i in vertex_values]
    y = [2 * (i % 3) for i in vertex_values]

    graph_layout = dict(zip(node_indices, zip(x, y)))
    print (graph_layout)
    graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

    plot.renderers.append(graph_renderer)

    labelSource = ColumnDataSource(data=dict(x=x,y=y,names=vertex_values))

    # TODO:  Label styles
    labels = LabelSet(x='x', y='y', text='names', level='glyph',
                text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

    plot.add_layout(labels)


    output_file('graph.html')
    show(plot)


if __name__ == "__main__":
    main()