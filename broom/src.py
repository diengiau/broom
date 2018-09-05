import pandas as pd

# try write lm() as in R
def lm(formula, data):
    import pandas as pd
    import numpy as np
    import patsy
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    result = smf.ols(formula, data).fit()
    print(result.params)
    return result
    
def tidy(model):
    import pandas as pd
    return pd.DataFrame({'coef'    : model.params,
                         't'       : model.tvalues,
                         'p_value' : model.pvalues
                        })

def glance(model):
    import pandas as pd
    return pd.DataFrame({'obs'        : [model.nobs],
                         'r2'         : [model.rsquared],
                         'ar2'        : [model.rsquared_adj],
                         'f'          : [model.fvalue],
                         'f_pvalue'   : [model.f_pvalue],
                         'df'         : model.df_model,
                         'df_resid'   : model.df_resid,
                         'aic'        : model.aic,
                         'bic'        : model.bic
                         })

def augment_simple(model, new_data = 0):
    import pandas as pd
    if type(new_data) == int:
        dt = {'.fitted' : model.fittedvalues, '.resid'  : model.resid}
    else:
            dt = {'.fitted' : model.predict(new_data)}
    return pd.DataFrame(dt)