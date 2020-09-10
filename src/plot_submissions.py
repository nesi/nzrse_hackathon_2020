#!/usr/bin/env python3

from pathlib import Path
from matplotlib import pylab
import defopt
import pandas as pd
import numpy as np


def quantile_loss(y_actual, y_predict):
    """
    Cost function to minimise
    - y_actual: the actual number of core hours consumed by the simulation (array-like)
    - y_predict: the model's prediction (array-like of same length as above)
    - returns positive number, the lower the better
    """
    quantile = 0.9
    errors = np.maximum(
        (y_actual - y_predict) * quantile, (y_predict - y_actual) * (1.0 - quantile)
    )
    return np.mean(errors)


DEFAULT_TEST_FILE = Path(__file__).parent / ".." / "data" / "emod3d_test_yexact.csv"


def main(
    submissions_folder: Path,
    *,
    target_file: Path = DEFAULT_TEST_FILE,
):
    """Compute scores for each submission and rank them

    :param submissions_folder: folder containing hackathon submisssions
    :param results_file: .csv file containing final scores
    :param target_file: .csv file containing target observations
    """

    y_actual = pd.read_csv(target_file)
    mask = (y_actual.core_hours > 0) & ((y_actual.core_hours % 40) != 0)

    print(
        f"Excluding {len(y_actual[~mask])} obervations with 0 or multiple of "
        "40 core-hours."
    )

    submissions = [p for p in submissions_folder.iterdir() if p.is_dir()]
    scores = {}

    legends = []
    for team_folder in submissions:
        try:
            y_predict = pd.read_csv(team_folder / "emod3d_test_y.csv")
        except FileNotFoundError:
            print(f"Warning: no file emod3d_test_y.csv under {team_folder}!")
            continue

        pylab.plot(y_predict, y_actual, 'x')
        legends.append(team_folder)

    pylab.legend(legends, loc='lower right')
    pylab.plot(y_actual, y_actual, 'k--')
    legends.append('exact')
    pylab.xlim([0, 1200])
    pylab.show()


if __name__ == "__main__":
    defopt.run(main)
