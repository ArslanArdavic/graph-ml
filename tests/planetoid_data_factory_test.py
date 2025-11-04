from data import PlanetoidDataFactory

if __name__ == "__main__":

    data_factory = PlanetoidDataFactory(name="Cora")
    dataset      = data_factory.load_dataset()
    data         = dataset[0]
    # Print information about the dataset
    print(f'Dataset: {dataset}')
    print('---------------')
    print(f'Number of graphs: {len(dataset)}')
    print(f'Number of nodes: {data.x.shape[0]}')
    print(f'Number of features: {dataset.num_features}')
    print(f'Number of classes: {dataset.num_classes}')

    # Print information about the graph
    print(f'\nGraph:')
    print('------')
    print(f"Number of edges: {data.edge_index.size(1)}")
    print(f'Edges are directed: {data.is_directed()}')
    print(f'Graph has isolated nodes: {data.has_isolated_nodes()}')
    print(f'Graph has loops: {data.has_self_loops()}')