select
    e.Name as Employee
from
    Employee as e
    left join Employee as m on e.ManagerId = m.Id
where
    m.Id is not null
    and e.Salary > m.Salary;
