-- Create a temporary table to calculate the lifespan of each band
CREATE TEMPORARY TABLE temp_band_lifespan AS
SELECT band_name,
       YEAR(MAX(split)) - YEAR(MIN(formed)) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
GROUP BY band_name;

-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, lifespan
FROM temp_band_lifespan
ORDER BY lifespan DESC;
