    function generate_form() {
        $('#gen').html('<form class="main-form" action="/sys_change/?ref={{ referal }}" method="get"> <h3>Обменять BTC в RUB</h3> <div class="input-group mb-3"> <input type="text" name="name" class="form-control" placeholder="Имя" required> </div> <div class="input-group mb-3"> <input type="email" name="mail" class="form-control" placeholder="Ваш Email" required> </div> <h5>Вы хотите перевести</h5> <div class="input-group mb-3"> <input type="number" step="0.001" name="count" class="form-control" placeholder="Сумма в BTC" required> <label><b>Вам будет переведено: <span class="ee1">0</span>₽ (с вычетом комиссии <span class="ee2">0</span>₽)</b></label> <label>* Необходимо для отслеживания перевода, переводите точно указанную сумму.</label> </div> <h5>Перевод на</h5> <div class="input-group mb-3"> <input type="text" class="form-control" name="card" id="cc-number" placeholder="Номер банковской карты" required="" pattern="[0-9]{16}"> <div class="invalid-feedback"> Номер кредитной карты должен содержать 16 цифр </div> <label>* Переводы осуществляются на Сбербанк, Тинькофф, Альфа-банк, ВТБ-24.</label> </div> <div class="input-group mb-3"> <input type="text" name="referal" class="form-control" placeholder="Реферальный № (можно не заполнять)"> </div> <button type="submit" class="btn btn-success" id="change">Обменять</button> <div class="btn btn-success" onclick="testing()">Тестировать</div> </form>');
    }

    // Проверка правильности номера кредитной карты

        function check_card() {
            var card = $('input[name="card"]').val();
            if (card.length != 16 || isNaN(card)) {
                $('#change').css('display', 'none');
            } else {
                $('#change').css('display', 'inline-block');
            }
        }

        $('input[name="card"]').on('input', check_card)

    function test(value) {
        $('input[name="name"]').val('Test');
        $('input[name="mail"]').val('qwe@rty.uio');
        $('input[name="count"]').val('1');

        $('input[name="card"]').val(value);

        // $('#change').trigger('click');
        check_card();

        // var form = $('form')[0];
        // return form.checkValidity();
        return !($('#change').css('display') == 'none');
    }

    function testing() {
        var test1 = test('12345');
        var test2 = test('1234123412341234');
        var test3 = test('123412341234123h');

        if (test1 == false && test2 == true && test3 == false) {
            $('#testing').html('<h4><span class="badge badge-success">OK</span></h4><br>');
        } else {
            $('#testing').html('<h4><span class="badge badge-danger">Error</span></h4><br>');
        }
    }