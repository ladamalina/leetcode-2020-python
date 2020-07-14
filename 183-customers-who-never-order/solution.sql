select
    c.Name as Customers
from
    Customers as c
    left join Orders as o
        on c.Id = o.customerId
where o.customerId is null;
