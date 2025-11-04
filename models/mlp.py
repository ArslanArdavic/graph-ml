import torch
import torch.nn as nn
import torch.nn.functional as F

class MLP(torch.nn.Module):
    def __init__(self, in_dim: int, hidden_dims: list[int], out_dim: int, bias: bool = True):
        super().__init__()
        
        widths = [in_dim] + list(hidden_dims) + [out_dim]

        self.layers = nn.ModuleList([
            nn.Linear(widths[i], widths[i + 1], bias=bias)
            for i in range(len(widths) - 1)
        ])

    def forward(self, x: torch.Tensor):
        for i, lin in enumerate(self.layers):
            x = lin(x)
            if i < len(self.layers) - 1:  # ReLU after all but last layer
                x = F.relu(x)
        return x