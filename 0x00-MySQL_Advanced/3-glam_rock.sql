-- Calculate the lifespan of each band
SELECT 
    band_name, 
    2022 - SUBSTRING_INDEX(lifespan, '-', 1) AS lifespan
INTO 
    bands_with_lifespan
FROM 
    metal_bands;

-- Filter bands with the main style "Glam rock" and rank them by longevity
SELECT 
    band_name, 
    RANK() OVER (ORDER BY 2022 - SUBSTRING_INDEX(lifespan, '-', 1) DESC) AS longevity_rank
FROM 
    bands_with_lifespan
WHERE 
    FIND_IN_SET('Glam rock', main_style) > 0
ORDER BY 
    longevity_rank;

