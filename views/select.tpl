<select name="{{!content[0][0]}}">
<option value=""> </option>
% for c in content[1:]:
<option value="{{!c[1]}}">{{!c[0]}}</option>
% end
</select>
