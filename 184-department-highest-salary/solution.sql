select
    m.d_name as Department,
    e.Name as Employee,
    m.max_salary as Salary
from
    (
        select
            d.Name as d_name,
            d.Id as d_id,
            max(e.Salary) as max_salary
        from
            Department as d
            left join Employee as e on d.Id = e.DepartmentId
        group by d.Name, d.Id
    ) m
    inner join Employee as e on m.d_id = e.DepartmentId and e.Salary = m.max_salary;
