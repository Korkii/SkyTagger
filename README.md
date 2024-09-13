
# SkyTagger 

This project revolves around the two models, WALDO and SparseMask, for segmentation & detection of satellite images.


## Demo




![App Screenshot](https://i.imgur.com/DcZ9Y9L.png)
## Run Locally

Clone the project

```bash
  git clone https://github.com/Korkii/SkyTagger
```

Go to the project directory

```bash
  cd SkyTagger
```

### Installing SparceMask
Create a folder inside `src` named `models`, inside it create another folder named `SparceMask`, and place the two files  `checkpoint_63750.pth` and `mask_thres_0.001.npy` inside it.
[The Open Earth Map Repo](https://github.com/cliffbb/oem-lightweight)


### Installing WALDO
Make sure you download the WALDO_25_RELEASE_2 zipped file, and unzip it so it's path will be: `\src\WALDO_25_RELEASE_2\`

[The WALDO Repo](https://github.com/stephansturges/WALDO)

### Python
Make sure to use the version *3.10*, the dependencies rely on that.
```bash
pip3 install -r requirements.txt
```

And you are all set!
