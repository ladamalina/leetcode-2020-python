select
    Salary as SecondHighestSalary
from (
    select * from Employee
    union all
    select null as Id, null as Salary
) t
group by Salary
order by Salary desc
limit 1
offset 1;
