<!DOCTYPE html>
<?php
session_start();
include_once ("lib/dbconn.php");
$conn=mysqli_connect("106.10.36.173","Bo","Dhsmfdms?1","food");
				
mysqli_query("SET NAMES utf8");
$Num=$_GET['HM_Jae'];
$query = "SELECT DISTINCT HM_Jae, HM_Url, HM_Price, HM_Menu, HM_Image FROM H_Mart WHERE HM_Jae LIKE '$Num' ORDER BY HM_Price ASC LIMIT 7";
$result=mysqli_query($conn,$query);
$data=mysqli_fetch_array($result);

   
?>
<html lang="ko">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>오늘 뭐먹지?</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/portfolio-item.css" rel="stylesheet">

  </head>

  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="index.php">오늘 뭐먹지?</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="index.php">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
          
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">
	
	<br>

      <div class="row">

        <div class="col-lg-3">
			

		
          <h1 class="my-4">마트 가격</h1>
          <div class="list-group">
             <a href= "price.php?HM_Jae=<?=$data['HM_Jae']?>" class="list-group-item">홈플러스</a>
			<a href= "price2.php?LM_Jae=<?=$data['HM_Jae']?>" class="list-group-item">롯데마트</a>
					
          </div>

        </div>
		
		
		
        <!-- /.col-lg-3 -->

        <div class="col-lg-9">

          
          <div class="row">
	
				
	<?php
						
			
				while($data=mysqli_fetch_array($result)){

					
									
			?>
		  
            <div class="col-lg-4 col-md-6 mb-4">
              <div class="card h-100">
                <a href="<?php echo $data['HM_Url']?>"><img src=<?=$data['HM_Image']?> width='255'height='150'></a>
                <div class="card-body">
                  <h4 class="card-title">
				  <br>
					<a class="JR_Menu"><?php print $data['HM_Menu'] ?></a>
                  </h4>
				  <br>
                  <h5><a class="JR_Menu"><?php print $data['HM_Price'] ?>원</a></h5>
                  
                </div>
               
			   
              </div>
            </div>
		<?php 
		
				}
				
					
						?>
					
					
          </div>
          <!-- /.row -->

        </div>
        <!-- /.col-lg-9 -->

      </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->

	
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
	<br>
    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2017</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>

</html>
