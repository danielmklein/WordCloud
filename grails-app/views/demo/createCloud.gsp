
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

        <!--<link rel="stylesheet" href="../../web-app/css/normalize/normalize.css">-->
        <!--<link rel="stylesheet" href="css/main.css">-->
        <!--<script src="js/vendor/modernizr-2.6.2.min.js"></script>-->
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <!-- Add your site or application content here -->
        <p>Hello world! This is HTML5 Boilerplate.</p>

        <!-- this might not be valid syntax...-->
        <tr>
        <g:each in="${terms}" var="term">
            <td>${term.term} (${term.weight})</td></br>
        </g:each>
        </tr>
        
        <g:javascript src="jquery/jquery-1.11.1.min.js" />
        <!--<script src="../js/jquery/jquery-1.11.1.min.js"></script>-->

        <g:javascript src="d3/d3.js" />
        <!--<script src="../js/d3/d3.js"></script>-->
        <g:javascript src="d3-cloud/d3.layout.cloud.js" />
        <!--<script src="../js/d3-cloud/d3.layout.cloud.js"></script>-->
        <script>
          var termList = [];
          var termDict = new Object();

          <g:each in="${terms}" var="term">
            termList[termList.length] = "${term.term}";
            termDict["${term.term}"] = ${term.weight};
          </g:each>

          var fill = d3.scale.category20();

          var fontSize = d3.scale.log().range([10,100]);
          for (idx = 0; idx < termList.length; idx++)
          {
            var curTerm = termList[idx];
            var curWeight = termDict[curTerm];
            console.log(curTerm + " " + curWeight)
          }

          d3.layout.cloud()
              .size([800 , 800])
              .words(termList.map(function(d) {
                return {text: d, size: termDict[d] * 125};
              }))
              .padding(5)
              .rotate(function() { return ~~(Math.random() * 5) * 30 - 60; })
              .font("Impact")
              .fontSize(function(d) { return d.size; })
              .on("end", draw)
              .start();

          function draw(words) {
            d3.select("body").append("svg")
                .attr("width", 800)
                .attr("height", 800)
              .append("g")
                .attr("transform", "translate(300,300)")
              .selectAll("text")
                .data(words)
              .enter().append("text")
                .style("font-size", function(d) { return d.size + "px"; })
                .style("font-family", "Impact")
                .style("fill", function(d, i) { return fill(i); })
                .attr("text-anchor", "right")
                .attr("transform", function(d) {
                  return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                })
                .text(function(d) { return d.text; });
          }
        </script>
        <!--<script src="js/plugins.js"></script>-->
        <!--<script src="js/main.js"></script>-->

        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <!--<script>
            (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
            function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
            e=o.createElement(i);r=o.getElementsByTagName(i)[0];
            e.src='//www.google-analytics.com/analytics.js';
            r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
            ga('create','UA-XXXXX-X');ga('send','pageview');
        </script>-->
    </body>
</html>
