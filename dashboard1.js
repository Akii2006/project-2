/* =====================================
   PATIENT MANAGEMENT JAVASCRIPT
===================================== */


/* ===============================
   PAGE LOAD ANIMATION
================================ */

document.addEventListener("DOMContentLoaded", () => {

    document.body.classList.add("loaded");

});





/* ===============================
   NUMBER COUNTER ANIMATION
================================ */


const counters = document.querySelectorAll(".stat-card h3");


counters.forEach(counter => {


    let target = Number(counter.innerText);

    let count = 0;


    let speed = target / 80;


    let updateCounter = () => {


        if (count < target) {


            count += speed;


            counter.innerText = Math.ceil(count);


            setTimeout(updateCounter, 20);


        } else {


            counter.innerText = target;


        }


    };


    updateCounter();


});







/* ===============================
   SEARCH TABLE FILTER
================================ */


const searchInput = document.querySelector(".search-box input");


if (searchInput) {


    searchInput.addEventListener("keyup", () => {


        let value = searchInput.value.toLowerCase();


        let rows = document.querySelectorAll(
            ".custom-table tbody tr"
        );



        rows.forEach(row => {


            let text = row.innerText.toLowerCase();


            if (text.includes(value)) {


                row.style.display = "";


                row.style.animation =
                    "fadeIn .5s";


            } else {


                row.style.display = "none";


            }


        });



    });


}







/* ===============================
   STATUS HOVER EFFECT
================================ */


const status =
    document.querySelectorAll(".status");


status.forEach(item => {


    item.addEventListener("mouseenter", () => {


        item.style.transform = "scale(1.1)";


    });


    item.addEventListener("mouseleave", () => {


        item.style.transform = "scale(1)";


    });


});






/* ===============================
   ACTION BUTTON ANIMATION
================================ */


const buttons =
    document.querySelectorAll(".action-btn");


buttons.forEach(btn => {


    btn.addEventListener("click", function() {


        this.style.transform =
            "scale(1.3)";


        setTimeout(() => {


            this.style.transform =
                "";


        }, 200);


    });


});







/* ===============================
   DELETE CONFIRMATION
================================ */


const deleteButtons =
    document.querySelectorAll(".delete");


deleteButtons.forEach(button => {


    button.addEventListener("click", () => {


        let result =
            confirm(
                "Are you sure you want to delete this patient?"
            );



        if (result) {


            let row =
                button.closest("tr");


            row.style.animation =
                "fadeOut .5s";


            setTimeout(() => {


                row.remove();


            }, 500);


        }



    });


});






/* ===============================
   ADD PATIENT BUTTON EFFECT
================================ */


const addButton =
    document.querySelector(".add-btn");


if (addButton) {


    addButton.addEventListener("click", () => {


        alert(
            "Open Patient Registration Form"
        );


    });


}







/* ===============================
   SEARCH BUTTON EFFECT
================================ */


const searchButton =
    document.querySelector(".search-btn");


if (searchButton) {


    searchButton.addEventListener("click", () => {


        searchButton.innerHTML =
            `
<i class="bi bi-hourglass-split"></i>
 Searching...
`;



        setTimeout(() => {


            searchButton.innerHTML =
                `
<i class="bi bi-search"></i>
 Search Patient
`;



        }, 1500);



    });


}






/* ===============================
   EXPORT BUTTON
================================ */


const exportBtn =
    document.querySelector(".btn-outline-primary");


if (exportBtn) {


    exportBtn.addEventListener("click", () => {


        alert(
            "Patient report exported successfully!"
        );


    });


}






/* ===============================
   TABLE ROW CLICK EFFECT
================================ */


const tableRows =
    document.querySelectorAll(".custom-table tbody tr");


tableRows.forEach(row => {


    row.addEventListener("click", () => {


        tableRows.forEach(r => {

            r.classList.remove("selected");

        });


        row.classList.add("selected");


    });


});







/* ===============================
   FADE OUT ANIMATION
================================ */


const style =
    document.createElement("style");


style.innerHTML = `

@keyframes fadeOut{

from{

opacity:1;
transform:translateX(0);

}

to{

opacity:0;
transform:translateX(100px);

}

}


.selected{

background:
rgba(37,99,235,.12)!important;

transform:
scale(1.02);

}

`;


document.head.appendChild(style);
