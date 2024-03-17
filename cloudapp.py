# from flask import Flask, render_template, request
# import numpy as np
# import joblib
# import pandas as pd
# import requests

# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return render_template('/index.html')
# def fun(x):
#     l=[]
#     l.append(float(np.sqrt(float(x[0]))))
#     l.append(float(np.sqrt(float(x[1]))))
#     l.append(x[2])
#     l+=x[3:]
#     payload_scoring = {"input_data": [{"fields": ['ApplicantIncome', 'LoanAmount', 'Married', 'Property_Area_Rural',
#         'Property_Area_Semiurban', 'Property_Area_Urban'], "values": [l]}]}

#     response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/42868dda-29fd-40a3-b666-1e9cbc93a0fc/predictions?version=2021-05-01', json=payload_scoring,
#     headers={'Authorization': 'Bearer ' + mltoken})
#     response_scoring=response_scoring.json()
#     print(response_scoring)
#     return response_scoring['predictions'][0]['values'][0][0]
 
# @app.route('/form', methods=['GET','POST'])
# def form():
#     if request.method == 'POST':
#         id = request.form['id'].strip()
#         name=request.form['name'].strip()
#         gender=request.form['gender'].strip()
#         married=request.form['married'].strip()
#         dependents=request.form['dependents'].strip()
#         education=request.form['education'].strip()
#         semployed=request.form['semployed'].strip()
#         aincome=request.form['aincome'].strip()
#         coincome=request.form['coincome'].strip()
#         lamount=request.form['lamount'].strip()
#         lterm=request.form['lterm'].strip()
#         chistory=request.form['chistory'].strip()
#         parea=request.form['parea'].strip()
#         print(id,name,gender,married,dependents,education,semployed,aincome,coincome,lamount,lterm,chistory,parea)
#         if id=='':
#             return '<script>alert("Please Enter a Valid Loan ID"); window.history.back();</script>'
#         elif name=='':
#             return '<script>alert("Please Enter a Valid Name"); window.history.back();</script>'
#         elif gender=='':
#             return '<script>alert("Please Choose Your Gender"); window.history.back();</script>'
#         elif married=='':
#             return '<script>alert("Please Choose Your Marrital Status"); window.history.back();</script>'
#         elif dependents=='':
#             return '<script>alert("Please Enter Valid Dependents"); window.history.back();</script>'
#         elif education=='':
#             return '<script>alert("Please Choose Your Education Status"); window.history.back();</script>'
#         elif semployed=='':
#             return '<script>alert("Please Choose Your Employment Status"); window.history.back();</script>'
#         elif aincome=='':
#             return '<script>alert("Please Enter valid Applicant Income"); window.history.back();</script>'
#         elif coincome=='':
#             return '<script>alert("Please Enter Valid CoApplicant Income"); window.history.back();</script>'
#         elif lamount=='':
#             return '<script>alert("Please Enter a Valid Loan Amount"); window.history.back();</script>'
#         elif lterm=='':
#             return '<script>alert("Please Enter a Valid Loan Term"); window.history.back();</script>'
#         elif chistory=='':
#             return '<script>alert("Please Choose Your Credit History"); window.history.back();</script>'
#         elif parea=='':
#             return '<script>alert("Please Choose Your Property Area"); window.history.back();</script>'
#         else:
#             married=int(married)
#             r=int(parea=='rural')
#             s=int(parea=='semiurban')
#             u=int(parea=='urban')
#             l=[aincome,lamount,married,r,s,u]
#             x=fun(l)
#             return result(x,id,name) 
#     else:
#         return render_template('/form.html')


# @app.route('/result')
# def result(x,id,name):
#     return render_template('result.html',x=x,id=id,name=name.capitalize())



# def cloud(d):
    
#     API_KEY = "H703QcOr25HijiCBL9fBNE2DNM01Q0H2KA4-qdpQayjk"
#     token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
#     API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
#     mltoken = token_response.json()["access_token"]

#     header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    
#     payload_scoring = {"input_data": [{"fields": ['ApplicantIncome', 'LoanAmount', 'Married', 'Property_Area_Rural',
#         'Property_Area_Semiurban', 'Property_Area_Urban'], "values": [d]}]}

#     response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/42868dda-29fd-40a3-b666-1e9cbc93a0fc/predictions?version=2021-05-01', json=payload_scoring,
#     headers={'Authorization': 'Bearer ' + mltoken})
#     print("Scoring response")
#     response_scoring=response_scoring.json()
#     print(response_scoring)
#     print(response_scoring['predictions'][0]['values'][0][0])
# if __name__ == '__main__':
#     API_KEY = "H703QcOr25HijiCBL9fBNE2DNM01Q0H2KA4-qdpQayjk"
#     token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
#     API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
#     mltoken = token_response.json()["access_token"]

#     header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    
    
    
#     app.run(debug=True)
