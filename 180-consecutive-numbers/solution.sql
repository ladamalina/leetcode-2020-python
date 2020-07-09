select l1.Num as ConsecutiveNums
from
    Logs as l1
    inner join Logs as l2 on l1.Id = l2.Id + 1 and l1.Num = l2.Num
    inner join Logs as l3 on l1.Id = l3.Id + 2 and l1.Num = l3.Num
group by l1.Num;
