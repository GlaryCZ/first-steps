var selectedValues = []; // Pole pro ukládání hodnot z tlačítek
const operators = ["*", "/", "+", "-"]

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
    for (i = 0; i < operators.length; i++) {
        while (negr.includes(operators[i])) {
            var cislo = 0
            var cisla = []
            // r1 = /[0-9]+[.]?[0-9]*[*][0-9]+[.]?[0-9]*/g
            var r1 = new RegExp(`[0-9]+[.]?[0-9]*[${operators[i]}][0-9]+[.]?[0-9]*`);
            var results = negr.match(r1);
            for (let j = 0; j < results.length; j++) {
                cisla = results[j].split(operators[i])
                if (operators[i] == "*") {
                    cislo = parseFloat(cisla[0]) * parseFloat(cisla[1])
                } else if (operators[i] == "/") {
                    cislo = parseFloat(cisla[0]) / parseFloat(cisla[1])
                } else if (operators[i] == "+") {
                    cislo = parseFloat(cisla[0]) + parseFloat(cisla[1])
                } else if (operators[i] == "-") {
                    cislo = parseFloat(cisla[0]) - parseFloat(cisla[1])
                } else { alert("CRITICAL ERROR") }
                negr = negr.replace(results[j], cislo.toString())
            }
        }
    }
    document.getElementById("vysledek").innerHTML = negr;
}