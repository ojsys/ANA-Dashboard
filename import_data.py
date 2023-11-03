import csv
from dashboard.models import Dissemination

def import_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            Dissemination.objects.create(
                today=row['today'],
                firstNameEN=row['firstNameEN'],
                lastNameEN=row['lastNameEN'],
                phoneNrEN=row['phoneNrEN'],
                country=row['country'],
                city=row['city'],
                Latitude=row['Latitude'],
                Longitude=row['Longitude'],
                orgEN=row['orgEN'],
                partner=row['partner'],
                event=row['event'],
                title=row['title'],
                startdate=row['startdate'],
                participant_list=row['participant_list'],
                farmers_M=row['farmers_M'],
            )


if __name__ == '__main__':
    file_path = "dissemination.csv"
    import_data_from_csv(file_path)