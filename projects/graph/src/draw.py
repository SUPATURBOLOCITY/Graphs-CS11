import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, Label, ColumnDataSource

from graph import Graph

def setup_plot():
                                                    # TODO: Magic Numbers
    plot = figure(title='Graph Layout Demonstration', x_range=(0,10), y_range=(0,10), 
                tools='', toolbar_location=None)
    plot.axis.visible=False
    plot.grid.visible=False

    return plot

def setup_graph_renderer(graph):
    N = len(graph.vertices)
    node_indices = list(range(N))

    graph_renderer = GraphRenderer()

    graph_renderer.node_renderer.data_source.add(node_indices, 'index')
    graph_renderer.node_renderer.data_source.add(['blue'] * N, 'color')
    # TODO: change to circle                  # TODO: Magic Numbers
    graph_renderer.node_renderer.glyph = Circle(size=35, fill_color='color')

    graph_renderer.edge_renderer.data_source.data = get_edge_indexes(graph)

    x = [v.pos['x'] for v in graph.vertices]
    y = [v.pos['y'] for v in graph.vertices]

    graph_layout = dict(zip(node_indices, zip(x, y)))
    graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

    return graph_renderer

def get_edge_indexes(graph):
    start_indices = []
    end_indices = []

    for start_index, vertex in enumerate(graph.vertices):
        for e in vertex.edges:
            start_indices.append(start_index)
            end_indices.append(graph.vertices.index(e.destination))

    return dict(start=start_indices, end=end_indices)

def setup_labels(graph):
    # add the labels
    labelSource = ColumnDataSource(data=dict(
                                    x=[pos['x'] for pos in graph.get_positions()],
                                    y=[pos['y'] for pos in graph.get_positions()],
                                    names=graph.get_names()))

    # TODO:  Label styles
    labels = LabelSet(x='x', y='y', text='names', level='glyph',
                text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

    return labels

def main():
    graph = Graph()

    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')

    plot = setup_plot()

    plot.renderers.append(setup_graph_renderer(graph))

    plot.add_layout(setup_labels(graph))

    output_file('../graph.html')
    show(plot)


if __name__ == "__main__":
    main()