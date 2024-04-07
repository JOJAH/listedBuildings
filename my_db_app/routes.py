from flask import render_template
from my_db_app import app
from my_db_app.models import every200YearslistBuildingTable
@app.route("/")
def home():
   
   dataList = every200YearslistBuildingTable.query.all()

   allListedBuildings = 0

   listedBuildingList = []
   for data in dataList:
      totListBuilds = data.totalListedBuildings
      listedBuildingList.append(totListBuilds)
   print(listedBuildingList)

   grade1Buildings = []
   for data in dataList:
      totGrade1s = data.grade1
      grade1Buildings.append(totGrade1s)
   
   grade2StarBuildings = []
   for data in dataList:
      totGradeStars = data.grade2Star
      grade2StarBuildings.append(totGradeStars)
   
   grade2Buildings = []
   for data in dataList:
      totGrade2s = data.grade2
      grade2Buildings.append(totGrade2s)


   datas = []
   i = 0
   for data in dataList:
      allListedBuildings += data.totalListedBuildings
      time_Period_info = {}
      time_Period_info["id"] = i
      time_Period_info["timePeriod"] = data.timePeriod
      num_str = repr(data.totalListedBuildings)
      last_Digit = int(num_str[-1])
      #print(last_Digit)
      unroundedTotal = data.totalListedBuildings
      if last_Digit == 0:
         pass
      if last_Digit <= 5:
         unroundedTotal += 5
      rounded_Total = (round(unroundedTotal/10))*10

      time_Period_info["roundedTotalAmounts"] = rounded_Total
      time_Period_info["totalListedBuildings"] = data.totalListedBuildings
      time_Period_info["grade1"] = data.grade1
      time_Period_info["grade2Star"] = data.grade2Star
      time_Period_info["grade2"] = data.grade2
      #print(time_Period_info)
      datas.append(time_Period_info)
      i += 1

   #print(datas)
   



   return render_template("home.html", datas = datas, listedBuildingList = listedBuildingList, grade1Buildings = grade1Buildings, grade2StarBuildings = grade2StarBuildings, grade2Buildings = grade2Buildings, allListedBuildings = allListedBuildings)