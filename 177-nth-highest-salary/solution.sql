CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE counter INT DEFAULT N - 1;
    RETURN (
    # Write your MySQL query statement below.
    select
        if(
            N <= (select count(distinct Salary) from Employee),
            (
                select Salary
                from Employee
                group by Salary
                order by Salary desc
                limit 1 offset counter
            ),
            null
        )
    );
END
