-- ==========================================
-- Healthcare Disease Prediction System
-- healthcare.sql
-- ==========================================

-- Drop database if exists to avoid conflicts
DROP DATABASE IF EXISTS healthcare;

-- Create fresh database
CREATE DATABASE healthcare;
USE healthcare;

-- ==========================================
-- Admin Table
-- ==========================================

CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default admin
INSERT INTO admin (username, password) VALUES
('admin', 'admin123'),
('superadmin', 'super123');

-- ==========================================
-- Departments Table
-- ==========================================

CREATE TABLE departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert departments
INSERT INTO departments (department_name, description) VALUES
('Cardiology', 'Heart and cardiovascular system treatment'),
('Neurology', 'Brain, spinal cord and nervous system disorders'),
('Orthopedics', 'Bone, joint, muscle and skeletal system treatment'),
('General Medicine', 'Comprehensive healthcare for all ages'),
('Pediatrics', 'Medical care for infants, children and adolescents'),
('Dermatology', 'Skin, hair, nail and mucous membrane disorders'),
('Pulmonology', 'Respiratory system and lung diseases'),
('Ophthalmology', 'Eye care and vision treatment'),
('ENT', 'Ear, Nose and Throat specialists'),
('Nephrology', 'Kidney disease diagnosis and treatment'),
('Oncology', 'Cancer diagnosis and treatment'),
('Emergency Care', '24×7 emergency medical services'),
('Gynecology', 'Women\'s reproductive health'),
('Psychiatry', 'Mental health and behavioral disorders');

-- ==========================================
-- Doctors Table
-- ==========================================

CREATE TABLE doctors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    qualification VARCHAR(100) NOT NULL,
    experience INT DEFAULT 0,
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    timing VARCHAR(100),
    image_url VARCHAR(255),
    rating DECIMAL(3,2) DEFAULT 4.5,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert doctors with proper professional photos
INSERT INTO doctors (doctor_name, department, qualification, experience, phone, email, timing, rating) VALUES
('Dr. Rajesh Sharma', 'Cardiology', 'MBBS, MD, DM (Cardiology)', 18, '9876543201', 'rajesh.sharma@apexcare.com', '10:00 AM - 4:00 PM', 4.9),
('Dr. Neha Patel', 'Neurology', 'MBBS, MD, DM (Neurology)', 15, '9876543202', 'neha.patel@apexcare.com', '9:00 AM - 2:00 PM', 4.8),
('Dr. Amit Mehta', 'Orthopedics', 'MBBS, MS (Orthopedics)', 20, '9876543203', 'amit.mehta@apexcare.com', '11:00 AM - 5:00 PM', 4.9),
('Dr. Pooja Shah', 'Dermatology', 'MBBS, MD (Dermatology)', 12, '9876543204', 'pooja.shah@apexcare.com', '10:00 AM - 3:00 PM', 4.7),
('Dr. Karan Desai', 'Pulmonology', 'MBBS, MD (Pulmonology)', 16, '9876543205', 'karan.desai@apexcare.com', '9:30 AM - 1:30 PM', 4.8),
('Dr. Riya Joshi', 'Pediatrics', 'MBBS, MD (Pediatrics)', 10, '9876543206', 'riya.joshi@apexcare.com', '8:00 AM - 1:00 PM', 4.9),
('Dr. Vikram Singh', 'Ophthalmology', 'MBBS, MS (Ophthalmology)', 14, '9876543207', 'vikram.singh@apexcare.com', '11:30 AM - 4:30 PM', 4.7),
('Dr. Meera Desai', 'ENT', 'MBBS, MS (ENT)', 11, '9876543208', 'meera.desai@apexcare.com', '9:00 AM - 3:00 PM', 4.6),
('Dr. Suresh Reddy', 'Nephrology', 'MBBS, MD, DM (Nephrology)', 17, '9876543209', 'suresh.reddy@apexcare.com', '10:00 AM - 2:00 PM', 4.8),
('Dr. Anjali Nair', 'General Medicine', 'MBBS, MD (Medicine)', 13, '9876543210', 'anjali.nair@apexcare.com', '8:30 AM - 2:30 PM', 4.7),
('Dr. Arjun Mehta', 'Oncology', 'MBBS, MD, DM (Oncology)', 19, '9876543211', 'arjun.mehta@apexcare.com', '10:30 AM - 5:30 PM', 4.9),
('Dr. Kavita Sharma', 'Emergency Care', 'MBBS, MD (Emergency)', 8, '9876543212', 'kavita.sharma@apexcare.com', '24×7 Available', 4.8),
('Dr. Manoj Gupta', 'Gastroenterology', 'MBBS, MD, DM (Gastro)', 16, '9876543213', 'manoj.gupta@apexcare.com', '10:00 AM - 4:00 PM', 4.7),
('Dr. Shweta Mishra', 'Psychiatry', 'MBBS, MD (Psychiatry)', 11, '9876543214', 'shweta.mishra@apexcare.com', '9:00 AM - 5:00 PM', 4.6),
('Dr. Ramesh Kumar', 'Urology', 'MBBS, MS (Urology)', 14, '9876543215', 'ramesh.kumar@apexcare.com', '11:00 AM - 5:00 PM', 4.7),
('Dr. Priya Menon', 'Rheumatology', 'MBBS, MD (Rheumatology)', 12, '9876543216', 'priya.menon@apexcare.com', '9:30 AM - 3:30 PM', 4.6),
('Dr. Sanjay Verma', 'Endocrinology', 'MBBS, MD, DM (Endo)', 15, '9876543217', 'sanjay.verma@apexcare.com', '10:00 AM - 3:00 PM', 4.8),
('Dr. Sunita Reddy', 'Gynecology', 'MBBS, MD (Gynecology)', 13, '9876543218', 'sunita.reddy@apexcare.com', '9:00 AM - 4:00 PM', 4.8);

-- ==========================================
-- Patients Table
-- ==========================================

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    mobile VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    dob DATE,
    gender VARCHAR(20),
    blood_group VARCHAR(10),
    city VARCHAR(100),
    address TEXT,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_mobile (mobile)
);

-- Insert sample patients
INSERT INTO patients (name, mobile, email, dob, gender, blood_group, city, address, password) VALUES
('Ankit Patel', '9999999999', 'ankit@gmail.com', '2003-05-15', 'Male', 'O+', 'Ahmedabad', 'Ahmedabad, Gujarat', '123456'),
('Rahul Shah', '9999999998', 'rahul@gmail.com', '1996-10-20', 'Male', 'A+', 'Ahmedabad', 'Ahmedabad, Gujarat', '123456'),
('Priya Patel', '9999999997', 'priya@gmail.com', '1999-12-10', 'Female', 'B+', 'Surat', 'Surat, Gujarat', '123456'),
('Amit Kumar', '9999999996', 'amit@gmail.com', '1991-06-15', 'Male', 'AB+', 'Rajkot', 'Rajkot, Gujarat', '123456');

-- ==========================================
-- Appointments Table
-- ==========================================

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    patient_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile VARCHAR(20) NOT NULL,
    department VARCHAR(100) NOT NULL,
    doctor VARCHAR(100) NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    problem TEXT,
    status VARCHAR(30) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_patient (patient_id),
    INDEX idx_date (appointment_date),
    INDEX idx_status (status),
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
);

-- Insert sample appointments
INSERT INTO appointments (patient_id, patient_name, email, mobile, department, doctor, appointment_date, appointment_time, problem, status) VALUES
(1, 'Ankit Patel', 'ankit@gmail.com', '9999999999', 'Cardiology', 'Dr. Rajesh Sharma', '2026-08-15', '10:00:00', 'Chest pain and breathing difficulty', 'Confirmed'),
(2, 'Rahul Shah', 'rahul@gmail.com', '9999999998', 'Neurology', 'Dr. Neha Patel', '2026-08-16', '11:15:00', 'Severe headache and dizziness', 'Pending'),
(3, 'Priya Patel', 'priya@gmail.com', '9999999997', 'Dermatology', 'Dr. Pooja Shah', '2026-08-17', '09:00:00', 'Skin rash and itching', 'Completed'),
(4, 'Amit Kumar', 'amit@gmail.com', '9999999996', 'Orthopedics', 'Dr. Amit Mehta', '2026-08-18', '02:00:00', 'Knee pain and joint stiffness', 'Pending');

-- ==========================================
-- Prediction History Table
-- ==========================================

CREATE TABLE prediction_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    patient_name VARCHAR(100) NOT NULL,
    disease VARCHAR(100) NOT NULL,
    confidence DECIMAL(5,2),
    symptoms TEXT,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_patient (patient_id),
    INDEX idx_date (prediction_date),
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE
);

-- Insert sample predictions
INSERT INTO prediction_history (patient_id, patient_name, disease, confidence, symptoms) VALUES
(1, 'Ankit Patel', 'Heart Disease', 96.80, 'Fever, Cough, Chest Pain'),
(2, 'Rahul Shah', 'Dengue', 94.50, 'Fever, Headache, Joint Pain'),
(3, 'Priya Patel', 'Viral Fever', 92.30, 'Cough, Fever, Fatigue'),
(4, 'Amit Kumar', 'Typhoid', 93.70, 'Vomiting, Fever, Abdominal Pain');

-- ==========================================
-- Contact Messages Table
-- ==========================================

CREATE TABLE contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    subject VARCHAR(150) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(30) DEFAULT 'Unread',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_email (email)
);

-- Insert sample contact messages
INSERT INTO contact (name, email, subject, message, status) VALUES
('Ankit Patel', 'ankit@gmail.com', 'Appointment Scheduling', 'I want to schedule a cardiology appointment', 'Unread'),
('Rahul Shah', 'rahul@gmail.com', 'Disease Prediction Feedback', 'The disease prediction system is very accurate', 'Read');

-- ==========================================
-- Admin Dashboard Statistics View
-- ==========================================

CREATE VIEW dashboard_stats AS
SELECT 
    (SELECT COUNT(*) FROM patients) AS total_patients,
    (SELECT COUNT(*) FROM appointments WHERE appointment_date = CURDATE()) AS today_appointments,
    (SELECT COUNT(*) FROM appointments) AS total_appointments,
    (SELECT COUNT(*) FROM prediction_history) AS total_predictions,
    (SELECT COUNT(*) FROM doctors) AS total_doctors,
    (SELECT COUNT(*) FROM departments) AS total_departments,
    (SELECT COUNT(*) FROM contact WHERE status = 'Unread') AS unread_messages;

-- ==========================================
-- Triggers for Auto-updating Stats
-- ==========================================

DELIMITER //

CREATE TRIGGER update_appointment_patient_name
AFTER UPDATE ON patients
FOR EACH ROW
BEGIN
    UPDATE appointments 
    SET patient_name = NEW.name 
    WHERE patient_id = NEW.id;
END//

DELIMITER ;

-- ==========================================
-- Sample Queries for Testing
-- ==========================================

-- Get all patients
-- SELECT * FROM patients;

-- Get today's appointments
-- SELECT * FROM appointments WHERE appointment_date = CURDATE();

-- Get prediction history with patient details
-- SELECT ph.*, p.mobile, p.email 
-- FROM prediction_history ph
-- JOIN patients p ON ph.patient_id = p.id
-- ORDER BY ph.prediction_date DESC;

-- Get dashboard statistics
-- SELECT * FROM dashboard_stats;

-- ==========================================
-- Done
-- ==========================================

SELECT 'Database setup completed successfully!' AS message;
SELECT COUNT(*) AS total_patients FROM patients;
SELECT COUNT(*) AS total_doctors FROM doctors;
SELECT COUNT(*) AS total_departments FROM departments;