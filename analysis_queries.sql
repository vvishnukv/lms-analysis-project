-- Query: How does accessibility impact grades and forum engagement?
WITH TieredData AS (
    SELECT 
        course_id,
        department,
        final_grade,
        forum_posts,
        video_watch_mins,
        CASE 
            WHEN accessibility_score >= 90 THEN '1. A - Fully Compliant'
            WHEN accessibility_score >= 70 THEN '2. B - Needs Minor Fixes'
            ELSE '3. C - High Risk'
        END AS wcag_tier
    FROM lms_accessibility_data
)
SELECT 
    wcag_tier,
    COUNT(course_id) AS total_enrollments,
    ROUND(AVG(final_grade), 1) AS avg_final_grade,
    ROUND(AVG(forum_posts), 1) AS avg_forum_posts,
    ROUND(AVG(video_watch_mins), 0) AS avg_video_mins
FROM TieredData
GROUP BY wcag_tier
ORDER BY wcag_tier;