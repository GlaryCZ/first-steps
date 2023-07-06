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
    for (var i = 0; i < operators.length; i++) {
        while (negr.includes(operators[i]) && (negr.charAt(0) != "-")) {
            var cislo = 0
            var cisla = []
            var r1 = new RegExp(`[0-9]+[.]?[0-9]*[${operators[i]}][0-9]+[.]?[0-9]*`);
            var results = negr.match(r1); // 5+59*5
            for (let j = 0; j < results.length; j++) { // 59*5
                cisla = results[j].split(operators[i]) //[59, 5]
                if (operators[i] == "*") {
                    cislo = (parseFloat(cisla[0])) * (parseFloat(cisla[1]))
                } else if (operators[i] == "/") {
                    cislo = (parseFloat(cisla[0])) / (parseFloat(cisla[1]))
                } else if (operators[i] == "+") {
                    cislo = (parseFloat(cisla[0])) + (parseFloat(cisla[1]))
                } else if (operators[i] == "-") {
                    cislo = (parseFloat(cisla[0])) - (parseFloat(cisla[1]))
                } else { alert("CRITICAL ERROR") }
                negr = negr.replace(results[j], cislo.toString()) // 300
            }
        }
    }


    document.getElementById("vysledek").innerHTML = negr

}