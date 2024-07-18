<?php
    function addition_add($email, $provider_id, $login_type, $pet_id,
    $heartworm, $external_parasites, $vaccine, $date, $hospital, $memo) {
        //초기화
        $code="";
        $db=mysqli_connect('localhost','root','mira!643','DogDiseaseApp'); //DogDiseaseApp DB
        mysqli_query($db,"set names utf8");
        
        if ($login_type=="naver" || $login_type=="kakao") {
            $sql= "SELECT * FROM user WHERE provider_id='$provider_id' AND login_type='$login_type'";
        } else if ($login_type=="email") {
            $sql= "SELECT * FROM user WHERE email='$email' AND login_type='$login_type'";
        }
        $result= mysqli_query($db, $sql);
        // 결과표($result)의 총 레코드(한줄:row) 개수
        $rowNum= mysqli_num_rows($result);
        if($rowNum<1) { // 서비스 회원으로 확인되지 않음
            $code= "4204";
        } else { // 서비스 회원으로 확인됨
            $row = mysqli_fetch_array($result);
            $user_id=$row['id'];
            $code=add_process($user_id, $pet_id, $heartworm, $external_parasites, $vaccine, $date, $hospital, $memo, $db);
        }

        mysqli_close($db);
        
        return $code;
    }

    function add_process($user_id, $pet_id, $heartworm, $external_parasites, $vaccine, $date, $hospital, $memo, $db) {
        $now= date('Y-m-d H:i:s');
        $sql= "
        INSERT INTO addition_vaccination(
            user_id, 
            pet_id,
            heartworm,
            external_parasites,
            vaccine, 
            date, 
            hospital,
            memo) 
        SELECT
            u.id,
            '$pet_id',
            '$heartworm',
            '$external_parasites',
            '$vaccine',
            '$date',
            '$hospital',
            '$memo'
        FROM user AS u
        WHERE u.id = '$user_id'";
        $result= mysqli_query($db, $sql);
        if($result) { // 추가접종 추가 성공시
            $code="8500";
        }
        else { // 추가접종 추가 실패시 
            $code="8501";
        }
        return $code;
    }
?>