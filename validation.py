import os, sys
sys.path.append(os.path.join(os.path.expanduser('~'), '.campanario'))
from connection import cur, connection


def music_state():
    music_query = f"select is_active from paginaweb_ClockInformation where name='play_songs';"
    cur.execute(music_query)
    music_state = cur.fetchall()
    return music_state

def server_state():
    server_query = f"select is_active from paginaweb_ClockInformation where name='server_active';"
    cur.execute(server_query)
    server_state = cur.fetchall()
    return server_state

def clock_state():
    clock_query = f"select is_active from paginaweb_ClockInformation where name='change_hour';"
    cur.execute(clock_query)
    clock_state = cur.fetchall()
    return clock_state

def lights_state():
    clock_query = f"select is_active from paginaweb_ClockInformation where name='clock_lights';"
    cur.execute(clock_query)
    clock_state = cur.fetchall()
    return clock_state


if len(music_state()) == 0:
    query = f"insert into paginaweb_ClockInformation(name, is_active) VALUES ('play_songs', false);"
    cur.execute(query)
    connection.commit()
    
if len(lights_state()) == 0:
    query = f"insert into paginaweb_ClockInformation(name, is_active) VALUES ('clock_lights', false);"
    cur.execute(query)
    connection.commit()

if len(server_state()) == 0:
    query = f"insert into paginaweb_ClockInformation(name, is_active) VALUES ('server_active', false);"
    cur.execute(query)
    connection.commit()
    
if len(clock_state()) == 0:
    query = f"insert into paginaweb_ClockInformation(name, is_active) VALUES ('change_hour', false);"
    cur.execute(query)
    connection.commit()


def update_music_state(state: bool):
    match(state):
        case True:
            query = f"update paginaweb_ClockInformation set is_active=true where name='play_songs';"
        case False:
            query = f"update paginaweb_ClockInformation set is_active=false where name='play_songs';"
    cur.execute(query)
    connection.commit()

def update_server_state(state: bool):
    match(state):
        case True:
            query = f"update paginaweb_ClockInformation set is_active=true where name='server_active';"
        case False: 
            query = f"update paginaweb_ClockInformation set is_active=false where name='server_active';"
    cur.execute(query)
    connection.commit()


def update_clock_state(state: bool):
    match (state):
        case True:
            query = f"update paginaweb_ClockInformation set is_active=true where name='change_hour';"
        case False:
            query = f"update paginaweb_ClockInformation set is_active=false where name='change_hour';"

    cur.execute(query)
    connection.commit()



