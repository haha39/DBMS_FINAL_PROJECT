from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/index')
def home():
    return index()

#name 表單提交
@app.route('/quary1')
def quary1():
    datalist = []
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    sql = "select * from id"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("quary1.html", ID=datalist)



#input : id.name, output : Type.type && Ability.ability
@app.route('/result1', methods=['POST', 'GET'])
def result1():
    if request.method == 'POST':
        result = request.form
        con = sqlite3.connect("db_project.db")
        cur = con.cursor()

        ability_list = []
        type_list = []

        #get input(name)
        for key, value in result.items():
            return_name = value

        sql_type = '''
                    SELECT id.name, Type.type
                    FROM id , Type
                    WHERE id.pokemon_id = Type.pokemon_id AND id.name =
                "''' + return_name +'''"'''

        TYPE = cur.execute(sql_type)  # 執行sql語句

        for row in TYPE:              #get its type
            type_list.append(row)

        sql_ability = '''
                SELECT id.name, Ability.ability
                FROM id , Ability
                WHERE id.pokemon_id = Ability.pokemon_id AND id.name =
            "''' + return_name +'''"'''

        ABILITY = cur.execute(sql_ability)  # 執行sql語句

        for row in ABILITY:         #get its ability
            ability_list.append(row)

        cur.close()
        con.close()

        return render_template("result1.html", result=result, ability_list=ability_list, type_list=type_list)






#name
@app.route('/quary2')
def quary2():
    datalist = []
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    sql = "select * from id"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("quary2.html", ID=datalist)


#input : id.name, output : location
@app.route('/result2')
def result2():
        return render_template("result2.html")

















#id
@app.route('/quary3')
def quary3():
    datalist = []
    con = sqlite3.connect("db_project.db")
    cur = con.cursor()
    sql = "select * from id"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("quary3.html", ID=datalist)

#input : id.name, output : evolve name
@app.route('/result3', methods=['POST', 'GET'])
def result3():
    if request.method == 'POST':
        result = request.form
        con = sqlite3.connect("db_project.db")
        cur = con.cursor()

        evolve_list = []

        #get input(name)
        for key, value in result.items():
            return_name = value

        sql_id = '''
                SELECT id.name,id.pokemon_id,id.evolve_id
                FROM id
                WHERE id.name = 
            "''' + return_name + '''"'''

        ID = cur.execute(sql_id)  # 執行sql語句

        datas = cur.fetchall()
        if (len(list(datas)) == 0):
            print("Error, Pokemon not exist")
            return

        flag = True

        output = list(datas)[0][0]
        back = str(list(datas)[0][1])
        forward = str(list(datas)[0][2])
        flag = True
        if (forward == "None"):
            flag = False

        while (flag):
            sql = '''
                    SELECT name,evolve_id
                    FROM id
                    WHERE pokemon_id = ''' + forward
            cur.execute(sql)
            datas = cur.fetchall()
            output = output + "->" + list(datas)[0][0]
            forward = str(list(datas)[0][1])
            if (forward == "None"):
                break

        while (True):

            sql = '''
                    SELECT name,pokemon_id
                    FROM id
                    WHERE evolve_id = ''' + back
            cur.execute(sql)
            datas = cur.fetchall()
            if (len(list(datas)) == 0):
                break
            output = list(datas)[0][0] + "->" + output
            back = str(list(datas)[0][1])

        cur.close()
        con.close()

        return render_template("result3.html", output=output)



#id
@app.route('/quary4')
def quary4():
    id_list = []
    type_list = []
    ability_list = []

    con = sqlite3.connect("db_project.db")
    cur = con.cursor()

    sql_id = "select * from id"
    data = cur.execute(sql_id)
    for item in data:
        id_list.append(item)

    sql_ability = "select distinct ability from Ability"
    data = cur.execute(sql_ability)
    for item in data:
        ability_list.append(item)

    sql_type = "select distinct type from Type"
    data = cur.execute(sql_type)
    for item in data:
        type_list.append(item)

    cur.close()
    con.close()
    return render_template("quary4.html", id_list=id_list, ability_list=ability_list, type_list=type_list)



#input : id.name, output : Type.type && Ability.ability
@app.route('/result4', methods=['POST', 'GET'])
def result4():
    if request.method == 'POST':
        result1 = request.form.get('key1')
        result2 = request.form.get('key2')
        result3 = request.form.get('key3')

        con = sqlite3.connect("db_project.db")
        cur = con.cursor()

        ability_list = []
        type_list = []
        return_list = []

        # get input(name)
        print(result1)
        print(result2)
        print(result3)

        # sql = '''
        #                SELECT name
        #                FROM id
        #                WHERE name <> "''' + pokemon_name + '''"'''
        #
        # cur.execute(sql)  # 執行sql語句
        # datas = cur.fetchall()
        #
        # pokemon_list = []
        # for row in datas:
        #     pokemon_list = pokemon_list + [row[0]]
        #
        # output = []
        # for p in pokemon_list:
        #     t, a = getinfo(p)
        #     if (func == 1):
        #         if (t == type_out):
        #             output = output + [p]
        #     elif (func == 2):
        #         if (a == ability_out):
        #             output = output + [p]
        #     elif (func == 3):
        #         if (t == type_out and a == ability_out):
        #             output = output + [p]
        # con.close()
        #
        # return render_template("result4.html")



#id
@app.route('/quary5')
def quary5():
    id_list = []
    type_list = []

    con = sqlite3.connect("db_project.db")
    cur = con.cursor()

    sql_id = "select * from id"
    data = cur.execute(sql_id)
    for item in data:
        id_list.append(item)

    sql_type = "select distinct type from Type"
    data = cur.execute(sql_type)
    for item in data:
        type_list.append(item)

    cur.close()
    con.close()
    return render_template("quary5.html", id_list=id_list,  type_list=type_list)

#input : id.name, output : location
@app.route('/result5')
def result5():

        return render_template("result5.html")





@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()

