from database.base import Base
from sqlalchemy import Boolean, Column, Integer, String, Text


# Common tables for all agent types (raspberry, g5k, iot-lab)
class Action(Base):
    __tablename__ = 'action'
    node_name = Column(Text, primary_key=True)
    node_ip = Column(Text)
    environment = Column(Text)
    process = Column(Text)
    state = Column(String(120))
    state_idx = Column(Integer)
    updated_at = Column(Integer)


    def __repr__(self):
        return "action(%s, %s, %s)" % (self.node_name, self.state, self.updated_at)


class ActionProperty(Base):
    __tablename__ = 'action_prop'
    node_name = Column(Text, primary_key=True)
    prop_name = Column(Text, primary_key=True)
    prop_value = Column(Text)
    owner = Column(Text, primary_key=True)


class Schedule(Base):
    __tablename__ = 'schedule'
    node_name = Column(Text, primary_key=True)
    owner = Column(Text, primary_key=True)
    bin = Column(Text)
    start_date = Column(Integer)
    end_date = Column(Integer)
    state = Column(Text)
    action_state = Column(Text)


    def __repr__(self):
        return "schedule(%s, %s, %s)" % (self.node_name, self.state, self.start_date)


# Tables for raspberry agents
class RaspNode(Base):
    __tablename__ = 'rasp_node'
    node_name = Column(Text, primary_key=True)
    prop_name = Column(Text, primary_key=True)
    prop_value = Column(Text)


    def __repr__(self):
        return "node(%s, %s, %s)" % (self.node_name, self.prop_name, self.prop_value)


class RaspSwitch(Base):
    __tablename__ = 'rasp_switch'
    name = Column(Text, primary_key=True)
    prop_name = Column(Text, primary_key=True)
    prop_value = Column(Text)


class RaspEnvironment(Base):
    __tablename__ = 'rasp_environment'
    name = Column(Text, primary_key=True)
    prop_name = Column(Text, primary_key=True)
    prop_value = Column(Text)

# Table for IoT-Lab agents
class IotSelection(Base):
    __tablename__ = 'iot_selection'
    # autoincrement unique identifier
    uid = Column(Integer, primary_key=True)
    owner = Column(Text)
    filter_str = Column(Text)
    archi = Column(Text)
    # node id list (node identifiers separated by '+'), e.g., '1+2+5+10'
    node_ids = Column(Text)
    node_nb = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer)


class IotNodes(Base):
    __tablename__ = 'iot_nodes'
    job_id = Column(Integer, primary_key=True, autoincrement=False)
    assigned_nodes = Column(Text)
