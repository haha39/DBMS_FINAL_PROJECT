
import sqlite3

def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def create_id():
    f = open("ID.txt", "r", encoding="utf-8")
    g = open("graph.txt", "r", encoding="utf-8")
    
    content = f.readlines()
    link = g.readlines()
    f.close()
    g.close()

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
        CREATE TABLE IF NOT EXISTS id
            (pokemon_id int primary key,
            name varchar(255) not null,
            evolve_id int,
            photo varchar(255)
            );
    '''
    c.execute(sql)      #執行sql語句
    
    j=0

    for file_data in content:
        
        datas = file_data.split("\t")
        
        pokemon_id, name, evolve_id = datas[0], "\"" + datas[1] + "\"", datas[2].strip()
        
        
        photo = "\"" +link[j].strip()+ "\""
        j=j+1
        
        
        print(pokemon_id, "|", name, "|", evolve_id)
        print(photo)
        
        #photo = convertToBinaryData("newpics/"+pokemon_id+".jpg")
        
        SQL_insert_command = f'''
                INSERT INTO id
                    (pokemon_id, name, evolve_id, photo)
                    VALUES ({pokemon_id}, {name}, {evolve_id}, {photo});
            '''
        #data_tuple = (pokemon_id,name,evolve_id,photo)
        print(SQL_insert_command)
        c.execute(SQL_insert_command)   #執行sql語句


    conn.commit()  # 提交數據庫操作
    conn.close()  # 關閉數據庫連結

def create_location():
    f = open("Location.txt", "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
        CREATE TABLE IF NOT EXISTS Location
            (L_id int primary key,
            pokemon_id int not null,
            location varchar(255) not null
            );
    '''
    c.execute(sql)      #執行sql語句



    for file_data in content:
        datas = file_data.split("\t")

        L_id, pokemon_id, location = datas[0], datas[1], "\"" + datas[2].strip() + "\""

        print(L_id, "|", pokemon_id, "|", location)

        SQL_insert_command = f'''
               INSERT INTO Location
                   (L_id, pokemon_id, location)
                   VALUES ({L_id}, {pokemon_id}, {location});
           '''
        print(SQL_insert_command)
        c.execute(SQL_insert_command)   #執行sql語句


    conn.commit()  # 提交數據庫操作
    conn.close()  # 關閉數據庫連結

def create_ability():
    f = open("Ability.txt", "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
        CREATE TABLE IF NOT EXISTS Ability
            (A_id int primary key,
            pokemon_id int not null,
            ability varchar(255) not null
            );
    '''
    c.execute(sql)      #執行sql語句



    for file_data in content:
        datas = file_data.split("\t")

        A_id, pokemon_id, ability = datas[0],  datas[1], "\"" + datas[2].strip() + "\""

        print(A_id, "|", pokemon_id, "|", ability)

        SQL_insert_command = f'''
               INSERT INTO Ability
                   (A_id, pokemon_id, ability)
                   VALUES ({A_id}, {pokemon_id}, {ability});
           '''
        print(SQL_insert_command)
        c.execute(SQL_insert_command)   #執行sql語句


    conn.commit()  # 提交數據庫操作
    conn.close()  # 關閉數據庫連結

def create_strong():
    f = open("Strong.txt", "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
        CREATE TABLE IF NOT EXISTS Strong
            (S_id int primary key,
            type varchar(255) not null,
            strong_type varchar(255) not null
            );
    '''
    c.execute(sql)      #執行sql語句



    for file_data in content:
        datas = file_data.split("\t")

        S_id, type, strong_type = datas[0],  "\"" + datas[1] + "\"", "\"" + datas[2].strip() + "\""

        print(S_id, "|", type, "|", strong_type)

        SQL_insert_command = f'''
               INSERT INTO Strong
                   (S_id, type, strong_type)
                   VALUES ({S_id}, {type}, {strong_type});
           '''
        print(SQL_insert_command)
        c.execute(SQL_insert_command)   #執行sql語句


    conn.commit()  # 提交數據庫操作
    conn.close()  # 關閉數據庫連結

def create_weak():
    f = open("Weak.txt", "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
        CREATE TABLE IF NOT EXISTS Weak
            (W_id int primary key,
            type varchar(255) not null,
            weak_type varchar(255) not null
            );
    '''
    c.execute(sql)      #執行sql語句



    for file_data in content:
        datas = file_data.split("\t")

        W_id, type, weak_type = datas[0],  "\"" + datas[1] + "\"", "\"" + datas[2].strip() + "\""

        print(W_id, "|", type, "|", weak_type)

        SQL_insert_command = f'''
               INSERT INTO Weak
                   (W_id, type, weak_type)
                   VALUES ({W_id}, {type}, {weak_type});
           '''
        print(SQL_insert_command)
        c.execute(SQL_insert_command)   #執行sql語句


    conn.commit()  # 提交數據庫操作
    conn.close()  # 關閉數據庫連結

def create_type():
    f = open("Type.txt", "r", encoding="utf-8")
    content = f.readlines()
    f.close()

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
        CREATE TABLE IF NOT EXISTS Type
            (T_id int primary key,
            pokemon_id int not null,
            type varchar(255) not null
            );
    '''
    c.execute(sql)      #執行sql語句



    for file_data in content:
        datas = file_data.split("\t")

        T_id, pokemon_id, type = datas[0], datas[1], "\"" + datas[2].strip() + "\""

        print(T_id, "|", pokemon_id, "|", type)

        SQL_insert_command = f'''
               INSERT INTO Type
                   (T_id, pokemon_id, type)
                   VALUES ({T_id}, {pokemon_id}, {type});
           '''
        print(SQL_insert_command)
        c.execute(SQL_insert_command)   #執行sql語句


    conn.commit()  # 提交數據庫操作
    conn.close()  # 關閉數據庫連結

def getinfo(pokemon_name):

    
    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
                SELECT id.name, Type.type
                FROM id , Type
                WHERE id.pokemon_id = Type.pokemon_id AND id.name =
            "''' + pokemon_name+'''"'''
    datas = c.execute(sql)  # 執行sql語句
    type_out=set()
    for row in datas:
        type_out=type_out|{row[1]}

    sql = '''
            SELECT id.name, Ability.ability
            FROM id , Ability
            WHERE id.pokemon_id = Ability.pokemon_id AND id.name =
        "''' + pokemon_name+'''"'''
    datas = c.execute(sql)  # 執行sql語句
    ability_out= set()    
    for row in datas:
        ability_out=ability_out|{row[1]}
        
    return type_out,ability_out
    conn.close()  # 關閉數據庫連結
    
def method1(pokemon_name):
    
    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
            SELECT id.photo
            FROM id
            WHERE id.name = "'''+pokemon_name+'''"'''
        
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    
    for row in datas:
        photo=row[0]
    
    print(photo)
    type_out,ability_out = getinfo(pokemon_name)
    print(pokemon_name)
    print("Type :",end=" ")
    for t in type_out:
        print(t,end=" ")
    print()
    print("Ability :",end=" ")
    for a in ability_out:
        print(a,end=" ")
    print()
    conn.close()  # 關閉數據庫連結
    return photo,list(type_out),list(ability_out)

def method2(pokemon_name):

    

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
            SELECT  L.location
            FROM    (SELECT pokemon_id
                    FROM id
                    WHERE name ="'''+pokemon_name+'''") AS P, Location AS L
            WHERE P.pokemon_id=L.pokemon_id
        '''
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    
    if(len(list(datas)) == 0):
        output=["Pokemon do not appear in regular location"]
        print("Pokemon do not appear in regular location")
        conn.close()  # 關閉數據庫連結
        return output
    
    location_set= []
    for row in datas:
        location_set=location_set+[row[0]]
    
    output=location_set
    print(output)
    conn.close()  # 關閉數據庫連結
    return output

def method3(pokemon_name):

    

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
            SELECT id.name,id.pokemon_id,id.evolve_id,id.photo
            FROM id
            WHERE id.name = "'''+pokemon_name+'''"'''
        
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    if(len(list(datas)) == 0):
        #print("Error, Pokemon not exist")
        conn.close()  # 關閉數據庫連結
        return 
    
    flag=True
    ret=[]
    output = list(datas)[0][0]
    ret = [output]
    p_list=[list(datas)[0][3]]
    back = str(list(datas)[0][1])
    forward = str(list(datas)[0][2])
    flag=True
    if(forward=="None"):
        flag=False
    

    while(flag):
        sql = '''
                SELECT name,evolve_id,photo
                FROM id
                WHERE pokemon_id = '''+forward
        c.execute(sql)
        datas = c.fetchall()
        output=output+"->"+list(datas)[0][0]
        ret = ret+[list(datas)[0][0]]
        p_list=p_list+[list(datas)[0][2]]
        forward=str(list(datas)[0][1])
        if(forward=="None"):
            break
    while(True):
       
        sql = '''
                SELECT name,pokemon_id,photo
                FROM id
                WHERE evolve_id = '''+back
        c.execute(sql)
        datas = c.fetchall()
        if(len(list(datas)) == 0):
            break
        output=list(datas)[0][0]+"->"+output
        ret=[list(datas)[0][0]]+ret
        p_list = [list(datas)[0][2]] + p_list
        back=str(list(datas)[0][1])      
                
    #print(output)
    #print(ret)
    #print(p_list)
    conn.close()
    
    return ret, p_list

def method4(pokemon_name,func):
    #func=1 type is the same
    #func=2 ability is the same
    #func=3 both are the same
    type_out,ability_out = getinfo(pokemon_name)
    
    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    
    sql = '''
               SELECT name
               FROM id
               WHERE name <> "'''+pokemon_name+'''"'''
        
        
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    
    pokemon_list=[]
    for row in datas:
        pokemon_list=pokemon_list+[row[0]]
    
    output=[]
    for p in pokemon_list:
        t,a= getinfo(p)
        if(func==1):
            if(t==type_out):
                output=output+[p]
        elif(func==2):
            if(a==ability_out):
                output=output+[p]
        elif(func==3):
            if(t==type_out and a==ability_out):
                output=output+[p]
    conn.close()  # 關閉數據庫連結
    if(output==[]):
        return ["There is no result is found"]
    else:
        print(output)
        return output
    
def method5(pokemon_type,pokemon_name):

    type_out,ability_out = getinfo(pokemon_name)

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
            SELECT strong_type
            FROM Strong
            WHERE type = "'''+pokemon_type+'''"'''
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    
    strong_set= set()    
    for row in datas:
        strong_set=strong_set|{row[0]}
         
    
    sql = '''
            SELECT weak_type
            FROM Weak
            WHERE type = "'''+pokemon_type+'''"'''
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    
    weak_set= set()    
    for row in datas:
        weak_set=weak_set|{row[0]}
    count=0
    
    for t in type_out:
        
        if(t in strong_set):
            count=count+1
        if(t in weak_set):
            count=count-1
    conn.close()  # 關閉數據庫連結       
    if(count>0):
        print("有效")
        return "有效"
    elif(count<0):
        print("不太有效")
        return "不太有效"
    else:
        print("一般")
        return "一般"
    
def method6(pokemon_location):

    

    # 連接或創建數據庫
    conn = sqlite3.connect("db_project.db")

    c = conn.cursor()  # 獲取游標
    sql = '''
            SELECT  I.name
            FROM    (SELECT pokemon_id
                    FROM Location
                    WHERE location ="'''+pokemon_location+'''") AS P, id AS I
            WHERE P.pokemon_id=I.pokemon_id
        '''
    c.execute(sql)  # 執行sql語句
    datas = c.fetchall()
    
    pokemon_set= set()    
    for row in datas:
        pokemon_set=pokemon_set|{row[0]}
    print(pokemon_set)
   
    conn.close()  # 關閉數據庫連結
    return list(pokemon_set)


#create_strong()
#create_id()
# create_ability()
# create_weak()
# create_type()
# create_location()
method3('''比比鳥''')
#method6('''1號公路''')

# conn = sqlite3.connect("db_project.db")
#
# c = conn.cursor()  # 獲取游標
# sql = '''
#         DROP TABLE id;
#     '''
#
# c.execute(sql)  # 執行sql語句
#
#
# conn.close()  # 關閉數據庫連結

