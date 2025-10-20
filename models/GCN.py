import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):
    def __init__(self, in_dim: int, hidden_dims: list[int], out_dim: int, bias: bool = True):
        super().__init__()
        
        widths = [in_dim] + list(hidden_dims) + [out_dim]

        self.convs = nn.ModuleList([
            GCNConv(widths[i], widths[i + 1], bias=bias)
            for i in range(len(widths) - 1)
        ])

    def forward(self, x: torch.Tensor, edge_index: torch.Tensor, edge_weight: torch.Tensor | None = None):
        for i, conv in enumerate(self.convs):
            x = conv(x, edge_index, edge_weight)
            if i < len(self.convs) - 1:  # ReLU after all but last layer
                x = F.relu(x)
        return x