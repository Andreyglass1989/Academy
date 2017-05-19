$(document).ready(function() {

    $(".click_me_player").click(function() {
        $(".clicked_player").toggleClass("clicked_player");
        $(this).toggleClass("clicked_player");
    });

    $(".click_me_enemy").click(function() {
        $(".clicked_enemy").toggleClass("clicked_enemy");
        $(this).toggleClass("clicked_enemy");
    });

    $("#room").data("id")

    $("#fight").click(function() {
            var $players = $('#players');
            var $enemys = $('#enemys');
            var $gameresult = $('#gameresult');
            $.ajax({
                    type: "GET",
                    url: "/attack/",
                    data: {
                        'partEnemy': $(".clicked_enemy").data('part'),
                        'partPlayer': $(".clicked_player").data('part'),
                        'enemyId': $(".player_name").data('id'),
                        'playerId': $(".enemy_name").data('id'),
                    },
                    cache: false,
                    success: function(data) {
                        console.log(data);
                        if (data == "You LOST") {
                            console.log("GameOver! You LOST!!!");
                            $("#gameresult").html("<h1>GameOver! You LOST!!!</h1>");
                            $(".player").fadeOut('slow');
                            $("#player, .progress, .player_name, table, col-xs-6").fadeOut('slow');
                            document.getElementById('fight').disabled = true;
                            alert("GameOver! You LOST!!!:)");

                            $('.click_me_enemy').click(function(data) {
                                document.location.href="/"
                                });

                            $('.enemy_name, col-xs-3').mouseenter(function() {
                            $(this).effect('bounce', {times:3}, 500);
                                });


                        }
                        else
                        {   console.log("fight time");
                        };
                        if (data == "You WIN")
                        {
                            console.log("GameOver! You WIN!!!");
                            $("#gameresult").html("<h1>GameOver! You WIN!!!</h1>");
                            $(".enemy").fadeOut('slow');
                            $("#enemy, .progress, .enemy_name, table, col-xs-6").fadeOut('slow');
                            document.getElementById('fight').disabled = true;
                            alert("GameOver! You WIN!!!:)");
                            }
                        else {
                            console.log("fight time");
                        };

                        if (data == "DRAW")
                        {
                            console.log("GameOver! DRAW!!!");
                            $("#gameresult").html("<h1>GameOver! DRAW!!!</h1>");
                            $(".enemy").fadeOut('slow');
                            $("#enemy, .progress, .enemy_name, table, col-xs-6").fadeOut('slow');
                            document.getElementById('fight').disabled = true;
                            alert("GameOver! DRAW!!!:)");
                            }
                        else {
                            console.log("fight time");
                        };


                        var obj = jQuery.parseJSON(data);
                        $("#enemy").css("width", obj.healthEnemy + "%");
                        $("#player").css("width", obj.healthPlayer + "%");
                        $('#players').append('<tr><td>' + obj.Player_Target + '</td><td>' + obj.Player_Block + '</td>');
                        $('#player_health').html(obj.healthPlayer)
                        $('#enemy_health').html(obj.healthEnemy)
                        $('#enemys').append('<tr><td>' + obj.Enemy_Target + '</td><td>' + obj.Enemy_Block + '</td>');



            },
    });
  });
});