<labelfor="{{!label}}">{{!label}}: </label>
<select name="{{!name}}">
<option value="" selected> </option>

	% for i in options:
		<option value="{{!i}}">{{!i}}</option>
	% end
</select>

