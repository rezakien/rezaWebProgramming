<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json,charset=utf-8",true);
function PushArr($arr,$existing_array){
	return $existing_array = array_merge($existing_array,$arr);
}
include '../functions.php';
$METHOD = $_SERVER['REQUEST_METHOD'];
if($METHOD=='GET'){
	if(isset($_GET['path'])){
		if(is_numeric(explode('/', $_GET['path'])[0])){
			$N = explode('/', $_GET['path'])[0];
			$i = 0;
			$a = 0; $b = 1;
			$fib = 0;
			while($i<$N){
				$fib = $b + $a;
				$a = $b;
				$b = $fib;
				$i++;
			}
			echo json_encode(array('Число Фибоначчи'=>$fib),JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
			SaveToJSON('lab1.json',array('Число Фибоначчи'=>$fib));
		}
	}
}

?>