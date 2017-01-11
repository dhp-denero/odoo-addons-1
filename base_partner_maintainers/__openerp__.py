# -*- coding:utf-8 -*-
#
#
#    Copyright (C) 2015 Sucros Clear Information Technologies PLC.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
    'name': 'Partner Maintainers',
    'summary': 'Centrally manage maintainers of partner records.',
    'description': """
Centrally manage who can maintain partners and contacts
=======================================================
Give specific users permission to add, remove, and update contact information.
    """,
    'author': 'Sucros Clear Information Technologies PLC',
    'website': 'http://clearict.com',
    'category': 'Generic Modules/Base',
    'version': '1.0',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'wizard/maintainers_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'active': False,
}
