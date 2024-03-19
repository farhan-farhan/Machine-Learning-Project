  
from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
# Load the model in binary mode
# model = pickle.load(open('model1.pkl', 'rb'))
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        # print(type(Credit_History))
        area = request.form['area']
        # loan = request.form['loan']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        
        # Data transformation
        if(gender=="Male"):
            Gender_Male=1
        else:
            Gender_Male =0
        # married
        if(married =="Yes"):
            Married_Yes = 1 
        else:
            Married_Yes = 0
        # dependents
        if(dependents=='1'):
            Dependents_1 =1               
            Dependents_2 =0               
            Dependents_3 =0 
        elif(dependents == '2'):
            Dependents_1 =0               
            Dependents_2 =1               
            Dependents_3 =0 
        elif(dependents=="3+"):
            Dependents_1 =0               
            Dependents_2 =0               
            Dependents_3 =1 
        else:
            Dependents_1 =0               
            Dependents_2 =0               
            Dependents_3 = 0  
        # education
        if (education=="Not Graduate"):
            Education_Not=1
        else:
            Education_Not=0

        # employed
        if (employed == "Yes"):
            Self_Employed_Yes=1
        else:
            Self_Employed_Yes=0

        # property area

        if(area=="Semiurban"):
            Property_Area_Semiurban=1
            Property_Area_Urban=0
        elif(area=="Urban"):
            Property_Area_Semiurban=0
            Property_Area_Urban=1
        else:
            Property_Area_Semiurban=0
            Property_Area_Urban=0
        # # credit
        # if (credit == 1.000000):
        #     Credit_History = 1.000000
        # elif(credit ==0.842199):    
        #     Credit_History=0.842199
        # else:    
        #     Credit_History=0.000000

        ApplicantIncomelog = np.log(ApplicantIncome)
        Total_Income_Log = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmount = np.log(LoanAmount)
        Loan_Amount_Term_Log = np.log(Loan_Amount_Term)
        
# yaha parr to value ja rahi hai to hum name kuch bhee rakh sakte hai
        prediction = model.predict([[credit, ApplicantIncomelog,LoanAmount, Loan_Amount_Term_Log, Total_Income_Log,Gender_Male, Married_Yes,Education_Not,Self_Employed_Yes,Property_Area_Semiurban ,Property_Area_Urban,Dependents_1,Dependents_2,Dependents_3]])

        print(prediction)
        
        if(prediction=="N"):
            prediction="No"
        else:
            prediction="Yes"
        
        return render_template("prediction.html",prediction_text=f"loan stats is  {prediction}")        
        # return render_template("prediction.html",prediction_text= "loan stats is {}".format(prediction))        
        
    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)