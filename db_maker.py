from my_db_app import db 
from my_db_app.models import every200YearslistBuildingTable, listBuildingTable

db.drop_all()

db.create_all()

pre_Historic = listBuildingTable(
    timePeriod = "Pre-Historic",
    date = "500000BC - 43AD",
    totalListedBuildings = 22,
    grade1 = 5,
    grade2Star = 4,
    grade2 = 13
     )

roman = listBuildingTable(
   timePeriod = "Roman",
    date = "43AD - 410AD",
    totalListedBuildings = 212,
    grade1 = 76,
    grade2Star = 28,
    grade2 = 108 
)

earlyMedieval = listBuildingTable(
   timePeriod = "Early Medieval",
    date = "410AD - 1066AD",
    totalListedBuildings = 727,
    grade1 = 374,
    grade2Star = 162,
    grade2 = 191 
)

Medieval = listBuildingTable(
   timePeriod = "Medieval",
    date = "1066AD - 1540AD",
    totalListedBuildings = 28978,
    grade1 = 6490,
    grade2Star = 7931,
    grade2 = 14557 
)

postMedieval = listBuildingTable(
   timePeriod = "Post Medieval",
    date = "1540AD - 1901AD",
    totalListedBuildings = 347881,
    grade1 = 7821,
    grade2Star = 19683,
    grade2 = 320377 
)

twentiethCentury = listBuildingTable(
   timePeriod = "20th Century",
    date = "1901AD - 2000AD",
    totalListedBuildings = 64330,
    grade1 = 2634,
    grade2Star = 6377,
    grade2 = 55319 
)

db.session.add(pre_Historic)
db.session.add(roman)
db.session.add(earlyMedieval)
db.session.add(Medieval)
db.session.add(postMedieval)
db.session.add(twentiethCentury)

zero_twoHundred = every200YearslistBuildingTable(
    timePeriod = "0 - 200",
    totalListedBuildings = 49,
    grade1 = 32,
    grade2Star = 3,
    grade2 = 14 
)


twoHundred_fourHundred = every200YearslistBuildingTable(
    timePeriod = "200 - 400",
    totalListedBuildings = 46,
    grade1 = 30,
    grade2Star = 7,
    grade2 = 9 
)

fourHundred_sixHundred = every200YearslistBuildingTable(
    timePeriod = "400 - 600",
    totalListedBuildings = 16,
    grade1 = 4,
    grade2Star = 4,
    grade2 = 8 
)

sixHundred_eightHundred = every200YearslistBuildingTable(
    timePeriod = "600 - 800",
    totalListedBuildings = 36,
    grade1 = 26,
    grade2Star = 5,
    grade2 = 5 
)

eightHundred_oneThousand = every200YearslistBuildingTable(
    timePeriod = "800 - 1000",
    totalListedBuildings = 85,
    grade1 = 48,
    grade2Star = 18,
    grade2 = 19 
)

oneThousand_oneThousandTwoHundred = every200YearslistBuildingTable(
    timePeriod = "1000 - 1200",
    totalListedBuildings = 4569,
    grade1 = 2386,
    grade2Star = 1610,
    grade2 = 573 
)

oneThousandTwoHundred_oneThousandFourHundred = every200YearslistBuildingTable(
    timePeriod = "1200 - 1400",
    totalListedBuildings = 9853,
    grade1 = 4101,
    grade2Star = 3480,
    grade2 = 2272 
)

oneThousandFourHundred_oneThousandSixHundred = every200YearslistBuildingTable(
    timePeriod = "1400 - 1600",
    totalListedBuildings = 37503,
    grade1 = 4381,
    grade2Star = 6836,
    grade2 = 26286 
)

oneThousandSixHundred_oneThousandEightHundred = every200YearslistBuildingTable(
    timePeriod = "1600 - 1800",
    totalListedBuildings = 190921,
    grade1 = 3965,
    grade2Star = 11878,
    grade2 = 178678 
)

oneThousandEightHundred_twoThousand = every200YearslistBuildingTable(
    timePeriod = "1800 - 2000",
    totalListedBuildings = 265747,
    grade1 = 6693,
    grade2Star = 16138,
    grade2 = 242916 
)

db.session.add(zero_twoHundred)
db.session.add(twoHundred_fourHundred)
db.session.add(fourHundred_sixHundred)
db.session.add(sixHundred_eightHundred)
db.session.add(eightHundred_oneThousand)
db.session.add(oneThousand_oneThousandTwoHundred)
db.session.add(oneThousandTwoHundred_oneThousandFourHundred)
db.session.add(oneThousandFourHundred_oneThousandSixHundred)
db.session.add(oneThousandSixHundred_oneThousandEightHundred)
db.session.add(oneThousandEightHundred_twoThousand)


db.session.commit()