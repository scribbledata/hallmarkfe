{
 "schema": "user:default:v1",
 "id": "user.none.completed_orders",
 "entity": "user",
 "granularity": "NONE",
 "name": "completed_orders",
 "owner": "feast@example.com",
 "description": "This feature represents a user's total completed orders",
 "uri": "https://example.com/",
 "valueType": "INT32",
 "tags": [],
 "options": {},
 "dataStores": {
   "serving": {
     "id": "example_serving"
   },
   "warehouse": {
     "id": "example_warehouse"
   }
 }
}