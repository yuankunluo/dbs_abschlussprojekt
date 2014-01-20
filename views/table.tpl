<table class="result">
            % header = content[0]
            <tr class="result">
            % for h in header:
            <th class="result">{{!h}}</th>
            %end
            </tr class="result">
            % for r in content[1:]:
            <tr>
                % for v in r:
                <td class="result">{{!v}}</td>
                % end
            </tr>
            % end
        </table>
