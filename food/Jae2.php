 <!DOCTYPE html>
 <?php
	 session_start();
	include_once ("lib/dbconn.php");
	$conn=mysqli_connect("106.10.36.173","Bo","Dhsmfdms?1","food");
	mysqli_query("SET NAMES utf8");
	$Num=$_GET['JR_Num'];
	$query="select JR_1,JR_2,JR_3,JR_4,JR_5,JR_6,JR_7,JR_8,JR_9,JR_10,
			JR_11,JR_12,JR_13,JR_14,JR_15,JR_16,JR_17,JR_18,JR_19,JR_20,
			JR_21,JR_22,JR_23,JR_24,JR_25,JR_26,JR_27,JR_28,JR_29,JR_30 from JaeRyo2 where JR_Num2 like '$Num' ";
	$result=mysqli_query($conn,$query);
	$data=mysqli_fetch_array($result);		
					
						?>
<html lang="ko">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">			

						<font size="5">
								<style>
										a{
											color:black;
										}
										a:hover{
											color:red;
										}
										a:active{
											color:black;
										}
								</style>
							
							<li><strong><a href= "price.php?HM_Jae=<?=$data['JR_1']?>"><?php echo $data['JR_1']?></a>
							<a href= "price.php?HM_Jae=<?=$data['JR_2']?>"><?php echo $data['JR_2']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_3']?>"><?php echo $data['JR_3']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_4']?>"><?php echo $data['JR_4']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_5']?>"><?php echo $data['JR_5']?></strong></a></li>
							<li><strong><a href= "price.php?HM_Jae=<?=$data['JR_6']?>"><?php echo $data['JR_6']?></a>
							<a href= "price.php?HM_Jae=<?=$data['JR_7']?>"><?php echo $data['JR_7']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_8']?>"><?php echo $data['JR_8']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_9']?>"><?php echo $data['JR_9']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_10']?>"><?php echo $data['JR_10']?></strong></a></li>
							<li><strong><a href= "price.php?HM_Jae=<?=$data['JR_11']?>"><?php echo $data['JR_11']?></a>
							<a href= "price.php?HM_Jae=<?=$data['JR_12']?>"><?php echo $data['JR_12']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_13']?>"><?php echo $data['JR_13']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_14']?>"><?php echo $data['JR_14']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_15']?>"><?php echo $data['JR_15']?></strong></a></li>
							<li><strong><a href= "price.php?HM_Jae=<?=$data['JR_16']?>"><?php echo $data['JR_16']?></a>
							<a href= "price.php?HM_Jae=<?=$data['JR_17']?>"><?php echo $data['JR_17']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_18']?>"><?php echo $data['JR_18']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_19']?>"><?php echo $data['JR_19']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_20']?>"><?php echo $data['JR_20']?></strong></a></li>
							<li><strong><a href= "price.php?HM_Jae=<?=$data['JR_21']?>"><?php echo $data['JR_21']?></a>
							<a href= "price.php?HM_Jae=<?=$data['JR_22']?>"><?php echo $data['JR_22']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_23']?>"><?php echo $data['JR_23']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_24']?>"><?php echo $data['JR_24']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_25']?>"><?php echo $data['JR_25']?></strong></a></li>
							<strong><a href= "price.php?HM_Jae=<?=$data['JR_26']?>"><?php echo $data['JR_26']?></a>
							<a href= "price.php?HM_Jae=<?=$data['JR_27']?>"><?php echo $data['JR_27']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_28']?>"><?php echo $data['JR_28']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_29']?>"><?php echo $data['JR_29']?>
							<a href= "price.php?HM_Jae=<?=$data['JR_30']?>"><?php echo $data['JR_30']?></strong></a>
							
							
							
							
							</font>
				
				
		  
    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>
  
 <?php
	
	mysqli_close($conn);
?>

</html>
