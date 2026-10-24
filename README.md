# Credit Risk Scorecard

A model that estimates which borrowers are likely to fall **90+ days behind on a payment within two years**. This is the kind of scorecard banks use to approve loans, set credit limits, and monitor risk.

Built on the Kaggle *Give Me Some Credit* dataset (150,000 borrowers, about 6.7% default rate).

**Status:** Part 1 of 4 complete. Part 2 due **November 14, 2026**.

---

## Approach

Every data-cleaning decision in this project is traced to evidence in the data and written down: what the output shows, why it happens, and what decision it forces. Nothing is imputed or capped just because that is the usual default. The goal is documentation that a model reviewer could audit.

## Findings so far (Notebook 01)

- **Missing income and zero income are different groups of borrowers.** They behave differently against the default rate, so they are kept as separate signals instead of being filled with an average.
- **The extreme DebtRatio values come from the rows with missing income.** When income is missing, the ratio stops being a ratio. The fix targets the cause instead of just clipping the outliers.
- **The past-due columns contain 96/98 placeholder codes, not real counts.** They appear together in the same rows, so they are treated as one data-recording issue.
- **Risk is U-shaped across the number of real-estate loans.** Both borrowers with none and borrowers with many default more than those in the middle, which a straight-line assumption would miss.

## Roadmap

| Part | Notebook | Status |
|---|---|---|
| 1 | Exploratory analysis and data-treatment decisions: `notebooks/01_eda.ipynb` | Complete |
| 2 | Train/test split, reusable preprocessing, binning, Weight of Evidence and Information Value (which variables separate good and bad borrowers) | Due Nov 14, 2026 |
| 3 | Logistic regression scorecard, points scaling, validation (Gini/KS), and a cutoff strategy table showing approval rate vs. bad rate at each score | Due Dec 5, 2026 |
| 4 | Monitoring: Population Stability Index (is the model still valid on new applicants?) | Due Jan 9, 2027 |

## Known limitations

- The dataset has no application dates, so a true out-of-time validation is not possible. Part 3 uses a stratified random split, which likely overstates performance compared with a time-based holdout.
- For the same reason, the monitoring in Part 4 runs on a simulated population shift, not real future applicants.

## How to run

1. Download `cs-training.csv` from the [Kaggle Give Me Some Credit competition](https://www.kaggle.com/c/GiveMeSomeCredit/data) and place it in the `data/` folder. The data is not included in this repo.
2. Install the requirements: `pip install -r requirements.txt`
3. Open `notebooks/01_eda.ipynb` and run all cells.