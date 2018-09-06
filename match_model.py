from Match import Match
from train_data import get_train

def match_model(X_test):
    match = Match()
    if not got_train:
        train = get_train()
        global got_train
        got_train = True
        X_train = train[['cpu', 'disk', 'storage']]
        Y_train = train['异常类别'].values
        match.preprocess(X_train, Y_train, X_test)
        return match.prob_fit_pred()[0]
    else:
        X_train = train[['cpu', 'disk', 'storage']]
        Y_train = train['异常类别'].values
        match.preprocess(X_train, Y_train, X_test)
        return match.prob_fit_pred()[0]
