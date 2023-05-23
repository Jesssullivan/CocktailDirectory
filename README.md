A simple, general purpose cocktail directory application.  

A work in progress for [The Watershed](https://ithacawatershed.com/), [The Downstairs](http://thedownstairsithaca.com/) and [Modern Alchemy Game Bar](https://www.alchemygamebar.com/).  

The objective of this project is to:
  - streamline the assembly of obscure house cocktails as a bartender
  - manage all recipes *without* a master database;
    - directory is managed as an exportable / servable dataframe
    - web client includes a complete client side typeahead search feature and a complete copy of the directory dataframe; this way bartenders do not need to rely on internet to continue service 
    - modifications from web clients are queued and parsed on the server- the dataframe object is available at a regularly updated static endpoint
- encurage bartenders to add / modify house cocktail recipes as they become available or deprecated
- encurage the creation of new, ephemeral cocktails as new local spirits / ingredients come and go



## Quickstart
```
# node:
npm install

# venv:
python3 -m venv cocktail_venv
source cocktail_venv/bin/activate
pip3 install -r requirements.txt

# serve: 
npm run-script setup-app  # interactive setup and build
npm run-script serve-app  # serve with default Flask WSGI
```

### Data structures
Hack on your data structures from an ipython notebook:
```
# install dev requirements: jupyterlab, pandas, matplotlib
pip3 install -r dev-requirements.txt

## launch jupyterlab:
jupyter lab # ...
```
