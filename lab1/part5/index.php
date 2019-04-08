<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json,charset=utf-8",true);
include '../functions.php';
function PushArr($arr,$existing_array){
	return $existing_array = array_merge($existing_array,$arr);
}
$METHOD = $_SERVER['REQUEST_METHOD'];
$URI = $_SERVER['REQUEST_URI'];
if($METHOD=='GET'){
	if(isset($_GET['city'])){
		$citiesFile = fopen("cities.txt", "r") or die("Невозможно открыть файл!");
		$cities = array();
		while(!feof($citiesFile)) {
			$city = explode('|',trim(fgets($citiesFile)));
			
			$cities[$city[0]] = $city[1];
		}
		fclose($citiesFile);
		if(isset($cities[$_GET['city']]))
			$res = array('Номер города'=>$_GET['city'],'Город'=>$cities[$_GET['city']]);
			echo json_encode($res,JSON_UNESCAPED_UNICODE);
			$URI = $_SERVER['REQUEST_URI'];
			$result = array('url' => 'http://localhost'.$URI ,'response'=> $res,'method'=>$METHOD);
			SaveToJSON('lab1.json',$result);
		}
}

?>