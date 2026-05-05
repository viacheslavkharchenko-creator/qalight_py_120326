import csv
from pathlib import Path


def get_csv_dict(csv_file: Path):
    with csv_file.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_csv_list(csv_file: Path):
    with csv_file.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def write_csv(csv_file: Path, data_list:list):
    with csv_file.open("w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_STRINGS)#
        writer.writerows(data_list)

if __name__ == "__main__":
    my_dir = Path(__file__).parent
    csv_file =  my_dir / "just.csv"
    # print(get_csv_dict(csv_file))
    csv_data = get_csv_list(csv_file)
    print(csv_data)
    new_file = my_dir / "new.csv"
    write_csv(new_file, csv_data)
