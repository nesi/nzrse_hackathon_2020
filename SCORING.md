# Scoring submissions


## Submissions folder

For each team, put their submission (code archive and `emod3d_test_y.csv`) in a
folder named according to the team, in `submissions` folder.


## Run scoring script

Install the dependencies in a virtual environment, using pip:
```
pip install -r requirements.txt
```

Run the [score_submissions.py](src/score_submissions.py) script on the folder
containing the submissions:
```
python src/score_submissions.py submissions/ final_scores.csv
```
where `final_scores.csv` will contain the final results, sorted in ascending
order (best first).

Use the `--help` flag to see the options of the script.

## Plot results

```
python src/plot_submissions.py submissions/
```


## Notes

Target observations with 0 core-hours or a multiple of 40 are excluded.
