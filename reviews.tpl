<html>
    <head>
        <meta charset="UTF-8">
        <title>{{title}}</title>
        <link href='reviews.css' rel='stylesheet' type='css'>
    </head>
    <body>
        <div class="container">
            <div class="raw clearfix">
                <div class="layout-column">
                     <form action="/review" method="post">
                        Name:<br>
                        <input type="text" name="name">
                        <br>
                        Review:<br>
                        <input type="text" name="review" size="50">
                        <br><br>
                        <input type="submit" value="Submit">
                    </form>
                </div>
                <div class="layout-column">
                     <ul>
                        <h1>{{title}}</h1>
                      % for review in reviews:
                        <br>
                        <li>
                        	<div>{{review[0]}}</div>
                        	<div>{{!review[1]}}</div>
                     	</li>
                      % end
                     </ul>
                </div>
            </div>
        </div>
    </body>
</html>