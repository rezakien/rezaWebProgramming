<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json,charset=utf-8",true);

$METHOD = $_SERVER['REQUEST_METHOD'];
$URI = $_SERVER['REQUEST_URI'];

if($METHOD=='GET'){
	if(isset($_GET['path'])){
		if(is_numeric(explode('/', $_GET['path'])[0])){
		echo explode('/', $_GET['path'])[0];
		}
	}
}
?>