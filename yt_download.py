#!/usr/bin/python

from __future__ import unicode_literals
import youtube_dl
import os
import re
import shutil

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('\n\nDone downloading, now converting ...\n\n')

ydl_opts = { 
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def get_it(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        print(60 * '-')
        print('title       : %s' %(info_dict['title']))
        print('description : %s' %(info_dict['description']))
        print('duration    : %s' %(info_dict['duration']))
        print('format      : %s' %(info_dict['format']))
        print(60 * '-')
        ydl.download([link])

def print_menu():
    print('\t\t' + 20 * '-' + 'MENU' + 20 * '-')
    print('\t\t' + '1. Download YouTube Video as MP3')
    print('\t\t' + '2. Exit')
    print('\t\t' + 44 * '-')


def downloader():
    print_menu()
    choice = int(input('# '))
    while choice != 2:
        get_it(input('Link: '))
        print_menu()
        choice = int(input('# '))

def move_that_shit(where):
    dir = '.'
    add = 1
    if where[len(where) - 1] == '/':
        add = 0
    mp3_reg = re.compile('(.*mp3)')
    for shit in os.walk(dir):
        for file in shit:
            for i in file:
                if mp3_reg.match(i) and add:
                    shutil.move(i, where + '/' + i)
                elif mp3_reg.match(i) and not add:
                    shutil.move(i, where  + i)



if __name__ == "__main__":
    downloader()
    move_that_shit(input('Move mp3 files to: (/absolute/path): '))
    exit(0)