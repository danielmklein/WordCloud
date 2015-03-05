
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

        <div id="general_info">
<p>This application allows users to construct word clouds from Supreme Court opinions.  These word clouds depict words that occur relatively frequently in a chosen subset of opinions compared to their frequency in a larger set of opinions. The smaller set, from which the words in the word cloud will be drawn, is called the subset. The larger set, which provides the background distribution, is called the corpus.</p>

<p>For example, if you want to see the terms used particularly often in the 1960s compared to all opinions since 1925, you would choose the years 1960 through 1969 for the subset, and all cases for the corpus.</p>

<p>Another example: if you want to see the words that Justice Scalia uses, compared to the words other justices on the Court at the same time use, you would choose Justice Scalia for the subset and the years 1986 to the present (i.e. the period during which Scalia has been on the Court) for the corpus. </p>

        </div> <!-- end general info -->


        <div id="tfidf_info">

<p>The terms in each word cloud, and the prominence of each term, are determined through a metric called "term frequency-inverse document frequency" (tf-idf).  It is computed as the product of two elements, term frequency and inverse document frequency. Term frequency (tf) is the relative frequency with which a term appears in a subset of text. That is, it is the frequency of the term divided by the number of words in the subset.  Inverse document frequency (idf) is the inverse of the proportion of documents in which the word appears.  So idf will be small for words that occur commonly across a set of documents.</p>
<p>The logic of tf-idf is that words which are used most often in a document are likely to be central to its message.  Words that are used commonly across many different documents are likely to be less important to the meaning of any particular document.  Putting these two propositions together, words that are used often in one document but rarely in other documents are likely to be particularly important to the meaning of that one document and so will get a high tf-idf score. </p>

<p>We adapt tf-idf for our purposes.  To create a word cloud, the user identifies a subset of Supreme Court opinions.  Examples of such subsets might be all majority opinions in a particular decade, all majority opinions in free speech cases during a specific time frame, or all dissenting opinions from a particular justice within a particular time frame. For each word cloud the user also chooses a broader set of opinions with which to compare the target subset. This background set is the corpus.  For example, if the user wants to know what terms are relatively important to the Court's free speech cases compared to all other types of cases, the subset would be free speech cases and the corpus would be all Supreme Court opinions.  But if the user wants know how free speech cases in one time frame are unique compared to free speech opinions overall, the subset would be free speech opinions within the desired time frame and the corpus would be all free speech opinions.</p>

<p>The tf-idf value for each term is tf/idf, where:
    <ul>
<li>idf=log(n/df)</li>
<li>n is total number of opinions in the corpus</li>
<li>df is the number of opinion in which the term appears .</li>
    </ul
</p>

        </div> <!-- end tfidf info-->

        <p> test </p>



        <a href="filter" class="btn btn-lg btn-success" role="button">Create A Cloud</a>
        </div> <!--end container -->
        </div> <!--end jumbotron --> 

    </body>

</html>