let select = document.getElementById("course");
let cyber = document.getElementById("cyber-details");
let cloud = document.getElementById("cloud-details");
let prp = document.getElementById("prp");
let bnkcrd = document.getElementById("bnkcrd");
let reg = document.getElementById("reg");
let pay = document.getElementById("pay");

prp.addEventListener('click', () => {
    if (bnkcrd.style.display === 'none') {
        bnkcrd.style.display = 'block';
    } else {
        bnkcrd.style.display = 'none';
    }
});

pay.addEventListener('click', () => {
    let confirm = document.getElementById("confirm");
    confirm.style.display = 'block';
    if (confirm.style.display = 'block') {
        confirm.innerText = "Proceed to Register";
        confirm.style.color = 'green';
        confirm.style.fontSize = 'x-large';
        reg.style.display = 'block';
    }
});

/* select.addEventListener('change', () => {
    if (select.value === "0") {
        cyber.style.display = 'block';
        cyber.style.display = 'none';
        cloud.style.display = 'none';
    }
    else if (select.value === "Cybersecurity") {
        cyber.style.display = 'block';
        cloud.style.display = 'none';
    }
    else if (select.value === "Cloud Computing (MS Azure)") {
        cyber.style.display = 'none';
        cloud.style.display = 'block';
    }
    else {
        details.style.display = 'none';
    }
})
 */

// document.querySelector('select[name="course"]').addEventListener('change', function() {
//     var selectedCourse = this.value;
    
//     if (selectedCourse === 'Cybersecurity') {
//         document.getElementById('cyber-du').value = '1 month';
//         document.getElementById('cyber-in').value = 'Nwanegbo Uchenna';
//         document.getElementById('cyber-am').value = '$300';
//     } else if (selectedCourse === 'Cloud Computing (MS Azure)') {
//         document.getElementById('cloud-du').value = '1 month';
//         document.getElementById('cloud-in').value = 'Anene Martins';
//         document.getElementById('cloud-am').value = '$300';
//     } else {
//         document.getElementById('hidden-duration').value = '';
//         document.getElementById('hidden-instructor').value = '';
//         document.getElementById('hidden-amount').value = '';
//     }
// });
