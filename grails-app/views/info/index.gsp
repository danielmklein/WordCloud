
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Supreme Court Word Cloud Creator</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->

        <!--<link rel="stylesheet" href="../css/normalize/normalize.css">-->
        <!--<link href="css/bootstrap/bootstrap.min.css" rel="stylesheet">-->
        <link rel="stylesheet" href="${resource(dir: 'css/bootstrap', file: 'bootstrap.min.css')}" type="text/css">
        <link rel="stylesheet" href="${resource(dir: 'css/normalize', file: 'normalize.css')}" type="text/css">
        <!--<script src="js/jquery/jquery-1.11.1.min.js"></script>-->
        <g:javascript src="jquery/jquery-1.11.1.min.js" />
        <!--<script src="js/bootstrap/bootstrap.min.js"></script>-->
        <g:javascript src="bootstrap/bootstrap.min.js" />
        <!--<script src="js/filters.js"></script>-->
        <g:javascript src="filters.js" />
    </head>

    <body role="document">

        <!-- Fixed navbar -->
        <nav class="navbar navbar-inverse navbar-fixed-top">
          <div class="container">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">Supreme Court Word Clouds</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="info">Info</a></li>
                    <li><a href="filter">Create A Cloud</a></li>
                </ul>
            </div><!--/.nav-collapse -->
          </div>
        </nav>

        <div class="jumbotron">
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <div class="container">
        </br>
        <p> test </p>

        <a href="filter" class="btn btn-lg btn-success" role="button">Create A Cloud</a>
        </div> <!--end container -->
        </div> <!--end jumbotron --> 

    </body>

</html>