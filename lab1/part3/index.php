<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json,charset=utf-8",true);
function PushArr($arr,$existing_array){
	return $existing_array = array_merge($existing_array,$arr);
}
$METHOD = $_SERVER['REQUEST_METHOD'];
if($METHOD=='GET'){
	if(isset($_GET['date'])){
		$date = $_GET['date']; // get param
	}
	else{
		$date = date('d.m.Y',strtotime('now')); //default date
	}
	$dates = ['2016-12-15'];
	$days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда','Четверг', 'Пятница', 'Суббота'];
    $res=  array(['Дата' => $date, 'День недели' => $days[date("w", strtotime($date) )]
    ]);
    echo json_encode($res,JSON_UNESCAPED_UNICODE);
}
?>