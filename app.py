
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import pandas as pd
import numpy as np
import pickle
import os

# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)
app.secret_key = "healthcare_secret_key"

# ==========================================
# Database Connection
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="healthcare"
)

cursor = db.cursor(dictionary=True)

# ==========================================
# Load Machine Learning Model
# ==========================================

MODEL_PATH = "model/disease_model.pkl"

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
else:
    model = None

# ==========================================
# Home Page
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")

# ==========================================
# About Page
# ==========================================

@app.route("/about")
def about():
    return render_template("about.html")

# ==========================================
# Departments
# ==========================================

@app.route("/departments")
def departments():
    return render_template("departments.html")

# ==========================================
# Doctors
# ==========================================

@app.route("/doctors")
def doctors():
    return render_template("doctors.html")

# ==========================================
# Appointment
# ==========================================

@app.route("/appointment")
def appointment():
    if not is_logged_in():
        flash("Please login first.", "warning")
        return redirect(url_for("patient_login"))
    return render_template("appointment.html")

# ==========================================
# Predict Page
# ==========================================

@app.route("/predict")
def predict():
    if not is_logged_in():
        flash("Please login first.", "warning")
        return redirect(url_for("patient_login"))
    return render_template("predict.html")

# ==========================================
# Result Page
# ==========================================

@app.route("/result")
def result():
    if not is_logged_in():
        flash("Please login first.", "warning")
        return redirect(url_for("patient_login"))
    
    disease = session.get("predicted_disease", "No Prediction")
    confidence = session.get("prediction_confidence", 0)
    
    return render_template(
        "result.html",
        disease=disease,
        confidence=confidence
    )

# ==========================================
# Patient Registration
# ==========================================

@app.route("/patient_register", methods=["GET", "POST"])
def patient_register():
    if request.method == "POST":
        name = request.form["name"]
        mobile = request.form["mobile"]
        email = request.form["email"]
        dob = request.form["dob"]
        gender = request.form["gender"]
        blood = request.form["blood"]
        city = request.form["city"]
        address = request.form["address"]
        password = request.form["password"]

        # Check Existing Email
        sql = "SELECT * FROM patients WHERE email=%s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone()

        if user:
            flash("Email already registered.", "danger")
            return redirect(url_for("patient_register"))

        # Insert New Patient
        sql = """
        INSERT INTO patients
        (name,mobile,email,dob,gender,blood_group,city,address,password)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            name,
            mobile,
            email,
            dob,
            gender,
            blood,
            city,
            address,
            password
        )

        cursor.execute(sql, values)
        db.commit()

        flash("Registration Successful. Please Login.", "success")
        return redirect(url_for("patient_login"))

    return render_template("patient_register.html")

# ==========================================
# Patient Login
# ==========================================

@app.route("/patient_login", methods=["GET", "POST"])
def patient_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        sql = """
        SELECT * FROM patients
        WHERE email=%s AND password=%s
        """

        cursor.execute(sql, (email, password))
        patient = cursor.fetchone()

        if patient:
            session["patient_id"] = patient["id"]
            session["patient_name"] = patient["name"]
            session["patient_email"] = patient["email"]
            flash("Login Successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid Email or Password!", "danger")
            return redirect(url_for("patient_login"))

    return render_template("patient_login.html")

# ==========================================
# Patient Logout
# ==========================================

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("patient_login"))

# ==========================================
# Check Login Session
# ==========================================

def is_logged_in():
    return "patient_id" in session

# ==========================================
# Protected Dashboard
# ==========================================

@app.route("/dashboard")
def dashboard():
    if not is_logged_in():
        flash("Please login first.", "warning")
        return redirect(url_for("patient_login"))

    return render_template(
        "dashboard.html",
        patient_name=session["patient_name"],
        patient_email=session["patient_email"]
    )

# ==========================================
# Protected History Page
# ==========================================

@app.route("/history")
def history():
    if not is_logged_in():
        flash("Please login first.", "warning")
        return redirect(url_for("patient_login"))

    patient_id = session["patient_id"]

    sql = """
    SELECT *
    FROM prediction_history
    WHERE patient_id=%s
    ORDER BY id DESC
    """

    cursor.execute(sql, (patient_id,))
    history_data = cursor.fetchall()

    return render_template(
        "history.html",
        history=history_data
    )

# ==========================================
# Appointment Booking
# ==========================================

@app.route("/appointment", methods=["GET", "POST"])
def appointment_booking():
    # Check Patient Login
    if "patient_id" not in session:
        flash("Please Login First", "warning")
        return redirect(url_for("patient_login"))

    if request.method == "POST":
        patient_id = session["patient_id"]
        patient_name = request.form["patient_name"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        department = request.form["department"]
        doctor = request.form["doctor"]
        appointment_date = request.form["appointment_date"]
        appointment_time = request.form["appointment_time"]
        problem = request.form["problem"]

        sql = """
        INSERT INTO appointments
        (
            patient_id,
            patient_name,
            email,
            mobile,
            department,
            doctor,
            appointment_date,
            appointment_time,
            problem
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """

        values = (
            patient_id,
            patient_name,
            email,
            mobile,
            department,
            doctor,
            appointment_date,
            appointment_time,
            problem
        )

        cursor.execute(sql, values)
        db.commit()

        flash("Appointment Booked Successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("appointment.html")

# ==========================================
# Admin Login
# ==========================================

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Simple admin check (you can replace with database validation)
        if username == "admin" and password == "admin123":
            session["admin_logged_in"] = True
            flash("Admin Login Successful!", "success")
            return redirect(url_for("admin_dashboard"))
        else:
            flash("Invalid Admin Credentials!", "danger")
            return redirect(url_for("admin_login"))
    
    return render_template("admin_login.html")

# ==========================================
# Admin Dashboard
# ==========================================

@app.route("/admin_dashboard")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        flash("Please login as admin first.", "warning")
        return redirect(url_for("admin_login"))
    
    # Get statistics
    cursor.execute("SELECT COUNT(*) as total_patients FROM patients")
    total_patients = cursor.fetchone()["total_patients"]
    
    cursor.execute("SELECT COUNT(*) as total_appointments FROM appointments")
    total_appointments = cursor.fetchone()["total_appointments"]
    
    cursor.execute("SELECT COUNT(*) as total_predictions FROM prediction_history")
    total_predictions = cursor.fetchone()["total_predictions"]
    
    return render_template(
        "admin_dashboard.html",
        total_patients=total_patients,
        total_appointments=total_appointments,
        total_predictions=total_predictions
    )

# ==========================================
# Disease Prediction
# ==========================================

@app.route("/predict", methods=["GET", "POST"])
def predict_disease():
    # Check Login
    if "patient_id" not in session:
        flash("Please Login First", "warning")
        return redirect(url_for("patient_login"))

    if request.method == "POST":
        patient_id = session["patient_id"]
        patient_name = session["patient_name"]

        # Read Symptoms from Form
        fever = int(request.form.get("fever", 0))
        cough = int(request.form.get("cough", 0))
        fatigue = int(request.form.get("fatigue", 0))
        headache = int(request.form.get("headache", 0))
        vomiting = int(request.form.get("vomiting", 0))
        nausea = int(request.form.get("nausea", 0))
        chest_pain = int(request.form.get("chest_pain", 0))
        breathing = int(request.form.get("breathing", 0))
        diabetes = int(request.form.get("diabetes", 0))
        bp = int(request.form.get("bp", 0))

        # Create Feature List
        symptoms = [
            fever,
            cough,
            fatigue,
            headache,
            vomiting,
            nausea,
            chest_pain,
            breathing,
            diabetes,
            bp
        ]

        # Check ML Model
        if model is None:
            flash("Machine Learning model not found.", "danger")
            return redirect(url_for("predict_disease"))

        # Convert to NumPy Array
        input_data = np.array(symptoms).reshape(1, -1)

        # Machine Learning Prediction
        prediction = model.predict(input_data)
        predicted_disease = prediction[0]

        # Confidence Score
        confidence = None
        try:
            probability = model.predict_proba(input_data)
            confidence = round(max(probability[0]) * 100, 2)
        except:
            confidence = 100

        # Disease Name Mapping
        disease_dict = {
            0: "Common Cold",
            1: "Flu",
            2: "COVID-19",
            3: "Diabetes",
            4: "Hypertension",
            5: "Heart Disease",
            6: "Migraine",
            7: "Pneumonia",
            8: "Asthma",
            9: "Typhoid"
        }

        disease_name = disease_dict.get(
            predicted_disease,
            "Unknown Disease"
        )

        # Save Prediction History
        sql = """
        INSERT INTO prediction_history
        (
            patient_id,
            patient_name,
            disease,
            confidence,
            prediction_date
        )
        VALUES
        (
            %s,%s,%s,%s,NOW()
        )
        """

        values = (
            patient_id,
            patient_name,
            disease_name,
            confidence
        )

        cursor.execute(sql, values)
        db.commit()

        # Store Result in Session
        session["predicted_disease"] = disease_name
        session["prediction_confidence"] = confidence

        flash("Disease Prediction Completed Successfully!", "success")
        return redirect(url_for("result"))

    return render_template("predict.html")

# ==========================================
# Contact Page
# ==========================================

@app.route("/contact")
def contact():
    return render_template("contact.html")

# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)
