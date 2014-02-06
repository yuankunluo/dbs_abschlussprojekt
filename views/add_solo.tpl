            % t = {"p":"Preliminaries","s":"Semifinal","f":"Finals"}
            <h1>Add Solo Event -- {{!t[et]}}</h1>
            <form class="add_event" action="../add_solo" method="post">
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
                    <!-- dateselectore -->
                    <div class="dateselector">
                        <label>Month</label>
                        <select name="event_month" required>
                            {{!month_options}}
                        </select>

                        <label for="">Day</label>
                        <select name="event_day" required>
                            {{!day_options}}
                        </select>

                        <label for="">Hour</label>
                        <select name="event_hour" required>
                            {{!hour_options}}
                        </select>

                        <label for="">Minute</label>
                        <select name="event_minute" required>
                            {{!minute_options}}
                        </select>
                    </div>
                </fieldset>
                <!-- athelets -->
                <fieldset name="Athletes">
                    <legend>Results</legend>
                    % for ath_nr in ath_number:
                    <!-- athelet formular -->
                    <div class="add_athletes">
                        <span class="ranking">Rank: {{!ath_nr}}</span>
                        <input type="text" name="ath{{!ath_nr}}_rangk" hidden="hidden" value="{{ath_nr}}" required>
                        <label>First Name:</label>
                        <input type="text" name="ath{{!ath_nr}}_firstname" placeholder="First Name" required>
                        <label>Last Name:</label>
                        <input type="text" name="ath{{!ath_nr}}_lastname" placeholder="Last Name" required>
                        <br/>
                        <label>Result</label>
                        <input name="ath{{!ath_nr}}_result" placeholder="Enter result">
                        % if et == "f" and ath_nr <7:
                        <label>Medal</label>
                        <select name="ath{{!ath_nr}}_melda" required>
                            <option value="" selected></option>
                            <option value="g">Gold</option>
                            <option value="s">Silver</option>
                            <option value="b">Bronze</option>
                        </select>
                        % end
                        <br/>
                        <label>Select Country</label>
                        <select name="ath{{!ath_nr}}_country" required>
                            {{!country_options}}
                        </select>
                        <label>Select Gender</label>
                        <select name="ath{{!ath_nr}}_gender" required>
                            <option value=""></option>
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
                    </div>
                    % end
                </fieldset>
                <button type="submit" value="Submit">Submit</button>
                <button type="reset" value="Reset">Reset</button>
            </form>