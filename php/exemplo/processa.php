<?php

    include'config.php';

    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $idade = $_POST['idade'];

    //inserir variavel no banco

    $sql = "INSERT INTO usuarios (nome, email, idade)
    VALUES('$nome','$email','$idade')";

    if($conexao->query($sql)){
        echo 'dados cadastrados com sucesso!';
    }else{
        echo'Houve erro na conexão';
    }
?>