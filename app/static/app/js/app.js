lista = [[0], [0]];

$(function () {
    popular(1);
    $('select').on('change', function () {
        alterar(this);
    });

});

function popular(id) {
    var select = $("#select_" + id);
    for (var i = 1; i <= 60; i++) {
        if (-1 == jQuery.inArray(i, lista[0]))
            select.append($('<option>', {
                value: i,
                text: i
            }));
    }
}

function repopular() {
    console.log("repopulando");
    $('select').each(
        function () {
            if (!$(this).is(":disabled")) {
                const defaultValue = Number($(this).find(":selected")[0].value);
                const id = Number($(this).attr("id").split("select_")[1]);
                $(this).empty();
                $(this).append($('<option>', {
                    value: 0,
                    text: "Selecione " +  id + "º valor"
                }));
                for (var i = 1; i <= 60; i++) {
                    if(defaultValue == i){
                        $(this).append($('<option>', {
                            value: i,
                            text: i,
                            selected: true
                        }));
                    }
                    else if (-1 == jQuery.inArray(i, lista[0])) {
                        $(this).append($('<option>', {
                            value: i,
                            text: i
                        }));
                    }
                }
            }
        });
}

function alterar(element) {
    const id = element.id.split("select_")[1];
    const value = element.value;
    if (value === "0") {
        lista[1][0] = Number(id);
        lista[0][id] = 0;
        for (var i = Number(id) + 1; i <= 6; i++)
            desativar(i)
        const j = lista[1].length - 1 - Number(id);
        for (var i = 0; i < j; i++) {
            lista[1].pop();
            lista[0].pop();
        }
        repopular();
    } else {
        lista[0][id] = Number(value);
        lista[1][0] = Number(id);
        lista[1][id] = Number(id);
        if ($("#select_" + (Number(id) + 1)).length)
            ativar((Number(id) + 1));

        console.log("populando");
        const j = lista[1].length;
        for (var i = 1; i < j; i++)
            if (i != Number(id))
                repopular();
    }

}

function ativar(id) {
    $("#select_" + id).prop("disabled", false);
    popular(id);

}
function desativar(id) {
    let element = $("#select_" + id);
    element.prop("disabled", true);
    element.empty();
    element.append($('<option>', {
        value: 0,
        text: "Selecione " + id + "º valor"
    }));
}