from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from zinobechallenge.db import get_db

import requests, json
import numpy as np
import pandas as pd
import time
import random
import hashlib

from werkzeug.security import check_password_hash, generate_password_hash

from zinobechallenge.db import get_db

bp = Blueprint('table', __name__)

@bp.route('/', methods=('GET', 'POST'))
def getallregions():
    if request.method == 'POST':
        pass
    
    headers = {
        "x-rapidapi-key": "3533828e5cmsh43f7bc55f9283e8p1a3a18jsn1873bcc56ba0",
        "x-rapidapi-host": "restcountries-v1.p.rapidapi.com",
        "useQueryString": 'true'
    }

    raw_regions = json.loads(requests.get('https://restcountries-v1.p.rapidapi.com/all', headers=headers).content)

    regions = []

    for country in raw_regions:

        if not country['region'] in regions and country['region']:
            regions.append(country['region'])

    countries = []
    hash_languages = []
    times = []

    for region in regions:

        start_time = time.time()
        raw_countries = json.loads(requests.get('https://restcountries.eu/rest/v2/region/%s'%region).content)
        
        country_seed = random.randint(0,len(raw_countries)-1)

        countries.append(raw_countries[country_seed]['name'])
        hash_languages.append(hashlib.sha1(raw_countries[country_seed]['languages'][0]['name'].encode()).hexdigest())

        end_time = time.time()

        times.append(end_time-start_time)

    df = pd.DataFrame({
        "Region": regions,
        "Country": countries,
        "Language": hash_languages,
        "Time [s]": times
    })

    statistics = {}
    statistics['total'] = df['Time [s]'].sum().round(2)
    statistics['mean'] = df['Time [s]'].mean().round(2)
    statistics['min'] = df['Time [s]'].min().round(2)
    statistics['max'] = df['Time [s]'].max().round(2)

    table_html = [df.to_html(index = False, justify = 'center', classes='table',)]

    db = get_db()

    db.execute(
        'INSERT INTO challenge_zinobe (total_time, mean_time, min_time, max_time) VALUES (?, ?, ?, ?)',
        (statistics['total'], statistics['mean'], statistics['min'], statistics['max'])
    )
    db.commit()

    df.to_json(path_or_buf='data.json')

    return render_template('index.html', tables=table_html, statistics=statistics)

