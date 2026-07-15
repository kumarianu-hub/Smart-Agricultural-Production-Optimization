document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (event) {

            const farmer = document.querySelector("input[name='farmer']").value.trim();
            const area = document.querySelector("input[name='area']").value;

            if (farmer === "") {
                alert("Please enter Farmer Name");
                event.preventDefault();
                return;
            }

            if (area === "" || parseFloat(area) <= 0) {
                alert("Please enter a valid land area");
                event.preventDefault();
                return;
            }

        });

    }

});