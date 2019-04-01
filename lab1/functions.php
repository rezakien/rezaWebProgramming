<?php 
function SaveToJSON($filename='results.json',$array){
	$fp = fopen($filename, 'w');
	fwrite($fp, json_encode($array, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
	fclose($fp);
}
?>