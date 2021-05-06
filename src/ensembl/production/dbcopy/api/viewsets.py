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
from rest_framework import viewsets, mixins, response, status

from ensembl.production.dbcopy.api.serializers import RequestJobDetailSerializer, RequestJobListSerializer, HostSerializer
from ensembl.production.dbcopy.models import RequestJob, Host, Group


class RequestJobViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = RequestJobListSerializer
    queryset = RequestJob.objects.all()
    pagination_class = None
    lookup_field = 'job_id'

    def get_serializer_class(self):
        if self.action == 'list':
            return RequestJobListSerializer
        else:
            return RequestJobDetailSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Only destroy object when status is still "submitted" otherwise raise an error and do not delete object
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        if instance.overall_status == 'Submitted':
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class SourceHostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HostSerializer
    lookup_field = 'name'

    def get_queryset(self):
        """
        Return a list of hosts according to a keyword
        """
        queryset = Host.objects.all()
        host = self.request.query_params.get('name', None)
        if host is not None:
            host_name = host.split(':')[0]
            queryset = queryset.filter(name__contains=host_name)
        return queryset


class TargetHostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HostSerializer
    lookup_field = 'name'

    def get_queryset(self):
        """
        Return a list of hosts according to a keyword

        """
        host_queryset = Host.objects.all()
        group_queryset = Group.objects.all()
        host_name = self.request.query_params.get('name', None)
        host_queryset_final = host_queryset
        # Checking that user is allowed to copy to the matching server
        # If he is not allowed, the server will be removed from the autocomplete
        if host_name is not None:
            host_queryset = host_queryset.filter(name__contains=host_name)
            host_queryset_final = host_queryset
            for host in host_queryset:
                group = group_queryset.filter(host_id=host.auto_id)
                if group:
                    host_groups = group.values_list('group_name', flat=True)
                    user_groups = self.request.user.groups.values_list('name', flat=True)
                    common_groups = set(host_groups).intersection(set(user_groups))
                    if not common_groups:
                        host_queryset_final = host_queryset.exclude(name=host.name)
        return host_queryset_final
