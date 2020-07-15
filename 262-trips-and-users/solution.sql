select
    t.Request_at as Day,
    round(count(if(t.Status = 'completed', null, t.Id)) / count(t.Id), 2) as `Cancellation Rate`
from
    Trips as t
    inner join Users as c
        on t.Client_Id = c.Users_Id
        and c.Banned = 'No'
        and c.Role = 'client'
    inner join Users as d
        on t.Driver_Id = d.Users_Id
        and d.Banned = 'No'
        and d.Role = 'driver'
where t.Request_at >= '2013-10-01' and t.Request_at <= '2013-10-03'
group by t.Request_at;
