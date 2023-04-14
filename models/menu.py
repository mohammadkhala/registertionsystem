# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [

        (T('coueses'), False, '#', [
            (T('list course'), False, URL('courses', 'courses')),
            (T('add course '), False, URL('courses', 'addCourse')),

        ]),
        ('students', False, '#', [
            (T('add student '), False, URL('students', 'addstudent')),
            (T('list students '), False, URL('students', 'students')),

          ]),

        (T('register course '), False, URL('coursereg', 'add_course_to_schedule')),

    ]
