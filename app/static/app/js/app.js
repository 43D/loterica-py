var lista = [[0], [0]];

$(function () {
    popular(1);
    $('select').on('change', function () {
        alterar(this);
    });
    $("#receba").click(function () { receba() });
});

function receba() {
    let nuns = []
    for (let i = 1; i <= 6; i++) {
        j = $("#select_" + i + " option:selected").val();
        if (j == 0)
            break;
        nuns.push(j)
    }
    const link = nuns.join("/");
    if (link) {
        const url = "http://127.0.0.1:8000/api/consultar/" + link + "/";
        $.getJSON(url, function (data) {
            preencherDados(data, nuns.join("-"));
        });
    }
}

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
    $('select').each(
        function () {
            if (!$(this).is(":disabled")) {
                const defaultValue = Number($(this).find(":selected")[0].value);
                const id = Number($(this).attr("id").split("select_")[1]);
                $(this).empty();
                $(this).append($('<option>', {
                    value: 0,
                    text: "Selecione " + id + "º valor"
                }));
                for (var i = 1; i <= 60; i++) {
                    if (defaultValue == i) {
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

function preencherDados(json, title) {
    $("#conteudo").removeClass("d-none")
    $("#title").html(title);
    let table = $("#tableBody");
    table.empty();
    $.each(json, function (key, value) {
        make(value, table);
    });
}

function make(json, table) {
    $.each(json, function (key, value) {
        $.each(value, function (k, v) {
            let tr = $("<tr>");
            let td1 = $("<td>");
            let td2 = $("<td>");
            let td3 = $("<td>");
            let td4 = $("<td>");

            td1.html(v.id);
            td2.html(v.contador);
            td3.html(v.media_frequencia);

            td4.append($('<a href="#' + v.id + '">Acessar</a>'));

            tr.append(td1);
            tr.append(td2);
            tr.append(td3);
            tr.append(td4);
            table.append(tr);
        });
    });
}
