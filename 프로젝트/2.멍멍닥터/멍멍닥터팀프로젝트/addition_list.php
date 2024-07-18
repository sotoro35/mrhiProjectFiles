<?php
    include $_SERVER['DOCUMENT_ROOT'].'/util/pet/addition_list.php';
    header('Content-Type:text/plain; charset:utf-8');
    $requestData=file_get_contents('php://input');
    $data=json_decode($requestData,true);

    $vaccinationList=array();
    
    $email=$data['email'];
    $provider_id=$data['provider_id'];
    $login_type=$data['login_type'];
    $pet_id=$data['pet_id'];
    $vaccinationList=addition_list($email, $provider_id, $login_type, $pet_id); 

    echo json_encode($vaccinationList);  // 8400 추가접종 목록 성공, 8401 추가접종 목록 실패 4204 서비스 회원 아님 
?>