# save this as app.p
from flask import Flask, render_template,request
import pickle
model =pickle.load(open('xgboost_model.pkl','rb'))

# model = xgb.Booster()
# model.load_model("model.txt")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    return render_template("churn.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        age = int(request.form['age'])
        last_login = int(request.form['last_login'])
        avg_time_spent =float(request.form['avg_time_spent'])
        avg_transaction_value =float(request.form['avg_transaction_value'])
        points_in_wallet =float(request.form['points_in_wallet'])
        date = request.form['date']
        time = request.form['time']
        gender = request.form['gender']
        region_category =request.form['region_category']
        membership_category = request.form['membership_category']
        joined_through_referral = request.form['joined_through_referral']
        preferred_offer_types =request.form['preferred_offer_type']
        medium_of_operation = request.form['medium_of_operation']
        internet_option = request.form['internet_option']
        used_special_discount = request.form['used_special_discount']
        offer_application_preference = request.form['offer_application_preference']
        past_complaint =request.form['past_complaint']
        feedback =request.form['feedback']
        
        #gender
        if gender=="M":
            gender_M =1
            gender_Unknown =0
        elif gender =="Unknown":
            gender_M =0
            gender_Unknown=1
        else:
            gender_M=0
            gender_Unknown=0
        # region_category
        if region_category =='Town':
            region_category_Town =1
            region_category_village =0
        if region_category =="Village":
            region_category_Town=0
            region_category_village=1
        else:
            region_category_Town = 0
            region_category_village =0 
        # membership_category
        if membership_category =='Gold Membership':
            membership_category_Gold =1
            membership_category_No =0
            membership_category_Platinum =0
            membership_category_Silver =0
            membership_category_Premium =0
        elif membership_category=="No Membership":
            membership_category_Gold =0
            membership_category_No =1
            membership_category_Platinum =0
            membership_category_Silver =0
            membership_category_Premium =0
        elif membership_category=="No Membership":
            membership_category_Gold =0
            membership_category_No =0
            membership_category_Platinum =1
            membership_category_Silver =0
            membership_category_Premium =0    
        elif membership_category=="No Membership":
            membership_category_Gold =0
            membership_category_No =0
            membership_category_Platinum =0
            membership_category_Silver =1
            membership_category_Premium =0        
        elif membership_category=="No Membership":
            membership_category_Gold =0
            membership_category_No =0
            membership_category_Platinum =0
            membership_category_Silver =0
            membership_category_Premium =1 
        else:
            membership_category_Gold =0
            membership_category_No =1
            membership_category_Platinum =0
            membership_category_Silver =0
            membership_category_Premium =0                            
        
        #preferred_offer_type
        if preferred_offer_types =='Gift Vouchers/Coupons':
            preferred_offer_types_Gift_VouchersCouons =1
            preferred_offer_types_Without_offers=0
        if preferred_offer_types =="Without Offers":
            preferred_offer_types_Gift_VouchersCouons=0
            preferred_offer_types_Without_offers =1
        else:
            preferred_offer_types_Without_offers=0
            preferred_offer_types_Without_offers=0
        
        # medium_of_operation
        if medium_of_operation =='Desktop':
            medium_of_operation_Desktop =1
            medium_of_operation_Both =0
            medium_of_operation_Smartphone =0        
        elif medium_of_operation =='Both':
            medium_of_operation_Desktop =0
            medium_of_operation_Both =1
            medium_of_operation_Smartphone =0  
        elif medium_of_operation =='Smartphone':
            medium_of_operation_Desktop =0
            medium_of_operation_Both =0
            medium_of_operation_Smartphone =1 
        # internet_option
        if internet_option =='Mobile_Data':
            internet_option_Mobile_Data = 1
            internet_option_Wi_Fi=0               
        if internet_option =='Wi_Fi':
            internet_option_Mobile_Data = 0
            internet_option_Wi_Fi=1
        else:
            internet_option_Mobile_Data = 0
            internet_option_Wi_Fi=0
        #used_special_discount
        if used_special_discount=='Yes':
            used_special_discount_Yes=1
        else:
            used_special_discount_Yes =1
        #offer_applicant_performce
        if offer_application_preference=='Yes':
            offer_application_preference_Yes =1
        else:
            offer_application_preference_Yes =1
        # past_complaint
        if past_complaint =='Yes':
            past_complaint_Yes =1
        else:
            past_complaint_Yes=1
        # feedback
        if feedback =='Poor Customer Service':
            feedback_Customer =1
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0
        elif feedback =='Poor Product Quality':
            feedback_Customer =0
            feedback_Poor_Product_Quality =1
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0
        elif feedback =='Poor Website':
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =1
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0
        elif feedback =='Products always in Stock':
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=1
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0       
        elif feedback =='Quality Customer Service':
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=1
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0                        
        elif feedback =='Reasonable Price':
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=1
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0            
        elif feedback =='Too many ads':
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =1
            feedback_User_Friendly_Website=0
        elif feedback =='User Friendly Website':
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=1   
        else:
            feedback_Customer =0
            feedback_Poor_Product_Quality =0
            feedback_Poor_Website =0
            feedback_Products_always_in_Stock=0
            feedback_Quality_Customer_Care=0
            feedback_Reasonable_Price=0
            feedback_Too_many_ads =0
            feedback_User_Friendly_Website=0  
            
        # date 
        date2 = date.split('-')
        joining_day =int(date2[0])
        joining_month = int(date2[1])
        joining_month = int(date2[2])
        
        time2 =time.split(':')
        last_visit_time_hour = int(time2[0])
        last_visit_time_minutes = int(time2[1])
        last_visit_time_seconds = int(time2[2]) 
        
        # import pandas as pd
        # df = pd.DataFrame.from_dict(data)
        
        # cols =model.get_booster().feature_names
        # df = df[cols]
        
        # print(prediction = model.predict(df))
    
    
        return render_template("prediction.html",f'prediction_text ="Churn Score is {prediction}')    
    else:
        return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)


