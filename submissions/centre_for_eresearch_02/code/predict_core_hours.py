# This script acts a command line interface to make predictions from the model
from joblib import load
import argparse

parser = argparse.ArgumentParser(description='Predict core hours')
parser.add_argument('--nt', type=int, help='Number of timesteps', required=True)
parser.add_argument('--nx', type=int, help='X dimension', required=True)
parser.add_argument('--ny', type=int, help='Y dimension', required=True)
parser.add_argument('--nz', type=int, help='Z dimension', required=True)
parser.add_argument('--n_sub', type=float, help='Sub faults', required=True)
parser.add_argument('--n_cores', type=int, help='Number of cores', required=True)

args = parser.parse_args()
model = load("model")
x = [[args.nt, args.nx, args.ny, args.nz, args.n_sub, args.n_cores]]
pred = model.predict(x, quantile=92)[0]
print(f"The model predicts this job would take about {pred:.4f} core hours")
