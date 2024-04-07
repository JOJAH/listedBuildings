from my_db_app import db 

class listBuildingTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timePeriod = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    totalListedBuildings = db.Column(db.Integer, nullable=False)
    grade1 = db.Column(db.Integer, nullable=False)
    grade2Star = db.Column(db.Integer, nullable=False)
    grade2 = db.Column(db.Integer, nullable=False)

class every200YearslistBuildingTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timePeriod = db.Column(db.String(80), nullable=False)
    totalListedBuildings = db.Column(db.Integer, nullable=False)
    grade1 = db.Column(db.Integer, nullable=False)
    grade2Star = db.Column(db.Integer, nullable=False)
    grade2 = db.Column(db.Integer, nullable=False)