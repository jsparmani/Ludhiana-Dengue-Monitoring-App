text = 'Katyal Palace Ludhiana Road to Haw Singh Nalua Chowk Barnala Chowk tp . KPipe Factory Bamal Rajpur Chowk Ahmedgarh Kurichulla, Malerkotla Road, Bo CHOwlto Fshery Farm, Jagraon Road'

a = text.split(',')

file = open('D:\Codes\Django\LDMA\Ludhiana-Dengue-Monitoring-App\loc.txt', 'a')

for e in a:
    file.write(e.strip()+'\n')

file.close()
