from flask import Flask, render_template, request
import numpy as np
import joblib
import pandas as pd
import requests

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('/index.html')
def fun(x):
    l=[]
    l.append(float(np.sqrt(float(x[0]))))
    l.append(float(np.sqrt(float(x[1]))))
    l.append(x[2])
    l+=x[3:]
    d = pd.DataFrame([l], columns=['ApplicantIncome', 'LoanAmount', 'Married', 'Property_Area_Rural', 'Property_Area_Semiurban', 'Property_Area_Urban'])
    return m.predict(d)[0]

# def myfun():
#     df=pd.read_csv('static/train.csv')
#     df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
#     df['Married'].fillna(df['Married'].mode()[0],inplace=True)
#     df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
#     df['Self_Employed'].fillna(df['Self_Employed'].mode()[0],inplace=True)
#     df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
#     df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
#     df['LoanAmount'].fillna(df['LoanAmount'].mean(),inplace=True)
#     df = df.drop(['Loan_ID'], axis = 1)
#     df = pd.get_dummies(df)
#     df = df.drop(['Gender_Female', 'Married_No', 'Education_Not Graduate',
#                 'Self_Employed_No', 'Loan_Status_N'], axis = 1)
#     new = {'Gender_Male': 'Gender', 'Married_Yes': 'Married',
#         'Education_Graduate': 'Education', 'Self_Employed_Yes': 'Self_Employed',
#         'Loan_Status_Y': 'Loan_Status'}

#     df.rename(columns=new, inplace=True)
#     print(df.head())
    
#     ddf=df['Loan_Status']
#     df.ApplicantIncome = np.sqrt(df.ApplicantIncome)
#     df.CoapplicantIncome = np.sqrt(df.CoapplicantIncome)
#     df.LoanAmount = np.sqrt(df.LoanAmount)
#     df=df[['ApplicantIncome', 'LoanAmount', 'Married', 'Property_Area_Rural',
#        'Property_Area_Semiurban', 'Property_Area_Urban']]
#     print(df.head())
#     res=[]
#     for i in range(len(df)):
#         d = pd.DataFrame([df.iloc[i]], columns=['ApplicantIncome', 'LoanAmount', 'Married', 'Property_Area_Rural', 'Property_Area_Semiurban', 'Property_Area_Urban'])
#         res.append(m.predict(d)[0])
#     c=0
#     for i,j in zip(ddf,res):
#         if i==j:
#             c+=1
#     print(len(ddf),len(res),c)



@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        id = request.form['id'].strip()
        name=request.form['name'].strip()
        gender=request.form['gender'].strip()
        married=request.form['married'].strip()
        dependents=request.form['dependents'].strip()
        education=request.form['education'].strip()
        semployed=request.form['semployed'].strip()
        aincome=request.form['aincome'].strip()
        coincome=request.form['coincome'].strip()
        lamount=request.form['lamount'].strip()
        lterm=request.form['lterm'].strip()
        chistory=request.form['chistory'].strip()
        parea=request.form['parea'].strip()
        print(id,name,gender,married,dependents,education,semployed,aincome,coincome,lamount,lterm,chistory,parea)
        if id=='':
            return '<script>alert("Please Enter a Valid Loan ID"); window.history.back();</script>'
        elif name=='':
            return '<script>alert("Please Enter a Valid Name"); window.history.back();</script>'
        elif gender=='':
            return '<script>alert("Please Choose Your Gender"); window.history.back();</script>'
        elif married=='':
            return '<script>alert("Please Choose Your Marrital Status"); window.history.back();</script>'
        elif dependents=='':
            return '<script>alert("Please Enter Valid Dependents"); window.history.back();</script>'
        elif education=='':
            return '<script>alert("Please Choose Your Education Status"); window.history.back();</script>'
        elif semployed=='':
            return '<script>alert("Please Choose Your Employment Status"); window.history.back();</script>'
        elif aincome=='':
            return '<script>alert("Please Enter valid Applicant Income"); window.history.back();</script>'
        elif coincome=='':
            return '<script>alert("Please Enter Valid CoApplicant Income"); window.history.back();</script>'
        elif lamount=='':
            return '<script>alert("Please Enter a Valid Loan Amount"); window.history.back();</script>'
        elif lterm=='':
            return '<script>alert("Please Enter a Valid Loan Term"); window.history.back();</script>'
        elif chistory=='':
            return '<script>alert("Please Choose Your Credit History"); window.history.back();</script>'
        elif parea=='':
            return '<script>alert("Please Choose Your Property Area"); window.history.back();</script>'
        else:
            married=int(married)
            r=int(parea=='rural')
            s=int(parea=='semiurban')
            u=int(parea=='urban')
            l=[aincome,lamount,married,r,s,u]
            x=fun(l)
            return result(x,id,name) 
    else:
        return render_template('/form.html')


@app.route('/result')
def result(x,id,name):
    return render_template('result.html',x=0,id=id,name=name.capitalize())
if __name__ == '__main__':
    m=joblib.load('mymodel_ensemble.pkl')
    app.run(debug=True)
