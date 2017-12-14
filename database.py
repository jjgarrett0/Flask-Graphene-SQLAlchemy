from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, func, String

# Replace 'sqlite:///rfg.db' with your path to database
engine = create_engine('sqlite:///rfg.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
											autoflush=False,
											bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Station(Base):
	__table__ = 'alt_fuel_stations'
	id = Column(Integer, primary_key=True)
	Fuel_Type_Code = Column(Text)
	Station_Name = Column(Text)
	Street_Address = Column(Text)
	Intersection_Directions = Column(Text)
	City = Column(Text)
	State = Column(String(2))
	ZIP = Column(Integer)
	Plus4 = Column(Integer)
	Phone = Column(Integer)
	Status_Code = Column(String(1))
	Expected_Date = Column(Text)
	Groups_With_Access_Code = Column(Text)
	Access_Days_Time = Column(Text)
	Cards_Accepted = Column(Text)
	BD_Blends = Column(Text)
	NG_Fill_Type_Code = Column(Text)
	NG_PSI = Column(Integer)
	EV_Level1_EVSE = Column(Integer)
	EV_Level2_EVSE = Column(Integer)
	EV_DC_Fast_Count = Column(Integer)
	EV_Other_Info = Column(Text)
	EV_Network = Column(Text)
	EV_Network_Web = Column(Text)
	Geocode_Status = Column(Text)
	Latitude = Column(Text)
	Longitude = Column(Text)
	Date_Last_Confirmed = Column(Text)
	ID = Column(Integer)
	Updated_At = Column(Text)
	Owner_Type_Code = Column(String(5))
	Federal_Agency_ID = Column(Integer)
	Federal_Agency_Name = Column(Text)
	Open_Date = Column(Text)
	Hydrogen_Status_Link = Column(Text)
	NG_Vehicle_Class = Column(String(4))
	LPG_Primary = Column(Integer)
	E85_Blender_Pump = Column(Integer)
	EV_Connector_Types = Column(String(255))

