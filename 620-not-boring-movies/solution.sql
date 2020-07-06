select *
from cinema
where (`id` & 0x1) = 1 and description != 'boring'
order by rating desc;
