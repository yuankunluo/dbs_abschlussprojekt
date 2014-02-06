% if len(content) == 0:
	<p>No such item</p>
% else:
<table class="result">
    % header = content[0]
    <tr class="result">
        % for e in header:
            % if isinstance(e,tuple):
            <th class="result">{{!e[0]}}</th>
            % else:
            <th class="result">{{!e}}</th>
            % end
        %end
    </tr>
    % for r in content[1:]:
    <tr>
        % for e in r:
            % if isinstance(e,tuple):
            <td class="result"><a href="/{{!e[1]}}/{{!e[2]}}">{{!e[0]}}</a></td>
            % else:
            <td class="result">{{!e}}</td>
            % end
        %end
    </tr>
    % end
</table>
% end
