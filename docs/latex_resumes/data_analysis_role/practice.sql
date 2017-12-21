/*
SELECT CASE WHEN G.Grade<8 THEN NULL ELSE S.Name END AS Name, G.Grade, S.Marks 
FROM Students S INNER JOIN Grades G ON S.Marks BETWEEN G.Min_Mark and G.Max_Mark ORDER BY G.Grade DESC,Name,Marks;


Order your output in descending order by the total number of 
challenges in which the hacker earned a full score. 

If more than one hacker received full scores in same number of 
challenges, then sort them by ascending hacker_id.


Write a query to print the respective hacker_id and name of 
hackers who achieved full scores for more than one challenge. 

Hackers:
- hacker_id
- name

Difficulty:
- difficulty_level
- score

Challenges:
- challenge_id
- hacker_id
- difficulty_level

Submissions:
- submission_id
- hacker_id
- challenge_id
- score
*/

group by
having



select hacker_submissions.hacker_id, hacker_submissions.name, count(*) as total_full_scores from (Submissions left join Hackers on 
	Submissions.hacker_id = Hackers.hacker_id) as hacker_submissions, 
	(select * from Challenges left join Difficulty 
	on Challenges.difficulty_level = Difficulty.difficulty_level) as challenge_scores where 
Submissions.score = challenge_scores.score and total_full_scores > 1,
group by hacker_submissions.hacker_id
order by total_full_scores desc, hacker_id;