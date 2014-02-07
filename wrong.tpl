<!DOCTYPE html>
<html>
    <head>
        <title> Olympic 2012 | {{ pagetitle if pagetitle else ""}}</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
        <link rel="stylesheet" href="static/css/london2012.css" type="text/css">
    </head>
    <body>
        % include header
        <div id="content">
            <span class="wrong">Sorry, the follows input caused problem:</span>
            {{!pagecontent}}
            <form action="{{!url}}">
    <input type="submit" value="Try Again">
</form>
        </div>
        % include footter.tpl
    </body>
</html>
