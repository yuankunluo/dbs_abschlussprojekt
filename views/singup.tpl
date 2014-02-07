<h1>Sing Up</h1>
<form name="singup" action="singup" method="post">
    <fieldset>
        <legend>Base Information</legend>
        <label>Username</label>
        <input name="user_name" placeholder="Username" required>
        <br/>
        <label>Email</label>
        <input name="user_email" type="email" placeholder="Email" required>
        <br/>
        <label>Password</label>
        <input name="user_password1" type="password" placeholder="Password" required>
        <input name="user_password2" type="password" placeholder="Password one more time" required>
    </fieldset>
    <fieldset>
        <legend>Personal Information</legend>
        <label>Name</label>
        <input name="user_firstname" placeholder="First name" required>
        <input name="user_lastname" placeholder="Last name" required>
        <br/>
        <label>Gender</label>
        <select name="user_gender" required>
            <option value=""> </option>
            <option value="m">Male</option>
            <option value="f">Female</option>
        </select>
        <label>Country</label>
        <select name="user_country">
            {{!country_options}}
        </select>
        <br/>
        <label>Birthday:</label>
        <label>Year</label>
        <select name="user_year" required>
            {{!year_options}}
        </select>
        <label>Month</label>
        <select name="user_month" required>
            {{!month_options}}
        </select>
        <label>Day</label>
        <select name="user_day" required>
            {{!day_options}}
        </select>
    </fieldset>
    <button type="submit" value="Submit">Submit</button>
    <button type="reset" value="Reset">Reset</button>
</form>
