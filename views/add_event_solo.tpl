            % t = {"p":"Preliminaries","s":"Semifinal","f":"Finals"}
            % m = {1:("g","Gold"),2:("s","Silver"),3:("b","Bronze")}
            <h1>Add Solo Event -- {{!t[et]}}</h1>
            <form class="add_event" action="/add_solo" method="post">
                <label>Event Name: </label>
                <input id="news_title" name="event_name" placeholder="Enter new Event Name" required>
                <fieldset name="event">
                    <legend>Event Information</legend>
                    <input name="event_type" value="{{!et}}" hidden="hidden">
                    <label>Select Vanue</label>
                    <select name="event_vanue" required>
                        {{!vanue_options}}
                    </select>

                    <label>Select Sport</label>
                    <select name="event_sport" required>
                        {{!sports_options}}
                    </select>
                    <br/>
                    <label>Datetime:</label>
                    <br/>

                        <input name="event_year" value="2012" hidden="hidden">
                        <label>Month</label>
                        <select name="event_month" required>
                            {{!month_options}}
                        </select>

                        <label>Day</label>
                        <select name="event_day" required>
                            {{!day_options}}
                        </select>

                        <label>Hour</label>
                        <select name="event_hour" required>
                            {{!hour_options}}
                        </select>

                        <label>Minute</label>
                        <select name="event_minute" required>
                            {{!minute_options}}
                        </select>
                </fieldset>
                <!-- athelets -->
                <fieldset name="Athletes">
                    <legend>Results</legend>
                    % for ath_nr in ath_number:
                    <!-- athelet formular -->
                        % if et == "f" and ath_nr <4:
                            <span class="ranking_{{!m[ath_nr][0]}}">{{!m[ath_nr][1]}}</span>
                            <input name="ath{{!ath_nr}}_medal" value="{{!m[ath_nr][0]}}" hidden="hidden">
                        % else:
                            <span class="ranking">{{!ath_nr}}</span>
                            <input name="ath{{!ath_nr}}_medal" value="" hidden="hidden">
                        % end
                        <input type="text" name="ath{{!ath_nr}}_rank" hidden="hidden" value="{{ath_nr}}" required>
                        <label>First Name:</label>
                        <input type="text" name="ath{{!ath_nr}}_firstname" placeholder="First Name" required>
                        <label>Last Name:</label>
                        <input type="text" name="ath{{!ath_nr}}_lastname" placeholder="Last Name" required>
                        <br/>
                        <label>Result</label>
                        <input name="ath{{!ath_nr}}_result" placeholder="Enter result">
                        <br/>
                        <label>Select Country</label>
                        <select name="ath{{!ath_nr}}_country" required>
                            {{!country_options}}
                        </select>
                        <label>Select Gender</label>
                        <select name="ath{{!ath_nr}}_gender" required>
                            <option value=""> </option>
                            <option value="f">Female</option>
                            <option value="m">Male</option>
                        </select>
                        <br/>
                        <label>Birthday:</label>
                        <label>Year</label>
                        <select name="ath{{!ath_nr}}_year" required>
                            {{!year_options}}
                        </select>
                        <label>Month</label>
                        <select name="ath{{!ath_nr}}_month" required>
                            {{!month_options}}
                        </select>
                        <label>Day</label>
                        <select name="ath{{!ath_nr}}_day" required>
                            {{!day_options}}
                        </select>
                        <hr/>
                    % end
                </fieldset>
                <button type="submit" value="Submit">Submit</button>
                <button type="reset" value="Reset">Reset</button>
            </form>
