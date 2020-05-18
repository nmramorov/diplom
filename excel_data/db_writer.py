from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

from excel_data.excel_data_getter import ExcelDataGetter

Base = declarative_base()

db_string = 'postgresql+psycopg2://dbadmin:password123@localhost/db'

db = create_engine(db_string)

meta = MetaData(db)

getter = ExcelDataGetter(filename="/home/nmramorov/repos/diplom/diplom_data/Chronometer/test_protocol_new_format.xlsx")

excel_data = getter.get_excel_data()

participants_table = Table('participants', meta,
                           Column('sheet', String(25)),
                           Column('index', Integer),
                           Column('identifier', Integer),
                           Column('initials', String(length=50)),
                           Column('team', String(length=100)),
                           Column('year_of_birth', Integer),
                           Column('grade', String(length=5)),
                           Column('first_track', DateTime),
                           Column('second_track', DateTime),
                           Column('sum', Integer))

with db.connect() as conn:
    participants_table.create()
    sheet_names = getter.get_sheetnames()

    for sheet, sheet_name in zip(excel_data, sheet_names):
        for participant in sheet:
            insert_statement = participants_table.insert().values(sheet=sheet_name,
                                                                  index=participant.index,
                                                                  identifier=participant.identifier,
                                                                  initials=participant.initials,
                                                                  team=participant.team,
                                                                  year_of_birth=participant.year_of_birth,
                                                                  grade=participant.grade,
                                                                  first_track=participant.first_track,
                                                                  second_track=participant.second_track,
                                                                  sum=participant.sum)

            conn.execute(insert_statement)

    select_statement = participants_table.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)
