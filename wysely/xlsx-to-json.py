import excel2json, os


xlsx_url = '/Users/pyry/Google Drive/projects/recruiter list/db.xlsx'
temp_json = "/Users/pyry/Google Drive/projects/recruiter list/Sheet1.json"
json_url = "/Users/pyry/Google Drive/projects/recruiter list/db.json"

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


xlsx_url = '/Users/pyry/Google Drive/projects/recruiter list/db-multi.xlsx'
temp_json = "/Users/pyry/Google Drive/projects/recruiter list/Sheet1.json"
json_url = "/Users/pyry/Google Drive/projects/recruiter list/db-multi.json"


excel2json.convert_from_file(xlsx_url)
os.rename(temp_json, json_url)

f = open(json_url,'r')
temp = f.read()
f.close()

f = open(json_url, 'w')
f.write("var db_multi = ")
f.write(temp)
f.close()
