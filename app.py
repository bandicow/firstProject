
from flask import Flask, render_template, request , url_for
import pickle
import numpy as np

model = pickle.load(open("C:/Users/gjaischool/Desktop/final_wish/data/pkl/wish_rf.pkl", 'rb'))
app = Flask(__name__)
ab=["상의","치마","바지","아우터","원피스","잠옷","속옷","수영복"]
ac=["검정","흰색","주황","초록","파랑","노랑","빨강","하늘"]
@app.route('/')
def main():
    return render_template('home.html')

# 테스트 시작하기
@app.route('/main')
def start():
    return render_template('main.html')
  
@app.route('/predict', methods=['GET','POST'])
def home(): 
        if request.method == 'GET':
            return render_template('main.html')

        if request.method == "POST":
            data1 = int(request.form['rating_count'])
            data2 = int(request.form['merchant_rating_count'])
            data3 = int(request.form['product_variation_inventory'])  
            
            for i in range(1,6,1):
                if i == int(request.form["rate"]):
                    data4 = i
        
            data5 = (request.form['n_tags'])  
            
            if (request.form["sex"])=="m":       
                data6=0
                data7=1
                성별 = "남성"    
            elif (request.form["sex"])=="f":
                data6=1
                data7=0
                성별 = "여성"
                
            for i in range(8,16,1):
                globals()['data'+str(i)]=i-5-int(request.form['clothing'])
                if globals()['data'+str(i)]!=1:
                    globals()['data'+str(i)]=0
            의류 = ab[int(request.form['clothing'])]
            색상 = ac[int(request.form['color'])]
            
            
            data16 = int(request.form['color'])
            
            arr = np.array([[data1, data2, data3, data4 ,data5, data6, data7,data8,data9,data10,data11,data12,data13,data14,data15, data16]])
            pred = model.predict(arr)
            pred=pred.astype(int)
            
            return render_template('result.html', data1=data1,data2=data2, data3=data3, data4=data4 ,data5=data5, 성별=성별, 의류=의류, 색상=색상,pred=pred,arr=arr)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0",port="8000")# --> 도커 실행 시
    
