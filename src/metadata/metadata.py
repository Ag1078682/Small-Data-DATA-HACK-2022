##ToDo
## all functions concerning creating, saving, and modifying of the query metadata


##ToDo
## remember, if target metadata is modified (i.e. fields are added),
## unless it is a complete reload
## we should modify target storage
## and be careful because it might affect other queries to the same data target
## and if it is a complete reload we should(?) clear or move outdated data to something like ".old" tables


##ToDo
## overall, the metadata DB contains 3 tables: metadata, scedule and statuses
## the metadata is to be stored in Postgres DB in a format of jsonb
## the scedule is for automatical issue of queries
## the statuses contains id of a query, id for each particular transaction, datetime of it, and a status
## (for each step i.e. start_get, write_raw, write_file, error, on_hold, canceled, etc.)
