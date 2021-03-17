#   See the NOTICE file distributed with this work for additional information
#   regarding copyright ownership.
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from django.urls import path, include

from .views import reset_failed_jobs, group_choice

app_name = 'ensembl.production.dbcopy'

urlpatterns = [
    path('reset_failed_jobs/<uuid:job_id>', reset_failed_jobs, name='reset_failed_jobs'),
    path('add', group_choice, name='group_choice'),
    path(f'api', include('ensembl.production.dbcopy.api.urls')),
]
