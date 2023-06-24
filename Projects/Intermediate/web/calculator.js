var selectedValues = []; // Pole pro ukládání hodnot z tlačítek

function storeValue(button) {
    var value = button.innerHTML;
    selectedValues.push(value); // Přidání hodnoty do pole
    document.getElementById("priklad").innerHTML = selectedValues;
}

function clear_sel_values() {
    selectedValues = []
    document.getElementById("priklad").innerHTML = selectedValues;
    document.getElementById("vysledek").innerHTML = "";
}

function updateResult() {
    var sum = parseInt(selectedValues[0]) + parseInt(selectedValues[1]);
    document.getElementById("demo").innerHTML = sum;
}

function getPriklad() {
    var res = ""
    for (let i = 0; i < selectedValues.length; i++) {
        res = res + selectedValues[i];
    }
    res = res + " = ";
    document.getElementById("priklad").innerHTML = res;
    getVysledek(res)
}


function getVysledek(negr) {
    negr = negr.replace(" = ", "")
    // najdi nasobeni
    while (negr.includes("*")) {
        var cislo = 0
        var cisla = []
        r1 = /[0-9]+[.]?[0-9]*[*][0-9]+[.]?[0-9]*/g
        var results = negr.match(r1);
        for (let i = 0; i < results.length; i++) {
            cisla = results[i].split("*")
            cislo = parseFloat(cisla[0]) * parseFloat(cisla[1])
            negr = negr.replace(results[i], cislo.toString())
        }
    }
    document.getElementById("vysledek").innerHTML = negr;
}