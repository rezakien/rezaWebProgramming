<?php
/**
 * Database Class
 */
class Database
{
	protected $db_host = '';
	protected $db_password = '';
	protected $db_username = '';
	protected $db_name = '';
	function __construct($db_name,$password='',$username = 'root')
	{
		$this->db_host = 'localhost';
		$this->db_password = '';
		$this->db_username = 'localhost';
	}
}
?>