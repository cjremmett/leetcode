# Write your MySQL query statement below
select studs.student_id, studs.student_name, subs.subject_name, ed.attended_exams from Students studs
left join Subjects subs on 1 = 1
left join (select e.student_id, e.subject_name, count(*) as "attended_exams" from Examinations e group by e.student_id, e.subject_name) ed on ed.student_id = studs.student_id and ed.subject_name = subs.subject_name