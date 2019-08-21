import time
from datetime import datetime as dt


hosts_path = '/etc/hosts'
redirect = "127.0.0.1"
website_urls = ["www.netflix.com", "www.facebook.com", "www.vk.com"]
start_working_hour = 9
finish_working_hour = 20


def add_sites_to_hosts_file():
    with open(hosts_path, 'r+') as hosts_file:
        content = hosts_file.read()
        for website in website_urls:
            if website in content:
                pass
            else:
                hosts_file.write('{} {}\n'.format(redirect, website))


def remove_blocking_sites_from_hosts_file():
    with open(hosts_path, 'r+') as hosts_file:
        content = hosts_file.readlines()
        hosts_file.seek(0)
        for line in content:
            if not any(website in line for website in website_urls):
                hosts_file.write(line)
            hosts_file.truncate()


start_work_dt = dt(dt.now().year, dt.now().month, dt.now().day, start_working_hour)
finish_work_dt = dt(dt.now().year, dt.now().month, dt.now().day, finish_working_hour)

while True:
    if start_work_dt < dt.now() < finish_work_dt:
        print('working')
        add_sites_to_hosts_file()
    else:
        print('chill')
        remove_blocking_sites_from_hosts_file()

    time.sleep(5)
