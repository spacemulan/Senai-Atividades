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
        $filhos = $_POST['filhoss'];
        $cargos = $_POST['CARGOS'];
        $lista = $_POST['lista'];
        $salario = $_POST['salarios'];

        $aumento = $salario; 
        if ($filhos >= 2) {
            $aumento += $salario * 0.05;
        }
        
        if ($lista == 'mestrado' || $lista == 'doutorado') {
            $aumento += $salario * 0.1;
        }
        
        if ($cargos == 'professor') {
            $aumento += 50;
        } elseif ($cargos == 'coordenador') {
            $aumento += 650;
        } elseif ($cargos == 'superintendente') {
            $aumento += 900;
        } elseif ($cargos == 'diretor') {
            $aumento += 2000;
        }
        
        echo "<h2>Olá {$nome}, <br> seu  salário com aumento é <br> R$ {$aumento} </h2>";
        ?>
    </div>
</body>
</html>