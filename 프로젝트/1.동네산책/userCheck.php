<?php
    header('Content-Type:text/plain; charset=utf-8');

    $nickname= $_GET['nickname'];
    $email= $_GET['email'];

    // 서버에 접속
    $db= mysqli_connect("localhost","ruaris","a1s2d3f4!","ruaris");
    mysqli_query($db,"set names utf8"); // 한글 깨지지 않게 설정


    $sqlname = "SELECT * FROM userData WHERE nickname = '$nickname'";
    $result= mysqli_query($db,$sqlname);

    $conunt= mysqli_num_rows($result);

    if($conunt > 0) {
        echo "이미 사용중입니다";
    } else {
        echo "사용가능합니다";
    }

    mysqli_close($db)

?>

