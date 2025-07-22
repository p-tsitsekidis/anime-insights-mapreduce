#!/usr/bin/env python3
"""
Convert anime dataset from CSV to structured JSON.

This script reads the original anime.csv file, processes and normalizes its contents,
and writes a clean, structured version (anime.json) for use in MongoDB and data analysis.
"""
import csv
import json

json_array = []

with open('data_preprocessing/anime.csv', newline='', encoding='utf-8') as anime_data :
    reader = csv.DictReader(anime_data, delimiter=',')
    
    for line in reader :
        # Empty values are 'None'
        for key in line :
            if line[key] == '' :
                line[key] = None
        
        # Dates are integers
        if line['Release_year'] != None :
                line['Release_year'] = int(float(line['Release_year']))
        if line['End_year'] != None :
                line['End_year'] = int(float(line['End_year']))
        if line['Episodes'] != None :
                line['Episodes'] = int(float(line['Episodes']))
        if line['Rank'] != None :
                line['Rank'] = int(float(line['Rank']))
        if line['Rating'] != None :
                line['Rating'] = float(line['Rating'])
        
        # JSON arrays
        for field in ['Tags', 'Content_Warning', 'Related_Mange', 'Related_anime']:
            if line.get(field) :
                line[field] = [value.strip() for value in line[field].split(',') if value.strip()]
            else :
                line[field] = None
            
        # Voice_actors
        if line.get('Voice_actors'):
            # Handle "\n" bug
            line['Voice_actors'] = line['Voice_actors'].replace('\n', ' ')
            
            voice_actors_items = line['Voice_actors'].split(',')
            if any(':' in item for item in voice_actors_items):
                voice_dict = {}
                for item in voice_actors_items:
                    key_value = item.split(':')
                    if len(key_value) == 2:  # Ensure there are two elements after splitting
                        voice_dict[key_value[0].strip()] = key_value[1].strip()
                line['Voice_actors'] = voice_dict
            else:
                line['Voice_actors'] = [actor.strip() for actor in voice_actors_items if actor.strip()]
        else:
            line['Voice_actors'] = None
        
        # Staff
        if line.get('staff'):
            staff_items = line.get('staff').split(',')
            staff_dict = {}
            for item in staff_items:
                key_value = item.split(':')
                if len(key_value) == 2:
                    # Trim whitespace from both key and value
                    staff_dict[key_value[1].strip()] = key_value[0].strip()
            line['staff'] = staff_dict
        
        json_array.append(line)
    
with open('data_preprocessing/anime.json', mode='w', encoding='utf-8', newline='\n') as json_file :
    json.dump(json_array, json_file, ensure_ascii=False, indent=4)