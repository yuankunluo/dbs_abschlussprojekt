<labelfor="{{!label}}">{{!label}}: </label>
<select name="{{!name}}">
	<option value=""></option>
	% for i in options:
		<option valune={{!i}}>{{!i}}</option>
	% end
</select>

