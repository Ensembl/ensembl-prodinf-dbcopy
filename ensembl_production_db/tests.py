# -*- coding: utf-8 -*-
"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ensembl_production_db.models import *

User = get_user_model()


class AnalysisTest(APITestCase):
    """ Test module for AnalysisDescription model """
    multi_db = True
    using_db = 'production'
    fixtures = ['ensembl_production_api']

    # Test Analysis description endpoints
    def test_AnalysisDescription(self):
        # Check get all
        response = self.client.get(reverse('analysisdescription-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test post
        response = self.client.post(reverse('analysisdescription-list'),
                                    {'logic_name': 'test', 'description': 'test analysis', 'display_label': 'test',
                                     'db_version': 1, 'displayable': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test post wth webdata
        valid_payload = {'logic_name': 'testwebtestdata', 'description': 'testwebdata analysis',
                         'display_label': 'testwebdata', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'cdna'}}}
        response = self.client.post(reverse('analysisdescription-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test post wth webdata, reusing existing webdata
        valid_payload = {'logic_name': 'testwebtestdata2', 'description': 'testwebdata2 analysis',
                         'display_label': 'testwebdata2', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'cdna'}}}
        response = self.client.post(reverse('analysisdescription-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test bad post
        response = self.client.post(reverse('analysisdescription-list'),
                                    {'logic_name': '', 'description': 'test analysis', 'display_label': 'test',
                                     'db_version': 1, 'displayable': 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Test get
        response = self.client.get(reverse('analysisdescription-detail', kwargs={'logic_name': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test get wth webdata
        response = self.client.get(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad get
        response = self.client.get(reverse('analysisdescription-detail', kwargs={'logic_name': 'cantgetit'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test put
        response = self.client.put(reverse('analysisdescription-detail', kwargs={'logic_name': 'test'}),
                                   {'logic_name': 'test2', 'description': 'test2 analysis updated',
                                    'display_label': 'test2', 'db_version': 1, 'displayable': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad put
        response = self.client.put(reverse('analysisdescription-detail', kwargs={'logic_name': 'dontexist'}),
                                   {'logic_name': 'newtest', 'description': 'newtest2 analysis',
                                    'display_label': 'newtest2', 'db_version': 1, 'displayable': 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test put changing webdata
        valid_payload = {'logic_name': 'testwebtestdata2', 'description': 'testwebdata2 analysis',
                         'display_label': 'testwebdata2', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test2', 'data': {'default': {'contigviewbottom': 'notnormal'},
                                                                       'dna_align_feature': {'do_not_display': '1'},
                                                                       'type': 'cdna'}}}
        response = self.client.put(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata2'}),
                                   data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad put changing webdata
        valid_payload = {'logic_name': 'testwebtestdata2', 'description': 'testwebdata2 analysis',
                         'display_label': 'testwebdata2', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test2', 'data': {'default': {'contigviewbottom': 'notnormal'},
                                                                       'dna_align_feature': {'do_not_display': '1'},
                                                                       'type': 'cdna'}}}
        response = self.client.put(reverse('analysisdescription-detail', kwargs={'logic_name': 'dontexistwebdata'}),
                                   data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test patch
        response = self.client.patch(reverse('analysisdescription-detail', kwargs={'logic_name': 'test2'}),
                                     {'logic_name': 'test3', 'description': 'test2 analysis updated',
                                      'display_label': 'test2', 'db_version': 1, 'displayable': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test get
        response = self.client.get(reverse('analysisdescription-detail', kwargs={'logic_name': 'test3'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad patch
        response = self.client.patch(reverse('analysisdescription-detail', kwargs={'logic_name': 'dontexist2'}),
                                     {'logic_name': 'newtest', 'description': 'newtest2 analysis',
                                      'display_label': 'newtest2', 'db_version': 1, 'displayable': 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test patch wth webdata
        valid_payload = {'logic_name': 'testwebtestdata', 'description': 'testwebdata analysis',
                         'display_label': 'testwebdata', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'core'}}}
        response = self.client.patch(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata'}),
                                     data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad patch wth webdata
        valid_payload = {'logic_name': 'testwebtestdata', 'description': 'testwebdata analysis',
                         'display_label': 'testwebdata', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'core'}}}
        response = self.client.patch(reverse('analysisdescription-detail', kwargs={'logic_name': 'dontexistwebdata'}),
                                     data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test delete
        response = self.client.delete(reverse('analysisdescription-detail', kwargs={'logic_name': 'test3'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test post wth webdata, reusing existing webdata for delete
        valid_payload = {'logic_name': 'testwebtestdata3', 'description': 'testwebdata3 analysis',
                         'display_label': 'testwebdata3', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'core'}}}
        response = self.client.post(reverse('analysisdescription-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test delete with webdata
        response = self.client.delete(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test get after deleted webdata
        response = self.client.get(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata3'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad delete
        response = self.client.delete(reverse('analysisdescription-detail', kwargs={'logic_name': 'cantdeleteit'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_AnalysisDescriptionUserName(self):
        valid_payload = {'logic_name': 'testwebtestdata4', 'description': 'testwebdata4 analysis',
                         'display_label': 'testwebdata4', 'db_version': 1, 'displayable': 1, "user": "testuser",
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'core'}}}
        response = self.client.post(reverse('analysisdescription-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username='testuser')
        new_elem = AnalysisDescription.objects.get(logic_name='testwebtestdata4')
        self.assertEqual(new_elem.created_by.username, user.username)

        valid_payload.update({'user': 'unknownuser', 'logic_name': 'failed_one'})
        response = self.client.post(reverse('analysisdescription-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        valid_payload = {'logic_name': 'testwebtestdata5', 'description': 'testwebdata5 analysis',
                         'display_label': 'testwebdata5', 'db_version': 1, 'displayable': 1,
                         'web_data': {'description': 'test', 'data': {'default': {'contigviewbottom': 'normal'},
                                                                      'dna_align_feature': {'do_not_display': '1'},
                                                                      'type': 'core'}}}
        response = self.client.post(reverse('analysisdescription-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_elem = AnalysisDescription.objects.get(logic_name='testwebtestdata5')
        self.assertIsNone(new_elem.created_by)
        # test update with username
        valid_payload = {'logic_name': 'testwebtestdata5', 'description': 'testwebdata5 analysis updated',
                         'display_label': 'testwebdata5', 'db_version': 1, 'displayable': 1, 'user': "testuserupdate"}
        response = self.client.patch(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata5'}),
                                     data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_elem = AnalysisDescription.objects.get(logic_name='testwebtestdata5')
        self.assertIsNotNone(new_elem.modified_by)
        self.assertEqual(new_elem.modified_by.username, 'testuserupdate')
        # test unknown user
        valid_payload = {'logic_name': 'testwebtestdata5', 'description': 'testwebdata5 analysis updated wrong user',
                         'display_label': 'testwebdata5', 'db_version': 1, 'displayable': 1, 'user': "unknownuser"}
        response = self.client.patch(reverse('analysisdescription-detail', kwargs={'logic_name': 'testwebtestdata5'}),
                                     data=json.dumps(valid_payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test attrib Type endpoint
    def test_AttribType(self):
        # Check get all
        response = self.client.get(reverse('attribtypes-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test post
        response = self.client.post(reverse('attribtypes-list'),
                                    {'code': 'test', 'name': 'test attribtypes', 'description': 'test'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test duplicated code post
        response = self.client.post(reverse('attribtypes-list'),
                                    {'code': 'test', 'name': 'test attribtypes', 'description': 'test'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Test bad post
        response = self.client.post(reverse('attribtypes-list'),
                                    {'code': '', 'name': 'test attribtypes', 'description': 'test'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Test get
        response = self.client.get(reverse('attribtypes-detail', kwargs={'code': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad get
        response = self.client.get(reverse('attribtypes-detail', kwargs={'code': 'cantgetit'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test put
        response = self.client.put(reverse('attribtypes-detail', kwargs={'code': 'test'}),
                                   {'code': 'test2', 'name': 'test2 attribtypes', 'description': 'test2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad put
        response = self.client.put(reverse('attribtypes-detail', kwargs={'code': 'dontexist'}),
                                   {'code': 'newtest', 'description': 'newtest2 analysis', 'name': 'newtest2'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test patch
        response = self.client.patch(reverse('attribtypes-detail', kwargs={'code': 'test2'}),
                                     {'code': 'test3', 'description': 'test2 analysis updated', 'name': 'test2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad patch
        response = self.client.patch(reverse('attribtypes-detail', kwargs={'code': 'dontexist2'}),
                                     {'code': 'newtest', 'description': 'newtest2 analysis', 'name': 'newtest2'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test delete
        response = self.client.delete(reverse('attribtypes-detail', kwargs={'code': 'test3'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test bad delete
        response = self.client.delete(reverse('attribtypes-detail', kwargs={'code': 'cantdeleteit'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_AttribTypeUserName(self):
        # create user known
        response = self.client.post(reverse('attribtypes-list'),
                                    {'code': 'test', 'name': 'test attribtypes', 'description': 'test',
                                     'user': 'testuser'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_elem = MasterAttribType.objects.get(code='test')
        user = User.objects.get(username='testuser')
        self.assertEqual(new_elem.created_by.username, user.username)
        # create user un-known
        response = self.client.post(reverse('attribtypes-list'),
                                    {'code': 'test2', 'name': 'test attribtypes', 'description': 'test',
                                     'user': 'unknown'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # update user known
        response = self.client.put(reverse('attribtypes-detail', kwargs={'code': 'test'}),
                                   {'code': 'test', 'name': 'test2 attribtypes', 'description': 'test2',
                                    'user': 'testuser'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_elem = MasterAttribType.objects.get(code='test')
        self.assertEqual(new_elem.modified_by.username, user.username)
        # update user un-known
        response = self.client.put(reverse('attribtypes-detail', kwargs={'code': 'test'}),
                                   {'code': 'test', 'name': 'test2 attribtypes', 'description': 'test2',
                                    'user': 'unknown'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test biotype endpoint
    def test_Biotype(self):
        # Test post object type 1
        response = self.client.post(reverse('type-list', kwargs={'biotype_name': 'test'}),
                                    {'name': 'test', 'description': 'test biotype gene', 'object_type': 'gene',
                                     'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test post object type 2
        response = self.client.post(reverse('type-list', kwargs={'biotype_name': 'test'}),
                                    {'name': 'test', 'description': 'test biotype transcript',
                                     'object_type': 'transcript', 'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Test bad post
        response = self.client.post(reverse('type-list', kwargs={'biotype_name': 'badtest'}),
                                    {'name': '', 'description': 'test biotype', 'display_label': 'test',
                                     'object_type': 'gene', 'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Test get
        response = self.client.get(reverse('type-list', kwargs={'biotype_name': 'test'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad get
        response = self.client.get(reverse('type-list', kwargs={'biotype_name': 'cantgetit'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test get wth types
        response = self.client.get(reverse('type-detail', kwargs={'biotype_name': 'test', 'type': 'gene'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad get wth types
        response = self.client.get(reverse('type-detail', kwargs={'biotype_name': 'cantgetit', 'type': 'gene'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test put
        response = self.client.put(reverse('type-detail', kwargs={'biotype_name': 'test', 'type': 'gene'}),
                                   {'name': 'test2', 'description': 'test2 biotype updated', 'object_type': 'gene',
                                    'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad put
        response = self.client.put(reverse('type-detail', kwargs={'biotype_name': 'dontexist', 'type': 'gene'}),
                                   {'name': 'newtest', 'description': 'newtest2 biotype', 'object_type': 'gene',
                                    'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test patch
        response = self.client.patch(reverse('type-detail', kwargs={'biotype_name': 'test2', 'type': 'gene'}),
                                     {'name': 'test3', 'description': 'test2 biotype updated', 'object_type': 'gene',
                                      'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test bad patch
        response = self.client.patch(reverse('type-detail', kwargs={'biotype_name': 'dontexist2', 'type': 'gene'}),
                                     {'name': 'newtest', 'description': 'newtest2 biotype', 'object_type': 'gene',
                                      'db_type': 'core', 'is_dumped': 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Test delete
        response = self.client.delete(reverse('type-detail', kwargs={'biotype_name': 'test3', 'type': 'gene'}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Test bad delete
        response = self.client.delete(reverse('type-detail', kwargs={'biotype_name': 'cantdeleteit', 'type': 'gene'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_BiotypeUserName(self):
        # Test post object type 1
        response = self.client.post(reverse('type-list', kwargs={'biotype_name': 'test'}),
                                    {'name': 'test', 'description': 'test biotype gene', 'object_type': 'gene',
                                     'db_type': 'core', 'is_dumped': 1, 'user': 'testuser'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_elem = MasterBiotype.objects.get(name='test')
        user = User.objects.get(username='testuser')
        self.assertEqual(new_elem.created_by.username, user.username)
        response = self.client.put(reverse('type-detail', kwargs={'biotype_name': 'test', 'type': 'gene'}),
                                   {'name': 'test update', 'description': 'test2 biotype updated',
                                    'object_type': 'gene',
                                    'db_type': 'core', 'is_dumped': 1, 'user': 'testuser'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_elem = MasterBiotype.objects.get(name='test update')
        self.assertEqual(new_elem.modified_by.username, user.username)
        response = self.client.put(reverse('type-detail', kwargs={'biotype_name': 'test update', 'type': 'gene'}),
                                   {'name': 'test update', 'description': 'test2 biotype updated',
                                    'object_type': 'gene', 'db_type': 'core', 'is_dumped': 1, 'user': 'unknown'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post(reverse('type-list', kwargs={'biotype_name': 'test'}),
                                    {'name': 'test another', 'description': 'test biotype gene', 'object_type': 'gene',
                                     'db_type': 'core', 'is_dumped': 1, 'user': 'unknown'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test attrib endpoint
    def test_Attrib(self):
        # Check get all
        response = self.client.get(reverse('attrib-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Test post wth attrib_type
        valid_payload = {'value': 'test', 'is_current': '1',
                         'attrib_type': {'code': 'test', 'name': 'test', 'description': 'test'}}
        response = self.client.post(reverse('attrib-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        attrib_type = MasterAttrib.objects.filter(value='test').first().attrib_type
        self.assertIsNotNone(MasterAttrib.objects.filter(value='test').first().attrib_type)
        # Test post wth attrib_type, reusing existing attrib_type
        valid_payload = {'value': 'test2', 'is_current': '1',
                         'attrib_type': {'code': 'test', 'name': 'test', 'description': 'test'}}
        response = self.client.post(reverse('attrib-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(MasterAttrib.objects.filter(value='test2').first().attrib_type.pk == attrib_type.pk)
        # Test bad post
        valid_payload = {'value': '', 'is_current': '1',
                         'attrib_type': {'code': 'test', 'name': 'test', 'description': 'test'}}
        response = self.client.post(reverse('attrib-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_attribUserName(self):
        valid_payload = {'value': 'test', 'is_current': '1', 'user': 'testuser',
                         'attrib_type': {'code': 'test', 'name': 'test', 'description': 'test'}}
        response = self.client.post(reverse('attrib-list'), data=json.dumps(valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_elem = MasterAttrib.objects.get(attrib_type__code='test')
        user = User.objects.get(username='testuser')
        self.assertEqual(new_elem.created_by.username, user.username)
        self.assertEqual(new_elem.attrib_type.created_by.username, user.username)