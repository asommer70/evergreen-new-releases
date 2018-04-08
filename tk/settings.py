from pony import orm


db = orm.Database()
db.bind(provider='sqlite', filename='db.sql', create_db=True)
db.generate_mapping(create_tables=True)

#http://nccardinal.org/eg/opac
#/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=132&pubdate=is&date1=&date2=&sort=pubdate.descending

class Setting(db.Entity):
    id = PrimaryKey(int, auto=True)
    key = Required(str)
    value = Required(str)
