from architectures import Director

if __name__ == "__main__":
    director = Director()
    gcn_spec = {
                "in_dim": 512,
                "hidden_dims": [1024,2048],
                "out_dim": 512,
                "bias": True
                }
    mlp_spec = {
                "in_dim": 512,
                "hidden_dims": [],
                "out_dim": 8,
                "bias": True
                }
    # Simple Architectures
    #arch_gcn = director.construct_gcn(blueprint=gcn_spec)
    #arch_mlp = director.construct_mlp(blueprint=mlp_spec)



    # Two-component Architectures
    arch_gcn_mlp = director.construct_gcn_with_head(blueprint_gcn=gcn_spec,blueprint_mlp=mlp_spec)
    #arch_mlp_gcn = director.construct_gcn_preproject(blueprint_gcn=gcn_spec,blueprint_mlp=mlp_spec)

    # Print architectures
    #print(repr(arch_gcn))
    #print(repr(arch_mlp))
    print(repr(arch_gcn_mlp))
    print(arch_gcn_mlp)
    #print(repr(arch_mlp_gcn))