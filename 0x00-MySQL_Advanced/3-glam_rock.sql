SELECT band_name, (IFNULL(split,2022) - formed) AS lifespan from metal_bands
where style LIKE '%Glam rock%';