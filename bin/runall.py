#!/usr/bin/env python

import os
import socket
import urllib
import subprocess
import time


path_apphome = os.path.dirname(os.path.abspath(__file__)) + '/..'
os.chdir(path_apphome)
# os.system('ls')

def checkportopen(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock.connect_ex(('127.0.0.1', port)) == 0

def mkapps():
    if not os.path.isdir(path_apphome + '/data'): os.makedirs(path_apphome + '/data')
    if not os.path.isdir(path_apphome + '/data/mcp-8100'): os.makedirs(path_apphome + '/data/mcp-8100')
    if not os.path.isdir(path_apphome + '/data/mcp-8100/apps'): os.makedirs(path_apphome + '/data/mcp-8100/apps')

# if not checkportopen(9200):
#     print "Elasticsearch is not running"
#     mkapps()
#     elasticversion = 'elasticsearch-5.6.5'
#     if not os.path.isfile(path_apphome + '/data/mcp-8100/apps/' + elasticversion + '.tar.gz'):
#         print('Downloading ' + elasticversion)
#         urllib.urlretrieve ('https://artifacts.elastic.co/downloads/elasticsearch/' + elasticversion + '.tar.gz', path_apphome + '/data/mcp-8100/apps/' + elasticversion + '.tar.gz')
#     if not os.path.isdir(path_apphome + '/data/mcp-8100/apps/elasticsearch'):
#         print('Decompressing' + elasticversion)
#         os.system('tar xfz ' + path_apphome + '/data/mcp-8100/apps/' + elasticversion + '.tar.gz -C ' + path_apphome + '/data/mcp-8100/apps/')
#         os.rename(path_apphome + '/data/mcp-8100/apps/' + elasticversion, path_apphome + '/data/mcp-8100/apps/elasticsearch')
#     # run elasticsearch
#     print('Running Elasticsearch')
#     os.chdir(path_apphome + '/data/mcp-8100/apps/elasticsearch/bin')
#     os.system('nohup ./elasticsearch &')

os.chdir(path_apphome)
    
#subprocess.call('bin/update_all.sh')

if not checkportopen(2121):
    print "ftp server is not Running"
   
if not checkportopen(8100):
    print "yacy_grid_mcp is not running,running yacy_grid_mcp"
    os.system('gradle run')
##    time.sleep(5)
##    
##
##if not checkportopen(8200):
##    print "yacy_grid_loader is not running,running yacy_grid_loader"
##    os.system('cd ../yacy_grid_loader')
##    os.system('gradle run')
##    time.sleep(5)
##    
##
##if not checkportopen(8300):
##    print "yacy_grid_crawler is not running,running yacy_grid_crawler"
##    os.system('cd ../yacy_grid_crawler')
##    os.system('gradle run')
##    time.sleep(5)
##    
##
##if not checkportopen(8500):
##    print "yacy_grid_parser is not running,running yacy_grid_parser"
##    os.system('cd ../yacy_grid_parser')
##    os.system('gradle run')
##    time.sleep(5)
