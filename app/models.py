from app import db

class Assessments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_code = db.Column(db.String(8))
    assess_title = db.Column(db.String(15))
    description = db.Column(db.String(100))
    due_date = db.Column(db.Date)
    #Value 1 == Complete -> default value for new assessments
    #Value 0 == Incomplete
    progress = db.Column(db.Integer)