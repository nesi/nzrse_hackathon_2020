# NZ Research Software Engineer Hackathon 2020


In this machine learning hackathon, New Zealand eScience Infrastructure (NeSI) is proud to partner with the New Zealand Centre for Earthquake Resilience (QuakeCoRE). QuakeCoRE is conducting large-scale, computationally intensive numerical ground motion simulations on NeSI supercomputers to assess earthquake risks around New Zealand. These low frequency ground motion simulations can take between a few compute core hours to thousands of core hours to complete. Having a good estimate for the required number of core hours before a simulation is launched is critical.

Of particular concern to QuakeCoRE and NeSI, some simulations may have a predicted number of core hours that falls short of the actual number of core hours. When this happens, the job will hit the time limit and fail. A significant number of core hours are thus wasted due to aborted jobs. Resubmitting a job also increases the time jobs spend waiting in the queue and has an adverse effect on QuakeCoRE's research productivity. 

## Goal

In this challenge, participating teams/individuals will develop a model to predict the number of core hours required to run a particular ground motion simulation given a number of features (problem size, number of parallel processes, domain decomposition, etc...). Since underestimating the core hour requirements of a job will result in the job failing, your predictions should ideally be a little higher than the actual number of core hours clocked by the job. [Click here to find out how the winner will be selected](#how-nesi-will-select-the-winner).

NeSI is looking for submissions which:

 1. are open-source (please include an open source license with your code submission, see [here](https://choosealicense.com/))
 2. the code must be written in either Julia, Python or R.
 3. the results must be reproducible -- running multiple times the same model returns the same result
 4. the code must be self-contained with exception of external dependencies (tools, libraries, modules)
 
NeSI may decide to share your contribution to other participants once the deadline of this hackathon has passed.


## The challenge

The data can be accessed at https://github.com/nesi/nzrse_hackathon_2020. [Click here to find out how to download the data](#Downloading-the-training-and-test-data).

In the [`data`](data) folder, you will find three CSV files:

  * [`emod3d_train_x.csv`](data/emod3d_train_x.csv) contains the input features (`nt`, `nx`, `ny`, `nz`, `n_sub` and `n_cores`) for training your model,
  * [`emod3d_train_y.csv`](data/emod3d_train_y.csv) contains the actual (target) core hours (`core_hours`) your model should be able to predict,
  * [`emod3d_test_x.csv`](data/emod3d_test_x.csv) contains data for testing the accuracy of your model.

Apply your model to [`data/emod3d_test_x.csv`](data/emod3d_test_x.csv) and save the result in a file named `emod3d_test_y.csv`. This file should have the same format as [`emod3d_train_y.csv`](data/emod3d_train_y.csv), i.e. it should contain a single column `core_hours`. 


## How to submit

Send an email to training@nesi.org.nz to let organisers know that your submission is ready. Your email should have `hackathon 2020` as subject and contain the following body:

```
Your team name: YOUR_TEAM_NAME
Your team email: YOUR_TEAM_EMAIL
```
(Fields YOUR_TEAM_NAME and YOUR_TEAM_EMAIL should be filled in.)

In addition, you will need to attach two files:

 * `emod3d_test_y.csv`,
 * an archive (tar.gz or zip) of your code.
 
**The hackathon starts 2020-09-03 at 15:00 NZST and the deadline for submission is 2020-09-08 at 15:00 NZST**

## How NeSI will select the winner

The winning solution will return the lowest loss for the `emod3d_test_y.csv` data. A *quantile loss function* set for the 90th percentile will be used to choose the best solution. In Python, this loss function can be written as:

```python
import numpy as np
def quantile_loss(y_actual, y_predict):
    """
    Cost function to minimise
    - y_actual: the actual number of core hours consumed by the simulation (array-like)
    - y_predict: the model's prediction (array-like of same length as above)
    - returns positive number, the lower the better
    """
    quantile = 0.9
    errors = np.maximum((y_actual - y_predict) * quantile, (y_predict - y_actual) * (1.0 - quantile))
    return np.mean(errors)
```

## Downloading the training and test data

This can be done in two ways:
  1. By cloning the repository: `git clone https://github.com/nesi/nzrse_hackathon_2020`, the data files are under the `data` directory. This method is recommended if you have `git` installed.
  2. By pointing your web browser `https://github.com/nesi/nzrse_hackathon_2020/blob/master/data/emod3d_train_x.csv` (for instance). Click on "Raw" to get the URL of the file. Then you could:
     * Use `wget`, `curl` or similar tools to fetch the file using this URL
     * Right click or go to file menu in the browser and "save as"

## Frequently asked questions

 * Can I submit multiple solutions? 
   - Yes. You can submit up to 10 solutions. You will need to send one email for each submission to training@nesi.org.nz. [See how to submit here](#how-to-submit)

 * If I submit multiple solutions, which one will be chosen? 
   - NeSI will select the solution that returns the smallest loss among all submissions

 * How and when will NeSI announce the winner?
   - NeSI will notify the winner by email, using the team email address provided in the submission email

 * What if I have a question during the hackathon?
   - Please share your questions in the #nesi_hackathon_open slack channel (https://nesi.slack.com/archives/C019EJ8V85S).  All registrants should have received an invitation via email to join this channel - if you have not received an invitation please get in touch by emailing training@nesi.org.nz

 * There are entries with zero core hours value in the dataset. Do these correspond to failed jobs?
   - Yes
  
 * Some core hour counts are below one hour. Could it be that these are failed jobs? 
   - A simulation with a small number of core hours (e.g. 0.3) likely indicates a "simple" simulation, probably a small magnitude earthquake with a relatively small domain

 * What are the meanings of nt, nx,  ny, nz, n_sub?
   - nx, ny and nz represent the number of grid points in each direction of the domain (the finite difference simulation has a uniform grid),
nt is the number of time steps and n_sub is the number of sub faults used to represent the earthquake source (a measure of complexity of the fault being simulated)

 * Some core hours are integers. Have these jobs reached the job's time limit?
   - An integer number that is a multiple of the number of cores (40) of a node likely indicates that the wall clock limit was hit

# Hackathon results

We would like to thank all participants for their hard work and for sharing what
their learned during this event.

Submissions have been regrouped in the [`submissions`](submissions) folder, one
per team and per submission:

 * `Centre for eResearch` team (Nick Young) [first submission](submissions/centre_for_eresearch_01/code), [second submission](submissions/centre_for_eresearch_02/code) and [external repository](https://github.com/neon-ninja/nzrse_hackathon_2020),
 * `Cameron Kerr` team [submission](submissions/cameron_kerr/code), [slides](submissions/cameron_kerr/NZRSE_2020_Hackathon.pptx) and [external repository](https://github.com/cameronkerrnz/nzrse_hackathon_2020),
 * `Kristin Wilson` team [submission](submissions/k_wilson/code),
 * `Chris Love Amy` team (Xiaoquan (Chris) Sun) [submission](submissions/chris_love_amy/code),
 * `Pablo Higuera` team [submission](submissions/pablo_higuera/code).

Final scores are available in a [`separate file`](submissions/scores.csv).
