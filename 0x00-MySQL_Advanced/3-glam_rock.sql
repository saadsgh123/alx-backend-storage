-- cript that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT band_name, (IFNULL(split,2022) - formed) AS lifespan from metal_bands
where style LIKE '%Glam rock%';
