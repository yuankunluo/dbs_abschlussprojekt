<table class="result">
            % header = content[0]
            <tr>
            % for h in header:
            <th>{{ h }}</th>
            %end
            </tr>
            % for r in content[1:]:
            <tr>
                % for v in r:
                <td>{{v}}</td>
                % end
            </tr>
            % end
        </table>
