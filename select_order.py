import pymysql.cursors
from conf import server_db_info
# sql="select * from test;"
sql="""
SELECT
	t_airport_trip_order.order_id,
	passenger_name,
	t_vendor.`name` AS vendor,
	t_cost_detail.amount AS amount,
	t_cost_detail.cost_type AS cost_type,
	t_cost_detail.cost_describe AS cost_describe,
	order_state,
	order_type,
	vehicle_id,
	model,
	t_vehicle.plate AS plate,
	t_vehicle.vin AS vin,
	t_vehicle.oil AS oil,
	passenger_phone,
	belong_unit,
	take_car_city,
	business_unit,
	airport_id,
	trip_address,
	driver_start_address,
	driver_end_address,
	airline_company,
	flight_number,
	take_car_date,
	return_car_date
FROM
	t_airport_trip_order
	LEFT JOIN t_vendor ON vendor_id = t_vendor.id
	LEFT JOIN t_cost_detail ON t_airport_trip_order.order_id = t_cost_detail.order_id
	LEFT JOIN t_vehicle ON vehicle_id = t_vehicle.id
	left join (select serial_number,model from t_vehicle left join t_vehicle_model on t_vehicle_model.id=t_vehicle.model_id) as model on model.serial_number=vehicle_id
	where {key}={value};
    
"""
key=input("input key")
value=input("input value")
sql=sql.format(key=key,value=value)
# print(sql)
connection=pymysql.connect(host=server_db_info["ip"],
                           user=server_db_info["username"],
                           password=server_db_info["passwd"],
                           db=server_db_info["db"],
                           charset="utf8")
try:
    with connection.cursor() as cursor:
        cursor.execute(sql,(server_db_info))
        result=cursor.fetchall()
        print(result)
finally:
    connection.close()
for i in result:
    print(i)



