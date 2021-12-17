#!/bin/sh
pip install --upgrade pip
pip install requests
python /scripts/te_deploy.py --files $1 --tenant_id $2 --db_url $3