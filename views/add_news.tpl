<h1>Add News</h1>
<div class="tipp">
    <h2>Tipps:</h2>
    <p>News can be about an event or not,if this news was about an event, please select an event.</p>
    <p>If this one is a <span>non-event-relevant news</span>, please ignore the event selector in below</p>
    <p>If the event was not in Datenbank, please go to <a href="/admin">Admin</a> to add one event.</p>
    <p>After adding this event, you can continue add news.</p>
    <h2>Images</h2>
    <p>Because ajax was not allowed to use. If you want to add picture for this news, pleas go to <a href="/admin">Admin</a>.</p>
    <p>:)</p>
</div>
<form name="add_news" action="/add_news" method="post">
    % if defined(user):
    <input name="news_user" value="{{!user}}" hidden="hidden">
    % end
    <fieldset>
        <legend>New Title</legend>
    <input class="news_title" name="news_title" placeholder="Enter title hier" required>
    </fieldset>
    <fieldset name="event_selector">
        <legend>Event Selector</legend>
        <label>Please select an event</label>
        <select name="news_event">
            {{!event_options}}
        </select>
    </fieldset>
    <fieldset name="news_content">
        <legend>Content</legend>
        <textarea name="news_content" placeholder="Enter content hier" required></textarea>
    </fieldset>
    <button type="submit" value="Submit">Submit</button>
    <button type="reset" value="Reset">Reset</button>
</form>
