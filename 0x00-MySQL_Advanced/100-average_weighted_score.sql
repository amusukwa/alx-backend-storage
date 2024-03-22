DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;

    -- Calculate the total weighted sum and total weight for the user
    SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
    INTO weighted_sum, total_weight
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Compute the average weighted score
    IF total_weight > 0 THEN
        SET avg_score = weighted_sum / total_weight;
    ELSE
        SET avg_score = 0;
    END IF;

    -- Update the average score for the user in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;
//

DELIMITER ;
