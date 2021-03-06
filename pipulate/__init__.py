#  _____ _     _       _       ____  _             _       _
# |_   _| |__ (_)___  (_)___  |  _ \(_)_ __  _   _| | __ _| |_ ___
#   | | | '_ \| / __| | / __| | |_) | | '_ \| | | | |/ _` | __/ _ \
#   | | | | | | \__ \ | \__ \ |  __/| | |_) | |_| | | (_| | ||  __/
#   |_| |_| |_|_|___/ |_|___/ |_|   |_| .__/ \__,_|_|\__,_|\__\___|
# There are many frameworks like it,  |_| but this one is mine. --MikeL

# IMPORTANT THINGS TO REMEMBER:
# 1. Make life easy by filling your ~/.bash_profile with aliases.
# 2. Make life easy by filling /usr/local/sbin with helper scripts.
# 3. Without virtualenv, pip ~puts things: /usr/local/lib/python3.6/dist-packages/
# 4. With virtualenv, pip ~puts things: /home/MikeL/py36/lib/python3.6/site-packages
# 5. oauth2client is deprecated. Replace it soon.

import sys
import os
import httplib2
import argparse
import json
import pytz
from collections import defaultdict
from datetime import datetime, timedelta
from inspect import currentframe, getouterframes
from oauth2client.client import OAuth2WebServerFlow
from oauth2client import file, tools
import gspread
import pandas as pd
from pyfiglet import figlet_format
from logzero import logger, setup_logger
from colorama import Fore


filename = "oauth.dat"
client_id = "769904540573-knscs3mhvd56odnf7i8h3al13kiqulft.apps.googleusercontent.com"
client_secret = "D2F1D--b_yKNLrJSPmrn2jik"
log = setup_logger(logfile='log.log')

# To count how frequently functions have been called.
counters = defaultdict(int)


def pipulate(tab, rows, cols, columns=None):
    """All that pipulate really is"""

    row1, row2 = rows
    col1, col2 = cols
    col1, col2 = a1(col1, reverse=True), a1(col2, reverse=True)
    cl = tab.range(row1, col1, row2, col2)
    list_of_lists = cl_to_list(cl)
    if not columns:
        columns = tab.range(row1, col1, row1, col2)
        columns = [a1(x.col) for x in columns]
    df = pd.DataFrame(list_of_lists, columns=columns)
    print('cl, df = gs.pipulate("%s", rows=%s, cols=%s) was successful.' % (tab.title, rows, cols))
    print("You may now manipulate the DataFrame but maintain its (%s x %s) shape." % df.shape)
    print('To update the GSheet with changes, gs.populate("%s", cl, df)' % tab.title)
    return cl, df


def populate(tab, cl, df):
    """Push df back to spreadsheet."""

    if cl_df_fits(cl, df):
        lol = df.values.tolist()
        flat = [y for x in lol for y in x]
        flat[:] = ['N/A' if pd.isnull(x) else x for x in flat]
        for i, cell in enumerate(cl):
            cell.value = flat[i]
        tab.update_cells(cl)
    else:
        raise SystemExit()
    print('gs.populate("%s", cl, df) <<< GSHEET UPDATED! >>>' % tab.title)
    print()


def cl_to_list(cl):
    new_table = []
    for i, cell in enumerate(cl):
        if i == 0:
            row_num = 1
            memory = cell.row
            row = [cell.value]
        if cell.row == memory and i > 0:
            row.append(cell.value)
        else:
            row_num += 1
            memory = cell.row
            row = [cell.value]
            new_table.append(row)
    return new_table


def cl_df_fits(cl, df):
    """Check if GSpread cell list same shape as Pandas dataframe."""
    list_of_lists = cl_to_list(cl)
    height = len(list_of_lists)
    width = len(list_of_lists[0])
    size_tuple = (height, width)
    if size_tuple == df.shape:
        return True
    print('GOOGLE SHEET NOT UPDATED.')
    print('cl %s and df %s different sizes.' % (size_tuple, df.shape))
    return False


def a1(pos, reverse=False):
    """Return the column letter for numeric column index."""
    if reverse:
        return gspread.utils.a1_to_rowcol('%s1' % pos)[1]
    if str(pos).isdigit():
        return gspread.utils.rowcol_to_a1(1, pos)[:-1]
    else:
        return "Must be integer"


def spreadsheet(key):
    """Return instance of GSheet by key."""
    return oauth().open_by_key(key)


def key(key):
    """Alias to Return instance of GSheet by key."""
    return oauth().open_by_key(key)


def get_email():
    """Return email given provided Google OAuth account."""
    service = create_google_service(filename, "oauth2", "v2")
    user_document = service.userinfo().get().execute()
    email = user_document['email']
    return email


def link(gsheet_key):
    """Return GSheet URL for data from Web UI."""
    return 'https://docs.google.com/spreadsheets/d/%s/edit' % gsheet_key


def name(name):
    """Return instance of GSheet by document name"""
    return oauth().open(name)


def module_name():
    """Return name of calling module; good at the end of cached functions.
    Also creates and increments a counter per calling function."""

    global counters
    current_frame = currentframe()
    outer_frame = getouterframes(current_frame, 2)
    name = outer_frame[1][3]
    counters[name] += 1
    return_me = '(%s: %s) ' % (name, counters[name])
    return return_me


class AccessToken(object):
    """Return authentication object given access_token."""
    def __init__(self, access_token=None):
        self.access_token = access_token


def creds():
    """Create Google OAuth credential object for resources that need it."""

    path = os.path.dirname(os.path.realpath('__file__'))
    path_filename = os.path.join(path, filename)
    storage = file.Storage(path_filename)
    credentials = storage.get()
    return credentials


def oauth():
    """Create a fully authenticated GSheet connection."""

    scopes = ["https://www.googleapis.com/auth/analytics.readonly",
              "https://www.googleapis.com/auth/webmasters.readonly",
              "https://www.googleapis.com/auth/yt-analytics.readonly",
              "https://www.googleapis.com/auth/youtube.readonly",
              "https://spreadsheets.google.com/feeds/",
              "https://www.googleapis.com/auth/gmail.modify",
              "https://www.googleapis.com/auth/userinfo.email"]

    path = os.path.dirname(os.path.realpath('__file__'))
    path_filename = os.path.join(path, filename)
    flow = OAuth2WebServerFlow(client_id, client_secret, scopes,
                               redirect_uri='urn:ietf:wg:oauth:2.0:oob',
                               response_type='code',
                               prompt='consent',
                               access_type='offline')
    storage = file.Storage(path_filename)
    credentials = storage.get()
    argparser = argparse.ArgumentParser(add_help=False)
    parents = [argparser]
    parent_parsers = [tools.argparser]
    parent_parsers.extend(parents)
    parser = argparse.ArgumentParser(
        description="__doc__",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=parent_parsers)
    flags = parser.parse_args(['--noauth_local_webserver'])
    try:
        http = credentials.authorize(http=httplib2.Http())
    except AttributeError:
        pass
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)
    else:
        credentials.refresh(http)
    with open(path_filename) as json_file:
        jdata = json.load(json_file)
    token = jdata['access_token']
    access = AccessToken(access_token=token)
    connect = gspread.authorize(access)
    return connect


def api_date(a_datetime, time=False):
    """Return datetime string in Google API friendly format."""
    if time:
        return ('{0:%Y-%m-%d %H:%M:%S}'.format(a_datetime))
    else:
        return ('{0:%Y-%m-%d}'.format(a_datetime))


def human_date(a_datetime, time=False):
    """Return datetime object as American-friendly string."""
    if time:
        return ('{0:%m/%d/%Y %H:%M:%S}'.format(a_datetime))
    else:
        return ('{0:%m/%d/%Y}'.format(a_datetime))


def date_ranges(human=False, yoy=True):
    """Return a list of 3 commonly used daterange tuples."""

    def dx(x):
        return api_date(x)

    def dh(x):
        return human_date(x)

    lot = list()
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    thirty_days_ago = yesterday - timedelta(days=30)
    prior_30_end = thirty_days_ago - timedelta(days=1)
    prior_30_start = prior_30_end - timedelta(days=30)
    if yoy:
        last_range_end = yesterday.replace(year=yesterday.year - 1)
        last_range_start = thirty_days_ago.replace(year=thirty_days_ago.year - 1)
    else:
        last_range_end = thirty_days_ago - timedelta(days=32)
        last_range_start = prior_30_end - timedelta(days=60)
    if human:
        lot.append((dh(thirty_days_ago), dh(yesterday)))
        lot.append((dh(prior_30_start), dh(prior_30_end)))
        lot.append((dh(last_range_start), dh(last_range_end)))
        lot = [(x + ' - ' + y) for x, y in lot]
    else:
        lot.append((dx(thirty_days_ago), dx(yesterday)))
        lot.append((dx(prior_30_start), dx(prior_30_end)))
        lot.append((dx(last_range_start), dx(last_range_end)))
    return lot


def date_ranger(starts=(30, 90, 180), days=30, start=1, human=False):
    """Returns 3 date ranges from days-ago starts to days-later."""

    def dx(x):
        return api_date(x)

    def dh(x):
        return human_date(x)

    lot = list()
    today = datetime.now()
    yesterday = today - timedelta(days=start)
    firstrange_start = yesterday - timedelta(days=starts[0])
    firstrange_end = firstrange_start + timedelta(days=days)
    midrange_start = yesterday - timedelta(days=starts[1])
    midrange_end = midrange_start + timedelta(days=days)
    lastrange_start = yesterday - timedelta(days=starts[2])
    lastrange_end = lastrange_start + timedelta(days=days)
    if human:
        lot.append((dh(firstrange_start), dh(firstrange_end)))
        lot.append((dh(midrange_start), dh(midrange_end)))
        lot.append((dh(lastrange_start), dh(lastrange_end)))
        lot = [(x + ' - ' + y) for x, y in lot]
    else:
        lot.append((dx(firstrange_start), dx(firstrange_end)))
        lot.append((dx(midrange_start), dx(midrange_end)))
        lot.append((dx(lastrange_start), dx(lastrange_end)))
    return lot


def gmt():
    """Returns current time in Greenwich Mean Time"""
    from time import gmtime, strftime
    return strftime("%a, %d %b %Y %H:%M", gmtime())


def timestamp():
    """Returns local time formatted for timestamp."""
    return '{0:%a, %b %d ~%I:%m %p} GMT'.format(datetime.now(pytz.utc))


def create_google_service(filename, api_name, version):
    """Return instance of Google Service object."""

    from apiclient.discovery import build
    path = os.path.dirname(os.path.realpath('__file__'))
    path_filename = os.path.join(path, filename)
    storage = file.Storage(path_filename)
    credentials = storage.get()
    http = credentials.authorize(http=httplib2.Http())
    service = build(api_name, version, http=http)
    return service


def ga_url(gaid, start, end, path):
    """Return Google Analytics metrics for a URL."""

    path = path.replace(',', r'\,')
    service = ga()
    metrics = ['users', 'newUsers', 'sessions', 'bounceRate',
               'pageviewsPerSession', 'avgSessionDuration']
    metrics = ''.join(['ga:%s,' % x for x in metrics])[:-1]
    ga_request = service.data().ga().get(
        ids='ga:' + gaid,
        start_date=start,
        end_date=end,
        metrics=metrics,
        dimensions='ga:pagePath',
        sort='-ga:users',
        filters='ga:pagePath==' + path,
        segment='sessions::condition::ga:medium==organic',
        max_results=1
    )
    ga_response = ga_request.execute()
    rval = []
    if 'rows' in ga_response:
        raw_rows = ga_response['rows'][0]
        rval = raw_rows
    return rval


def gsc_url_keyword(prop, start, end, query, url):
    service = gsc()
    request = {
        "startDate": start,
        "endDate": end,
        "dimensions": [
            "query",
            "page"],
        "dimensionFilterGroups": [
        {
            "filters": [
            {
                "operator": "equals",
                "expression": url,
                "dimension": "page"
            },
            {
                "operator": "equals",
                "expression": query,
                "dimension": "query"
            }]
        }]
    }
    dat = service.searchanalytics().query(siteUrl=prop, body=request).execute()
    val = []
    if 'rows' in dat:  # For the foolish Hobgoblins of PEP8 consistency
        r = dat['rows'][0]
        val = [start] + [r['keys'][0]] + [r['keys'][1]] + [
            r['position']] + [r['clicks']] + [r['impressions']] + [r['ctr']]
    return val


def ga():
    """Return instance of Google Analytics object."""
    return create_google_service(filename, "analytics", "v3")


def gsc():
    """Return instance of Google Search Console object."""
    return create_google_service(filename, "webmasters", "v3")


def h1(print_me, color=Fore.GREEN, font='standard'):
    ''' Never underestimate the power of a good nickname. '''
    ascii_art = figlet_format(print_me, font=font)
    print('%s%s%s' % (color, ascii_art, Fore.WHITE))
    return print_me


def h2(print_me, color=Fore.GREEN, font='cybermedium'):
    ''' The human brain generally only deals well with shallow nesting. '''
    ascii_art = figlet_format(print_me, font=font)
    print()
    print('%s%s%s' % (color, ascii_art, Fore.WHITE))
    return print_me


class Unbuffered(object):
    """Provides more real-time streaming in Jupyter Notebook"""

    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


# Importing pipulate prompts for 1st-time Google login.
try:
    force_it = oauth()
except httplib2.ServerNotFoundError:
    print("You are probably not connected to the Internet.")
    raise SystemExit()
except Exception as e:
    print(type(e).__name__)
# Forces Jupyter Notebook to not buffer output (like streaming).
sys.stdout = Unbuffered(sys.stdout)
api_now = api_date(datetime.now())
human_now = human_date(datetime.now())
