# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save')
def save():
    return render_template('save.html')

## API 역할을 하는 부분
@app.route('/save_animal', methods=['POST'])
def animal_save():
    result = 1 #0:실패, 1:성공
    msg = ""

    #사용자가 입력한 값을 변수에 담기
    input_animal = request.form['animal']
    input_count = request.form['count']
    print(input_animal, input_count)

    #입력한 값을 DB에 저장하기
    check_animal = db.animals.find_one({'animal': input_animal})
    if check_animal is None:
        doc = {
            'animal' : input_animal,
            'count' : input_count
        }
        db.animals.insert_one(doc)
    else:
        result = 0
        msg = "해당 값이 이미 존재합니다."
        return jsonify({'result':result, 'msg':msg})

    #DB에서 저장여부를 확인해보기
    search_animal = input_animal
    search_count = input_count
    find_result = db.animals.find_one({'animal':search_animal, 'count':search_count})
    print (find_result)
    if find_result == None:
        result = 0
        msg = "저장에 실패했습니다."

    return jsonify({'result':result, 'msg':msg})


@app.route('/count')
def count():
    return render_template('count.html')

# ## API 역할을 하는 부분
@app.route('/search_count', methods=['GET'])
def search_count():
    result = 1 #0:실패, 1:성공

    #초기값 체크 - 변수 값 입력받기
    input_animal = request.args.get('animal')
    print (input_animal)

    if input_animal == "":
        result = 0
        print ('입력값이 : ', input_animal)
        return jsonify({'result':result})

    #프로세스 수행 - DB에 count값 찾기
    search_animal = input_animal
    result_animal = db.animals.find_one({'animal':search_animal}) #DB에 저장된 값이 아닐 경우 None으로 반환함

    print (result_animal)
    #DB에 저장여부에 따라 count값 설정
    if result_animal is None:
        #DB에 저장이 안되어 있을 때 임의의 값으로 0을 준다.
        result_count = 0
    else:
        result_count = result_animal['count']

    return jsonify({'result':result, 'count':result_count})






if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)