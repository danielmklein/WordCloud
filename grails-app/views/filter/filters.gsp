
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
        <p>This is the page for creating subsets and adding them to the corpus in order to create word clouds from sets of Supreme Court opinions.</p>

        <p>First, create one or more subset definitions using the dropdown menu and input boxes.</p>
        <p>Then, add one or more of your subsets to the corpus using the "Add Subset to Corpus" or "Add All Subsets to Corpus" buttons. The corpus is the set of opinions against which your subset will be compared when performing the analysis and generating the word cloud. If you specify multiple sets for the corpus, it will be constructed as the union of those sets.</p>
        <p>Finally, select a subset in the subset selection box and click "Create Word Cloud". After a few moments, the 50 most characteristic terms of the selected subset when compared to the corpus will appear, along with a word cloud of those terms</p>

        </div> <!-- end container --> 
        </div> <!-- end jumbotron -->

        <div class="container">
        <g:form action="createSubset">

            
            <label for="name">Subset Name</label>
            <g:textField name="name" 
                            value="${filter.name}" 
                            id="name_field" 
                            data-toggle="tooltip" 
                            data-placement="right" 
                            title="Enter a name for the subset you'd like to create." 
                            />
            
            <br/>
            
            <div id="phase1">
            <label for="sortField">Sort Field</label><!--this should actually a dropdown box-->
            <!--<g:textField name="sortField" value="${filter.sortField}"/>-->
            
            <g:select name="sortField1" 
                        from="${dbFields}" 
                        value="${dbField}"
                        id="sort_field1"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Select the field on whose values you wish to filter for your subset."
                        />
            <br/>

            <label for="allowedValues1">Allowed Values</label>
            <g:textField name="allowedValues1" 
                        value="${filter.allowedValues}"
                        id="allowed_vals1"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Enter the values for the sort field you want to allow. In other words, only opinions who have any of these values for the sort field will make it into your subset."
                        />
            <br/>
            </div> <!-- end phase1-->
            <button type="button" id="toggle_phase1">
                <span>Show Phase 1</span>
            </button>

            <div id="phase2">
            <label for="sortField">Sort Field</label><!--this should actually a dropdown box-->
            <!--<g:textField name="sortField" value="${filter.sortField}"/>-->
            
            <g:select name="sortField2" 
                        from="${dbFields}" 
                        value="${dbField}"
                        id="sort_field2"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Select the field on whose values you wish to filter for your subset."
                        />
            <br/>

            <label for="allowedValues2">Allowed Values</label>
            <g:textField name="allowedValues2" 
                        value="${filter.allowedValues}"
                        id="allowed_vals2"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Enter the values for the sort field you want to allow. In other words, only opinions who have any of these values for the sort field will make it into your subset."
                        />
            <br/>
            </div> <!-- end phase2-->
            <button type="button" id="toggle_phase2">
                <span>Show Phase 2</span>
            </button>

            
            <div id="phase3">
            <label for="sortField">Sort Field</label><!--this should actually a dropdown box-->
            <!--<g:textField name="sortField" value="${filter.sortField}"/>-->
            
            <g:select name="sortField3" 
                        from="${dbFields}" 
                        value="${dbField}"
                        id="sort_field3"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Select the field on whose values you wish to filter for your subset."
                        />
            <br/>

            <label for="allowedValues3">Allowed Values</label>
            <g:textField name="allowedValues3" 
                        value="${filter.allowedValues}"
                        id="allowed_vals3"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Enter the values for the sort field you want to allow. In other words, only opinions who have any of these values for the sort field will make it into your subset."
                        />
            <br/>
            </div> <!-- end phase3-->
            <button type="button" id="toggle_phase3">
                <span>Show Phase 3</span>
            </button>

            <div id="phase4">
            <label for="sortField">Sort Field</label><!--this should actually a dropdown box-->
            <!--<g:textField name="sortField" value="${filter.sortField}"/>-->
            
            <g:select name="sortField4" 
                        from="${dbFields}" 
                        value="${dbField}"
                        id="sort_field4"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Select the field on whose values you wish to filter for your subset."
                        />
            <br/>

            <label for="allowedValues4">Allowed Values</label>
            <g:textField name="allowedValues4" 
                        value="${filter.allowedValues}"
                        id="allowed_vals4"
                        data-toggle="tooltip"
                        data-placement="right"
                        title="Enter the values for the sort field you want to allow. In other words, only opinions who have any of these values for the sort field will make it into your subset."
                        />
            <br/>
            </div> <!-- end phase4-->
            <button type="button" id="toggle_phase4">
                <span>Show Phase 4</span>
            </button>


            <!--TODO: add more phases, figure out how to show/hide properly and update button text-->

            <!-- TODO: for some sort field types, allowedValues should be a dropdown! or have autocomplete! -->

            </br>
            
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
                            optionValue="name"/>
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
