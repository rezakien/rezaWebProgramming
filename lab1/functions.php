<?php 
function SaveToJSON($filename,$array){
	if(file_exists('../'.$filename)){
		if(file_get_contents('../'.$filename)!=null){
			$jsondata = file_get_contents('../'.$filename);
			$arr_data = json_decode($jsondata, true);
			array_push($arr_data,$array);
			$jsondata = json_encode($arr_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
			file_put_contents('../'.$filename, $jsondata);
		}
		
	}
	else{
		$fp = fopen('../'.$filename, 'w');
		fwrite($fp, json_encode($array, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE)) or die('error');
		fclose($fp);
		}
}
?>