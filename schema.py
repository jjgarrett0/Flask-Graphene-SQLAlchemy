import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import db_session, Station as StationModel


class Stations(SQLAlchemyObjectType):
    class Meta:
        model = StationModel
        interfaces = (relay.Node,)


# Used to Create a new station
class CreateStation(graphene.Mutation):
    class Input:
        Fuel_Type_Code = graphene.String()
        Station_Name = graphene.String()
        Street_Address = graphene.String()
        Intersection_Directions = graphene.String()
        City = graphene.String()
        State = graphene.String()
        ZIP = graphene.Int()
        Plus4 = graphene.Int()
        Phone = graphene.Int()
        Status_Code = graphene.String()
        Expected_Date = graphene.String()
        Groups_With_Access_Code = graphene.String()
        Access_Days_Time = graphene.String()
        Cards_Accepted = graphene.String()
        BD_Blends = graphene.String()
        NG_Fill_Type_Code = graphene.String()
        NG_PSI = graphene.Int()
        EV_Level1_EVSE = graphene.Int()
        EV_Level2_EVSE = graphene.Int()
        EV_DC_Fast_Count = graphene.Int()
        EV_Other_Info = graphene.String()
        EV_Network = graphene.String()
        EV_Network_Web = graphene.String()
        Geocode_Status = graphene.String()
        Latitude = graphene.String()
        Longitude = graphene.String()
        Date_Last_Confirmed = graphene.String()
        ID = graphene.Int()
        Updated_At = graphene.String()
        Owner_Type_Code = graphene.String()
        Federal_Agency_ID = graphene.Int()
        Federal_Agency_Name = graphene.String()
        Open_Date = graphene.String()
        Hydrogen_Status_Link = graphene.String()
        NG_Vehicle_Class = graphene.String()
        LPG_Primary = graphene.Int()
        E85_Blender_Pump = graphene.Int()
        EV_Connector_Types = graphene.String()

    ok = graphene.Boolean()
    station = graphene.Field(Stations)

    @classmethod
    def mutate(cls, _, args, context, info):
        station = StationModel(Fuel_Type_Code=args.get('Fuel_Type_Code'), Station_Name=args.get('Station_Name'),
                               Street_Address=args.get('name'), Intersection_Directions = args.get('name'),
                               City=args.get('name'), State=args.get('name'), ZIP=args.get('name'),
                               Plus4=args.get('name'), Phone= args.get('name'), Status_Code=args.get('name'),
                               Expected_Date=args.get('name'), Groups_With_Access_Code=args.get('name'),
                               Access_Days_Time=args.get('name'), Cards_Accepted=args.get('name'),
                               BD_Blends=args.get('name'), NG_Fill_Type_Code=args.get('name'),
                               NG_PSI=args.get('name'), EV_Level1_EVSE=args.get('name'), EV_Level2_EVSE=args.get('name'),
                               EV_DC_Fast_Count=args.get('name'), EV_Other_Info=args.get('name'),
                               EV_Network=args.get('name'), EV_Network_Web=args.get('name'),
                               Geocode_Status=args.get('name'), Latitude=args.get('name'), Longitude=args.get('name'),
                               Date_Last_Confirmed=args.get('name'), ID=args.get('name'), Updated_At=args.get('name'),
                               Owner_Type_Code=args.get('name'), Federal_Agency_ID=args.get('name'),
                               Federal_Agency_Name=args.get('name'), Open_Date=args.get('name'),
                               Hydrogen_Status_Link=args.get('name'), NG_Vehicle_Class=args.get('name'),
                               LPG_Primary=args.get('name'), E85_Blender_Pump=args.get('name'),
                               EV_Connector_Types=args.get('name'))
        db_session.add(station)
        db_session.commit()
        ok = True
        return CreateStation(station=station, ok=ok)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    user = SQLAlchemyConnectionField(Stations)
    find_user = graphene.Field(lambda: Stations, username=graphene.String())
    all_users = SQLAlchemyConnectionField(Stations)

    def resolve_find_station(self, args, context, info):
        query = Stations.get_query(context)
        username = args.get('username')
        return query.filter(StationModel.username == username).first()


class MyMutations(graphene.ObjectType):
    create_user = CreateStation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations, types=[Stations])
