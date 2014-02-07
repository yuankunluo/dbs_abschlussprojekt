<h1>Sing Up</h1>
<div class="tipp">
    <h2>About User Type</h2>
    <p>You can here choose which type your account should have.</p>
    <h3>Normal User can do:</h3>
    <ul>
        <li>Add pictures to news.</li>
        <li>Add pictures to athlete.</li>
        <li>Add pictures as account facepic.</li>
        <li>Update personal information.</li>
    </ul>
    <h3>Reporter User can do:</h3>
    <ul>
        <li>What normal user can.</li>
        <li>Add event and athletes.</li>
        <li>Add news</li>
    </ul>
    <p>The user type can only choose once.</p>
    <h3>About Password</h3>
    <p>The password will be stored in db without protection. Just for simple.</p>
    <p>:)</p>
</div>
<form name="singup" action="singup" method="post">
    <fieldset>
        <label>Select User Type</label>
        <select name="user_reporter" required>
            <option></option>
            <option value="0">Normal User</option>
            <option value="1">Reporter User</option>
        </select>
        <br/>
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
