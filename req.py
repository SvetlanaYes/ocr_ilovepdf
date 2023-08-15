try:
    import requests
    from os import walk
    import os
    from PyPDF2 import PdfReader, PdfWriter
    import sys
    import argparse
except ImportError as exception:
    print("You should import certain libraries")
    exit(0)


URL = 'http://www.ilovepdf.com/ru/ocr-pdf'


def argument_parser():
    parser = argparse.ArgumentParser("Performing OCR on PDFs using ilovepdf.com")
    parser.add_argument("-dir", "--directory", type=str, required=True, help='Path to directory containing pdf files.')
    return parser.parse_args()


def get_task(t):
    index = t.find("taskId")
    index1 = t[index:].find("'") + 1
    index2 = t[index + index1:].find("'")
    return t[index + index1: index + index1 + index2]


def split_pdf_to_allowed_size(full_name, dir_name, f):
    i = 0
    with open(full_name, "rb") as s:
        pdf_rdr = PdfReader(s)
        os.makedirs(dir_name[1:] + "splited/" + f[:-4])
        for i in range(len(pdf_rdr.pages) // 10):
            pdf_wrt = PdfWriter()
            for j in range(10):
                pdf_wrt.add_page(pdf_rdr.pages[i * 10 + j])
            with open(dir_name[1:] + "splited/" + f[:-4] + "/" + str(i) + ".pdf", "wb") as o:
                pdf_wrt.write(o)

        count = (i + 1) * 10
        pdf_wrt = PdfWriter()
        while count < len(pdf_rdr.pages) - 1:
            count += 1
            pdf_wrt.add_page(pdf_rdr.pages[count])
            with open(dir_name[1:] + "splited/" + f[:-4] + "/" + str(i + 1) + ".pdf", "wb") as o:
                pdf_wrt.write(o)


def upload_pdf(my_path, f, task, full_name, url):


    payload = {'name': my_path + "/" + f,
               'chunk': '0',
               'chunks': '2',
               'task': task,
               'preview': '1',
               'pdfinfo': '0',
               'pdfforms': '0',
               'pdfresetforms': '0',
               'v': 'web.0',

               }

    files = {
        'file': open(full_name, "rb")}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIiLCJhdWQiOiIiLCJpYXQiOjE1MjMzNjQ4MjQsIm5iZiI6MTUyMzM2NDgyNCwianRpIjoicHJvamVjdF9wdWJsaWNfYzkwNWRkMWMwMWU5ZmQ3NzY5ODNjYTQwZDBhOWQyZjNfT1Vzd2EwODA0MGI4ZDJjN2NhM2NjZGE2MGQ2MTBhMmRkY2U3NyJ9.qvHSXgCJgqpC4gd6-paUlDLFmg0o2DsOvb1EUYPYx_E',
        'Origin': 'https://www.ilovepdf.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ilovepdf.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Cookie': '_csrf=-uOJUzTAbqZjgoEspw2IxbXmHqLaQw4a'
    }

    r = requests.request("POST", url, headers=headers, data=payload, files=files)
    if r.status_code == 200:
        print("Response status code is 200 (OK) for upload")
    else:
        print(f"Response status code is {response.status_code}")


def get_server_filename(my_path, f, task, url):
    payload = {'name': my_path + "/" + f,
               'chunk': '1',
               'chunks': '2',
               'task': task,
               'preview': '0',
               'v': 'web.0'}
    files = {
        'file': open(my_path + "/" + f, "rb")}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIiLCJhdWQiOiIiLCJpYXQiOjE1MjMzNjQ4MjQsIm5iZiI6MTUyMzM2NDgyNCwianRpIjoicHJvamVjdF9wdWJsaWNfYzkwNWRkMWMwMWU5ZmQ3NzY5ODNjYTQwZDBhOWQyZjNfT1Vzd2EwODA0MGI4ZDJjN2NhM2NjZGE2MGQ2MTBhMmRkY2U3NyJ9.qvHSXgCJgqpC4gd6-paUlDLFmg0o2DsOvb1EUYPYx_E',
        'Origin': 'https://www.ilovepdf.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ilovepdf.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Cookie': '__cf_bm=Y91EghaucFsN7oj3_XBmsfVAsGnRWPz6hZqafU0Rino-1684491255-0-AQ1Z5oEFclejXdkZjeyix02gx9zOy5M4yKLffyRQdvfUCOfmlJWnwXHI95cHnYyvJdj5d6Y1piuIOafhhY8QZGY=; _csrf=L5JnjzEaDu-3vT9o9Vz-NC5z-zf__qmr'
    }

    r = requests.request("POST", url, headers=headers, data=payload, files=files)
    if r.status_code == 200:
        print("Response status code is 200 (OK) for getting server filename")
    else:
        print(f"Response status code is {response.status_code}")
    t = r.json()
    return t


def ocr_pdf(task, t, my_path, f, url):
    payload = {'convert_to': 'pdf',
               'output_filename': '{filename}',
               'packaged_filename': 'ilovepdf_ocr',
               'ocr_languages[0]': 'rus',
               'task': task,
               'tool': 'pdfoffice',
               'files[0][server_filename]': t["server_filename"],
               'files[0][filename]': my_path + "/" + f}
    files = [
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIiLCJhdWQiOiIiLCJpYXQiOjE1MjMzNjQ4MjQsIm5iZiI6MTUyMzM2NDgyNCwianRpIjoicHJvamVjdF9wdWJsaWNfYzkwNWRkMWMwMWU5ZmQ3NzY5ODNjYTQwZDBhOWQyZjNfT1Vzd2EwODA0MGI4ZDJjN2NhM2NjZGE2MGQ2MTBhMmRkY2U3NyJ9.qvHSXgCJgqpC4gd6-paUlDLFmg0o2DsOvb1EUYPYx_E',
        'Origin': 'https://www.ilovepdf.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ilovepdf.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Cookie': '_csrf=B_JcfvL_iANE0tLedNteOaGIJl5o14G-'
    }

    return requests.request("POST", url, headers=headers, data=payload, files=files)


def save_pdf(task, dir_name, f):
    url = "https://api13o.ilovepdf.com/v1/download/" + task
    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ilovepdf.com/',
        'Cookie': '__cf_bm=tC90skJmrNV_3T1PcPVJPt6566wmRd578_IdnFwVHPw-1684495775-0-AbxfA7bj4KgC/H9QhYPdSCS8evyWAKJB1iyjYfMOcV1+XhZYRItdR5TEVryDMESENzwTLmtRGRNq3hoYq/A29t0=; _csrf=_5ePF74rrcn3ixImid-M8jA6aEcqQ7Mt',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    content = response.content
    os.makedirs(os.path.dirname("ocred" + dir_name + f[:-4] + "/" + f[:-4] + "_ocr.pdf"), exist_ok=True)
    with open("ocred" + dir_name + f[:-4] + "/" + f[:-4] + "_ocr.pdf", 'wb') as f:
        f.write(content)


def main(args, URL):
    r = requests.get(URL)
    t = r.text

    my_path = args.directory
    dir_name = my_path[my_path.rfind("/"):] + "/"
    filenames = next(walk(my_path), (None, None, []))[2]

    task = get_task(t)
    current_path = my_path

    for f in filenames:
        full_name = current_path + "/" + f
        split_pdf_to_allowed_size(full_name, dir_name, f)
        splt_name = dir_name[1:] + "splited/" + f[:-4]
        filenames_splt = next(walk(splt_name), (None, None, []))[2]
        
        for f_splt in filenames_splt:
            my_path = splt_name
            f = f_splt
            full_name = my_path + "/" + f
            url = "https://api13o.ilovepdf.com/v1/upload"
            upload_pdf(my_path, f, task, full_name, url)
            t = get_server_filename(my_path, f, task, url)
            url = url[:-6] + "process"
            response = ocr_pdf(task, t, my_path, f, url)

            if response.json()["status"] == "TaskSuccess":
                save_pdf(task, dir_name, f)


if __name__ == "__main__":
    args = argument_parser()
    main(args, URL)
