$('#send').on('click', function () {

    $.ajax({
        url: $(this).parent('form').attr('action'),
        type: 'post',
        data: $(this).parent('form').serialize()
    }).done(function (data) {
        // テキストボックスを空白にする
        var input_ = document.getElementById('input_')
        input_.value = '';
        // 結果の取得
        // JSONObjectに変換
        var json = JSON.stringify(data);
        //　パース
        var answear = JSON.parse(json).answear;
        var result = JSON.parse(json).result;
        //　表に結果を追加
        addTableRow(answear, result);
    });
    return false;
});

function addTableRow(answear, result) {
    var table = document.getElementById('result');  //表のオブジェクトを取得

    var row = table.insertRow(-1);  //行末に行(tr要素)を追加

    var cell1 = row.insertCell(0);  //セル(td要素)の追加
    var cell2 = row.insertCell(1);

    cell1.innerHTML = answear;   //セルにデータを挿入する
    cell2.innerHTML = result;
}

