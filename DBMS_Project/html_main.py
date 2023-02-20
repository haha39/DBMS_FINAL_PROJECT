from flask import Flask, render_template, request
import sqlite3
import dbset_main


#from dbset_main import



app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/index')
def home():
    return index()

def getinfo(pokemon_name):
    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
                SELECT id.name, Type.type
                FROM id , Type
                WHERE id.pokemon_id = Type.pokemon_id AND id.name =
            "''' + pokemon_name + '''"'''
    datas = c.execute(sql)  # 執行sql語句
    type_out = set()
    for row in datas:
        type_out = type_out | {row[1]}

    sql = '''
            SELECT id.name, Ability.ability
            FROM id , Ability
            WHERE id.pokemon_id = Ability.pokemon_id AND id.name =
        "''' + pokemon_name + '''"'''
    datas = c.execute(sql)  # 執行sql語句
    ability_out = set()
    for row in datas:
        ability_out = ability_out | {row[1]}

    conn.close()  # 關閉數據庫連結
    return type_out, ability_out

def get_name_list():
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    datalist = []
    sql = "select * from id"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    return datalist

def get_location_list():
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    datalist = []
    sql = "select distinct location " \
          "from Location " \
          "order by location"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    return datalist

def get_type_list():
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    type_list = []
    sql_type = "select distinct type from Type"
    data = cur.execute(sql_type)
    for item in data:
        type_list.append(item)
    data = cur.execute(sql_type)
    for item in data:
        type_list.append(item)
    return type_list

def get_ability_list():
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    ability_list = []
    sql_ability = "select distinct ability from Ability"
    data = cur.execute(sql_ability)
    for item in data:
        ability_list.append(item)
    data = cur.execute(sql_ability)
    for item in data:
        ability_list.append(item)
    return ability_list


#name 表單提交
@app.route('/quary1')
def quary1():
    datalist = get_name_list()

    return render_template("quary1.html", ID=datalist)

#input : id.name, output : Type.type && Ability.ability
@app.route('/result1', methods=['POST', 'GET'])
def result1():
    if request.method == 'POST':
        result = request.form

        #get input(name)
        for key, value in result.items():
            return_name = value

        datalist = get_name_list()

        photo, type_list, ability_list = dbset_main.method1(return_name)    #get type, ability, location

        location_list = dbset_main.method2(return_name)

        return render_template("result1.html", ID=datalist, return_name=return_name, ability_list=ability_list
            , type_list=type_list, location_list=location_list, photo=photo)

#name
@app.route('/quary2')
def quary2():
    datalist = get_location_list()

    return render_template("quary2.html", datalist=datalist)

#input : id.name, output : location
@app.route('/result2', methods=['POST', 'GET'])
def result2():
    if request.method == 'POST':
        result = request.form

        # get input(name)
        for key, value in result.items():
            return_name = value

    datalist = get_location_list()
    list = dbset_main.method6(return_name)


    return render_template("result2.html", datalist=datalist, list=list)

#id
@app.route('/quary3')
def quary3():
    datalist = get_name_list()

    return render_template("quary3.html", ID=datalist)

#input : id.name, output : evolve name
@app.route('/result3', methods=['POST', 'GET'])
def result3():
    if request.method == 'POST':
        result = request.form

        # get input(name)
        for key, value in result.items():
            return_name = value

        datalist = get_name_list()

        evolve_list, photo_list = dbset_main.method3(return_name)

        return render_template("result3.html", ID=datalist, evolve_list=evolve_list, photo_list=photo_list)

#id
@app.route('/quary4')
def quary4():
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()

    id_list = get_name_list()
    type_list = get_type_list()
    ability_list = get_ability_list()

    cur.close()
    con.close()
    return render_template("quary4.html", id_list=id_list, ability_list=ability_list, type_list=type_list)

#input : id.name, output : Type.type && Ability.ability
@app.route('/result4', methods=['POST', 'GET'])
def result4():
    if request.method == 'POST':
        result_name = request.form.get('key1')
        result_type = request.form.get('key2')
        result_ability = request.form.get('key3')

        id_list = get_name_list()
        type_list = get_type_list()
        ability_list = get_ability_list()

        if result_type == "1" and result_ability == "0":
            print("1")
            name_list = dbset_main.method4(result_name, 1)
        elif result_type == "0" and result_ability == "1":
            print("2")
            name_list = dbset_main.method4(result_name, 2)
        elif result_type == "1" and result_ability == "1":
            print("3")
            name_list = dbset_main.method4(result_name, 3)

        return render_template("result4.html", id_list=id_list, ability_list=ability_list, type_list=type_list, name_list=name_list)

#id
@app.route('/quary5')
def quary5():
    id_list = get_name_list()
    type_list = get_type_list()

    return render_template("quary5.html", id_list=id_list,  type_list=type_list)

#input : id.name, output : location
@app.route('/result5', methods=['POST', 'GET'])
def result5():
    if request.method == 'POST':
        result_name = request.form.get('key1')
        result_type = request.form.get('key2')

        id_list = get_name_list()
        type_list = get_type_list()

        output = dbset_main.method5(result_type, result_name)

        return render_template("result5.html", id_list=id_list,  type_list=type_list, output=output
                    , result_name=result_name, result_type=result_type)



@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()






