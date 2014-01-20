% for news in content[1:]:
<div class="news_short">
                <span class="sport"><a href="{{!news[-2][1]}}/{{!news[-2][2]}}">{{!news[-2][0]}}</a></span>
                <h3><a href="{{!news[0][1]}}/{{!news[0][2]}}">{{!news[0][0]}}</a></h3>
                <span class="reporter">By {{!news[2]}}</span>
                <span class="time">at {{!news[1]}}</span>
                <span class="count">Comments: {{!news[-1]}}</span>
                <img class="news_short" src="static/images/{{!news[4]}}" alt="{{!news[0][0]}}"> 
                <p class="news_short">{{!news[3][:200]}} ...
                <a href="{{!news[0][1]}}/{{!news[0][2]}}">more</a>
                </p>
</div>
%end
