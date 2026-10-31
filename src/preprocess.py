import numpy as np

def drop_invalid_rows(df):
    """Drop records that cannot be a real applicant (the age = 0 row)."""
    return df.drop(df[df['age'] < 18].index)




def preprocess(df):
    """Apply the notebook 01 treatments. Returns a new DataFrame."""
    out = df.copy()
    out.loc[out['RevolvingUtilizationOfUnsecuredLines'] > 10, 'RevolvingUtilizationOfUnsecuredLines'] = np.nan
    income_unknown = (out['MonthlyIncome'].isna()) | (out['MonthlyIncome'] == 0)
    out.loc[income_unknown, 'DebtRatio'] = np.nan
    return out
