<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
    <div class="caixa">
    <?php
        $nome = $_POST['nome'];
        $peso = $_POST['peso'];
        $altura =number_format($_POST['altura'], 2);
        $hiper = $_POST['hiper'];

        $imc = round($peso/($altura*$altura),2);

        if($imc<18.5){
        $situacao = 'Magro';
        }elseif($imc>=18.5 and $imc<25){
        $situacao = 'Normal';
        }elseif($imc>=25 and $imc<35){
        $situacao = 'Sobrepeso';
    }elseif($imc>=30 and $imc<35){
        $situacao = 'Obesidade leve';
        
    }elseif($imc>=30 and $imc<35 and $hiper=='sim'){
        $situacao = 'Obesidade leve e perigosa';
    }elseif($imc>=35 and $hiper=='sim'){
        $situacao = 'Obesidade grau II e hipertenso';
    }elseif($imc>=35 and $hiper=='nao'){
        $situacao = 'Obesidade grau II';
       
    }
    echo"<h2> Olá {$nome}, seu imc é {$imc} <br> você está {$situacao}</h2>";
?>

    </div>
</body>
</html>