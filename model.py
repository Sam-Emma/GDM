import pandas as pd
import pickle
import numpy as np
print("pass")
def load_model():
    model = pickle.load(open("model.sav", 'rb'))
    return model

def validation(age,bmi,miscarriage,n_pregnancy):
    empty_spaces = 0
    error = 0
    if(age == "" or bmi == "" or miscarriage == "" or n_pregnancy == "" ):
        empty_spaces = empty_spaces + 1
    elif int(age) < 13 or int(age) > 70:
        error = error + 1
    elif float(bmi) < 12.0 or float(bmi) > 80.0:
        error = error + 1
    elif int(miscarriage) < 0 or int(miscarriage) > 6:
        error = error + 1
    elif int(n_pregnancy) < 0 or int(n_pregnancy) > 20:
        error = error + 1
    
    return error, empty_spaces
    
    

def predict(age,bmi,miscarriage,n_pregnancy):
    error, empty_spaces = validation(age,bmi,miscarriage,n_pregnancy)
    print(error," " ,empty_spaces)
    if empty_spaces > 0:
        predict_real = 'empty'
        FPG = 'empty'
    elif error > 0:
        predict_real = 'invalid'
        FPG = 'invalid'  
    else:
        X_dataframe = pd.DataFrame([{'AGE':int(age), 'BMI':float(bmi), 'Miscariage Before 6 month':int(miscarriage),
                                      'Number of Pregnancy':int(n_pregnancy)}])        
        predict_real, FPG = makePrediction(X_dataframe)
        FPG = np.round(FPG[0],2)
    return predict_real, FPG

def makePrediction(test_pre):
    classifier = load_model()
    predict_real = ""
    FPG = classifier.predict(test_pre)
    if FPG >= 5.10:
        predict_real = "Positive"
    else:
        predict_real = "Negative"
        
    return predict_real, FPG

#print(predict('34',	'64.062500',	'0.0',	'2.0'))
