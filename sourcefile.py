def searchCity(filename,citySearch):
  cityName = []
  with open(filename,"r") as f:
    for lines in f.readlines():
      line=lines.replace("\n","")  
      cityName.append(line)
    if citySearch in cityName:
      return 'Yes it is Present'
  return None

   
a=searchCity('cities.txt','Odisha')
print(a)