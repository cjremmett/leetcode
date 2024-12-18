# Write your MySQL query statement below
select * from (select s.user_id, c.action, count(*) from Signups s
left join Confirmations c on s.user_id = c.user_id
group by s.user_id, c.action) gb