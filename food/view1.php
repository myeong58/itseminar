<!DOCTYPE html>
<?php
session_start();
include_once ("lib/dbconn.php");
$conn=mysqli_connect("106.10.36.173","Bo","Dhsmfdms?1","food");
mysqli_query("SET NAMES utf8");
$Num=$_GET['JR_Num'];
$query = " select JR_Image, JR_Menu, JR_Url from JaeRyo where JR_Num like '$Num' ";
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

      <!-- Portfolio Item Heading -->
      <h1 class="my-4">< 오늘의 뭐먹지? > 
        
      </h1>

      <!-- Portfolio Item Row -->
      <div class="row">

        <div class="col-md-8">
       <img class="JR_Image"><img src=<?=$data['JR_Image']?> width='600'height='500'>
        </div>

        <div class="col-md-4">
			<h3 class="JR_Menu">[오늘의 레시피]</h3>
          <h3 class="JR_Menu"><?php print $data['JR_Menu'] ?></h3>
          <p><a href="<?php echo $data['JR_Url']?>"><?php echo $data['JR_Url']?></a></p>
          <h3 class="my-3">재료</h3>
          <ul>
              <?php 
				session_start();
				include_once("Jae2.php");
			?>
          </ul>
        </div>

      </div>
	  <br>
	  <br>
	  <br>
	  <br>
      <!-- /.row -->

      <!-- Related Projects Row -->
      
		
      </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2018</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  </body>
  
 <?php
		
	mysqli_close($conn);
?>

</html>