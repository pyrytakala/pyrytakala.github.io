import excel2json, os

BASE = '/Users/pyry/Google Drive/g/pyrytakala.github.io/wysely/'

xlsx_url = BASE + "db.xlsx"
temp_json = BASE + "Sheet1.json"
json_url = BASE + "db.json"

excel2json.convert_from_file(xlsx_url)
os.rename(temp_json, json_url)


# turn to variable


f = open(json_url,'r')
temp = f.read()
f.close()

f = open(json_url, 'w')
f.write("var db = ")
f.write(temp)
f.close()



## pt 2


xlsx_url = BASE + "db-multi.xlsx"
temp_json = BASE + "Sheet1.json"
json_url = BASE + "db-multi.json"


excel2json.convert_from_file(xlsx_url)
os.rename(temp_json, json_url)

f = open(json_url,'r')
temp = f.read()
f.close()

f = open(json_url, 'w')
f.write("var db_multi = ")
f.write(temp)
f.close()
