import re

def get_job_url(text):
    url_pattern = r'<(.*?)>'
    matches = re.findall(url_pattern, text)
    url = matches[0] if len(matches)>0 else ''
    url = url.split('|')[0] if len(url.split('|'))>0 else url
    url = url[7:] if 'mailto:' in url else url
    return url


