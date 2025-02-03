![Logo](https://media.licdn.com/dms/image/v2/D4D3DAQGTSkRQxBmfnw/image-scale_191_1128/image-scale_191_1128/0/1709985276576/myket_cover?e=2147483647&v=beta&t=m4DBwtRJ0DWvIH3qaPbC4fRPZxUXnb4_V8eiLI_kZ9w)

# Scrape animations on myket.ir

## Table of Contents
- [Introduction](#introduction)
- [Data Collection](#DataCollection)

## Introduction

This project focuses on collecting, modeling, and interpreting data related to animations. The data collection step involves scraping relevant features and responses, storing them in a CSV file, and providing a brief description of the extracted features. In the modeling step, various machine learning models are fitted and evaluated to select the best-performing one. The tuning process is documented, including parameter values and selection criteria. Finally, the interpretation step applies both global and local model-agnostic methods to analyze the final model's predictions, ensuring clarity and alignment with intuition.

# Data Collection

## Overview
This project aims to scrape animation-related data from the Myket website using R. The extracted data will be structured into a dataframe for further analysis. The project involves web scraping techniques using the `rvest` and `RSelenium` libraries to collect data from various animation pages.


## Date
The script dynamically sets the date using `r Sys.Date()`.

## Requirements
To run this project, you need to have the following R packages installed:

- `tidyverse`
- `rvest`
- `RSelenium`
- `knitr`

You can install them using:
```r
install.packages(c("tidyverse", "rvest", "RSelenium", "knitr"))
```

## Components

### 1. Data Collection
The project starts by loading the necessary libraries and defining the main URL for animation videos on Myket:
```r
main_url = 'https://myket.ir/video/animation'
```

An example URL is also provided to demonstrate the extraction process for a single animation page:
```r
example_url <- 'https://myket.ir/video/v-U5ZS7UJ6LZ/snoopy-presents-welcome-home-franklin'
webpage <- read_html(example_url)
```

### 2. Web Scraping Functions
Several functions are defined to automate the web scraping process:

- **`scrape()`**: Extracts data from a given webpage based on an HTML selector and attribute.
- **`get_anime_data()`**: Collects specific features from an animation page.
- **`get_anime_urls()`**: Retrieves URLs of all animation videos by navigating through the pages.
- **`create_anime_data()`**: Aggregates data from all collected animation pages into a dataframe.

### 3. Data Processing
Each animation feature is extracted from specific HTML tags and attributes. The project structures the scraped data into a dataframe, making it suitable for further analysis.

## Thank you all!![![](https://raw.githubusercontent.com/aregtech/areg-sdk/master/docs/img/pin.svg)](#thank-you)

Special thanks to all contributors and supporters that starred this repository.

Our amazing contributors:
- [@3oop](https://www.github.com/3oop)
- [@yasinaghaee](https://www.github.com/yasinaghaee)
- [@mkhsa](https://www.github.com/mkhsa)
- [@Rosa-Kariman ](https://www.github.com/Rosa-Kariman)

