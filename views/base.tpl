<!DOCTYPE html>
<html>
    <head>
        <title> Olympic 2012 | {{ pagetitle if pagetitle else ""}}</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width">
        <link rel="stylesheet" href="/static/css/london2012.css" type="text/css">
    </head>
    <body>
        <div id="header">
            <a class="logo" href="homepage">Olympic 2012 London</a>
            <br/>
            <form class="top_search" action="../search">
                <input class="top_search" type="text" name="search" placeholder="Input to search" required>
                <input class="top_search" type="submit" value="search">
            </form>
                <ul class="navi">
                    <li class="navi"><a class="navi" href="/homepage">Homepage</a></li>
                    <li class="navi"><a class="navi" href="/news">News</a></li>
                    <li class="navi"><a class="navi" href="/sports">Sports</a></li>
                    <li class="navi"><a class="navi" href="/events">Events</a></li>
                    <li class="navi"><a class="navi" href="/athletes">Athletes</a></li>
                    <li class="navi"><a class="navi" href="/medalists">Medalists</a></li>
                    <li class="navi"><a class="navi" href="/admin">Admin</a></li>
                    % if login:
						<li class="navi"><a class="navi" href="/logout">Logout</a></li>
					% else:
						<li class="navi"><a class="navi" href="/login">Login</a></li>
					% end
                </ul>
        </div>
        <div id="content">
            {{!pagecontent}}
        </div>
        % include footter.tpl
    </body>
</html>
