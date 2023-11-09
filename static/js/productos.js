function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function setOption(option) {
    document.getElementById("myDropdown").classList.remove("show");
    document.querySelector('.dropbtn').innerHTML = document.getElementById(option).text;

    // Quitar la clase 'selected' de todas las opciones
    var dropdownItems = document.querySelectorAll('.dropdown-content a');
    dropdownItems.forEach(function(item) {
        item.classList.remove('selected');
    });

    // Agregar la clase 'selected' a la opción seleccionada
    document.getElementById(option).classList.add('selected');
}