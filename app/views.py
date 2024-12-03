from flask import render_template, flash, request, redirect, url_for
from app import app, db, models
from .forms import CreateAssessment
from flask_sqlalchemy import SQLAlchemy
import datetime

app.app_context().push()

@app.route('/')
def home():
    heading = {'head': 'All Assessments'}
    assessments = models.Assessments.query.all()
    #DISPLAY IF THERE ARE NO ASSESSMENTS
    exists = models.Assessments.query.count()
    if exists == 0:
        heading = {'head': 'No Assessments'}
    return render_template('home.html', title='Home', heading=heading, assessments=assessments)


@app.route('/in_progress')
def in_progress():
    heading = {'head': 'Current Assessments'}
    #GET ONLY THE "IN PROGRESS" ASSESSMENTS
    assessments = models.Assessments.query.filter_by(progress=0).all()
    exists = models.Assessments.query.count()
    #DISPLAY IF THERE ARE NO ASSESSMENTS
    if exists == 0:
        heading = {'head': 'No Assessments'}
    return render_template('home.html', title='Home', heading=heading, assessments=assessments)


@app.route('/completed')
def completed():
    heading = {'head': 'Completed Assessments'}
    #GET ONLY THE "COMPLETED" ASSESSMENTS
    assessments = models.Assessments.query.filter_by(progress=1).all()
    exists = models.Assessments.query.count()
    #DISPLAY IF THERE ARE NO ASSESSMENTS
    if exists == 0:
        heading = {'head': 'No Assessments'}
    return render_template('home.html', title='Home', heading=heading, assessments=assessments)


@app.route('/create', methods=['GET', 'POST'])
def create():
    heading = {'head': 'Create Assessment'}
    form = CreateAssessment()
    assessments = models.Assessments.query.all()
    if request.method == "POST":
        #VALIDATE DATA
        if form.validate_on_submit():
            if form.due_date.data > datetime.date.today():
                #SAVES DATA FROM FORM AS RECORD IN DATABASE
                record = models.Assessments(module_code=form.module_code.data, assess_title=form.assess_title.data, description=form.description.data, due_date=form.due_date.data, progress=0)
                db.session.add(record)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                flash("Due Date is Invalid, Try Again")
        #DATA INVALID
        else:
            flash('Invalid Data, Try Again')
    return render_template('create.html', title='Create', form=form, assessments=assessments, heading=heading)


@app.route('/edit', methods=['POST'])
def edit():
    heading = {'head': 'Edit Assessment'}
    form = CreateAssessment()
    #GET THE DATA FROM THE CURRENT ASSESSMENT
    record = request.form.get("edit_button")
    p = models.Assessments.query.get(record)
    #FILL IN FORM WITH ASSESSMENT TO EDIT
    form.module_code.data = p.module_code
    form.assess_title.data = p.assess_title
    form.description.data = p.description
    form.due_date.data = p.due_date
    #DELETE IT SO DON'T DUPLICATE
    db.session.delete(p)
    db.session.commit()
    #GET ALL ASSESSMENTS
    return render_template('create.html', title='Create', form=form, heading=heading)


@app.route('/delete', methods=['POST'])
def delete():
    heading = {'head': 'All Assessments'}
    #GET THE ID OF RECORD TO DELETE
    record = request.form.get("del_button")
    #DELETE RECORD
    p = models.Assessments.query.get(record)
    db.session.delete(p)
    db.session.commit()
    #GET ALL ASSESSMENTS TO RE-DISPLAY - CHECK IF ANY EXIST NOW
    assessments = models.Assessments.query.all()
    exists = models.Assessments.query.count()
    if exists == 0:
        heading = {'head': 'No Assessments'}
    return render_template('home.html', title='Home', heading=heading,assessments=assessments)


@app.route('/update_assess', methods=['POST'])
def update_assess():
    heading = {'head': 'All Assessments'}
    #GET ID OF RECORD TO UPDATE
    record = request.form.get("upd_button")
    #UPDATE PROGRESS
    p = models.Assessments.query.get(record)
    if p.progress == 0:
        p.progress = 1
    else:
        p.progress = 0
    db.session.commit()
    assessments = models.Assessments.query.all()
    return render_template('home.html', title='Home', heading=heading,assessments=assessments)