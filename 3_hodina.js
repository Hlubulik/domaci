
console.log_("jsem tu");

function klik_na_tlacitko() {
    const odpoved = window.prompt("Zadej odpověď");
    console.log(odpoved);
    console.log(document.getElementById("input1"));

    if (odpoved !== null) {
        document.getElementById("input1").value = odpoved;
    }
    //odpoved = 7;

    //console.log(('5' == 5));
    //console.log(('5' === 5));

    //console.log(Math.sin(2*));

    //const A = undefined;
    //console.log(A);
}