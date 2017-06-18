import urllib
import os
import json

PARENT_DIR = './images'
DATA_SOURCE = 'data.json'

def get_data():
    with open(DATA_SOURCE) as data:
        return json.load(data)


def collect_images(data):
    """
    Expected format:
        {
            "subdir name": [
                url1,
                url2,
                ...
            ]
        }
    """
    for subdir in data.keys():
        print 'PROCESSING ' + subdir
        print '='*80

        mkdir_if_not_exists(subdir)

        unique_id = 0

        for image_url in data[subdir]:
            unique_id += 1
            image_name = "%s_%s" % (subdir, unique_id)
            image_dest = os.path.join(PARENT_DIR, subdir, image_name)
            download_image(image_url, image_dest)


def mkdir_if_not_exists(dir_name):
    path = os.path.join(PARENT_DIR, dir_name)
    if not os.path.exists(path):
        os.makedirs(path)


def download_image(image_url, image_dest):
    file_extension = image_url.split('.')[-1]
    image_dest = "%s.%s" % (image_dest, file_extension)

    print "Downloading %s to %s" % (image_url, image_dest)
    try:
        urllib.urlretrieve(image_url, image_dest)
        print "Success!"
        return image_dest
    except Exception as e:
        print "Got error!"
        print (str(e))
        return False


if __name__ == '__main__':
    collect_images(get_data())
