import pandas as pd
import pickle
import numpy as np
print("pass")
def load_model():
    model = pickle.load(open("model.sav", 'rb'))
    return model

def validation(age,sex,weight,height,
              q_pregnancy,
              miscarriage,n_pregnancy,w_pregnancy):
    error = 0
    message = ""
    if(age == "" or  miscarriage == "" or
       n_pregnancy == "" or height == "" or weight == "" ):
        error = 1
        message = "Fill in all the required data"
    elif sex == "male" or sex == "null":
        error = 1
        message = "Only a female can take this test"
    elif q_pregnancy == "no" or q_pregnancy == "null":
        error = 1
        message = "Only pregnant women can take this test"
    elif w_pregnancy == "null":
        error = 1
        message = "Failed to enter the duration of pregnancy"
    elif int(age) < 15 or int(age) > 51:
        error = 1
        message = "Allowed age range is 15 to 51"
    elif float(height) < 0 or float(height) > 5:
        error = 1
        message = "Exceeded acceptable height"
    elif float(weight) < 20 or float(weight) > 100:
        error = 1
        message = "Exceeded acceptable height"
    elif int(miscarriage) < 0 or int(miscarriage) > 6:
        error = 1
        message = "Invalid input"
    elif int(n_pregnancy) < 0 or int(n_pregnancy) > 20:
        error = 1
        message = "Invalid input"
    
    return error, message
    
    

def predict(age,sex,q_pregnancy,
                            height, weight,
                            miscarriage,n_pregnancy,w_pregnancy):
    
    error, message = validation(age,sex,
                                weight,height, q_pregnancy,
                                miscarriage,n_pregnancy, w_pregnancy)
    
    
    predict_real  = ""
    FPG = ""
    bmi =""
    if error != 0:
        predict_real = '-'
        FPG = '-'
    else:
        bmi = float(weight)/(float(height)**2)
        X_dataframe = pd.DataFrame([{'AGE':int(age), 'BMI':float(bmi), 'Miscariage Before 6 month':int(miscarriage),
                                      'Number of Pregnancy':int(n_pregnancy)}])        
        predict_real, FPG = makePrediction(X_dataframe)
        FPG = np.round(FPG[0],2)
        message = 'success'
    return predict_real, FPG, bmi, message

def makePrediction(test_pre):
    classifier = load_model()
    predict_real = ""
    FPG = classifier.predict(test_pre)
    if FPG >= 5.10:
        predict_real = "At risk"
    else:
        predict_real = "Not at risk"
        
    return predict_real, FPG

#print(predict('34',	'64.062500',	'0.0',	'2.0'))
