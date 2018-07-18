# -*- coding:utf-8 -*-
"""
@project = 0527-2
@file = matplotlib_3
@author = Liangjisheng
@create_time = 2018/5/27 0027 下午 19:56
"""
# 通过抓取GitHub上受欢迎程度最高的Python项目，绘制出图表
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Staus code: ', r.status_code)

response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])
# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

# 研究仓库有关的信息
# Name: macOS-Security-and-Privacy-Guide
# Owner: drduh
# Stars: 12348
# Repository: https://github.com/drduh/macOS-Security-and-Privacy-Guide
# Description: A practical guide to securing macOS.
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict["stargazers_count"])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化数据
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Stared Python Project on Github'
chart.x_labels = names
print(plot_dicts)
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
