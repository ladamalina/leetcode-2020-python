select
    d.Name AS Department,
    e1.Name AS Employee,
    e1.Salary as Salary
from
    Employee as e1
    join Department as d on e1.DepartmentId = d.Id
    left join (select distinct DepartmentId, Salary from Employee) e2
        on e1.DepartmentId = e2.DepartmentId and e1.Salary < e2.Salary
group by e1.DepartmentId, e1.Name
having count(e1.Salary) < 3;
