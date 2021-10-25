import csv


def read_stamp_infos():
    """
    read the opensea csv file from the /data folder
    :return: list of csv elements
    """
    nft_data = []

    with open('data/OpenSea.CSV', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            nft_data.append({
                "asset_title": row[0],
                "external_url": row[1],
                "description": row[2],
                "unlockable": row[3],
                "max_supply": row[4],
                "property": row[5],
                "value": row[6],
                "image_name": row[7]
            })

    return nft_data
