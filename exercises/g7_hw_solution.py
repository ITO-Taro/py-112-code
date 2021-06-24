import sqlite3

work_dir = r"../sql-data/"
fn = "World_country_populations.csv"

conn = sqlite3.connect(work_dir+"world_populations.db")
c = conn.cursor()

countries = ('Canada', 'France','Germany','Italy','United States','United Kingdom','Japan')
c.execute("""select sum(migrants) from pop_data where country in {0} and migrants > 0""".format(countries))
total_g7_migrants = c.fetchone()[0]
c.execute("""select sum(migrants) from pop_data where migrants > 0""")
total_migrants_world_wide =  c.fetchone()[0]
total_migrants_rest_of_world = total_migrants_world_wide - total_g7_migrants
#total_migrants_rest_of_world_ratio = 100 - round((total_g7_migrants/total_migrants_world_wide)*100,2) 
print(f"Percentage of migrants G7 takes {round((total_g7_migrants/total_migrants_world_wide)*100,2)}")
print(f"Percentage of migrants the rest of the world takes {round((total_migrants_rest_of_world/total_migrants_world_wide)*100,2)}")

for country in countries:
    c.execute("""select sum(migrants) from pop_data where country = '{0}' and migrants > 0""".format(country))
    g_country_count = c.fetchone()[0]
    print(f"Percentage of migrants {country} takes: { round((g_country_count/total_g7_migrants)*100,2 ) }")
