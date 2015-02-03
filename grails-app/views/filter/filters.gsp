
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

        <link rel="stylesheet" href="../css/normalize/normalize.css">
        <link href="../css/bootstrap/bootstrap.min.css" rel="stylesheet">
    </head>

    <body role="document">

            <!-- Fixed navbar -->
            <nav class="navbar navbar-inverse navbar-fixed-top">
              <div class="container">
                <div class="navbar-header">
                  <a class="navbar-brand" href="#">Supreme Court Word Clouds</a>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                </div><!--/.nav-collapse -->
              </div>
            </nav>

        
        <div class="jumbotron">
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
        <div class="container">
        </br>

        <h1>Welcome!</h1>
        <p>This is the page for creating subsets and adding them to the corpus.</p>

        <p>TODO: add some help text here to instruct the user!</p>
        </div> <!-- end container --> 
        </div> <!-- end jumbotron -->

        <div class="container">
        <g:form action="createSubset">

            <label for="name">Subset Name</label>
            <g:textField name="name" value="${filter.name}"/>
            <br/>
            
            <label for="sortField">Sort Field</label><!--this should actually a dropdown box-->
            <!--<g:textField name="sortField" value="${filter.sortField}"/>-->
            
            <g:select name="sortField" 
                        from="${dbFields}" 
                        value="${dbField}"/>
            <br/>

            <label for="allowedValues">Allowed Values</label>
            <g:textField name="allowedValues" value="${filter.allowedValues}"/>
            <br/>
            
            <g:submitButton name="createSubset" value="Create Subset" class="btn btn-lg btn-default"/>

        </g:form>
        
        <br/>

        <p>Here's a list of the subsets we've already defined!</p>
        <g:each var="subset" in="${subsets}">
            <ul>
                <li>Subset Name: ${subset.name}</li>
                <li>Sort Field: ${subset.sortField}</li>
                <li>Allowed Values: ${subset.allowedValues}</li>
            </ul>
            <br/>
        </g:each>
        
        <g:form>
            <div class="row">
            <div class="col-md-4">
            <p>Subsets:</p>
            <g:select name="subset" 
                        size="${subsets.size()}"
                        from="${subsets}" 
                        value="${subset?.name}"
                        optionKey="name"
                        optionValue="name"/>
            </div> <!-- end column -->
            
            <div class="col-md-4">
            <p>Corpus Subsets:</p>
            <g:select name="corpusFilter" 
                            size="${corpusSubsets.size()}"
                            from="${corpusSubsets}" 
                            value="${corpusFilter?.name}"
                            optionKey="name"
                            optionValue="name"
                            multiple="true"/>
            </div> <!-- end column -->

            </div> <!-- end row -->

            </br>
            <g:actionSubmit name="addSubsetToCorpus" 
                            value="Add Subset To Corpus" 
                            action="addSubsetToCorpus"
                            class="btn btn-lg btn-default"/>

            <g:actionSubmit name="removeSubsetFromCorpus" 
                            value="Remove Subset From Corpus" 
                            action="removeSubsetFromCorpus"
                            class="btn btn-lg btn-default"/>

            <g:actionSubmit name="addAllSubsetsToCorpus"
                            value="Add All Subsets To Corpus"
                            action="addAllSubsetsToCorpus"
                            class="btn btn-lg btn-default"/>

            <g:submitButton name="removeAllSubsetsFromCorpus" 
                            value="Remove All Subsets From Corpus"
                            action="removeAllSubsetsFromCorpus"
                            class="btn btn-lg btn-default"/>

            <g:actionSubmit name="createWordCloud"
                            value="Create WordCloud"
                            action="createWordCloud" 
                            class="btn btn-lg btn-primary"/>
        </g:form>
        </br>
        
        <!--<script src="js/jquery/jquery-1.11.1.min.js"></script>-->
        </div> <!-- end container -->
    </body>
</html>
