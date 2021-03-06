create table alt_fuel_stations(
	id INTEGER primary key autoincrement,
    Fuel_Type_Code char(8),
    Station_Name text,
    Street_Address text,
    Intersection_Directions text,
    City text,
    State char(2),
    ZIP int(5),
    Plus4 int(4),
    Phone int(10),
    Status_Code char(1),
    Expected_Date text,
    Groups_With_Access_Code text,
    Access_Days_Time text,
    Cards_Accepted text,
    BD_Blends text,
    NG_Fill_Type_Code text,
    NG_PSI int,
    EV_Level1_EVSE int,
    EV_Level2_EVSE int,
    EV_DC_Fast_Count int,
    EV_Other_Info text,
    EV_Network text,
    EV_Network_Web text,
    Geocode_Status text,
    Latitude text,
    Longitude text,
    Date_Last_Confirmed text,
    ID int,
    Updated_At text,
    Owner_Type_Code char(5),
    Federal_Agency_ID int,
    Federal_Agency_Name text,
    Open_Date text,
    Hydrogen_Status_Link text,
    NG_Vehicle_Class char(4),
    LPG_Primary int,
    E85_Blender_Pump int,
    EV_Connector_Types varchar(255)
);
