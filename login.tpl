<h1>Login</h1>
<div class="tipp">
    <p>If you have want to have account for this site, please <a href="/singup">Singup</a></p>
    <h2>The Reporter Account </h2>
    <p>Username: <span>admin</span></p>
    <p>Password: <span>123</span></p>
    <h2>The normal user account </h2>
    <p>Username: test</p>
    <p>Password: 123</p>
    <p>:)</p>
</div>
<form name="login" action="/login" method="post">
    <fieldset>
        <legend>Login Information</legend>
        <label>Username:</label>
        <input name="user_name" placeholder="Username" required>
        <br/>
        <label>Password</label>
        <input name="user_password" type="password" placeholder="Password" required>
    </fieldset>
    <button type="submit" value="Submit">Submit</button>
    <button type="reset" value="Reset">Reset</button>
</form>
