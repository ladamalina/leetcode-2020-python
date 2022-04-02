delete
from Person
where Id not in (
    select min(Id) as Id
    from (select * from Person) t
    group by Email
);
