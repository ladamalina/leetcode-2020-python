select today.Id
from
    Weather as today
    left join Weather as yest
        on date_add(yest.RecordDate, interval 1 day) = today.RecordDate
where
    yest.Temperature is not null
    and today.Temperature > yest.Temperature;
