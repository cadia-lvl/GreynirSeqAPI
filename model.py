import torch

# Initialize the tagger
device = torch.device("cpu")  # CPU

model_isen = torch.hub.load(
    repo_or_dir="mideind/GreynirSeq:main", 
    skip_validation=True,
    model="transformer-isen", 
    device=device,
    force_reload=False,
    force_download=False,
)
model_isen.eval()


model_enis = torch.hub.load(
    repo_or_dir="mideind/GreynirSeq:main", 
    skip_validation=True,
    model="transformer-enis", 
    device=device,
    force_reload=False,
    force_download=False,
)
model_enis.eval()
