import re


def get_job_url(text):
    url_pattern = r"<(.*?)>"
    matches = re.findall(url_pattern, text)
    url = matches[0] if len(matches) > 0 else ""
    url = url.split("|")[0] if len(url.split("|")) > 0 else url
    url = url[7:] if "mailto:" in url else url
    return url


def prepare_slack_message(df):
    main_text = ""
    main_text += "# DataTalks.Club Job Postings\n"
    divider = " ".join([" 🌐 " for i in range(3)]) + "\n"
    for i, row in df.iterrows():
        if row["url"] and row["slack_message_id"] and row["slack_message"]:
            url = row["url"] + "\n"
            message = row["slack_message"] + "\n"
            main_text += divider + " JOB ALERT " + divider + "\n"
            main_text += url + "\n"
            main_text += message + "\n"
    return main_text


def write_to_file(file_name, data):
    with open(file=file_name, mode="w") as file:
        file.write(data)
        return True
