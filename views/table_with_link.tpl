<table class="result">
            % header = content[0]
            <tr class="result">
            % for h in header:
            <th class="result">{{!h[0]}}</th>
            %end
            </tr>
            % for r in content[1:]:
            <tr>
                % for v in r:
                <td class="result"><a href="{{!v[1]}}/{{!v[2]}}">{{!v[0]}}</td>
                % end
            </tr>
            % end
        </table>
