                    <option value="" selected> </option>

                    % for c in content[1:]:
                    <option value="{{!c[1]}}">{{!c[0]}}</option>
                    % end
