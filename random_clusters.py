import argparse, os
import numpy as np
import anndata as ad

p = argparse.ArgumentParser()
p.add_argument("--output_dir", required=True)
p.add_argument("--name", required=True)
p.add_argument("--data.h5ad", dest="data", required=True)
p.add_argument("--data.clusters_truth_num", dest="k_file", required=True)
p.add_argument("--seed", type=int, default=42)
a = p.parse_args()

adata = ad.read_h5ad(a.data)
k = int(open(a.k_file).read().strip())
rng = np.random.default_rng(a.seed)
labels = rng.integers(0, k, size=adata.n_obs)

os.makedirs(a.output_dir, exist_ok=True)
np.savetxt(os.path.join(a.output_dir, f"{a.name}_clusters.txt"), labels, fmt="%d")
