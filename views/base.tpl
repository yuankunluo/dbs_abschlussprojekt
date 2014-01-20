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
            {{ pagecontent }}
        </div>
        
        % include footter.tpl
    </body>
</html>
