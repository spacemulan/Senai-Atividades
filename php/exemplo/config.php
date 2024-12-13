<?php

$servidor = 'localhost';
$login = 'root';
$senha = '';
$bd = 'exemplo_db';

$conexao = new mysqli($servidor, $login, $senha, $bd);

// if($conexao->connect_error){
//    echo 'ERRO!!';
// }else{
//    echo'Conexão efetuada com sucesso!!';    }

  
?>