# Import necessary libraries
import wekeo_utils
import xarray as xr
import matplotlib.pyplot as plt

# Set endpoint and access token for WEkEO API
wekeo_utils.set_token(token='<insert token here>')
wekeo_utils.set_endpoint(url='https://wekeo-api.brockmann-consult.de')

# Define search parameters
search_params = {
    "dataset": "Copernicus Sentinel-2",
    "productType": "S2MSI1C",
    "platform": "Sentinel-2",
    "start": "2022-01-01",
    "end": "2022-12-31",
    "latitude": "52.52, 52.56",
    "longitude": "13.35, 13.42"
}

# Search for data based on search parameters
search_result = wekeo_utils.search(search_params, show_progress=True)

# Get URLs of the first three results for the search and download the data
urls = wekeo_utils.get_download_urls(search_result, max_results=3, subset=False)
datasets = wekeo_utils.download(urls)

# Concatenate the downloaded datasets
combined_dataset = xr.concat(datasets, dim='time')

# Visualize the data using matplotlib
combined_dataset['B04'].plot(col='time', col_wrap=3)
plt.show()
