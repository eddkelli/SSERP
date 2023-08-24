import geopandas as gpd
from shapely.geometry import Point

# Define the lat/long point
latitude = 38.2615
longitude = -120.4335

# Create a GeoDataFrame with the point
point = Point(longitude, latitude)
gdf = gpd.GeoDataFrame(geometry=[point], crs="EPSG:4326")

# Convert buffer distance to meters (approximately 1609.34 meters in a mile)
buffer_distance_meters = 1609.34

# Create a buffer around the point
buffered_gdf = gdf.buffer(buffer_distance_meters)


# Save the buffered GeoDataFrame as a Shapefile
buffered_gdf.to_file("buffered_circle.shp")