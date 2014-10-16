
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->

        <link rel="stylesheet" href="css/normalize/normalize.css">
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <p>This is the page for creating subsets and adding them to the corpus.</p>
        <g:form action="createSubset">
            <label for="name">Subset Name</label>
            <g:textField name="name" value="${filter.name}"/>
            <br/>
            <label for="sortField">Sort Field</label><!--this should actually a dropdown box-->
            <g:textField name="sortField" value="${filter.sortField}"/>
            <br/>
            <label for="allowedValues">Allowed Values</label>
            <g:textField name="allowedValues" value="${filter.allowedValues}"/>
            <br/>
            <g:submitButton name="createSubset" value="Create Subset"/>
        </g:form>

        <script src="js/jquery/jquery-1.11.1.min.js"></script>
    </body>
</html>
