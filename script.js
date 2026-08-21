// ======================================
// Healthcare Disease Prediction System
// script.js
// ======================================

// ======================================
// Page Loaded - DOM Ready
// ======================================
document.addEventListener("DOMContentLoaded", function() {

    console.log("Healthcare ML Website Loaded Successfully");

    // Active Navbar - highlight current page
    const currentPage = window.location.pathname.split("/").pop();
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (href === currentPage || (currentPage === "" && href === "index.html")) {
            link.classList.add("active");
        }
    });

    // Set current date if element exists
    const dateElement = document.getElementById("currentDate");
    if (dateElement) {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        dateElement.innerHTML = now.toLocaleDateString('en-US', options);
    }

    // Initialize current time
    updateTime();
    setInterval(updateTime, 1000);

    // Hide loader if exists
    const loader = document.getElementById("loader");
    if (loader) {
        loader.style.display = "none";
    }

    // Auto-hide flash messages after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const closeBtn = alert.querySelector('.btn-close');
            if (closeBtn) {
                closeBtn.click();
            }
        }, 5000);
    });

});

// ======================================
// Update Current Time
// ======================================
function updateTime() {
    const timeElement = document.getElementById("currentTime");
    if (timeElement) {
        const now = new Date();
        timeElement.innerHTML = now.toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
    }
}

// ======================================
// Smooth Scroll for Anchor Links
// ======================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        const targetId = this.getAttribute("href");
        if (targetId !== "#") {
            e.preventDefault();
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        }
    });
});

// ======================================
// Patient Registration Form Validation
// ======================================
function validateRegisterForm() {
    const name = document.getElementById("name");
    const email = document.getElementById("email");
    const mobile = document.getElementById("mobile");
    const password = document.getElementById("password");
    const confirm = document.getElementById("confirm_password");

    // Check required fields
    if (name && name.value.trim() === "") {
        alert("Please enter your full name.");
        name.focus();
        return false;
    }

    if (email && email.value.trim() === "") {
        alert("Please enter your email address.");
        email.focus();
        return false;
    }

    // Email validation
    if (email && !isValidEmail(email.value)) {
        alert("Please enter a valid email address.");
        email.focus();
        return false;
    }

    if (mobile && mobile.value.trim() === "") {
        alert("Please enter your mobile number.");
        mobile.focus();
        return false;
    }

    // Mobile validation (10 digits)
    if (mobile && !/^\d{10}$/.test(mobile.value.trim())) {
        alert("Please enter a valid 10-digit mobile number.");
        mobile.focus();
        return false;
    }

    if (password && password.value === "") {
        alert("Please enter a password.");
        password.focus();
        return false;
    }

    if (password && confirm) {
        if (password.value !== confirm.value) {
            alert("Password and Confirm Password do not match.");
            confirm.focus();
            return false;
        }
        if (password.value.length < 6) {
            alert("Password must be at least 6 characters long.");
            password.focus();
            return false;
        }
    }

    alert("Registration Successful! Please login.");
    return true;
}

// ======================================
// Email Validation Helper
// ======================================
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// ======================================
// Patient Login Validation
// ======================================
function validateLoginForm() {
    const email = document.getElementById("email");
    const password = document.getElementById("password");

    if (email && email.value.trim() === "") {
        alert("Please enter your email address.");
        email.focus();
        return false;
    }

    if (email && !isValidEmail(email.value)) {
        alert("Please enter a valid email address.");
        email.focus();
        return false;
    }

    if (password && password.value === "") {
        alert("Please enter your password.");
        password.focus();
        return false;
    }

    return true;
}

// ======================================
// Patient Login Success
// ======================================
function loginSuccess() {
    alert("Login Successful! Redirecting to Dashboard...");
    return true;
}

// ======================================
// Appointment Booking Validation
// ======================================
function validateAppointment() {
    const patientName = document.getElementById("patient_name") || document.querySelector('input[name="patient_name"]');
    const email = document.getElementById("email") || document.querySelector('input[name="email"]');
    const mobile = document.getElementById("mobile") || document.querySelector('input[name="mobile"]');
    const department = document.getElementById("department") || document.querySelector('select[name="department"]');
    const doctor = document.getElementById("doctor") || document.querySelector('select[name="doctor"]');
    const date = document.getElementById("appointment_date") || document.querySelector('input[name="appointment_date"]');
    const time = document.getElementById("appointment_time") || document.querySelector('input[name="appointment_time"]');

    if (patientName && patientName.value.trim() === "") {
        alert("Please enter patient name.");
        patientName.focus();
        return false;
    }

    if (email && email.value.trim() === "") {
        alert("Please enter email address.");
        email.focus();
        return false;
    }

    if (email && !isValidEmail(email.value)) {
        alert("Please enter a valid email address.");
        email.focus();
        return false;
    }

    if (mobile && mobile.value.trim() === "") {
        alert("Please enter mobile number.");
        mobile.focus();
        return false;
    }

    if (mobile && !/^\d{10}$/.test(mobile.value.trim())) {
        alert("Please enter a valid 10-digit mobile number.");
        mobile.focus();
        return false;
    }

    if (department && department.value === "") {
        alert("Please select a department.");
        department.focus();
        return false;
    }

    if (doctor && doctor.value === "") {
        alert("Please select a doctor.");
        doctor.focus();
        return false;
    }

    if (date && date.value === "") {
        alert("Please select appointment date.");
        date.focus();
        return false;
    }

    if (time && time.value === "") {
        alert("Please select appointment time.");
        time.focus();
        return false;
    }

    alert("Appointment Booked Successfully!");
    return true;
}

// ======================================
// Disease Prediction
// ======================================
function predictDisease() {
    const symptoms = document.getElementById("symptoms");

    if (symptoms && symptoms.value.trim() === "") {
        alert("Please enter your symptoms.");
        symptoms.focus();
        return false;
    }

    // Get all symptom checkboxes
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    let anyChecked = false;
    checkboxes.forEach(cb => {
        if (cb.checked) anyChecked = true;
    });

    if (!anyChecked && !symptoms) {
        alert("Please select at least one symptom or describe your symptoms.");
        return false;
    }

    alert("Analyzing symptoms using Machine Learning...\nPlease wait for the prediction result.");
    return true;
}

// ======================================
// Contact Form
// ======================================
function validateContactForm() {
    const name = document.getElementById("name") || document.querySelector('input[name="name"]');
    const email = document.getElementById("email") || document.querySelector('input[name="email"]');
    const subject = document.getElementById("subject") || document.querySelector('input[name="subject"]');
    const message = document.getElementById("message") || document.querySelector('textarea[name="message"]');

    if (name && name.value.trim() === "") {
        alert("Please enter your name.");
        name.focus();
        return false;
    }

    if (email && email.value.trim() === "") {
        alert("Please enter your email address.");
        email.focus();
        return false;
    }

    if (email && !isValidEmail(email.value)) {
        alert("Please enter a valid email address.");
        email.focus();
        return false;
    }

    if (subject && subject.value.trim() === "") {
        alert("Please enter a subject.");
        subject.focus();
        return false;
    }

    if (message && message.value.trim() === "") {
        alert("Please enter your message.");
        message.focus();
        return false;
    }

    alert("Thank you! We will contact you soon.");
    return true;
}

// ======================================
// Search Table Function
// ======================================
function searchTable() {
    const input = document.getElementById("searchInput");
    if (!input) return;

    const filter = input.value.toUpperCase();
    const table = document.getElementById("dataTable");
    if (!table) return;

    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");
        let found = false;
        for (let j = 0; j < cells.length; j++) {
            const text = cells[j].textContent || cells[j].innerText;
            if (text.toUpperCase().indexOf(filter) > -1) {
                found = true;
                break;
            }
        }
        rows[i].style.display = found ? "" : "none";
    }
}

// ======================================
// Delete Confirmation
// ======================================
function deleteRecord(recordId, recordName) {
    const message = recordName ?
        `Are you sure you want to delete "${recordName}"?` :
        "Are you sure you want to delete this record?";
    return confirm(message);
}

// ======================================
// Toggle Password Visibility
// ======================================
function togglePasswordVisibility(inputId) {
    const input = document.getElementById(inputId);
    if (!input) return;

    const icon = document.querySelector(`[onclick="togglePasswordVisibility('${inputId}')"] i`);
    if (input.type === "password") {
        input.type = "text";
        if (icon) {
            icon.className = "bi bi-eye-slash";
        }
    } else {
        input.type = "password";
        if (icon) {
            icon.className = "bi bi-eye";
        }
    }
}

// ======================================
// Scroll To Top
// ======================================
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// ======================================
// Show/Hide Password Toggle (Generic)
// ======================================
function togglePassword() {
    const passwordField = document.getElementById("password");
    if (!passwordField) return;

    const icon = document.querySelector("#togglePasswordIcon");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        if (icon) {
            icon.className = "bi bi-eye-slash";
        }
    } else {
        passwordField.type = "password";
        if (icon) {
            icon.className = "bi bi-eye";
        }
    }
}

// ======================================
// Print Report
// ======================================
function printReport() {
    window.print();
}

// ======================================
// Export Table to CSV
// ======================================
function exportToCSV(tableId, filename) {
    const table = document.getElementById(tableId);
    if (!table) return;

    let csv = [];
    const rows = table.querySelectorAll("tr");

    for (let i = 0; i < rows.length; i++) {
        const row = [];
        const cells = rows[i].querySelectorAll("td, th");
        for (let j = 0; j < cells.length; j++) {
            let text = cells[j].textContent.trim();
            // Remove action buttons and other HTML
            text = text.replace(/[^a-zA-Z0-9\s\-.,%]/g, '');
            row.push('"' + text + '"');
        }
        csv.push(row.join(","));
    }

    const csvContent = csv.join("\n");
    const blob = new Blob([csvContent], { type: "text/csv" });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename || "export.csv";
    a.click();
    window.URL.revokeObjectURL(url);
}

// ======================================
// Dashboard Welcome Message
// ======================================
function dashboardWelcome() {
    const welcomeElement = document.getElementById("welcomeMessage");
    if (welcomeElement) {
        const hour = new Date().getHours();
        let greeting = "Good Morning";
        if (hour >= 12 && hour < 17) greeting = "Good Afternoon";
        else if (hour >= 17 && hour < 21) greeting = "Good Evening";
        else if (hour >= 21 || hour < 5) greeting = "Good Night";
        welcomeElement.innerHTML = `${greeting}! Welcome to Healthcare ML Dashboard`;
    }
}

// ======================================
// Initialize Dashboard
// ======================================
if (document.getElementById("dashboardStats")) {
    dashboardWelcome();
}

// ======================================
// Toast Notification Helper
// ======================================
function showToast(message, type) {
    const toastContainer = document.getElementById("toastContainer");
    if (!toastContainer) return;

    const colors = {
        success: "bg-success",
        danger: "bg-danger",
        warning: "bg-warning",
        info: "bg-info"
    };

    const toast = document.createElement("div");
    toast.className = `toast align-items-center text-white ${colors[type] || 'bg-primary'} border-0`;
    toast.setAttribute("role", "alert");
    toast.setAttribute("aria-live", "assertive");
    toast.setAttribute("aria-atomic", "true");

    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;

    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();

    setTimeout(() => {
        toast.remove();
    }, 5000);
}

// ======================================
// Form Auto-Save (Local Storage)
// ======================================
function autoSaveForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return;

    const inputs = form.querySelectorAll("input, textarea, select");
    inputs.forEach(input => {
        input.addEventListener("change", function() {
            const data = {};
            inputs.forEach(el => {
                if (el.name) {
                    data[el.name] = el.value;
                }
            });
            localStorage.setItem(`form_${formId}`, JSON.stringify(data));
        });
    });

    // Load saved data
    const saved = localStorage.getItem(`form_${formId}`);
    if (saved) {
        try {
            const data = JSON.parse(saved);
            inputs.forEach(el => {
                if (el.name && data[el.name]) {
                    el.value = data[el.name];
                }
            });
        } catch (e) {
            console.log("Error loading saved form data");
        }
    }
}

// ======================================
// Console Helpers
// ======================================
console.log("%c Healthcare Disease Prediction System ", "background:#0d6efd;color:white;padding:10px;font-size:18px;border-radius:5px;");
console.log("%c Version 2.0 | Developed with ❤️ ", "color:#0d6efd;font-size:14px;");
