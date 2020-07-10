select
    s1.id as id,
    if(
        (s1.id & 0x1) = 1,
        if(
            s2.id is not null,
            s2.student,
            s1.student
        ),
        s3.student
    ) as student
from
    seat as s1
    -- odd rows
    left join seat as s2 on s1.id + 1 = s2.id and (s1.id & 0x1) = 1
    -- even rows
    left join seat as s3 on s1.id - 1 = s3.id and (s1.id & 0x1) = 0
order by id;
