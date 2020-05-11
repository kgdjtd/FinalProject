#Gage Dennis
#Python 3
#Final Project
#Discord bot website scraper

import os
import random
from discord.ext import commands
from datetime import datetime
import pickle
import requests
from bs4 import BeautifulSoup

#pickle_in = open("Discord_Token","rb")
#TOKEN = pickle.load(pickle_in)
#pickle_in.close()

file_open = open('Discord_Token', 'r')
TOKEN = file_open.read()
file_open.close()

GUILD = 'Test Server'

bot = commands.Bot(command_prefix='!')

@bot.command(name='jobsearch', title=' ', location=' ')

async def jobsearch(ctx, title, location):
        main_URL = 'https://www.monster.com/jobs/search/?q='
        part_URL = '&where='
        URL = main_URL + title + part_URL + location
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='ResultsContainer')
        #await ctx.send(results.prettify())

        job_elems = results.find_all('section', class_='card-content')
        run = 0
        while run < 2 :
                run = run + 1
                for job_elem in job_elems:
                        while run == 1:
                                title_elem = job_elem.find('h2', class_='title')
                                company_elem = job_elem.find('div', class_='company')
                                location_elem = job_elem.find('div', class_='location')
                                if None in (title_elem, company_elem, location_elem):
                                        continue

                                job_title = (title_elem.text)
                                company_title = (company_elem.text)
                                location_title = (location_elem.text)
                                await ctx.send(job_title)
                                await ctx.send(company_title)
                                await ctx.send(location_title)
                                run = run + 1

        #python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
        #for p_job in python_jobs:
                #link = p_job.find('a')['href']
                #await ctx.send(p_job.text.strip())
                #await ctx.send('Apply here: {link}\n')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')

async def nine_nine(ctx):
        brooklyn_99_quotes = [
                'Im the human form of the :100: emoji.',
                'Bingpot!',
                (
                        'Cool. Cool cool cool cool cool cool cool.',
                        'no doubt no doubt no doubt no doubt.'
                ),
        ]

        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)

@bot.command(name='taco', help='Responds as a taco fanatic')

async def taco(ctx):
        taco_quotes = [
                'Did I hear taco?!?!',
                'Taco Tuesday! My favorite day!',
                'Which Taco Bell we crashin?',
                'I asked for sauce, and I got NONE!',
                'Taco cat spelled backwards is taco cat',
                'Am I spelling taco right? Taco, Taco, Taco!',
                'Me me me!',
                'Gimme.',
                ':eyes:'
                ]
        response = random.choice(taco_quotes)
        await ctx.send(response)

@bot.command(name='date', help='Responds with current date and time')

async def date(ctx):
        now = datetime.now()
        date = now.strftime('%m/%d/%Y, %H:%M:%S')
        response = date
        await ctx.send(response)

bot.run(TOKEN)

