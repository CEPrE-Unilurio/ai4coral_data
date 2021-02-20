# ai4coral_data
<p align="center">
  <a href="https://typer.tiangolo.com"><img src="https://cdn4.iconfinder.com/data/icons/technology-83/1000/technology_app_system_grid_system_grid_data_water-128.png" alt="AI Coral Data"></a>
</p>
<p align="center">
    <em>Data plumbing CLI for the AI Coral Project.</em>
</p>
<p align="center">
<a href="https://github.com/CEPrE-Unilurio/ai4coral_data/actions?query=workflow:'Ai Coral Data Python package'" target="_blank">
    <img src="https://github.com/tiangolo/typer/workflows/Test/badge.svg" alt="Test">
</a>
</p>



# overview
![Alt text](coral_ai_data.png?raw=true "Title")

# goal
Make and run datapipelines for training on for underwater_od modelling package.

# features
1. Produce training data in Tensorflow format based on Raspberry PI data from the data acquisition mechanism
2. Deal with annotation system

# how to use it

1. Clone the repo

2. CD into the main folder

3. Create a config.json copied from conf.json and add the right token

4. To download data : `python aicoral_data/main.py sa_download_files "Test Project"`

4. To upload data : `python ai4coral_data/main.py sa_upload_image_folder_files "Test Project" ./Downloads`

