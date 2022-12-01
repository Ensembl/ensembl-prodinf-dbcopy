CHANGELOG - Ensembl Prodinf Database copy
=========================================
1.7.0
-----
- Added user/pass settings vars to enable usage with db_introspect module


1.6.0
-----
- Prevent empty `src_incl_db` in submission
- TransferLogs display updates
- Fix List filter by status
- Use the request host defined user for Host/DB introspections validation (instead of default `ensro`)
- Restore full fields recovery (tgt_host and src_host) when Form errors spotted (initially lost)

1.5.1
-----
- Added feature to prevent duplicated request_job insertion through GUI or API calls
  To prevent multiple same job (considered same job is currently the exact same parameters)

1.5.0
-----
- Optimized querie to reduce list retrieval latencies
- Added expected field for better status follow up
- Updated JS / CSS 
- Added detailed link to inlines (transfer_logs) for more details

1.4.0
-----
- Fix/simplify database and table ajax alerts
- Use ensembl-prodinf-core 2.0.0

v1.3.1
------
- Reintroduce job_id in Request job REST response

v1.3
----
- Fix long standing request when transfer_logs list is huge, causing time out on REST requests. https://github.com/Ensembl/ensembl-prodinf-dbcopy/pull/19
- Integrate new prodinf-core updates regarding db copy filtering/checking in place (prodinf-core@1.3) https://github.com/Ensembl/ensembl-prodinf-core/releases/tag/1.3

v1.2
----
- Fix whole server copy check issue preventing submission
- Updated Controls to remove annoying initial messages
- Updates TargetHost Lookup not to offer current typed chars 
- Added Create and Start Date time to edit view
- Corrected Style

v1.1
----
- moved RequestJob validation at model level. (Initiall in Admin form)
- Bumped django-admin-inline-paginator version to 0.2 
- Changed Django dependency requirements compatibility level
- Updated CSS to for RequestJob lists display (added colors / progress bar)
- Request Job fix user not being associated  
- Optimised queries for listing job loading time

v1.0
----
- Moved from initial production services monolithic application (https://github.com/Ensembl/ensembl-production-services)
- Django standard layout / templates integration (enable backend skinning)
- Refactored App API to enable usage of external service for db introspection
- Changed namespace to `ensembl.production.dbcopy`
- Changed app name to `ensembl_dbcopy`  
  
