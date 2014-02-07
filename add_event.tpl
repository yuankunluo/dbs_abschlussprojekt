<form action="/add_news" method="post">
            <input  class="title" type="text" name="news_title" placeholder="Enter News Title"><br>
            <fieldset>
                <legend>Event</legend>
                <label>Select an old event</label>
                {{!select_events}}
                <br class="line">
                <label>Or enter a new Event</label>
                <label>Event:</label>
                <input type="text" name="news_event" placeholder="Enter Event Name">
                <br>
                <label>Select a sport:</label>
                {{!select_sports}}
                <br>
                <label>Select a vanue:</label>
                {{!select_vanues}}
                <br>
                <label>Date:</label>
                <input type="date" name="date">
                <br>
                <label>Time:</label>
                <input type="time" name="time">                
            </fieldset>
            
            <fieldset>
                <legend>Athelets</legend>
                % for i in range(numberofathelets):
                <div class="inputtable">
                    <div class="athelet_number">{{!i+1}}</div>
                    <label>Select Country</label>
                    <select name="athelet{{!i}}_country">
                        {{!select_countries}}
                    </select>
                    <label>Firstname:</label>
                    <input name="athelet{{!i}}_firstname" type="text">
                    <label>Lastname:</label>
                    <input name="athelet{{!i}}_lastname" type="text">
                    <label>Result</label>
                    <input name="athelet{{!i}}_result" type="text">
                    <label>Rank</label>
                    <input name="athelet{{!i}}_rank" type="number">
                        <label>Gender</label>
                    <select name="athelet{{!i}}_gender">
                        <option value="m">Male</option>
                        <option value="f">Female</option>
                    </select>
                    <label>Birthdate</label>
                    <input name="birthdate" type="date">
                </div>
                % end
            </fieldset>
            
            <fieldset>
                <legend>News Content</legend>
                <textarea name="news_content" placeholder="Enter News here!"></textarea>
            </fieldset>
            <input type="submit">
        </form>
