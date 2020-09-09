import pandas as pd


def getValidMask(y):
    return y["core_hours"] % 40 != 0


x = pd.read_csv("data/emod3d_test_x.csv")
y = pd.read_csv("data/emod3d_test_yexact.csv")
valid_mask = getValidMask(y)

x["core_hours"] = y["core_hours"]
valid_mask = getValidMask(y)
x_reduced = x.loc[valid_mask]
print(f"Original shape: {x.shape} after taking out suspicious rows: {x_reduced.shape}.")
