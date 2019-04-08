<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json,charset=utf-8",true);
include '../functions.php';

function PushArr($arr,$existing_array){
	return $existing_array = array_merge($existing_array,$arr);
}
$METHOD = $_SERVER['REQUEST_METHOD'];
if($METHOD=='GET'){
	$res = '';
	$resArray = array('httpResponse' =>  http_response_code());
	if(isset($_GET) && !empty($_GET)){
		$_params = $_GET;
		if(isset($_GET['a'])&&isset($_GET['b'])&&isset($_GET['c'])){
			$a = $_GET['a'];
			$b = $_GET['b'];
			$c = $_GET['c'];
			$d = pow($b, 2) - 4*$a*$c;
			if($d>0){
				$response = array('x1'=>(-$b+sqrt($d))/2*$a,'x2'=>(-$b-sqrt($d))/2*$a);
			}
			elseif ($d==0) {
				$response = array('x'=>(-$b)/2*$a);
			}
			elseif ($d<0) {
				$response = array('response'=>'Дискриминант меньше 0');
			}
			$resArray = PushArr($response,$resArray);
		}
		else{
			$error_ParamsNotExist = array('Error'=>'Not all params are executed'); 
			$resArray = PushArr($error_ParamsNotExist,$resArray);
		}
		//$resArray = PushArr($_params,$resArray);
		$res = json_encode($resArray,JSON_UNESCAPED_UNICODE);
	}
	echo($res);
	$URI = $_SERVER['REQUEST_URI'];
	$result = array('url' => 'http://localhost'.$URI ,'response'=> $resArray,'method'=>$METHOD);
	SaveToJSON('lab1.json',$result);
}

?>