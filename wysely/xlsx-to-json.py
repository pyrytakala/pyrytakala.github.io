import excel2json, os

BASE = '/Users/pyry/Google Drive/g/pyrytakala.github.io/wysely/'

def turn_to_json(infile, outfile, dbname):


    xlsx_url = BASE + infile
    temp_json = BASE + "Sheet1.json"
    json_url = BASE + outfile

    excel2json.convert_from_file(xlsx_url)
    os.rename(temp_json, json_url)

    f = open(json_url,'r')
    temp = f.read()
    f.close()

    f = open(json_url, 'w')
    f.write("var " + dbname + " = ")
    f.write(temp)
    f.close()

turn_to_json('db.xlsx', 'db.json', 'db')
turn_to_json('db-active.xlsx', 'db-active.json', 'db_active')
turn_to_json('db-historical.xlsx', 'db-historical.json', 'db_historical')