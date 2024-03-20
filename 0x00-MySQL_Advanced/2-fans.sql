-- Create a temporary table to store the count of fans for each country origin
CREATE TEMPORARY TABLE temp_country_fans AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the country origins of bands based on the number of (non-unique) fans
SELECT origin, nb_fans
FROM temp_country_fans
ORDER BY nb_fans DESC;
