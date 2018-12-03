<?
$connect = mysqli_connect('210.117.181.105','Bo','Dhsmfdms?1');

if($connect)
{
	echo "connect.<br>";
	echo "<hr>";
	
}
else
{
	echo "<br>";
	echo "mysql fail";
}

mysqli_close($connect);
?>