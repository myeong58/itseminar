 <!DOCTYPE html>
 <?php
	 session_start();
	include_once ("lib/dbconn.php");
	$conn=mysqli_connect("106.10.36.173","Bo","Dhsmfdms?1","food");
	$query="select JR_1,JR_2,JR_3,JR_4,JR_5,JR_6,JR_7,JR_8,JR_9,JR_10,
			JR_11,JR_12,JR_13,JR_14,JR_15,JR_16,JR_17,JR_18,JR_19,JR_20,
			JR_21,JR_22,JR_23,JR_24,JR_25,JR_26,JR_27,JR_28,JR_29,JR_30 from JaeRyo2 where JR_Num2 ='1'";
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
		
							<li><a><strong><?php print $data['JR_1']?></a>
							<a><?php print $data['JR_2']?></a>
							<a><?php print $data['JR_3']?></a>
							<a><?php print $data['JR_4']?></a>
							<a><?php print $data['JR_5']?><strong></a></li>
							<li><a><strong><?php print $data['JR_6']?></a>
							<a><?php print $data['JR_7']?></a>
							<a><?php print $data['JR_8']?></a>
							<a><?php print $data['JR_9']?></a>
							<a><?php print $data['JR_10']?><strong></a></li>
							<li><a><strong><?php print $data['JR_11']?></a>
							<a><?php print $data['JR_12']?></a>
							<a><?php print $data['JR_13']?></a>
							<a><?php print $data['JR_14']?></a>
							<a><?php print $data['JR_15']?><strong></a></li>
							<li><a><strong><?php print $data['JR_16']?></a>
							<a><?php print $data['JR_17']?></a>
							<a><?php print $data['JR_18']?></a>
							<a><?php print $data['JR_19']?></a>
							<a><?php print $data['JR_20']?><strong></a></li>
							<li><a><strong><?php print $data['JR_21']?></a>
							<a><?php print $data['JR_22']?></a>
							<a><?php print $data['JR_23']?></a>
							<a><?php print $data['JR_24']?></a>
							<a><?php print $data['JR_25']?></a>
							<a><?php print $data['JR_26']?></a>
							<a><?php print $data['JR_27']?></a>
							<a><?php print $data['JR_28']?></a>
							<a><?php print $data['JR_29']?></a>
							<a><?php print $data['JR_30']?><strong></a></li>
							</font>
				
		  
    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>
  
 <?php
	
	mysqli_close($conn);
?>

</html>
